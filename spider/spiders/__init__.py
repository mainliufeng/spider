# -*- coding: utf-8 -*-

import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst, MapCompose, Join

from spider.loader import ItemLoader
from spider.items import UradarNewsItem, UradarBlogItem
from spider.loader.processors import (text, DateProcessor, PipelineProcessor,
                                      RegexProcessor, SafeHtml)


class LoaderMappingSpider(CrawlSpider):

    mapping = None

    def __init__(self):
        if not getattr(self, 'mapping', None):
            raise ValueError(
                "%s must have a mapping" % type(self).__name__
            )
        self.__generate_rules()
        super(LoaderMappingSpider, self).__init__()

    def __generate_rules(self):
        '''生成scrapy.contrib.spiders.CrawlSpider中的rules
        '''
        rule_list = []
        for url, loader in self.mapping.iteritems():
            rule = Rule(
                LinkExtractor(allow=(url),
                              allow_domains=self.allowed_domains),
                callback=lambda response: loader().load(response),
                follow=False)
            rule_list.append(rule)
        rule_list.append(
            Rule(
                LinkExtractor(allow=('.*'), allow_domains=self.allowed_domains)
            )
        )
        self.rules = tuple(rule_list)


class TargetUrlCallbackMappingSpider(CrawlSpider):
    '''目标链接回调映射爬虫
    url_callback_mapping中设置，目标链接正则:这类链接的callback函数
    爬虫从start_urls开始抓取，遍历在allowed_domains以内的链接
    直到链接匹配目标链接正则表达式，请求目标链接，调用对应的callback函数
    '''

    url_callback_mapping = None

    def __init__(self):
        if not getattr(self, 'url_callback_mapping', None):
            raise ValueError(
                "%s must have a url_callback_mapping" % type(self).__name__
            )
        if not getattr(self, 'allowed_domains', None):
            raise ValueError(
                "%s must have a nonempty allowed_domains" % type(self).__name__
            )
        self.__generate_rules()

        super(TargetUrlCallbackMappingSpider, self).__init__()

    def __generate_rules(self):
        '''生成scrapy.contrib.spiders.CrawlSpider中的rules
        '''
        rule_list = []
        for url, callback in self.url_callback_mapping.iteritems():
            rule = Rule(
                LinkExtractor(allow=(url),
                              allow_domains=self.allowed_domains),
                callback=callback,
                follow=False)
            rule_list.append(rule)
        rule_list.append(
            Rule(
                LinkExtractor(allow=('.*'), allow_domains=self.allowed_domains)
            )
        )
        self.rules = tuple(rule_list)


class TargetUrlsCallbackSpider(TargetUrlCallbackMappingSpider):
    '''目标链接回调爬虫
    url_callback_mapping中设置，目标链接正则:这类链接的callback函数
    爬虫从start_urls开始抓取，遍历在allowed_domains以内的链接
    直到链接匹配目标链接正则表达式，请求目标链接，调用对应的callback函数
    '''

    target_urls = None
    target_url_callback = None

    def __init__(self):
        if not getattr(self, 'target_urls', None):
            raise ValueError(
                "%s must have a target_urls" % type(self).__name__
            )
        if not getattr(self, 'target_url_callback', None):
            raise ValueError(
                "%s must have a nonempty target_url_callback" %
                type(self).__name__
            )

        self.url_callback_mapping = {
            url: self.target_url_callback for url in self.target_urls
        }

        super(TargetUrlsCallbackSpider, self).__init__()


