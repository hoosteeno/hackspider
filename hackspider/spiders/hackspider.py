from scrapy import Spider, Item, Field

class Page(Item):
    img = Field()

class HackSpider(Spider):
    name = 'hackspider'
    start_urls = ['http://hacks.mozilla.org']
    allowed_domains = ['hacks.mozilla.org']

    def parse(self, response):
        #print(response.css("img").xpath('@src').extract())
        return [Page(img = e.extract()) for e in response.css("img").xpath('@src')]

