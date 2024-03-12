# import the required modules
import os
from datetime import datetime
from scrapy.spiders import Spider
 
class PokemonSpider(Spider):
    # Init
    name = 'pokemon'
    scraped_date = datetime.today().strftime("%Y-%m-%d")
    start_urls = ['https://scrapeme.live/product-category/pokemon/']
    custom_settings = {
        "FEEDS": {
            "s3://%(bucket_name)s/%(name)s/%(name)s_%(job_id)s_%(scraped_date)s.jl": { "format": "jsonlines" }
        }
    }

    def __init__(
            self,
            bucket_name: str,
            published_date: str,
            *args,
            **kwargs):
        self.job_id = kwargs.get('_job')
        self.bucket_name = bucket_name
        self.published_date = published_date
        super(PokemonSpider, self).__init__(*args, **kwargs)
 
    # parse HTML page as response
    def parse(self, response):
        # extract text content from the ul element
        self.logger.info(f"Published date: {self.published_date}")
        products = response.css('ul.products li.product')
 
        for product in products:
            # parent = product.css('li.product')
            product_name = product.css('h2.woocommerce-loop-product__title::text').get()
            price = product.css('span.woocommerce-Price-amount::text').get()
 
            # append the scraped data into the empty data array
            data = {
                'product_name': product_name,
                'price': price,
            }

            yield data
