from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext_lazy as _
from blog.models import Post


class RssBlogFeed(Feed):
    title = _("Citra-emu blog")
    link = "/sitenews/"
    description = _("Updates regarding the citra-emu emulator.")

    def items(self):
        return Post.objects.order_by('-date_published')[:10]

    def item_description(self, item):
        return item.content_brief


class AtomBlogFeed(RssBlogFeed):
    feed_type = Atom1Feed
    subtitle = RssBlogFeed.description


atom = AtomBlogFeed()
rss = RssBlogFeed()
