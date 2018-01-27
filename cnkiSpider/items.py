# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnkispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    patentName=scrapy.Field()
    applicationNum=scrapy.Field()
    applicationDay=scrapy.Field()
    publicNum=scrapy.Field()
    publicDay=scrapy.Field()
    applicant=scrapy.Field()
    location=scrapy.Field()
    inventor=scrapy.Field()
    patentAgency=scrapy.Field()
    agent=scrapy.Field()
    countryCode=scrapy.Field()
    abstract=scrapy.Field()
    sovereign=scrapy.Field()
    pages=scrapy.Field()
    mainCategoryNumber=scrapy.Field()
    patentCategoryNumber=scrapy.Field()

