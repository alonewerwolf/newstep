from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)
        views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        slug = models.SlugField()

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __str__(self):  
                return self.name
        def get_absolute_url(self):
            return reverse('newstep.views.category', args=[self.slug])
        @property
        def get_products(self):
            return Category.objects.filter(category=self.name)

        class Meta:
            managed = False     
            db_table = 'category' 
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):     
        return self.title
    class Meta:
        managed = False
        db_table = 'page'       	