# coding: utf-8
from urllib import urlencode
import httplib2
import requests
import robot
from robot.libraries.BuiltIn import BuiltIn
import json
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


class HttpLibrary(object):
    """Http Client"""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._cache = robot.utils.ConnectionCache(u'未创建sessions')
        self.builtin = BuiltIn()
        self.alias = None
        self.host = None
        self.port = None
        self.cookie = None

    def create_session(self, host, port, Alias):
        """Create Session : 创建一个连接host server的HTTP会话

        `Alias` 对当前会话指定别名,在Http请求中可用于识别在高速缓存中的Session对象

        也可参考robotframework-requests库中create session关键字

        Examples:
        | Create Session | &{enviro}[host] | &{enviro}[port] | alias |

        """
        self.alias = Alias
        self.host = host
        self.port = port
        url = self._checkport()
        session = requests.Session()
        res = session.get(url)
        self._cache.register(session, alias=self.alias)

    def post_request(self, uri, form_data=None, para=None, json_data=None):
        """Issues a HTTP POST request.

        `uri`  请求路径

        `para` 追加在URL后面的参数，键值字典或Json格式，URL长度有限制，最多只能是1024字节.

        `form_data` 在POST请求的HTTP消息主体中发送的数据，键值字典。对应headers Content-Type:application/x-www-form-urlencoded

        `json_data` 在POST请求的HTTP消息主体中发送的数据，json格式。 对应headers Content-Type:application/json

        也可参考robotframework-requests库中Post Request关键字     

        Examples:
        | ${res} | Post Request | /checkUser.do | {'userName':'&{account}[username]','password':'&{account}[password]'} | None |#登录接口获取cookie
        | ${res} | Post Request | /manualreply/addClassify | {'name':'${name}'} | None |None|
        | ${res} | Post Request | /api/device/addDevice | None | None | {"deviceId":"${deviceId}","deviceName":"${deviceName}"} |

        """

        session = self._cache.switch(self.alias)
        url = self._get_url(uri)
        print "HttpRequest Url is " + url
        if self.cookie == None :
            if str(form_data) != 'None':
               response = session.post(url, data=eval(form_data))
            elif str(json_data) != 'None':
               response = session.post(url, json=json.dumps(eval(json_data)))
            elif 'Set-Cookie' in response.headers.keys():
                self.cookie = response.headers['Set-Cookie']
                return self._replace_null(response.content).decode('utf-8')
            return self._replace_null(response.content).decode('utf-8')       
        else:
            if str(para) == 'None' and str(form_data) == 'None' and str(json_data) == 'None':
               response = session.post(url, cookies={'Cookie':self.cookie})
            elif str(para) != 'None' and str(form_data) == 'None' and str(json_data) == 'None':
               response = session.post(url, params=eval(para), cookies={'Cookie':self.cookie})
            elif str(para) == 'None' and str(form_data) != 'None' and str(json_data) == 'None':
               response = session.post(url, data=eval(data), cookies={'Cookie':self.cookie})
            elif str(para) == 'None' and str(form_data) == 'None' and str(json_data) != 'None':
                response = session.post(url, json=json.dumps(eval(json_data)), cookies={'Cookie':self.cookie})
            elif str(para) != 'None' and str(form_data) != 'None' and str(json_data) != 'None':
                response = session.post(url, params=eval(para), data=eval(data), cookies={'Cookie':self.cookie})
            elif str(para) != 'None' and str(form_data) == 'None' and str(json_data) != 'None':
                response = session.post(url, params=eval(para), json=json.dumps(eval(json_data)), cookies={'Cookie':self.cookie}) 
            return self._replace_null(response.content).decode('utf-8') 
   
    
    def post_file_request(self, uri, file, data=None, para=None,headers=None):
        """Issues a HTTP Post Request to  upload file.

        `file` file must be dictionary of {filename: fileobject} files to multipart upload. 

        `para` dictionary of URL parameters to append to the URL.

        `data` the body to attach to the request must be a python dictionary.

        `headers` 若不通过cookie登录，则可以在headers中填写与登录有关的字段（根据项目需求来）

        文件类型字段以参数或请求体参数传入

        Examples:
        | ${res} |  Post File Request | /cgi-bin/file/upload | {'content':open('Resources/Material/logo.jpg','rb')} | {'type':'jpg'} | {'access_token':'${access_token}'} | 
      
        """

        session = self._cache.switch(self.alias)
        url = self._get_url(uri)
        print "HttpRequest Url is " + url
        if self.cookie == None:
            if data =='None' and para =='None':
                response = session.post(url, files=eval(file), headers=eval(headers))
            elif data != 'None' and para == 'None':
                response = session.post(url, files=eval(file), data=eval(data), headers=eval(headers))
            elif data != 'None' and para != 'None':
                response = session.post(url, files=eval(file), data=eval(data),params=eval(para), headers=eval(headers))
            return self._replace_null(response.content).decode('utf-8')
        else:
            if para == 'None' and data == None:
                response = session.post(url, files=eval(file), cookies={'Cookie':self.cookie})
            elif para == 'None' and data != None:
                response = session.post(url, files=eval(file), data=eval(data), cookies={'Cookie':self.cookie})
            elif para != 'None' and data !=None:
                response = session.post(url, files=eval(file), params=eval(para), data=eval(data), cookies={'Cookie':self.cookie})
            return self._replace_null(response.content).decode('utf-8')


    def get_request(self, uri, para=None, headers=None):
        """Issues a HTTP Get Request.

        `para` 追加在URL后面的参数，键值字典或Json格式，URL长度有限制，最多只能是1024字节.

        `uri` 可以是请求路径，也可以是带host的url

        Examples: 
        | ${res} | Get Request | /cgi-bin/jssdk/ticket / {'access_token':'${acces_token}'}
        
        |${res} | post request | /weblogin/user/generate | {"mac":"${mac}"} | None | 
        | ${resdic} | Evaluate | ${res} |
        | Set Suite Variable | ${url} | ${resdic['result']['url']} |
        | ${res} | get request | ${url} | {'uid':'${uidencode}','timestamp':'${strtime}','signature':'${sign}','unique':'${unique}'} |

        """
        session = self._cache.switch(self.alias)
        if self.host in uri:
            url = uri
        else:
            url = self._get_url(uri)
        print "HttpRequest Url is " + url
        if self.cookie == None:
            response = session.get(url, params=eval(para),headers=eval(headers))
            if 'Set-Cookie' in response.headers.keys():
               self.cookie = response.headers['Set-Cookie']
               return self._replace_null(response.content).decode('utf-8')
            else:
                return self._replace_null(response.content).decode('utf-8')
        
        else:
            if para == 'None':
               response = session.get(url, cookies={'Cookie':self.cookie})
            else: 
               response = session.get(url, params=eval(para), cookie={'Cookie':self.cookie})
            return self._replace_null(response.content).decode('utf-8')

    def encrypt_post(self,uri,para,body,headers):
        """Issues a encrpyt or specific headers Http Post Request

        `para` 键值字典或json格式

        `body` 若需要加密，加密前键值字典或json格式格式，加密后是字符串格式
               对于不需要加密的body，则为字典或json格式，json格式需在headers里指定Content-Type类型

        `headers` 根据相应的请求加密算法定制请求头 键值字典格式，例如可包含时间戳，请求唯一标示符，对请求体的签名，用户Id等
                  返回的response 内容也是加密后的，需要相对应的解密算法来解密。
                  对于某些特殊的登录方式，可能需要在headers中加入与登录有关的字段，如id,key,token等，具体根据开发项目需求来.

        Examples:
        | ${enres} | encrpyt post | {"c":"100"} | ${enbody} | {'Content-Type':'text/plain','time':'${strtime}','unique':'${unique}','sign':'${sign}','uid':'','ua':'IOS/1.0'} |
        | ${res} | encrpyt post | /api/device/addDevice | None | {"deviceId":"${deviceId}"} | {'Content-Type':'application/json','token':'${token}'}|
        """
        if para == 'None':
            url = self._get_url(uri)
        else:
            url = self._checkport() + '?' + str(self._encodepara(para))
        print 'HttpPost url is ' + url
        http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
        if type(body) == str:
            resp,content = http.request(url,'POST', headers=eval(headers), body=body)
        else:
            resp,content = http.request(url,'POST', headers=eval(headers), body=json.dumps(eval(body)))
        return content    


    def delete_request(self, uri, para, data, headers):
        """ Issues a HTTP DELETE request.
        `headers` 请求以字典格式的报头
        """
        session = self._cache.switch(self.alias)
        url = self._get_url(uri)
        response = session.delete(url, params=eval(para), data=eval(data),headers=headers,cookies=self.cookie)
        return self._replace_null(response.content).decode('utf-8')
    

    def head_request(self, uri, headers):
        """Issues a HTTP HEAD request.
        `headers` 请求以字典格式的报头
        """
        session = self._cache.switch(alias)
        url = self._get_url(uri)
        print "HttpRequest Url is " + url
        response = session.head(url, headers=headers, cookies=self.cookie)
        return self._replace_null(response.content).decode('utf-8')

    def _get_url(self, uri):
        ''' Helper method to get the full url
        '''
        url = self._checkport()
        if uri:
            slash = '' if uri.startswith('/') else '/'
            url = "%s%s%s" % (url, slash, uri)
        return url

    def _replace_null(self, response):
        strres = json.dumps(response, ensure_ascii=False)
        return eval(strres.replace('null', '\\"null\\"').replace('false', '\\"false\\"').replace('true', '\\"true\\"'))

    def _checkport(self):
        if self.port == '0':
            url = self.host
        else:
            url = self.host + ':' + self.port
        return url

    def _encodepara(self, para):
        encodepara = urlencode(eval(para))
        return encodepara




    