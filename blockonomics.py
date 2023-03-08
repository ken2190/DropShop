import requests
import configloader

# Define all the database tables using the sqlalchemy declarative base
class Blockonomics:
    def fetch_new_btc_price():
        url = 'https://www.blockonomics.co/api/price'
        params = {'currency':configloader.user_cfg["Payments"]["currency"]}
        r = requests.get(url,params)
        if r.status_code == 200:
          price = r.json()['price']
          print ('Bitcoin price ' + str(price))
          return price
        else:
          print(r.status_code, r.text)

    def new_address(reset=False):
        api_key = configloader.user_cfg["Bitcoin"]["api_key"]
        secret = configloader.user_cfg["Bitcoin"]["secret"]
        url = 'https://www.blockonomics.co/api/new_address'
        if reset == True:
          url += '?match_callback='+secret+'&reset=1'
        else:
          url += "?match_callback=" + secret
        headers = {'Authorization': "Bearer " + api_key}
        print(url)
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
          return r
        else:
          print(r.status_code, r.text)
          return r
