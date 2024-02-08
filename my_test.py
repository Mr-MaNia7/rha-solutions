import requests
import json
from datetime import timedelta as td
from datetime import datetime as time

user_id = '396646592'

URL = 'https://api.telegram.org/bot5354086805:AAGmdqRXfcWQpu3oe_2R6Bt2SzITRyRjQQo/sendMessage?'

headers = {'Content-type': 'application/json',
                       'Accept': 'text/plain'}


def tele():
        message = str(
            "<b>### Incident Report! ###</b>" +
            "<br><b>Client</b>:" + "Interstis" +
            "<br><b>Track no</b>: Int/" + str(1234568) +
            "<br><b>Reported By</b>:" + "Reporter" +
            "<br><b>Issue</b>:" + "Hihi-issue" +
            "<br><b>Description</b>:" + "Test desription")
        return message.replace("<br>", "\n")


#reply_markup={inline_keyboard:[[{text: hi, callback_data: hi }]]}


data = {
            "chat_id": user_id,
            "text": tele(),
            "reply_markup": {
                "inline_keyboard": [
                    [
                        {
                            "text": "Accept",
                            "callback_data": "accept"
                        }
                    ]
                ]
            },
            "parse_mode": "html",
    }
#res = requests.post(URL, data=json.dumps(data), headers=headers)

#print(res.json())

time_str = '2022-08-04T:14:29:04Z'

now = time.now()
date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
print(date_time)

def time_to_str(time):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ")

data = {
                "reporter": "name",
                "company": "company",
                "track_number": "123",
                "error_type": "DeviceNetwork",
                "desc": "Description",
                "reason": "Reason",
                "desktop_id": "369"
            }


URL = "https://atcom.pythonanywhere.com/api/"

#res = requests.get(URL)
print("++++++++++++++++++++++++++++++++++++++++")
#print(res.json())
print("++++++++++++++++++++++++++++++++++++++++")
res = requests.post(URL, data=data)
print(res)
