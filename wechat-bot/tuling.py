#!/usr/bin python3
# -*- coding: utf-8 -*-

import requests
import json

class Tuling(object):
    key = ''
    api_url = 'http://www.tuling123.com/openapi/api/v2'

    def get_response(self, text):
        headers = {'Content-Type': 'application/json'}
        data = {
            'perception': {
                'inputText': {
                    'text': text
                }
            },
            'userInfo': {
                'apiKey': self.key,
                'userId': 'wechat'
            }
        }

        r = requests.post(self.api_url, headers=headers, data=json.dumps(data))
        result_dict = r.json()
        return result_dict['results'][0]['values']['text']

if __name__ == '__main__':
    tuling = Tuling()
    result = tuling.get_response('哈哈哈哈')
    print(result)