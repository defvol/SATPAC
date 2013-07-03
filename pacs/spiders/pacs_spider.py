from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from pacs.items import PacsItem

class PacsSpider(CrawlSpider):
    name = "pacs"
    allowed_domains = ["sat.gob.mx"]
    start_urls = [
        "http://www.sat.gob.mx/sitio_internet/asistencia_contribuyente/principiantes/comprobantes_fiscales/66_19264.html"
    ]
    rules = [Rule(SgmlLinkExtractor(allow=['/66_\d+.html']), 'parse_provider')]

    def parse_provider(self, response):
        x = HtmlXPathSelector(response)

        provider = PacsItem()
        provider['url'] = response.url
        provider['name'] = x.select("//div[@class='titulo_contint']/text()").extract()
        provider['address'] = x.select("//div[@class='contenidoSAT']/ul//li[4]/text()").extract()
        provider['phone'] = x.select("//div[@class='contenidoSAT']/ul//li[5]/text()").extract()
        provider['site'] = x.select("//div[@class='contenidoSAT']/ul//li[6]/a/text()").extract()
        return provider

