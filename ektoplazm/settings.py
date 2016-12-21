BOT_NAME = 'ektoplazm'
SPIDER_MODULES = ['ektoplazm.spiders']
NEWSPIDER_MODULE = 'ektoplazm.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
FILES_STORE = 'albums'
DOWNLOAD_HANDLERS_BASE = {
    'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
    'http': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
    'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
    's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
    'ftp': 'scrapy.core.downloader.handlers.ftp.FTPDownloadHandler',
}
DOWNLOAD_DELAY = 5
DOWNLOAD_MAXSIZE = '5368709120'
DOWNLOAD_WARNSIZE = 0
DOWNLOAD_TIMEOUT = '1800'
LOG_FILE = 'ektoplazm.log'
