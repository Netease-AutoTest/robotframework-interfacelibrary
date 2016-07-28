This Library for RobotFramework
=====================================================

Introduction
---------------

RobotFramework-IFHttpLibrary is an Interface testing library for `RobotFramework`
It includes post, get, delete, put method to send http requests,and also use MySql 
datebase to verify the Correctness of response datas.

It support Python 2.x and MySql database only.

Installation
------------

Using ``pip``
'''''''''''''

The recommended installation method is using
`pip <http://pip-installer.org>`__::

   pip install robotframework-interfacelibrary

The main benefit of using ``pip`` is that it automatically installs all
dependencies needed by the library. Other nice features are easy upgrading
and support for un-installation::

    pip install --upgrade robotframework-interfacelibrary
    pip uninstall robotframework-interfacelibrary
 

Usage Guider:
----------------------------------------

* Web端：通过Cookie登录访问。
  设置环境变量keyword:
  create session
  connect to database
  post/get request  登录接口
* Mobile端:包括PC和Mobile客户端,通过Proxy访问需要加密，根据项目需求可扩展测试库然后增加相应的加密算法关键字，
  定制相应的request headers和加密请求体body，再调用 ``encrypt post`` 关键字发送加密http 请求。
 

Project Contributors
--------------------
* `Wuqi <wuqi@yixin.im>`_
* `WeiYaTing <hzweiyating@corp.netease.com>`_

.. _Robot Framework: http://robotframework.org
.. _requests: http://docs.python-requests.org/en/master
.. _mysql: https://github.com/sanpingz/mysql-connector
