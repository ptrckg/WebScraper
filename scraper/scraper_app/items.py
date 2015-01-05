from scrapy.item import Item, Field


class LivingSocialDeal(Item):
    """LivingSocial container for scraped data"""
    title = Field()
    description = Field()
    link = Field()
    category = Field()
    location = Field()
    original_price = Field()
    price = Field()