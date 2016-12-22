# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.http import Request


class WavSpider(scrapy.Spider):
    name = "wav"
    allowed_domains = ["ektoplazm.com"]

    def __init__(self, style='darkpsy', *args, **kwargs):
        super(WavSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.ektoplazm.com/style/%s' % style]

    def parse(self, response):
        reg = '//div[@class="post"]//a[contains(@href, "WAV")]/@href'
        nextpage = None
        pagespan = response.xpath('//span[@class="pages"]').extract_first()
        pagearray = pagespan.split(' of ')
        pagecountspan = pagearray[1]
        pagecountarray = pagecountspan.split('</span>')
        pagecount = pagecountarray[0]
        arrayresponse = response.url.split('/page/')
        if len(arrayresponse) > 1 and int(arrayresponse[1]) <= int(pagecount):
            nextpage = str(arrayresponse[0])+'/page/'+str(int(arrayresponse[1])+1)
        elif len(arrayresponse) == 1:
            nextpage = response.url+'/page/2'
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
        if nextpage:
            yield Request(
                    url=nextpage,
                    callback=self.parse
                )
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
