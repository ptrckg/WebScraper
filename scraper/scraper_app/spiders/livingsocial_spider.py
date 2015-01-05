from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(BaseSpider):
    """
    """
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["https://www.livingsocial.com/cities/187-syracuse"]
    
    deals_list_xpath = '//li[@dealid]'
    item_fields = {'title': '',
                   'link': './/a/@href',
                   'description': '',
                   'category': '',
                   'location': '',
                   'original_price': '',
                   'price': ''}
    
    def parse(self, response):
        """
        """
        selector = HtmlXPathSelector(response)
        
        # iterate through deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)
            
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()
            
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()