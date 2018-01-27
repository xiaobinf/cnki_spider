# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class CnkispiderPipeline(object):
    def process_item(self, item, spider):
        filename="patent.txt"
        # with open("patent.txt","a") as f:
        #     f.write(item['patentName']+'\n'+item['applicationNum']+'\n'+item['applicationDay']+'\n'+item['publicNum']+'\n'+item['publicDay']+'\n'+item['applicant']+'\n'+item['location']+'\n')
        patentItem=[item['patentName'],item['applicationNum'],item['applicationDay'],item['publicNum'],item['publicDay'],item['applicant'], item['location'],item['inventor'],item['patentAgency'],item['agent'],item['countryCode'],item['abstract'],item['sovereign'],item['pages'],item['mainCategoryNumber'],item['patentCategoryNumber']]
        with open('patent.csv','a') as f:
            writer=csv.writer(f)
            writer.writerow(patentItem)
        return item
