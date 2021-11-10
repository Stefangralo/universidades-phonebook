import scrapy
from universidades_phonebook.items import UniversidadesPhonebookItem

class UcaSpider(scrapy.Spider):
    name = 'uca'
    start_urls = ['https://transparencia.uca.es/claustro-profesores-dpto/?dpto=D106', 'https://transparencia.uca.es/claustro-profesores-dpto/?dpto=D107']

    def parse(self, response):

        for personal_data in response.css('div.personal_data'):

            item = UniversidadesPhonebookItem()
            
            item['name'] = personal_data.css('.name::text').get()
            item['position'] = personal_data.css('p.position::text').get()
            item['phone'] = personal_data.css('p.phone::text').get()
            item['department'] = response.css('div.col-md-9.mainContent').css('h1::text').get()

            yield item
