# -*- coding: utf-8 -*-
import scrapy


class WhatcmsSpider(scrapy.Spider):
    name = 'whatcms'
    allowed_domains = ['whatcms.org']
    start_urls = ['https://whatcms.org/']

    def parse(self, response):
		for row in response.xpath('//*[@class="table table-sm"]//tbody/tr'):
			yield {
				'url' : (row.xpath('td[1]//text()').extract_first()).encode( "utf-8" ) ,
                'cms': (row.xpath('td[2]//text()').extract_first(default='')).encode( "utf-8" ) ,
                'version' : (row.xpath('td[3]//text()').extract_first(default='')).encode( "utf-8" ) ,
            }