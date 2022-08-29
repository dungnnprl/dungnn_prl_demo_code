import scrapy
from scrapy.crawler import CrawlerProcess

class CrawlDemo3(scrapy.Spider):
    name = 'singlemalts'
    def start_requests(self):
        yield scrapy.Request('https://market-api-testnet.theparallel.io/')
    
    def parse(self, response):
        product =response.css('')
