from threatresponse import ThreatResponse


def main():
    client_id = "<YOUR TR CLIENT ID>"
    client_password = "<YOUR TR CLIENT ID>"

    client = ThreatResponse(
        client_id=client_id,  # required
        client_password=client_password,  # required
        region="eu",  # optional
    )

    # Query Inspect to parse observables from string then query Deliberate to get verdicts for the observables
    print("Direct / manual response:")
    observable = "This is a string and has one observabvle -- 45.146.165.37 -- and only one observable"
    response_inspect = client.inspect.inspect({"content": f"{observable}"})
    print(response_inspect)

    response_deliberate = client.enrich.deliberate.observables(response_inspect)
    print(response_deliberate)

    # Command to perform both actions with string as input
    print("\nCommand response:")
    response = client.commands.verdict(observable)
    print(response)


if __name__ == "__main__":
    main()
