from django.core.management.base import BaseCommand
from django.db.models import Sum, Min, Max, Avg, Count
from shop.models import Item, Category, Tag

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        one_category = Category.objects.filter(id=1).aggregate(count=Count('items'))
        print(one_category)


        min_max_avg = Item.objects.aggregate(
            min=Min('price'), 
            max=Max('price'), 
            avg = Avg('price'))
        
        print(min_max_avg)

        categories = Category.objects.annotate(count=Count('items'))
        for category in categories:
            print(category.name, category.count)
          
        
        total_sum = Category.objects.annotate(total_sum=Sum('items__price', default = 0))
        for sum in total_sum:
            print(sum.name, sum.total_sum)

        
        items_category = Item.objects.select_related('category')
        for item in items_category:
            print(item.name, item.category.name)

        items_tags = Item.objects.prefetch_related('tags').all()
        for item in items_tags:
            print(item.name, [tag.name for tag in item.tags.all()])
