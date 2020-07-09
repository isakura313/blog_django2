from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')


class Post(models.Model):
    """ Так как это у нас модель, то мы  здесь определяем
        через класс, какие у нас будут колонки
    """
    STATUS_CHOICES = (('draft', 'Draft'), ('published', "Published"))
    title = models.CharField(max_length= 250) #заголовок нашего поста
    slug = models.SlugField(max_length=250, unique_for_date='publish') # здесь у нас будет путь нашего Поста
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_post')
    body = models.TextField() #основное содержимое нашего поста
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length= 10, choices= STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog_part:post_detail',
                       args = [self.slug])


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

