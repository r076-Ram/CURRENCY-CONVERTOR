import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or not data.get("success", False):
        print("Failed to get exchange rate.")
        return None

    converted_amount = data["result"]
    return converted_amount

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("From Currency (e.g., USD): ").upper()
to_currency = input("To Currency (e.g., INR): ").upper()

result = convert_currency(amount, from_currency, to_currency)
if result is not None:
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
