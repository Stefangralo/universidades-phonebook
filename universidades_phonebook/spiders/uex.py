import scrapy

from universidades_phonebook.items import UniversidadesPhonebookItem


class UexSpider(scrapy.Spider):
    name = 'uex'
    allowed_domains = ['unex.es']
    start_urls = ['https://www.unex.es/conoce-la-uex/departamentos/listado_personal?idDpto=Y006&personal=1']


    def parse(self, response):
        
        baseurl = 'https://www.unex.es/conoce-la-uex/departamentos'

        

        for contact in response.css('a[href*=ficha_personal]::attr(href)').getall():
            
            yield scrapy.Request(response.urljoin(contact), self.parse_contact)

    def parse_contact(self,response):
        
        item = UniversidadesPhonebookItem()
        
        item['name'] = response.css('div[class=dpto] h3 span::text').get()
        item['email'] = response.css('div[class=dpto] div a[href*=mailto]::text').get()
        item['subject'] = response.css('div[class=dpto] span:nth-of-type(3)::text').get()
        item['position'] = response.css('div[class=dpto] span:nth-of-type(2) span::text').get()
        item['department'] = response.css('div[id=content-core] h3 span::text').get()


        yield item