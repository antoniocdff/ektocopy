# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.http import Request


class WavSpider(scrapy.Spider):
    name = "wav"
    allowed_domains = ["ektoplazm.com"]
    start_urls = [
        'http://www.ektoplazm.com/style/darkpsy',
    ]

    def parse(self, response):
        reg = '//div[@class="post"]//a[contains(@href, "WAV")]/@href'
        for href in response.xpath(reg).extract():
            linkarray = href.split('/files/')
            is_file = self.check_exist(linkarray[1])
            if href.endswith('.rar') and not is_file:
                yield Request(
                    url=response.urljoin(href),
                    callback=self.save_file
                )
            elif is_file:
                self.logger.info('File exists: %s', linkarray[1])
        pass

    def check_exist(self, filename):
        folder = os.getcwd()
        folder = folder + '/' + self.settings.attributes['FILES_STORE'].value + '/'
        fname = folder+filename
        is_file = os.path.isfile(fname)
        return is_file

    def save_file(self, response):
        path = response.url.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(response.body)
