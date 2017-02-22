#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = main
#author = tangtao
#time   = 2017/2/20 16:04
#Description=添加描述信息
#eMail   =tangtao@lhtangtao.com
#git     =lhtangtao
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
import sys
from scrapy import cmdline

from douban.sql.my_sqldb import create_table

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    movieInfo = '387612人评价'
    year =  filter(lambda ch: ch in '0123456789', movieInfo)
    print year
