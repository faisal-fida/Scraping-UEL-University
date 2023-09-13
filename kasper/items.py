import scrapy


class KasperItem(scrapy.Item):
    course_url = scrapy.Field()
    course_title = scrapy.Field()
    course_duration = scrapy.Field()
    course_code = scrapy.Field()
    course_type = scrapy.Field()
    course_title = scrapy.Field()
    
    course_fees_uk = scrapy.Field()
    course_fees_int = scrapy.Field()
    course_location = scrapy.Field()
    course_intake = scrapy.Field()

    data_requirements = scrapy.Field()
    




