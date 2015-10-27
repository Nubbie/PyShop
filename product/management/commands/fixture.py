from django.core.management.base import BaseCommand, CommandError
from product.models import Category, Picture, Product
import os
from os import path
from django.conf import settings


class Command(BaseCommand):
    help = "inject fixture data"

    def handle(self, **options):
        categories = [
            ("کلاه", "انواع کلاه ها با رنگبندی های مختلف برای آقایان و بانوان"),
            ("عینک", "عینک های آفتابی متنوع با کیفیت عالی"),
            ("ساعت مچی", "ساعت مچی متناسب برای زیباپسندان"),
            ("انگشتر", "انواع انگشتر های زیبا و جذاب"),
            ("کیف پول", "انواع کیف پول پارچه ای و چرمی "),
        ]

        for category_data in categories:
            c = Category()
            c.title, c.description = category_data
            c.save()
        hat_images_path = path.join(settings.BASE_DIR, "media", "hat")
        pictures = [f for f in os.listdir(hat_images_path) if
                    path.isfile(os.path.join(hat_images_path, f))]
        hat_product_data = [
            ("چنار", "کلاه ساده و زیبا", 12000),
            ("روزگار", "یک کلاه متفاوت و زیبا", 16000),
            ("یادگار", "سازگار با هر نوع تیپ", 20000),
            ("نوین", "شکلی و ساده", 10000),
            ("جوانی", "کلاه مناسب نسل جوان", 22000),
            ("سحاب", "کلاه خاص برای افراد خاص", 18000),
            ("چنار", "کلاه ساده و زیبا", 12000),
            ("روزگار", "یک کلاه متفاوت و زیبا", 16000),
            ("یادگار", "سازگار با هر نوع تیپ", 20000),
            ("نوین", "شکلی و ساده", 10000),
            ("جوانی", "کلاه مناسب نسل جوان", 22000),
            ("سحاب", "کلاه خاص برای افراد خاص", 18000),
            ("چنار", "کلاه ساده و زیبا", 12000),
            ("روزگار", "یک کلاه متفاوت و زیبا", 16000),
            ("یادگار", "سازگار با هر نوع تیپ", 20000),
            ("نوین", "شکلی و ساده", 10000),
            ("جوانی", "کلاه مناسب نسل جوان", 22000),
            ("سحاب", "کلاه خاص برای افراد خاص", 18000),

        ]
        hat_category = Category.objects.filter(pk=1).first()

        for hat in hat_product_data:
            p = Product()
            p.name, p.description, p.price = hat
            p.category = hat_category
            p.save()
            pic = Picture()
            pic.path.name = "hat/" + pictures.pop()
            pic.product = p
            pic.save()
