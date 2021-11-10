import scrapy


class UexSpider(scrapy.Spider):
    name = 'uex'
    allowed_domains = ['unex.es']
    start_urls = ['https://www.unex.es/conoce-la-uex/departamentos/listado_personal?idDpto=Y006&personal=1']


    def parse(self, response):
        baseurl = 'https://www.unex.es/conoce-la-uex/departamentos'

        for contact in response.css('a[href*=ficha_personal]::attr(href)').getall():
            
            yield scrapy.Request(response.urljoin(contact), self.parse_contact)

    def parse_contact(self,response):
        print(response.css())