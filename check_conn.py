#!/usr/bin/python
import subprocess 
import requests
import re
import time
import json
import socket

ts = int(time.time())
servername = socket.gethostbyname(socket.gethostname())
def push_result(status):
  payload = [
     {
        "endpoint": servername,
        "metric": "Check_net",
        "timestamp": ts,
        "step": 60,
        "value": int(status),
        "counterType": "GAUGE",
        "tags": " ",
     }]
  r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
cmdnetstat = "netstat -antp | grep 113.208.136.26"
p = subprocess.call(cmdnetstat,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
push_result(p)
