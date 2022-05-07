#!/usr/bin/env python3
import requests
import re
requests.packages.urllib3.disable_warnings()
import json

ip_port = ""	#灯塔ip+端口
url1 = "https://" + ip_port + "/api/task/?page=1&size=1&name=****8D&ts=1651718713424"	#删除重复任务名/目标/状态
head = {
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
	"Token":"****",	#修改token
	"Content-Type": "application/json"
}
res1 = requests.get(url=url1, headers = head, verify=False)
#print(res1.text)
obj = re.compile(r'.*?{"_id": (?P<name>.*?),.*?', re.S)
while len(res1.text) > 200:
	res2 = requests.get(url=url1, headers = head, verify=False)
	result = obj.finditer(res2.text)
	for i in result:
#		print(i.group("name"))
		url_stop = "https://" + ip_port + "/api/task/batch_stop/"
#		{"task_id":["626c26123a8fed00278e1593"]}
		date = '"task_id":[{}]'.format(i.group("name"))
		jsonData = "{"+date+"}"
		print(jsonData)
#		jsonData = json.dumps(date)
		res_stop = requests.post(url = url_stop, headers= head, verify= False, data=jsonData)
#		print(res_stop.text)
		url_del = "https://" + ip_port + "/api/task/delete/"
		res_del = requests.post(url = url_del, headers= head, verify= False, data=jsonData)
		print(res_del.text)