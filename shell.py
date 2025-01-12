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
# from apps.advertising.utils.validate_ladder_advertising import ValidateLadderAdvertising
from apps.advertising.models import Advertising, Category
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
# print(ValidateLadderAdvertising.get_ladder_advertising())


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

# from django.conf import settings
# import requests
# import json
#
# # ? sandbox merchant
# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'
#
# ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
#
# amount = 1000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080/verify/'
#
#
# def send_request(request):
#     data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Description": description,
#         "Phone": phone,
#         "CallbackURL": CallbackURL,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     try:
#         response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
#
#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
#                         'authority': response['Authority']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response
#
#     except requests.exceptions.Timeout:
#         return {'status': False, 'code': 'timeout'}
#     except requests.exceptions.ConnectionError:
#         return {'status': False, 'code': 'connection error'}
#
#
# def verify(authority):
#     data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Authority": authority,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
#
#     if response.status_code == 200:
#         response = response.json()
#         if response['Status'] == 100:
#             return {'status': True, 'RefID': response['RefID']}
#         else:
#             return {'status': False, 'code': str(response['Status'])}
#     return response

from mixer.backend.django import mixer
from apps.advertising.models import FieldCategory, CategoryField, Category
from apps.advertising.models import State, City
from faker import Faker

# fake = Faker()
# states = [
#     'alborz',
#     'ardabil',
#     'isfahan',
#     'east_azerbaijan',
#     'west_azerbaijan',
#     'bushehr',
#     'chaharmahal_and_bakhtiari',
#     'fars',
#     'gilan',
#     'golestan',
#     'hamadan',
#     'hormozgan',
#     'kerman',
#     'kermanshah',
#     'khuzestan',
#     'lorestan',
#     'markazi',
#     'mazandaran',
#     'qazvin',
#     'qom',
#     'semnan',
#     'sistan_and_baluchestan',
#     'tehran',
#     'yazd',
#     'zanjan'
# ]
# provinces_and_cities = {
#     'alborz': ['Karaj', 'Mohammadshahr', 'Hasanabad', 'Fardis', 'Golestan', 'Kahrizak', 'Taleqan', 'Nazarabad'],
#     'ardabil': ['Ardabil', 'Namin', 'Meshkinshahr', 'Ghazvin', 'Siahkal', 'Bileh Savar', 'Parsabad'],
#     'Isfahan': ['Isfahan', 'Kashan', 'Najafabad', 'Semirom', 'Khomain', 'Golpayegan', 'Fereydunkenar'],
#     'east_azerbaijan': ['Tabriz', 'Maragheh', 'Ahar', 'Bostanabad', 'Hashtrood', 'Osko', 'Sarab', 'Kaleybar'],
#     'west_azerbaijan': ['Urmia', 'Khoy', 'Salmas', 'Piranshahr', 'Bukan', 'Chaldoran', 'Naghadeh'],
#     'bushehr': ['Bushehr', 'Kangan', 'Deylam', 'Genaveh', 'Bassij', 'Borazjan'],
#     'chaharmahal_and_bakhtiari': ['Shahr-e Kord', 'Lordegan', 'Farsan', 'Kiar', 'Bojnurd', 'Bakhtegan'],
#     'fars': ['Shiraz', 'Marvdasht', 'Fasa', 'Jahrom', 'Kazerun', 'Lar', 'Mamasani'],
#     'gilan': ['Rasht', 'Siahkal', 'Astara', 'Fuman', 'Lahijan', 'Langarud', 'Talesh'],
#     'golestan': ['Gorgan', 'Aliabad', 'Minudasht', 'Kordkuy', 'Aghala', 'Galikesh'],
#     'hamadan': ['Hamadan', 'Bahar', 'Malayer', 'Nehavand', 'Asadabad', 'Toos', 'Lahijan'],
#     'hormozgan': ['Bandar Abbas', 'Minab', 'Jask', 'Qeshm', 'Hormuz', 'Haji Abad'],
#     'kerman': ['Kerman', 'Sirjan', 'Bam', 'Rostam', 'Jiroft', 'Zarand'],
#     'kermanshah': ['Kermanshah', 'Ghasr Shirin', 'Javanrud', 'Kangavar', 'Eslam Abad'],
#     'khuzestan': ['Ahvaz', 'Abadan', 'Khorramshahr', 'Shush', 'Andimeshk', 'Izeh'],
#     'morestan': ['Khorramabad', 'Dorood', 'Borujerd', 'Aligudarz', 'Selseleh'],
#     'markazi': ['Arak', 'Saveh', 'Khomein', 'Khondab', 'Delijan'],
#     'mazandaran': ['Sari', 'Babol', 'Noshahr', 'Amol', 'Chalus', 'Tonekabon'],
#     'qazvin': ['Qazvin', 'Alvand', 'Takestan', 'Bojnurd', 'Avaj'],
#     'qom': ['Qom', 'Koharshahr'],
#     'semnan': ['Semnan', 'Garmsar', 'Shahrud', 'Mehrafshan', 'Khoshkrud'],
#     'sistan and Baluchestan': ['Zahedan', 'Zabol', 'Iranshahr', 'Chabahar', 'Saravan'],
#     'tehran': ['Tehran', 'Shemiranat', 'Rey', 'Islamshahr', 'Pardis', 'Damavand', 'Varamin', 'Farahzad',
#                'Gonbad Qabus', 'Sarbandar', 'Nazariyeh', 'Eslamshahr', 'Rudaki', 'Tajrish',
#                'Baharistan', 'Shahrak-e Gharb', 'Narmak'],
#     'yazd': ['Yazd', 'Ashkezar', 'Taft', 'Mahdishahr', 'Bafq', 'Nain'],
#     'zanjan': ['Zanjan', 'Mahneshan', 'Tarom', 'Ain al-Huda', 'Eli', 'Ghazvin'],
# }
#
# # Loop through each province and create cities
#
# for state in states:
#     try:
#         State.objects.create(title=state)
#     except Exception as e:
#         print('state: ', state, e)
# for province, cities in provinces_and_cities.items():
#     try:
#         state = State.objects.get(title=province)  # Retrieve the state using the exact title
#         for city in cities:
#             City.objects.create(title=city, state_id=state.pk)  # Create a city linked to its state
#     except Exception as e:
#         print(f'province :{province} City:{city} error:{e}')
#
# # داده‌های نمونه برای برندها و مدل‌ها
# # داده‌های نمونه برای دسته‌بندی ماشین‌ها، لوازم خانگی، تجهیزات الکترونیکی و املاک
# category_data = {
#     'vehicles': {
#         'cars': {
#             'sedans': {
#                 'compact': {},
#                 'mid_size': {},
#                 'full_size': {}
#             },
#             'suvs': {
#                 'compact_suv': {},
#                 'midsize_suv': {},
#                 'full_size_suv': {}
#             },
#             'trucks': {
#                 'light_trucks': {},
#                 'heavy_trucks': {}
#             },
#             'vans': {
#                 'minivans': {},
#                 'cargo_vans': {}
#             }
#         },
#         'motorcycles': {
#             'sport_bikes': {},
#             'cruisers': {},
#             'touring_bikes': {}
#         },
#         'electric_vehicles': {
#             'sedans': {},
#             'suvs': {},
#             'trucks': {}
#         },
#         'bicycles': {
#             'mountain_bikes': {},
#             'road_bikes': {},
#             'hybrid_bikes': {}
#         }
#     },
#     'home_appliances': {
#         'kitchen_appliances': {
#             'refrigerators': {
#                 'double_door': {},
#                 'single_door': {},
#                 'side_by_side': {},
#                 'mini_fridge': {}
#             },
#             'microwaves': {
#                 'convection': {},
#                 'grill': {},
#                 'solo': {}
#             },
#             'ovens': {
#                 'built_in': {},
#                 'countertop': {}
#             },
#             'blenders': {
#                 'hand_blender': {},
#                 'table_blender': {},
#                 'juicer': {}
#             }
#         },
#         'washing_machines': {
#             'front_load': {},
#             'top_load': {},
#             'semi_auto': {}
#         },
#         'vacuum_cleaners': {
#             'robot_vacuum': {},
#             'upright_vacuum': {},
#             'canister_vacuum': {}
#         },
#         'air_conditioners': {
#             'window_ac': {},
#             'split_ac': {},
#             'portable_ac': {}
#         },
#         'heaters': {
#             'ceramic_heater': {},
#             'oil_heater': {},
#             'fan_heater': {}
#         }
#     },
#     'electronics': {
#         'televisions': {
#             'led_tv': {
#                 '4k': {},
#                 '1080p': {},
#                 'smart_tv': {}
#             },
#             'lcd_tv': {},
#             'plasma_tv': {}
#         },
#         'audio_systems': {
#             'home_theater': {},
#             'soundbar': {},
#             'portable_speakers': {}
#         },
#         'computers': {
#             'laptops': {
#                 'gaming': {},
#                 'business': {},
#                 'ultrabooks': {}
#             },
#             'desktops': {
#                 'all_in_one': {},
#                 'gaming_desktops': {}
#             }
#         },
#         'cameras': {
#             'dslr': {},
#             'mirrorless': {},
#             'action_cameras': {}
#         },
#         'mobile_devices': {
#             'smartphones': {
#                 'android': {},
#                 'ios': {}
#             },
#             'tablets': {
#                 'android_tablets': {},
#                 'ipad': {}
#             }
#         }
#     },
#     'real_estate': {
#         'residential': {
#             'houses': {
#                 'single_family': {},
#                 'multi_family': {},
#                 'townhouses': {}
#             },
#             'apartments': {
#                 'studio': {},
#                 '1_bedroom': {},
#                 '2_bedroom': {}
#             },
#             'villas': {}
#         },
#         'commercial': {
#             'offices': {
#                 'small_offices': {},
#                 'large_offices': {}
#             },
#             'retail_spaces': {
#                 'shops': {},
#                 'malls': {}
#             },
#             'warehouses': {}
#         },
#         'land': {
#             'residential_lots': {},
#             'commercial_lots': {},
#             'agricultural_land': {}
#         }
#     },
#     'other': {
#         'furniture': {
#             'living_room': {},
#             'bedroom': {},
#             'office': {},
#             'outdoor': {}
#         },
#         'garden_tools': {
#             'lawn_mowers': {},
#             'trimmers': {},
#             'shovels': {},
#             'gardening_kits': {}
#         },
#         'pets': {
#             'dogs': {},
#             'cats': {},
#             'fish': {},
#             'birds': {}
#         }
#     }
# }
#
#
# # تابع برای ایجاد دسته‌بندی‌ها
# def create_categories(category_data, parent=None):
#     for title, subcategories in category_data.items():
#         # ایجاد یک دسته‌بندی جدید
#         category = Category(title=title, parent=parent)
#         category.save()  # ذخیره دسته‌بندی در پایگاه داده
#
#         # بررسی وجود زیر دسته‌بندی‌ها و ایجاد آن‌ها
#         if subcategories:
#             create_categories(subcategories, parent=category)
#
#
# create_categories(category_data)


