import time
import requests

API_TOKEN = "zkjxx2furd@pomail.net"
USER_KEY = "ucnhoiq6gn7uucxi8rbqef7mnmze6i"

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
