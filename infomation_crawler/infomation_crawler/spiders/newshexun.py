# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule


from infomation_crawler.items import WebArticleItem
import datetime
import pymongo
from scrapy.http import Request


class NewsHexunSpider(CrawlSpider):
  name = 'newshexun'

  allowed_domains = ['news.hexun.com']
  start_urls = ['http://news.hexun.com/']
  conn = pymongo.Connection('localhost',27017)
  infoDB = conn.info
  tWebArticles = infoDB.web_articles
  rules = (
      Rule(SgmlLinkExtractor(allow=(r'news.hexun.com/\d{4}-\d{2}-\d{2}/\d+.html')),callback='parse_item'),
  )

  def parse_item(self, response):
    sel = Selector(response)
    i =WebArticleItem()
    title = sel.xpath('//h1/text()').extract()
    i['title'] = len(title)>0 and title[0].strip() or ''
    i['siteName'] = 'hexun'
    i['url'] = response.url
    author = sel.xpath('//span[@id="source_baidu"]/font/text()').extract()
    i['author'] = len(author)>0 and author[0].strip() or ''
    source = sel.xpath('//span[@id="source_baidu"]/a/text()').extract()
    i['source'] = len(source)>0 and source[0].strip() or ''
    pubtime = sel.xpath('//span[@id="pubtime_baidu"]/text()').extract()
    i['publishTime'] = len(pubtime)>0 and pubtime[0].split(' ')[0] or str(datetime.date.today())
    i['addTime'] = datetime.datetime.now()
    content= sel.xpath('//div[@id="artibody"]').extract()
    #i['addTime'] = (len(sel.xpath('//div[@class="detail"]/span[2]/text()').extract())) and sel.xpath('//div[@class="detail"]/span[2]/text()').extract()[0] or ''
    i['content'] = len(content)>0 and content[0] or ''
    i['keyWords'] = ''
    i['abstract'] = ''
    return i


