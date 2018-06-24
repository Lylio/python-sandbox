
import time
from datetime import datetime as dt
#Script uses a temporary hosts file as an example
hosts_temp = "hosts"
#hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

#Loop blocks Facebook and Twitter in hosts file between hours of 9am - 5pm; checks current time every 5 seconds
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\r" + redirect + " " + website + "\n")

    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)