import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

import django
django.setup()

from newstep.models import Category, Page


def populate():
    inn_cat = add_cat('Innovation')

    add_page(cat=inn_cat,
        title="Innovation in Genetic Engineering",
        url="http://www.environmentindex.com/en/article/innovation-in-genetic-engineering-dna-based-test-for-the-inspection-of-food-product-quality-53.aspx")

    add_page(cat=inn_cat,
        title="Tesla electric car innovation",
        url="https://www.youtube.com/watch?v=AEqRYx97j9I")

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

#for c in Category.objects.all():
#    for p in Page.objects.filter(category=c):
#    	print ("- {0} - {1}").format(str(c), str(p))



if __name__ == '__main__':
    print ("Starting Newstep population script...")

populate()
