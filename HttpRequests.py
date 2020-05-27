#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import json


class HttpRequests(object):
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Host': 'weixin.sogou.com',

        }
        self.cookies = {}
        self.timeout = 60
        self.responses = {}
        self.errorMsg = ""

    def get(self, url, paramsData=None):
        response = self.send(url, "GET", paramsData)
        self._updateCookies(response)
        return response

    def post(self, url, postData):
        response = self.send(url, "POST", postData)
        self._updateCookies(response)
        return response

    def _parseResInfo(self, response):
        if not response:
            _responseInfo = {
                "json": None,
                "status": -1,
                "url": None,
                "responseRaw": None,
                "errorMsg": self.errorMsg
            }
        else:
            self._updateCookies(response)
            _responseInfo = {
                "json": response.json(),
                "status": response.status_code,
                "url": response.url,
                "responseRaw": response,
                "errorMsg": self.errorMsg
            }
        return _responseInfo

    def send(self,
             url,
             method="GET",
             data=None,
             headers=None,
             errorTimes=3,
             timeout=60,
             allow_redirects=False,
             *args,
             **kwargs):
        if not headers:
            headers = self.headers
        _errorTimes = 0  # 错误次数计数

        while True:
            if _errorTimes == errorTimes:
                _response = None
                break
            try:
                if method == "POST":
                    _response = self.session.post(
                        url=url,
                        data=json.dumps(data),
                        verify=False,
                        headers=headers,
                        cookies=self.cookies,
                        timeout=timeout,
                        allow_redirects=allow_redirects)
                else:
                    _response = self.session.get(
                        url=url,
                        params=data,
                        verify=False,
                        headers=headers,
                        cookies=self.cookies,
                        timeout=timeout,
                        allow_redirects=allow_redirects)
                return _response
            except Exception as e:
                print ("！！！！！请求异常！！！！！" + str(e))
                self.errorMsg = str(e)
                _errorTimes += 1
        return _response

    def _updateCookies(self, response):
        _cookies = response.cookies.get_dict()
        for k in _cookies:
            self.cookies[k] = _cookies[k]

    def jdosHeader(self):
        self.headers = {}
        # self.headers["erp"] = "zhuyuefei"
        # self.headers["token"] = "547e5e64-9094-499e-a124-b797bfad6c74"
        # self.headers["erp"] = "liufeng53"
        # self.headers["token"] = "18f1cd91-d4bb-406d-9c22-99e569fa8c02"
        # self.headers["erp"] = "wangxiuping3"
        # self.headers["token"] = "9d4ea316-8d9a-4f86-9aaa-ba0abec9ec56"
        self.headers["Accept"] = "application/json"
        self.headers["Content-Type"] = "application/json;charset=UTF-8"
        return self
