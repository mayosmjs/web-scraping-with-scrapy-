# -*- coding: utf-8 -*-
import scrapy


class WholepageSpider(scrapy.Spider):
    name = 'wholepage'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        
        quotes_container = response.css('div.quote')
        
        for quote in quotes_container:
            yield {
                 'author': quote.css('small.author::text').extract_first(),
                 'quote' : quote.css('span.text::text').extract_first(),
                 'tags'  : quote.css('a.tag::text').extract(),
                 'about' : response.urljoin(quote.css('span > a::attr(href)').extract_first())

                }
        next_page_link = response.css('li.next > a::attr(href)').extract_first()
        
        if next_page_link:
            next_url = response.urljoin(next_page_link)
            yield scrapy.Request(url=next_url,callback=self.parse)

       
