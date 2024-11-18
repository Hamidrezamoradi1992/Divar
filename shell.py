
import os
import random
from time import sleep

import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# logger = logging.getLogger('django.db.backends')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

# from mixer.backend.django import mixer
# from apps.book.models import Author, Book, Category  # noqa:E402
# books = mixer.cycle(10).blend(Book)

# book = Book(title="The 1", price=10000)
# book.save()

# print(Book.objects.all())
# print(Book.objects.all())
# print(Book.objects.deleted())
# print(Book.objects.archive().filter(is_deleted=True))
# print(Book.objects.get(id=9).title)
# print(Book.objects.all())
# print(Book.objects.filter(id__gte=1))
# print("Deleted: ", Book.objects.deleted().undelete())
# print("All: ", Book.objects.all())

# from apps.accounts.models import User
# User.objects.create(email="ismr3@gmailpo.co")

# print(User.objects.all()[0])
# User.objects.create_superuser('yazdan', password="1")
# books = mixer.cycle(10).blend(Book)

# send mail:
# from django.core.mail import send_mail
# send_mail("subject of test mail", "this is message ...", "maktab@mryazdan.ir", recipient_list=[
#     "ismryazdan@gmail.com"
# ])
# from service.email import EmailService
# from time import time
#
# mail = (
#     "Welcome",
#     "ismryazdan@gmail.com",
#     "mail/welcome.html",
# )
#
# start_time = time()
# mail.send()
# print(f"{time()-start_time}s")
# s = EmailService('hamid', 'test.html', "hamidreza@gmail.com", context={})
# print(s)
# from apps.loger.models import Log
# from django.contrib.auth.models import User
# from django.contrib.contenttypes.models import ContentType
# user=User.objects.get(pk=1)
# content=ContentType.objects.get(model='user')
# object_ide=user.id
# c=Log.objects.create(user=user,content_type=content,object_id=object_ide)
# print(Log.objects.filter(content_type=content,object_id=object_ide))

# @receiver(pre_save, sender=MyModel)
# def on_change(sender, instance: MyModel, **kwargs):
#     if instance.id is None: # new object will be created
#         pass # write your code here
#     else:
#         previous = MyModel.objects.get(id=instance.id)
#         if previous.field_a != instance.field_a: # field will be updated
#             pass  # write your code here


# from mixer.backend.django import mixer
# from django.contrib.auth import get_user_model
# from apps.advertising.models import Advertising, Category
#
# user = get_user_model().objects.get(id=1)
#
# # Creating a category instance to be used as a foreign key
# category = Category.objects.filter(pk=1)
#
# # Generating fake data for the Advertising model using mixer
# ad_instance = mixer.blend(
#     Advertising,
#     title=mixer.FAKE,                # Auto-generates a fake title
#     description=mixer.FAKE,          # Auto-generates a fake description
#     price=mixer.faker.random_number(digits=5),  # Generates a random price
#     diffusion=mixer.faker.boolean(),
#     ladder=mixer.faker.boolean(),
#     category=category,               # Using the created category
#     user=user                        # Using the created user
# )
#
# print(ad_instance)  # Prints the generated Advertising instance
from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.advertising.models import Advertising
# valid_ladder_advertising = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=1).first())
# valid_ladder_advertising1 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=3).first())
# valid_ladder_advertising3 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=2).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=4).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=5).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=6).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=7).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=8).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=9).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=10).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=11).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=12).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=12).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=11).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=10).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=9).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=8).first())
# valid_ladder_advertising4 = ValidateLadderAdvertising(queryset=Advertising.objects.filter(id=4).first())
# print('hamid',len(valid_ladder_advertising._LADDER_INSTANCE))
print(ValidateLadderAdvertising.get_ladder_advertising())


# sleep(2)
#
# random.sample(['red', 'blue'], counts=[4, 2], k=5)

# sleep(2)
# print('hamid',(valid_ladder_advertising._LADDER_INSTANCE))



# import random
#
# # دیکشنری نمونه
# data = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': 'value4'
# }
#
# # انتخاب یک کلید به صورت رندوم
# random_key = random.choice(list(data.keys()))
# random_value = data[random_key]
#
# # print(f"Random key: {random_key}, Random value: {random_value}")
#
# # اگر بخواهید چندین عنصر را به صورت تصادفی انتخاب کنید
# random_items = random.sample(list(data.items()), 2)  # عدد 2 تعداد عناصر انتخابی است
# print("Random items:", random_items)