#https://docs.scrapy.org/en/latest/intro/tutorial.html

import scrapy


class JobSpider(scrapy.Spider):
    """
    A Job Spider crawls the website Fake jobs and extracts all the jobs application URLS
    """
    name = 'job-spider'
    start_urls = ['https://realpython.github.io/fake-jobs/']

    def parse(self, response):
        url_selector = '.card-footer>a:nth-child(2)'
        for url in response.css(url_selector):
            print(url)

        # Todo
        # Extract the Job titles
        job_title_selector = "div.media-content > h2::text"
        for job_title in response.css(job_title_selector):
            print(job_title)
        
# Run from terminal
# scrapy runspider scrapy_scraper.py