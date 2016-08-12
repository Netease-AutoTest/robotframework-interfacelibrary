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

##### depend 
[**mysql-connector-python**](https://pypi.python.org/pypi/mysql-connector-python/2.0.4) should be installed manually first:        
```
pip install http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df
```

##### pypi

The main benefit of using **pip** is that it installs all
depended libraries automatically.    
Another nice feature is easy to manipulate:

```pip install robotframework-interfacelibrary```  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# install    
```pip install -U robotframework-interfacelibrary```  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# to stable            
```pip install -U robotframework-interfacelibrary --pre```  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# to lastest         
```pip uninstall robotframework-interfacelibrary```  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# uninstall

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
 

- Web端:<br>
  1.通过Cookie登录访问:<br>
  设置环境变量keyword:<br>
  create session<br>
  connect to database<br>
  post/get request  登录接口<br>
  2.通过特殊的方式登录比如传入token key id等 可调用encrypt post 将字段放入headers中来实现登录

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


