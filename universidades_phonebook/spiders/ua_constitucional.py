import scrapy
from universidades_phonebook.items import UniversidadesPhonebookItem


class Ua_Constitucional_Spider(scrapy.Spider):
    name = 'ua_constitucional'
    allowed_domains = ['ua.es']
    start_urls = ['https://web.ua.es/servicios/ws2.php?plengua=C&pcoddep=B113&pcodarea=135&servicioweb=wsprofdep&wsid=53F8B513']

    def parse(self, response):
        
        
        jsonresponse = response.json()
        selector = scrapy.Selector(text=jsonresponse['html'])

        for personal_data in selector.css('tbody > tr'):
            
            item = UniversidadesPhonebookItem()
            item['name'] = personal_data.css('td:nth-child(1)::text').get()
            item['phone'] = personal_data.css('td:nth-child(2)::text').get()
            item['email'] = personal_data.css('td:nth-child(3)::text').get()
            item['department'] = 'Derecho Constitucional'

            yield item