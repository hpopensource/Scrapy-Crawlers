# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import datetime
#from tutorial import settings
from scrapy.exceptions import DropItem
from scrapy.http import Request
import logging

class CmsPipeline(object):
	def __init__(self):
		self.connect = pymysql.connect(
			host = 'localhost',
			db ='cms_data',
			user = 'root',
			passwd = '',
			charset = 'utf8',
			use_unicode = True
		)
		self.cursor = self.connect.cursor();

	def process_item(self, item, spider):
		try:
			self.cursor.execute(
				"insert into whatcms (`url`, `cms`, `ver`) values(%s, %s, %s)",
				(item['url'].encode('utf-8', 'ignore'),
				 item['cms'].encode('utf-8', 'ignore'),
				 item['version'].encode('utf-8', 'ignore')
				 ))
			self.connect.commit()
			#print str(item['url'])
			#print str(item['cms'])
			#print str(item['ver'])
			#print item['url'].encode('utf-8')
		except Exception as error:
			#logging.basicConfig(filename="whatcms.log", level=logging.INFO)
			#logging.log(error)
			print error
		return item

	def close_spider(self, spider):
		self.connect.close();
