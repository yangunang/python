__author__ = 'wang'
#!/usr/bin/evn python
import requests
import re
import time
import json
import socket

ts = int(time.time())
servername = socket.gethostbyname(socket.gethostname())
URL = 'http://rocketMQ/rmq/consumer/consumerProgress.do'
grouplist = ['a','b','c']

def push_result(custom,mode):
  payload = [
     {
        "endpoint": servername,
        "metric": "MQ."+custom,
        "timestamp": ts,
        "step": 60,
        "value": int(mode),
        "counterType": "GAUGE",
        "tags": "info=MQ",
     }]
#  print payload
  r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
for onegroup in grouplist:
 paygroup = {
    'groupName': onegroup,
 }
 r = requests.post(URL, data=paygroup)
 text = r.text
 size = re.findall('p>Diff Total::Diff Total:=(.*?):value</p>',text,re.S)
 for number in size:
   if r.status_code == 200:
      push_result(onegroup,number)
   else:
     print 'error'

