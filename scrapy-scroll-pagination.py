# -*- coding: utf-8 -*-
import scrapy
import json


class ScrollPaginatonSpider(scrapy.Spider):
    name = 'scroll-paginaton'
    allowed_domains = ['quotes.toscrape.com/scroll']
    site_url = "http://quotes.toscrape.com/api/quotes?page="
    start_urls = [site_url + '1']
    download_delay = 1.5


    def parse(self, response):
                    
            data = json.loads(response.body)
            
            for item in data['quotes']:
                yield {
                      'author': item['author']['name'],
                      'quote' : item['text'],
                      'tags'  : item['tags'],
                      'about' : item['author']['goodreads_link']
                    
                    }
                    
            if data['has_next']:
                next_page = data['page'] + 1
                yield scrapy.Request(self.site_url + str(next_page))


