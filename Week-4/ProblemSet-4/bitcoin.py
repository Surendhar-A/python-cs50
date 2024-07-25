import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
elif len(sys.argv) > 2:
    sys.exit("Expecting only one command-line argument")
else:
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = response.json()
        rate = data["bpi"]["USD"]["rate_float"]
        cost = float(sys.argv[1]) * rate
        print(f"${cost:,.4f}")

    except requests.RequestException:
        print("Request Failed")
