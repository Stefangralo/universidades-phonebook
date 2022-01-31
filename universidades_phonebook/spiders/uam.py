import scrapy
from universidades_phonebook.items import UniversidadesPhonebookItem

class UamSpider(scrapy.Spider):
    name = 'uam'
    allowed_domains = ['uam.es']
    start_urls = ['https://www.uam.es/Derecho/PDI-DCONS/1242658739609.htm?language=es&np=1', 'https://www.uam.es/Derecho/PDI-DCONS/1242658739609.htm?language=es&np=2', 'https://www.uam.es/Derecho/PDI-DE/1242658739637.htm?language=es&nodepath=Personal%20Docente%20e%20Investigador']

    def parse(self, response):
        
        for personal_data in response.css('li.noticia.clear'):
            
            item = UniversidadesPhonebookItem()

            item['name'] = personal_data.css('span.tit > a::text').get()
            item['position'] = personal_data.css('div:nth-child(1)::text').get()
            item['phone'] = personal_data.css('div.txt_noticia::text').re_first(r'\d+')
            item['email'] = personal_data.css('div.txt_noticia > a::text').get()
            item['department'] = response.css('#menu_vertical > li > a::text').get()

            yield item
