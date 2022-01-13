import requests


def get_access_token(client_id, client_password):
    url = "https://visibility.eu.amp.cisco.com/iroh/oauth2/token"
    payload = {"grant_type": "client_credentials"}
    return requests.post(url, data=payload, auth=(client_id, client_password))


def inspect(access_token, observable):
    url = "https://visibility.eu.amp.cisco.com/iroh/iroh-inspect/inspect"
    headers = {"authorization": f"Bearer {access_token}"}
    payload = {"content": f"{observable}"}
    return requests.post(url, json=payload, headers=headers)


def deliberate(access_token, payload):
    url = "https://visibility.eu.amp.cisco.com/iroh/iroh-enrich/deliberate/observables"
    headers = {"authorization": f"Bearer {access_token}"}
    return requests.post(url, json=payload, headers=headers)


def main():
    client_id = "<YOUR TR CLIENT ID>"
    client_password = "<YOUR TR CLIENT ID>"

    response = get_access_token(client_id, client_password)
    access_token = response.json().get("access_token")

    observable = "45.146.165.37"
    response = inspect(access_token, observable)

    payload = response.json()
    response = deliberate(access_token, payload)
    print(response.text)


if __name__ == "__main__":
    main()
