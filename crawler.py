import requests
import sys

url = raw_input("Enter domain name:")
try:
    def get_request(url):
    try:
        response = requests.get("http://" + url)
        return response
    except requests.exceptions.ConnectionError:
        pass

    def get_response(file_name)
        with open(file_name,"r") as wordlist:
            for line in wordlist:
                new_url = line.strip() + "." + url
                response = get_request(new_url)
                if response:
                    print("[+]Success: " + new_url)
                else:
                    print("[-]Not Found...")

    file_name = raw_input("Enter wordlist:")
    get_response(file_name)

except KeyboardInterrupt:
    print("\nExiting..")
    sys.exit()


