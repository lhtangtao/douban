# coding=utf-8
# coding=gbk

import MySQLdb
import sys
import uniout  # 没有这行就会出现数据库中无法读取中文
import time

time.localtime(time.time())
current_data = time.strftime('%Y%m%d', time.localtime(time.time()))


def init_db():
    """
    请在此处输入数据库的信息
    :return:
    """
    connect = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        db='test',
        charset="utf8",  # 确保没有乱码
        passwd='root'
    )
    assert isinstance(connect, object)
    return connect


def create_table():
    """
    创建一张表，如果这个表存在的话则跳过 必须要确保数据库名字为test且存在
    :return: 如果存在 返回False，如果不存在则会建立一张表并且返回true
    """
    conn = init_db()
    cur = conn.cursor()
    try:
        sql_script = 'CREATE TABLE DoubanMovieTop250 (title varchar(30),foreign_title VARCHAR(1000),nation varchar(30),year VARCHAR(30),kind VARCHAR (30),director varchar(30),yanyuan varchar(30),star varchar(30),pingjiarenshu varchar(30),inq varchar(1000), url varchar(300),page varchar(30))'
        # print sql_script
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        print e
    cur.close()
    conn.commit()
    conn.close()
    return x


def insert_info(kind, value):
    """
    要插入的数据列名和数值
    :param kind:
    :param value:
    :return:
    """
    conn = init_db()
    cur = conn.cursor()
    try:
        sql_script0 = "INSERT INTO DoubanMovieTop250"
        sql_script1 = "(%s) VALUES " % kind
        sql_script2 = "('%s')" % value
        sql_script = sql_script0 + sql_script1 + sql_script2
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        print e
    cur.close()
    conn.commit()
    conn.close()
    return x


def update_info(kind, value, title):
    conn = init_db()
    cur = conn.cursor()
    try:
        sql_script0 = "UPDATE DoubanMovieTop250 SET"
        sql_script1 = " %s =" % kind
        sql_script2 = "('%s')" % value
        sql_script3 = 'where title =("'
        sql_script4 = '")'
        sql_script = sql_script0 + sql_script1 + sql_script2 + sql_script3+title+sql_script4
        # print sql_script
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        print e
    cur.close()
    conn.commit()
    conn.close()
    return x


def get_row():
    """
    获取目前的数据库的行数
    :return:
    """
    conn = init_db()
    cur = conn.cursor()
    sql_script = 'SELECT * FROM DoubanMovieTop250'
    # sql_script = 'SELECT * FROM houseinfo20170216'
    row = cur.execute(sql_script)
    cur.close()
    conn.commit()
    conn.close()
    return row


if __name__ == '__main__':
    print create_table()
    print get_row()
