from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from uuslug import slugify
import reversion


@reversion.register
class Post(models.Model):
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Authorship')
    tags = models.ManyToManyField('Tag')
    title = models.CharField(max_length=128)
    title_seo = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=128)

    content_brief = models.TextField()
    content = models.TextField()
    image = models.ImageField(null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField()
    date_published = models.DateTimeField(null=True, blank=True)

    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-view', args=[self.slug])

    def save(self, update_mtime=True, **kwargs):
        # A '...' by itself will act as our 'read more' tag.
        i = self.content.find('\n...\n')
        if i >= 0:
            self.content_brief = self.content[:i]
            self.content = self.content.replace('\n...\n', '\n')
        else:
            self.content_brief = self.content[:200]
            if len(self.content) > 200:
                self.content_brief += '...'

        # When inserting, perform certain normalization.
        if not self.pk:
            # Automatically calculate slug with UUSlug.
            if self.slug == '':
                self.slug = slugify(self.title)

            # Slug exists? Try suffixing.
            if Post.objects.filter(slug=self.slug):
                base = self.slug
                for i in range(1, 10):
                    self.slug = '{base}-{suffix}'.format(base=base, suffix=str(i))
                    if not Post.objects.filter(slug=self.slug):
                        break

        if self.title_seo == '':
            self.title_seo = self.title

        # We use this instead of auto_now to allow 'quiet' saves
        if update_mtime or self.date_modified is None:
            self.date_modified = datetime.now()

        # If we're publishing, set the date published.
        if self.is_published and self.date_published is None:
            self.date_published = self.date_modified

        super().save(**kwargs)


class Authorship(models.Model):
    ROLE_WRITER = 'wr'
    ROLE_EDITOR = 'ed'
    ROLE_ARTIST = 'ar'
    ROLE_CHOICES = (
        (ROLE_WRITER, 'Writer'),
        (ROLE_EDITOR, 'Editor'),
        (ROLE_ARTIST, 'Artist')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    char_count = models.IntegerField()
    edit_count = models.IntegerField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=2)


class Tag(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
