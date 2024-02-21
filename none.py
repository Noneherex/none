import requests

def send_verification(phone_number):
    url = "https://bikroy.com/data/phone_number_login/verifications/phone_login"
    payload = {"phone": phone_number}
    response = requests.post(url, data=payload)
    return response.text

if __name__ == "__main__":
    phone_number = input("Enter Bangladeshi phone number (without country code): ")
    response = send_verification(phone_number)
    print(response)