class NewsSpider(TargetUrlsCallbackSpider):
    '''新闻爬虫'''

    subclass_required_attrs = [
        'content_xpath',
        'publish_time_xpath',
        'publish_time_format'
    ]

    title_xpath = '//title'
    abstract_xpath = '//meta[@name="description"]/@content'
    keywords_xpath = '//meta[@name="keywords"]/@content'

    def __init__(self):
        self.target_url_callback = 'parse_news'
        TargetUrlsCallbackSpider.__init__(self)

        for attr in self.subclass_required_attrs:
            if not getattr(self, attr, None):
                raise ValueError(
                    "%s must have a %s" % (type(self).__name__, attr)
                )

        if not getattr(self, 'site_domain', None) and \
                not getattr(self, 'source_domain', None):
            raise ValueError(
                "%s must have a site_domain" % (type(self).__name__, attr)
            )

        if not getattr(self, 'site_name', None) and \
                not getattr(self, 'source_name', None):
            raise ValueError(
                "%s must have a site_name" % (type(self).__name__, attr)
            )

    def parse_news(self, response):
        l = ItemLoader(item=UradarNewsItem(), response=response)

        l.default_output_processor = TakeFirst()

        l.add_value('url', response.url)

        l.add_xpath('title', self.title_xpath, MapCompose(text))

        l.add_xpath('content', self.content_xpath,
                    MapCompose(SafeHtml(response.url)), Join('\n'))

        # author可选
        auther_xpath = getattr(self, 'author_xpath', None)
        if auther_xpath is not None:
            auther_re = getattr(self, 'author_re', None)
            if auther_re is None:
                l.add_xpath('author', self.author_xpath, MapCompose(text))
            else:
                l.add_xpath('author', self.author_xpath, MapCompose(text),
                            MapCompose(RegexProcessor(auther_re)))

        # publish_time_re可选

        processor_list = [text]

        publish_time_re = getattr(self, 'publish_time_re', None)
        if publish_time_re is not None:
            processor_list.append(
                RegexProcessor(
                    publish_time_re,
                    join_str=getattr(self, 'publish_time_re_join', u'')
                )
            )

        publish_time_filter = getattr(self, 'publish_time_filter', None)
        if publish_time_filter is not None:
            processor_list.append(
                publish_time_filter
            )

        processor_list.append(DateProcessor(self.publish_time_format))

        l.add_xpath('publish_time', self.publish_time_xpath,
                    MapCompose(
                        PipelineProcessor(
                            *processor_list
                        )
                    ))

        # abstract默认使用meta中description
        l.add_xpath('abstract', self.abstract_xpath, MapCompose(text))

        # keywords默认使用meta中keywords
        l.add_xpath('keywords', self.keywords_xpath, MapCompose(text))

        # source可选
        source_xpath = getattr(self, 'source_xpath', None)
        if source_xpath:
            source_re = getattr(self, 'source_re', None)
            if source_re is None:
                l.add_xpath('source', self.source_xpath, MapCompose(text))
            else:
                l.add_xpath('source', self.source_xpath, MapCompose(text),
                            MapCompose(RegexProcessor(source_re)))

        l.add_value('site_domain', getattr(self, 'site_domain', None))
        l.add_value('site_name', getattr(self, 'site_name', None))

        # 兼容原有爬虫
        l.add_value('site_domain', getattr(self, 'source_domain', None))
        l.add_value('site_name', getattr(self, 'source_name', None))

        l.add_value('add_time', datetime.datetime.now())

        i = l.load_item()
        return i


class BlogSpider(TargetUrlsCallbackSpider):
    '''新闻爬虫'''

    subclass_required_attrs = [
        'title_xpath',
        'content_xpath',
        'author_xpath',
        'publish_time_xpath',
        'publish_time_format'
    ]

    abstract_xpath = '//meta[@name="description"]/@content'
    keywords_xpath = '//meta[@name="keywords"]/@content'

    def __init__(self):
        self.target_url_callback = 'parse_blog'
        TargetUrlsCallbackSpider.__init__(self)

        for attr in self.subclass_required_attrs:
            if not getattr(self, attr, None):
                raise ValueError(
                    "%s must have a %s" % (type(self).__name__, attr)
                )

        if not getattr(self, 'site_domain', None) and \
                not getattr(self, 'source_domain', None):
            raise ValueError(
                "%s must have a site_domain" % (type(self).__name__, attr)
            )

        if not getattr(self, 'site_name', None) and \
                not getattr(self, 'source_name', None):
            raise ValueError(
                "%s must have a site_name" % (type(self).__name__, attr)
            )

    def parse_blog(self, response):
        l = ItemLoader(item=UradarBlogItem(), response=response)

        l.default_output_processor = TakeFirst()

        l.add_value('url', response.url)

        l.add_xpath('title', self.title_xpath, MapCompose(text))

        l.add_xpath('content', self.content_xpath,
                    MapCompose(SafeHtml(response.url)))

        # author_re可选
        auther_re = getattr(self, 'author_re', None)
        if auther_re is None:
            l.add_xpath('author', self.author_xpath, MapCompose(text))
        else:
            l.add_xpath('author', self.author_xpath, MapCompose(text),
                        MapCompose(RegexProcessor(auther_re)))

        # publish_time_re可选
        publish_time_re = getattr(self, 'publish_time_re', None)
        if publish_time_re is None:
            l.add_xpath('publish_time', self.publish_time_xpath,
                        MapCompose(PipelineProcessor(
                                   text,
                                   DateProcessor(self.publish_time_format))))
        else:
            l.add_xpath('publish_time', self.publish_time_xpath,
                        MapCompose(PipelineProcessor(
                                   text,
                                   RegexProcessor(publish_time_re),
                                   DateProcessor(self.publish_time_format))))

        # abstract默认使用meta中description
        l.add_xpath('abstract', self.abstract_xpath, MapCompose(text))

        # keywords默认使用meta中keywords
        l.add_xpath('keywords', self.keywords_xpath, MapCompose(text))

        # source_re可选
        if getattr(self, 'source_xpath', None) is not None:
            source_re = getattr(self, 'source_re', None)
            if source_re is None:
                l.add_xpath('source', self.source_xpath, MapCompose(text))
            else:
                l.add_xpath('source', self.source_xpath, MapCompose(text),
                            MapCompose(RegexProcessor(source_re)))

        l.add_value('site_domain', getattr(self, 'site_domain', None))
        l.add_value('site_name', getattr(self, 'site_name', None))

        # 兼容原有爬虫
        l.add_value('site_domain', getattr(self, 'source_domain', None))
        l.add_value('site_name', getattr(self, 'source_name', None))

        l.add_value('add_time', datetime.datetime.now())

        i = l.load_item()
        return i
