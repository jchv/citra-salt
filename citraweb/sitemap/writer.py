import datetime
from decimal import Decimal
from django.http import HttpResponse
from django.utils.encoding import smart_text
from django.utils.feedgenerator import SyndicationFeed
from django.utils.xmlutils import SimplerXMLGenerator
import six


class Url(object):
    CHANGEFREQ_ALWAYS = 'always'
    CHANGEFREQ_HOURLY = 'hourly'
    CHANGEFREQ_DAILY = 'daily'
    CHANGEFREQ_WEEKLY = 'weekly'
    CHANGEFREQ_MONTHLY = 'monthly'
    CHANGEFREQ_YEARLY = 'yearly'
    CHANGEFREQ_NEVER = 'never'
    CHANGEFREQ_CHOICES = (
        (CHANGEFREQ_ALWAYS, 'always'),
        (CHANGEFREQ_HOURLY, 'hourly'),
        (CHANGEFREQ_DAILY, 'daily'),
        (CHANGEFREQ_WEEKLY, 'weekly'),
        (CHANGEFREQ_MONTHLY, 'monthly'),
        (CHANGEFREQ_YEARLY, 'yearly'),
        (CHANGEFREQ_NEVER, 'never')
    )
    CHANGEFREQ_VALUES = [CHANGEFREQ_ALWAYS, CHANGEFREQ_HOURLY, CHANGEFREQ_DAILY,
                         CHANGEFREQ_WEEKLY, CHANGEFREQ_MONTHLY, CHANGEFREQ_YEARLY,
                         CHANGEFREQ_NEVER]

    def __init__(self, loc=None, lastmod=None, changefreq=None, priority=None):
        self.loc = loc
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.priority == priority

        if self.loc:
            self.loc = smart_text(self.loc)
            assert isinstance(self.loc, six.string_types), "`loc` should be a string."

        if self.lastmod:
            assert isinstance(self.lastmod, datetime.date), "`lastmod` should be a datetime.date"

        if self.changefreq:
            self.changefreq = smart_text(self.changefreq)
            assert isinstance(self.changefreq, six.string_types), "`changefreq` should be a string."

        if self.priority:
            self.priority = Decimal(self.priority)
            assert 0.0 <= self.priority <= 1.0, "`priority` should be a number."


class Sitemap(object):
    mime_type = 'application/xml; charset=utf-8'

    def __call__(self, request, *args, **kwargs):
        response = HttpResponse(content_type=self.mime_type)
        self.write(response, 'utf-8')
        return response

    def write(self, outfile, encoding):
        self.handler = SimplerXMLGenerator(outfile, encoding)
        self.handler.startDocument()
        self.handler.startElement("urlset", {'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'})
        self.write_urls(self.get_urls())
        self.handler.endElement("urlset")

    def write_urls(self, urls):
        for url in urls:
            self.write_url(url)

    def write_url(self, url: Url):
        self.handler.startElement('url', {})
        self.handler.addQuickElement('loc', url.loc)
        if url.lastmod:
            self.handler.addQuickElement('lastmod', url.lastmod.strftime('%Y-%m-%d'))
        if url.changefreq:
            self.handler.addQuickElement('changefreq', url.changefreq)
        self.handler.addQuickElement('priority', url.priority)
        self.handler.endElement('url')