fields = FieldCategory.objects.all()
categories = ['compact', 'mid_size', 'full_size', 'compact_suv', 'midsize_suv', 'full_size_suv', 'light_trucks',
            'heavy_trucks', 'minivans', 'cargo_vans', 'sport_bikes', 'cruisers', 'touring_bikes', 'sedans', 'suvs',
            'trucks', 'mountain_bikes', 'road_bikes', 'hybrid_bikes', 'double_door', 'single_door', 'side_by_side',
            'mini_fridge', 'convection', 'grill', 'solo', 'built_in', 'countertop', 'hand_blender', 'table_blender',
            'juicer', 'front_load', 'top_load', 'semi_auto', 'robot_vacuum', 'upright_vacuum', 'canister_vacuum',
            'window_ac', 'split_ac', 'portable_ac', 'ceramic_heater', 'oil_heater', 'fan_heater', '4k', '1080p',
            'smart_tv', 'lcd_tv', 'plasma_tv', 'home_theater', 'soundbar', 'portable_speakers', 'gaming', 'business',
            'ultrabooks', 'all_in_one', 'gaming_desktops', 'dslr', 'mirrorless', 'action_cameras', 'android', 'ios',
            'android_tablets', 'ipad', 'single_family', 'multi_family', 'townhouses', 'studio', '1_bedroom',
            '2_bedroom', 'villas', 'small_offices', 'large_offices', 'shops', 'malls', 'warehouses', 'residential_lots',
            'commercial_lots', 'agricultural_land', 'living_room', 'bedroom', 'office', 'outdoor', 'lawn_mowers',
            'trimmers', 'shovels', 'gardening_kits', 'dogs', 'cats', 'fish', 'birds']

for category in categories:
    cat = Category.objects.filter(title=category).first()
    if cat:
        for field in fields:
            CategoryField.objects.create(category_id=cat, fieldcategory_id=field)
    else:
        print(f"Category '{category}' does not exist.")
