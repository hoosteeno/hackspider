import re
from scrapy import Item, Field, Spider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class Page(Item):
    url = Field()
    imgs = Field()

class HackSpider(CrawlSpider):
#class HackSpider(Spider):
    name = "hackspider"
    allowed_domains = ["hacks.mozilla.org"]
    start_urls = ["http://hacks.mozilla.org"]

    rules = (
        Rule(LinkExtractor(deny=(
            '.*hacks\.mozilla\.org\/author.*', 
            '.*\/by\.*/', 
            '.*\/as\/.*', 
            '.*\/comment-page/.*',
        )), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
    #def parse(self, response):
        imgs = []

        for e in response.css("img").xpath("@src"):
            img = e.extract()
            if (re.search('-\d+x\d+\.(png|jpg|gif)', img)):
                imgs.append(img)

        if imgs:
            return Page(url=response.url, imgs=imgs)

