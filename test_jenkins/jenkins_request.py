#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/6/28 15:20
# @Author:  haiyong
# @File:    jenkins_request.py
import json

import requests

url = "http://admin:admin@192.168.2.104:8080/job/first_test/build"
ret = requests.post(url)
print(ret.text)

# url = "http://admin:admin@192.168.2.104:8080/job/first_test/lastBuild/buildNumber"
# ret = requests.get(url)
# print(ret.text)

# url = "http://admin:admin@192.168.2.104:8080/job/first_test/1/api/json"
# ret = requests.get(url)
# print(json.dumps(ret.json(),indent=2))