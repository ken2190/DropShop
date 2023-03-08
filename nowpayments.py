import requests

# set your API key
API_KEY = "JRBJJ2F-EP747K6-H50YFAQ-DZ5ZJNV"

# set the endpoint URL
ENDPOINT = "https://api.nowpayments.io/v1/payment"

def create_payment(amount, currency):
    # construct the payment request body
    payload = {
        "amount": amount,
        "currency": currency,
        "order_id": "my_order_id", # replace with your own order ID
        "pay_currency": currency, # use the same currency as the payment currency
        "ipn_callback_url": "https://example.com/ipn", # replace with your own IPN callback URL
    }

    # send the POST request to create the payment
    headers = {"x-api-key": API_KEY}
    response = requests.post(ENDPOINT, headers=headers, json=payload)

    # parse the response to extract the payment information
    if response.status_code == 200:
        payment_data = response.json()["data"]
        payment_id = payment_data["id"]
        payment_address = payment_data["address"]
        payment_amount = payment_data["amount"]
        payment_currency = payment_data["currency"]
        return payment_id, payment_address, payment_amount, payment_currency
    else:
        raise Exception("Failed to create payment: " + response.text)