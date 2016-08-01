This Library for RobotFramework
----------------------------------------
[![Latest Version](https://img.shields.io/pypi/v/robotframework-interfacelibrary.svg)](https://pypi.python.org/pypi/robotframework-interfacelibrary)
[![Build Status](https://travis-ci.org/Netease-AutoTest/robotframework-interfacelibrary.svg?branch=master)](https://travis-ci.org/Netease-AutoTest/robotframework-interfacelibrary)
[![Documentation Status](https://readthedocs.org/projects/robotframework-interfacelibrary/badge/?version=latest)](http://robotframework-interfacelibrary.readthedocs.io/en/latest/?badge=latest)
## Introduction

RobotFramework-InterfaceLibrary is an Interface library for `RobotFramework` 
It includes post, get, delete, put method to send http requests,and also use MySql 
datebase to verify the Correctness of response datas.
 
It depends on [requests](https://github.com/kennethreitz/requests) library,and support Python 2.x and MySql database only.

## Install
### pip
```
   pip install robotframework-interfacelibrary
```

The main benefit of using **pip** is that it installs all
depended libraries automatically. Another nice feature is easy to upgrade or uninstall:
```
    pip install --upgrade robotframework-interfacelibrary
    pip uninstall robotframework-interfacelibrary
```
## Usage Guide:
Here is a sample test case.

|                     |                         |                     |                       |                                    |                            |                |
| --------------------| ------------------------| ------------------- | --------------------- | -----------------------------------|----------------------------|--------------- |
|  **Settings**     |                         |                             |                       |                                    |　　　　                    |                |
| Library             | String                  |                           |                       |                                    |                            |                |
| Library             | Collections             |                           |                       |                                    |                            |                |
| Library             | InterfaceLibrary        |                           |                       |                                    |                            |                |
| Test Cases          |                         |                           |                       |                                    |　　　　                    |                |
| Post Requests       |                         |                           |                       |                                    |　　　                      |                |
|                     | Create Session          | &{enviro}[host]           | &{enviro}[port]       | alise                              |                            |                |
|                     | Conncet To Datebase     | ${host}                   | ${user}               | ${password}                        | ${database}                | ${port}        |
|                     | ${res}                  | Post Request              | /activity/addActivity | {'activityName':'${activityName}'} | None                       |                |
|                     | Check Code              | ${resp}                   | 200                   |                                    |                            |                |
|                     | ${res}                  |Post File Request          | /cgi-bin/file/upload  | {'file':open('logo.jpg','rb')}  | {'type':'jpg'}             |
|  Datebase requests  | ${list}                 | Mysql Select              | SELECT name, age FROM tab WHERE ID = ${id}             |
   |                            |                |
|                     | ${name}                 | Get From List             | 0 |
|                     | ${age}                  | Get From List             | 1 |
|                     | Should be equal         | ${activityName}           | ${name}|
|                     | Delete Rows From Table  | id=${id} | comapp_tab |#condition and table name 
|                     | Check If Not Exist In Datebase | SELECT * FROM comapp_tab WHERE id=${id} |
|                     | Check if Exist In Datebase | SELECT name,company_id FROM staff_tab WHERE id=${id} |
 

- Web端：
  通过Cookie登录访问。<br>
  设置环境变量keyword:<br>
  create session<br>
  connect to database<br>
  post/get request  登录接口<br>
- Mobile端:
  包括PC,Mobile客户端,通过Proxy访问需要加密，根据项目需求可扩展测试库增加相应的加密算法关键字，<br>
  定制request headers,加密请求体body，再调用encrypt post关键字发送加密http 请求。
 
## Project Contributors
--------------------
[Wu Qi](https://github.com/seven57)   
Wei Yating

Robot Framework: http://robotframework.org    
requests: http://docs.python-requests.org/en/master     
mysql: https://github.com/sanpingz/mysql-connector     

