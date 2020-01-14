import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path = r"D:\Downloads\Prog_Elvira\MegaPythonProject\WebBlocker(app3)\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < \
            dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("Working hours...")
        with open(hosts_path, "r+") as hosts:
            content = hosts.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hosts.write("\n" + website)
    else:
        print("Fun hours...")
    time.sleep(5)
