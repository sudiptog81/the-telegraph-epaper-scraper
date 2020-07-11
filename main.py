import os
import requests
from datetime import date
from notify_run import Notify

count = 1
notify = Notify()
date_today = date.today().strftime("%d%m%Y")

while (count <= 12):
    request_url = "https://epaper.telegraphindia.com/epaperimages" + \
        f"////{date_today}////{date_today}" + \
        f"-md-hr-{str(count)}ll.png"
    response = requests.get(request_url)
    if response.status_code != 200:
        break
    filename = f"{'{0:03}'.format(count)}.png"
    with open(os.path.join(os.path.curdir, filename), 'wb') as f:
        try:
            f.write(response.content)
            count += 1
        except Exception as e:
            print(e)

new_count = 1

while (new_count <= 12):
    request_url = "https://epaper.telegraphindia.com/epaperimages" + \
        f"////{date_today}////{date_today}" + \
        f"-md-ct2-{str(new_count)}ll.png"
    response = requests.get(request_url)
    if response.status_code != 200:
        break
    filename = f"{'{0:03}'.format(count)}.png"
    with open(os.path.join(os.path.curdir, filename), 'wb') as f:
        try:
            f.write(response.content)
            new_count += 1
            count += 1
        except Exception as e:
            print(e)
try:
    os.system(f"convert *.png -quality 100 TheTelegraph-{date_today}.pdf")
    os.system("rm *.png")
    print(f"SAVED: The Telegraph {date.today().strftime('%d-%m-%Y')}")
    notify.send(f"SAVED: The Telegraph {date.today().strftime('%d-%m-%Y')}")
except Exception as e:
    print(e)
    notify.send(f"FAILURE: The Telegraph {date.today().strftime('%d-%m-%Y')}")
