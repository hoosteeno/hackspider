hackspider
==========

spider hacks.mozilla.org finding pages with images that have pixel dimensions in their URLs.

not recommended for general use since it is terribly impolite to spider people's websites.

usage: 
* scrapy crawl hackspider -o items.json
* (then do some undocumented commandline magic to make items.json unique, but still valid JSON)
* cp items.json site/js/data.json
* open in a website like http://hacks-images-broken.bitballoon.com/
* see all the broken images
