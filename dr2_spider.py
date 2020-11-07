import scrapy


class DR2Spider(scrapy.Spider):
    name = 'dr_indland'
    start_urls = [
        'https://www.dr.dk/nyheder/indland',
    ]

    def parse(self, response):
        titles = set()
        a_selectors = response.xpath("//a")
        for selector in a_selectors:
            text = selector.xpath("@aria-label").extract_first()
            if text is not None:
                titles.add(text)

        for title in titles:
            print(title)


