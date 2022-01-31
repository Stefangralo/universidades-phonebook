import scrapy
from universidades_phonebook.items import UniversidadesPhonebookItem


class UaEclesiasticoSpider(scrapy.Spider):
    name = 'ua_eclesiastico'
    allowed_domains = ['ua.es']
    start_urls = ['https://dchj.ua.es/es/eclesiastico/profesorado-area-derecho-eclesiastico.html']

    def parse(self, response):
        
        for contact in response.css('a[href*=FichaPersona]'):

            contact_url = contact.css('::attr(href)').get()
            name = contact.css('::text').get()
            yield scrapy.Request(contact_url, self.parse_contact, meta = {'name': name})

    def parse_contact(self, response):
        
        item = UniversidadesPhonebookItem()

        item['name'] = response.meta.get('name')
        item['email'] = response.css('.bloque_datos').css('li:nth-child(1) > a::text').get()
        item['phone'] = response.css('.bloque_datos').css('li:nth-child(2)::text').re_first(r'\d+ \d+')
        
        yield item