import scrapy
import pandas as pd
from kasper.items import KasperItem

class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["uel.ac.uk"]
    df = pd.read_csv('uel.csv')
    start_urls = df['urls'].tolist()

    def start_requests(self):
        for url in self.start_urls:
            self.logger.warning(f'Scraping {url}')
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        fees = response.css('div.coh-container.fees-funding-paragraph.fees-funding-ajax.coh-ce-2b1d158a article div.coh-container.fees-tbl-data.coh-ce-5d63392c div::text').extract()
        intake = response.css('td.coh-container.row-body.start-date-width p::text')
        course_duration = response.css('td.coh-container.row-body.attendance-width li::text')
        try:
            requirements_initial = response.xpath('//h3[text()="Accepted Qualifications"]')[0]
            requirements = requirements_initial.xpath('..').css('li span::text')
            if not requirements:
                requirements = requirements_initial.xpath('..').css('li::text')
                if not requirements:
                    requirements = requirements_initial.xpath('..').css('p::text')
        except IndexError:
            requirements_initial = ''

        course_location = response.css('h4.coh-heading.coh-ce-fb89dca7 div::text')

        item = KasperItem()
        item['course_url'] = response.url
        splitted_url = item['course_url'].split('/')
        item['course_type'] = splitted_url[-3].title()
        item['course_title'] = splitted_url[-1].replace('-', ' ').title()
        item['course_code'] = splitted_url[-1].split('-')[0].title()
        try:
            item['course_fees_uk'] = fees[0].replace('£', '').replace(',', '')
        except IndexError:
            item['course_fees_uk'] = ''
        try:
            item['course_fees_int'] = fees[1].replace('£', '').replace(',', '')
        except IndexError:
            item['course_fees_int'] = ''
        item['course_intake'] = intake.extract_first().strip()
        item['course_duration'] = course_duration.extract_first().strip()
        item['data_requirements'] = requirements.extract()
        item['course_location'] = course_location.extract_first().strip()
        yield item