# -*- coding: utf-8 -*-
import scrapy
import csv
from cnkiSpider.items import CnkispiderItem

class PatentspiderSpider(scrapy.Spider):
    name = 'patentSpider'
    allowed_domains = ['http://dbpub.cnki.net']
    patentUrls=[]
    with open('patentUrls.csv','r') as f:
        reader=csv.reader(f)
        for row in reader:
            patentUrls = row
    start_urls = patentUrls

    def parse(self, response):
        items=[]
        item=CnkispiderItem()
        # item['patentName']=response.xpath('//title//text()').extract()[0]
        item['patentName'] = response.xpath('/html/body/table[1]/tr/td[2]//text()').extract()[0]
        item['applicationNum'] = response.xpath('/html/body/table[2]/tr[1]/td[2]//text()').extract()[0][1:]
        item['applicationDay'] = response.xpath('/html/body/table[2]/tr[1]/td[4]//text()').extract()[0][1:]
        item['publicNum'] = response.xpath('/html/body/table[2]/tr[2]/td[2]//text()').extract()[0][1:]
        item['publicDay'] = response.xpath('/html/body/table[2]/tr[2]/td[4]//text()').extract()[0][1:]
        item['applicant'] = response.xpath('/html/body/table[2]/tr[3]/td[2]//text()').extract()[0][1:]
        item['location'] = response.xpath('/html/body/table[2]/tr[3]/td[4]//text()').extract()[0][1:]
        item['inventor'] = response.xpath('/html/body/table[2]/tr[5]/td[2]//text()').extract()[0][1:]
        item['patentAgency'] = response.xpath('/html/body/table[2]/tr[8]/td[2]//text()').extract()[0][1:]
        item['agent'] = response.xpath('/html/body/table[2]/tr[8]/td[4]//text()').extract()[0][1:]
        item['countryCode']=response.xpath('/html/body/table[2]/tr[10]/td[2]//text()').extract()[0][1:]
        item['abstract']=response.xpath('/html/body/table[2]/tr[11]/td[2]//text()').extract()[0][1:]
        item['sovereign']=response.xpath('/html/body/table[2]/tr[12]/td[2]//text()').extract()[0][1:]
        item['pages']=response.xpath('/html/body/table[2]/tr[13]/td[2]//text()').extract()[0][1:]
        item['mainCategoryNumber']=response.xpath('/html/body/table[2]/tr[14]/td[2]//text()').extract()[0][1:]
        item['patentCategoryNumber']=response.xpath('/html/body/table[2]/tr[15]/td[2]//text()').extract()[0][1:]


        items.append(item)
        return items
