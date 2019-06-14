#!/usr/bin python3
# -*- coding: utf-8 -*-

import itchat
from itchat.content import *
from tuling import Tuling

def main():
    @itchat.msg_register(TEXT, isFriendChat=True)
    def tuling_reply(msg):
        # 只回复备注名为xxx的信息
        if msg.user.RemarkName == 'xxx':
            reply = tuling.get_response(msg.text)
        else:
            reply = '哈哈哈哈'

        return reply

    itchat.auto_login(hotReload=True)
    itchat.run()

if __name__ == '__main__':
    tuling = Tuling()
    main()