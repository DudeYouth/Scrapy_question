# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):
    # define the fields for your item here like:
    # 问题
    question = scrapy.Field()
    # 选项
    options = scrapy.Field()
    # 等级
    level = scrapy.Field()
    # 答案
    answer = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 课目
    subject = scrapy.Field()
    pass
