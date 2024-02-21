import requests
import re

def send_verification_code(url):
    # Extract phone number from the URL
    phone_number_match = re.search(r'\bphone=(\d+)', url)
    if phone_number_match:
        phone_number = phone_number_match.group(1)
        print("Phone number extracted:", phone_number)
        
        # Send POST request with the extracted phone number
        api_url = "https://bikroy.com/data/phone_number_login/verifications/phone_login"
        data = {"phone": phone_number}
        
        response = requests.post(api_url, data=data)
        
        if response.status_code == 200:
            print("Verification code sent successfully!")
        else:
            print("Failed to send verification code. Status code:", response.status_code)
    else:
        print("Phone number not found in the URL.")

# Example URL provided by the user
user_url = input("Enter the URL containing the phone number: ")
send_verification_code(user_url)
