import re
from scrapy import Item, Field, Spider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class Page(Item):
    url = Field()
    imgs = Field()

class HackSpider(CrawlSpider):
    name = "hackspider"
    allowed_domains = ["hacks.mozilla.org"]
    start_urls = ["http://hacks.mozilla.org"]

    rules = (
        Rule(LinkExtractor(unique=True, 
            deny=(
                '.*\/author\/.*', 
                '.*\/by\.*/', 
                '.*\/as\/.*', 
                '.*\/comment\-page.*',
                '.*\/articles\/.*',
                '.*\/replytocom\/.*',
                '^https.*',
            ),
            # using categories as our index gives us the simplest ruleset
            allow=(
                '.*\/category\/.*',
                '.*\/\d{4}\/\d{2}\/.*',
            )
        ), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        imgs = []

        for e in response.css("img").xpath("@src"):
            img = e.extract()
            if (re.search('-\d+x\d+\.(png|jpg|gif)', img)):
                imgs.append(img)

        if imgs:
            return Page(url=response.url, imgs=imgs)

