import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.in"]
    start_urls = ["https://www.audible.in/adblbestsellers"]

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]/li')
        for product in product_container:
            product.xpath('.//li[contains(@class , "authorLabel")]')
            
