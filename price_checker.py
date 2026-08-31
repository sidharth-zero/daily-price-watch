import requests

WATCHED = "https://example.com"
LIMIT = 20.0


def price_now():
    page = requests.get(WATCHED, timeout=10)
    return len(page.text) / 1000.0


def main():
    price = price_now()
    if price < LIMIT:
        print(f"cheap today: {price}")
    else:
        print(f"still {price}")


main()
