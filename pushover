import time
import requests

API_TOKEN = "# Find this on your pushover.net account!#
USER_KEY = "# Find this on the project you create on your Pushover.net account!"

def send_notification(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": API_TOKEN,
            "user": USER_KEY,
            "message": "Ahoy! Enjoy me message ya band o' blethering bleeding hearts!"
        }
    )

counter = 1

while True:
    send_notification(f"Test notification #{counter}")
    print(f"Sent notification #{counter}")

    counter += 1
    time.sleep(15)
