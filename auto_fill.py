#!/usr/bin/python
#yum install python-mechanize -y
import mechanize
url = 'http://192.168.6.36:8600/rmq/topic/add.do'
serverlist = ['']
grouplist = []
def add_topic(MqName,BrName):
	br=mechanize.Browser()
	br.open(url)
	br.select_form(nr=0) #check yoursite forms to match the correct number
	br['writeQueueNums']='4' #use the proper input type=text name
	br['topic']=MqName 
	br['brokerAddr']=BrName
	br['readQueueNums']='4' 
	br['clusterName']='DefaultCluster' 
	br.submit()
for oneserver in serverlist:
    for onegroup in grouplist:
        print oneserver,onegroup
        add_topic(onegroup,oneserver)

