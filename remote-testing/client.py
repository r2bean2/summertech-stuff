import sys
import requests

url = "http://127.0.0.1:5000"
payload = {"score": 100}

try:
    # Attempt to connect and send data
    # timeout=3 prevents the script from freezing forever if the server is dead
    response = requests.post(url, json=payload, timeout=3)
    
    # Optional: Raises an error if the server is online but returns a 404 or 500 error
    response.raise_for_status() 

except requests.exceptions.ConnectionError:
    print("Could not find the server. Is it running?")
    sys.exit(1)  # Cleanly exits the entire script right here

except requests.exceptions.Timeout:
    print("The server took too long to respond.")
    sys.exit(1)

except requests.exceptions.HTTPError as e:
    print(f"Server found, but returned an error: {e}")
    sys.exit(1)
print(response.text)