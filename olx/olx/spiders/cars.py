import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    # allowed_domains = ['olx.com.br']
    start_urls = ['https://olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']

    def parse(self, response):
        items = response.xpath('//*[@id="ad-list"]/li')
        for item in items:
            self.log(item.xpath('./a/@href').get())

# //body/div[@id='root']/div[@id='content']/div[2]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[10]/div[1]/div[1]/div[1]
# response.xpath("//span[contains(text(),'Ano')]/following-sibling::a/text()").get()
