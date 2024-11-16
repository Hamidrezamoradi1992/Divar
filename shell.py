
import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# logger = logging.getLogger('django.db.backends')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

# from mixer.backend.django import mixer
# from apps.book.models import Author, Book, Category  # noqa:E402

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