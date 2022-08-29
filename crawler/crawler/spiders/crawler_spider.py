import json
import scrapy

class CrawlerSpider(scrapy.Spider):
    name = "parallel"

    def start_requests(self):
        urls = [
            'https://testnet.theparallel.io/market/shop/paragon',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)

    def parse_artilce(self, response):
        artilce = {}
        artilce['Paragon'] = response.xpath('//script[@type="application/ld+json"]/text()').extract()
        test = json.dumps(artilce['Paragon'])
        print(test)
  
