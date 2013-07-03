from scrapy.item import Item, Field

class PacsItem(Item):
    url = Field()
    name = Field()
    address = Field()
    phone = Field()
    site = Field()

