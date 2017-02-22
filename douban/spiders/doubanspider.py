#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = doubanspider
#author = tangtao
#time   = 2017/2/20 16:02
#Description=豆瓣爬虫
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
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.http import Request
from scrapy import cmdline

from douban.sql.my_sqldb import insert_info, update_info, create_table

reload(sys)
sys.setdefaultencoding('utf-8')


class Douban(CrawlSpider):
    name = "douban"
    start_urls = ['http://movie.douban.com/top250']
    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMoive in Movies:
            url = eachMoive.xpath('div[@class="hd"]/a/@href').extract()[0]
            url=str(url)
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()[0]
            # 把两个名称合起来
            fullTitle = ''
            for each in title:
                fullTitle += each
            foreign_title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()[1]
            # 把两个名称合起来
            fullTitle_foreign = ''
            for each in foreign_title:
                fullTitle_foreign += each
            movieInfo0 = eachMoive.xpath('div[@class="bd"]/p/text()').extract()[0]  # 此处出现的是导演和主演
            movieInfo1 = eachMoive.xpath('div[@class="bd"]/p/text()').extract()[1]  # 此处出现的是年份和国籍以及类型
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            pingjiashu = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
            pingjiashu = filter(lambda ch: ch in '0123456789', pingjiashu)  # 去掉评价数中的中文
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            quote = str(quote)
            year = str(movieInfo1).replace('/', '*').replace('  ', '').split('*')[0]
            nation = str(movieInfo1).replace('/', '*').replace('  ', '').split('*')[1]
            kind = str(movieInfo1).replace('/', '*').replace('  ', '').split('*')[2]
            insert_info('title', fullTitle)
            update_info('foreign_title', foreign_title, fullTitle)
            update_info('inq', quote, fullTitle)
            update_info('star', star, fullTitle)
            update_info('year', year, fullTitle)
            update_info('nation', nation, fullTitle)
            update_info('kind', kind, fullTitle)
            update_info('pingjiarenshu', pingjiashu, fullTitle)
            update_info('url', url, fullTitle)
            yield item
            nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
            # 第10页是最后一页，没有下一页的链接
            if nextLink:
                nextLink = nextLink[0]
                # print nextLink
                yield Request(self.url + nextLink, callback=self.parse)


if __name__ == '__main__':
    create_table()
    cmdline.execute("scrapy crawl douban".split())
