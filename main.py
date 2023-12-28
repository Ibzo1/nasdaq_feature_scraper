import json
from short_interest import scrape_short_interest
from options_chain import scrape_options_chain
from institutional_investors import scrape_institutional_investors, determine_action, max_min


def main():
    ticker = input("Enter ticker symbol: ")
    print("Select data type to pull:")
    print("1. Short Interest")
    print("2. Options Chain")
    print("3. Institutional Investors")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        data = scrape_short_interest(ticker)
        print(json.dumps(data, indent=4))

    elif choice == '2':
        data = scrape_options_chain(ticker)
        print(json.dumps(data, indent=4))

    elif choice == '3':
        Analysis = input("Would you like to only recieve top buyers/sellers? (y/n)")
        if Analysis.lower() == "y":
            output = max_min(ticker)
            print(output)
        else: 
            data = scrape_institutional_investors(ticker)
            print(json.dumps(data, indent=4))
    else:
        print("Invalid choice.")
        return

    

if __name__ == "__main__":
    main()
