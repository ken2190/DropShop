import sys
import telegram
import configloader
import flask
import duckbot
from blockonomics import Blockonomics
import database as db
import datetime
import configloader
from decimal import Decimal
import sqlalchemy

# Start the bitcoin callback listener
app = flask.Flask(__name__)
@app.route('/callback', methods=['GET'])
def callback():
    # Create a bot instance
    bot = duckbot.factory(configloader.user_cfg)(request=telegram.utils.request.Request(configloader.user_cfg["Telegram"]["con_pool_size"]))

    # Test the specified token
    try:
        bot.get_me()
    except telegram.error.Unauthorized:
        print("The token you have entered in the config file is invalid.\n"
              "Fix it, then restart this script.")
        sys.exit(1)

    # Fetch the callback parameters
    secret = flask.request.args.get("secret")
    status = int(flask.request.args.get("status"))
    address = flask.request.args.get("addr")
    # Check the secret
    if secret == configloader.user_cfg["Bitcoin"]["secret"]:
        # Fetch the current transaction by address
        engine = sqlalchemy.create_engine(configloader.user_cfg["Database"]["engine"])
        dbsession = sqlalchemy.orm.sessionmaker(bind=engine)()
        transaction = dbsession.query(db.BtcTransaction).filter(db.BtcTransaction.address == address).one_or_none()
        if transaction and transaction.txid == "":
            # Check the status
            if transaction.status == -1:
                current_time = datetime.datetime.now()
                timeout = 30
                # If timeout has passed, use new btc price
                if current_time - datetime.timedelta(minutes = timeout) > datetime.datetime.strptime(transaction.timestamp, '%Y-%m-%d %H:%M:%S.%f'):
                    transaction.price = Blockonomics.fetch_new_btc_price()
                transaction.timestamp = current_time
                transaction.status = 0
                bot.send_message(transaction.user_id, "Payment recieved!\nYour account will be credited on confirmation.")
            if status == 2:
                # Convert satoshi to fiat
                satoshi = float(flask.request.args.get("value"))
                received_btc = satoshi/1.0e8
                received_dec = round(Decimal(received_btc * transaction.price), int(configloader.user_cfg["Payments"]["currency_exp"]))
                received_float = float(received_dec)
                print ("Recieved "+str(received_float)+" "+configloader.user_cfg["Payments"]["currency"]+" on address "+address)
                # Add the credit to the user account
                user = dbsession.query(db.User).filter(db.User.user_id == transaction.user_id).one_or_none()
                user.credit += int(received_float * (10 ** int(configloader.user_cfg["Payments"]["currency_exp"])))
                # Add a transaction to list
                new_transaction = db.Transaction(user=user,
                                             value=int(received_float * (10 ** int(configloader.user_cfg["Payments"]["currency_exp"]))),
                                             provider="Bitcoin",
                                             notes = address)
                # Add and commit the transaction
                dbsession.add(new_transaction)
                # Update the received_value for address in DB
                transaction.value += received_float
                transaction.txid = flask.request.args.get("txid")
                transaction.status = 2
                dbsession.commit()
                bot.send_message(transaction.user_id, "Payment confirmed!\nYour account has been credited with "+str(received_float)+" "+configloader.user_cfg["Payments"]["currency"]+".")
                return "Success"
            else:
                dbsession.commit()
                return "Not enough confirmations"
        else:
            dbsession.commit()
            return "Transaction already proccessed"
    else:
        dbsession.commit()
        return "Incorrect secret"

if __name__ == "__main__":
    # Run the flask app in the main process
    app.run()
