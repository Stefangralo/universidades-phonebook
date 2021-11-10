import scrapy


class UcaSpider(scrapy.Spider):
    name = 'uca'
    start_urls = ['https://transparencia.uca.es/claustro-profesores-dpto/?dpto=D106']

    def parse(self, response):
        for personal_data in response.css('div.personal_data'):
            yield {
                'name': personal_data.css('.name::text').extract()
            }