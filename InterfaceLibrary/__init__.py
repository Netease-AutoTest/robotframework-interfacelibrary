# -*- coding: utf-8 -*-
from HttpLibrary import HttpLibrary
from CheckResult import CheckResult
from version import VERSION

_version_ = VERSION


class InterfaceLibrary(HttpLibrary, CheckResult):
    """ IFHttpLibrary is a HTTP client keyword library that uses requests,httplib2 module.

    It can be applied to Interface test.

    HttpLibrary: Http Request keywords such as `create session`,`post request`, `get request`, `post file request`, `head request` 
                 can be used to send Http request.

    CheckResult: It provide keywords to verify the result.Keyword 'Check Code' can verify the http response code.
                 It also can allow you to query your MySQL Datebase to verify the results
                 Warning: Datebase Verfication is only applied to MySQL Datebase.

    ----------------------------------------------------

       Examples:
       | Create Session | &{enviro}[host] | &{enviro}[port] | alise |
       | Conncet To Datebase | ${host} | ${user} | ${password} | ${database} | ${port} |
       | Post Request | /login/in | ${'username':${username},'password':${password}} | None |#获取登录状态的cookie
       | ${res} | Post Request| /activity/addActivity.p | {'activityName':'${activityName}'} |
       | Check Code | ${res} | 200 |
       | ${res} |  Post File Request | /cgi-bin/file/upload | {'content':open('Resources/Material/logo.jpg','rb')} | {'type':'jpg'} | {'access_token':'${access_token}'} | 
       | ${res} | Get Request | /cgi-bin/jssdk/ticket / {'access_token':'${acces_token}'}
       | ${list} | Mysql Select | SELECT name, age FROM elf_activity_tab WHERE ID = ${id} |
       | ${name} | Get From List | 0 |
       | ${age} | Get From List | 1|
       | Should be equal | ${activityName} | ${name}|
       | Delete Rows From Table | id=${id} | elf_comapp_tab |#condition and table name 
       | Check If Not Exist In Datebase | SELECT * FROM elf_comapp_tab WHERE id=${id} |
       | Check if Exist In Datebase | SELECT name,company_id FROM elf_staff_tab WHERE id=${id} |


    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = _version_ 

    def __init__(self):    
        for base in InterfaceLibrary.__bases__:
            base.__init__(self)

