import os
import random
from time import sleep

import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from mixer.backend.django import mixer
from apps.advertising.models import FieldCategory, CategoryField, Category
from apps.advertising.models import State, City
from faker import Faker

fake = Faker()
states = [
    'alborz',
    'ardabil',
    'isfahan',
    'east_azerbaijan',
    'west_azerbaijan',
    'bushehr',
    'chaharmahal_and_bakhtiari',
    'fars',
    'gilan',
    'golestan',
    'hamadan',
    'hormozgan',
    'kerman',
    'kermanshah',
    'khuzestan',
    'lorestan',
    'markazi',
    'mazandaran',
    'qazvin',
    'qom',
    'semnan',
    'sistan_and_baluchestan',
    'tehran',
    'yazd',
    'zanjan'
]
provinces_and_cities = {
    'alborz': ['Karaj', 'Mohammadshahr', 'Hasanabad', 'Fardis', 'Golestan', 'Kahrizak', 'Taleqan', 'Nazarabad'],
    'ardabil': ['Ardabil', 'Namin', 'Meshkinshahr', 'Ghazvin', 'Siahkal', 'Bileh Savar', 'Parsabad'],
    'isfahan': ['Isfahan', 'Kashan', 'Najafabad', 'Semirom', 'Khomain', 'Golpayegan', 'Fereydunkenar'],
    'east_azerbaijan': ['Tabriz', 'Maragheh', 'Ahar', 'Bostanabad', 'Hashtrood', 'Osko', 'Sarab', 'Kaleybar'],
    'west_azerbaijan': ['Urmia', 'Khoy', 'Salmas', 'Piranshahr', 'Bukan', 'Chaldoran', 'Naghadeh'],
    'bushehr': ['Bushehr', 'Kangan', 'Deylam', 'Genaveh', 'Bassij', 'Borazjan'],
    'chaharmahal_and_bakhtiari': ['Shahr-e Kord', 'Lordegan', 'Farsan', 'Kiar', 'Bojnurd', 'Bakhtegan'],
    'fars': ['Shiraz', 'Marvdasht', 'Fasa', 'Jahrom', 'Kazerun', 'Lar', 'Mamasani'],
    'gilan': ['Rasht', 'Astara', 'Fuman', 'Lahijan', 'Langarud', 'Talesh'],
    'golestan': ['Gorgan', 'Aliabad', 'Minudasht', 'Kordkuy', 'Aghala', 'Galikesh'],
    'hamadan': ['Hamadan', 'Bahar', 'Malayer', 'Nehavand', 'Asadabad', 'Toos'],
    'hormozgan': ['Bandar Abbas', 'Minab', 'Jask', 'Qeshm', 'Hormuz', 'Haji Abad'],
    'kerman': ['Kerman', 'Sirjan', 'Bam', 'Rostam', 'Jiroft', 'Zarand'],
    'kermanshah': ['Kermanshah', 'Ghasr Shirin', 'Javanrud', 'Kangavar', 'Eslam Abad'],
    'khuzestan': ['Ahvaz', 'Abadan', 'Khorramshahr', 'Shush', 'Andimeshk', 'Izeh'],
    'morestan': ['Khorramabad', 'Dorood', 'Borujerd', 'Aligudarz', 'Selseleh'],
    'markazi': ['Arak', 'Saveh', 'Khomein', 'Khondab', 'Delijan'],
    'mazandaran': ['Sari', 'Babol', 'Noshahr', 'Amol', 'Chalus', 'Tonekabon'],
    'qazvin': ['Qazvin', 'Alvand', 'Takestan', 'Avaj'],
    'qom': ['Qom', 'Koharshahr'],
    'semnan': ['Semnan', 'Garmsar', 'Shahrud', 'Mehrafshan', 'Khoshkrud'],
    'sistan and Baluchestan': ['Zahedan', 'Zabol', 'Iranshahr', 'Chabahar', 'Saravan'],
    'tehran': ['Tehran', 'Shemiranat', 'Rey', 'Islamshahr', 'Pardis', 'Damavand', 'Varamin', 'Farahzad', 'Gonbad Qabus',
               'Sarbandar', 'Nazariyeh', 'Eslamshahr', 'Rudaki', 'Tajrish', 'Baharistan', 'Shahrak-e Gharb', 'Narmak'],
    'yazd': ['Yazd', 'Ashkezar', 'Taft', 'Mahdishahr', 'Bafq', 'Nain'],
    'zanjan': ['Zanjan', 'Mahneshan', 'Tarom', 'Ain al-Huda', 'Eli'],
}

# state_objects = [State(title=state) for state in states]
# State.objects.bulk_create(state_objects)
#
# city_objects = []
# for province, cities in provinces_and_cities.items():
#     try:
#         state = State.objects.get(title=province)
#         for city in cities:
#             city_objects.append(City(title=city, state_id=state.pk))
#     except Exception as e:
#         print(f'province :{province} error:{e}')
#
# City.objects.bulk_create(city_objects)

category_data = {
    'vehicles': {
        'cars': {
            'sedans': {
                'compact': {},
                'mid_size': {},
                'full_size': {}
            },
            'suvs': {
                'compact_suv': {},
                'midsize_suv': {},
                'full_size_suv': {}
            },
            'trucks': {
                'light_trucks': {},
                'heavy_trucks': {}
            },
            'vans': {
                'minivans': {},
                'cargo_vans': {}
            }
        },
        'motorcycles': {
            'sport_bikes': {},
            'cruisers': {},
            'touring_bikes': {}
        },
        'electric_vehicles': {
            'sedans': {},
            'suvs': {},
            'trucks': {}
        },
        'bicycles': {
            'mountain_bikes': {},
            'road_bikes': {},
            'hybrid_bikes': {}
        }
    },
    'home_appliances': {
        'kitchen_appliances': {
            'refrigerators': {
                'double_door': {},
                'single_door': {},
                'side_by_side': {},
                'mini_fridge': {}
            },
            'microwaves': {
                'convection': {},
                'grill': {},
                'solo': {}
            },
            'ovens': {
                'built_in': {},
                'countertop': {}
            },
            'blenders': {
                'hand_blender': {},
                'table_blender': {},
                'juicer': {}
            }
        },
        'washing_machines': {
            'front_load': {},
            'top_load': {},
            'semi_auto': {}
        },
        'vacuum_cleaners': {
            'robot_vacuum': {},
            'upright_vacuum': {},
            'canister_vacuum': {}
        },
        'air_conditioners': {
            'window_ac': {},
            'split_ac': {},
            'portable_ac': {}
        },
        'heaters': {
            'ceramic_heater': {},
            'oil_heater': {},
            'fan_heater': {}
        }
    },
    'electronics': {
        'televisions': {
            'led_tv': {
                '4k': {},
                '1080p': {},
                'smart_tv': {}
            },
            'lcd_tv': {},
            'plasma_tv': {}
        },
        'audio_systems': {
            'home_theater': {},
            'soundbar': {},
            'portable_speakers': {}
        },
        'computers': {
            'laptops': {
                'gaming': {},
                'business': {},
                'ultrabooks': {}
            },
            'desktops': {
                'all_in_one': {},
                'gaming_desktops': {}
            }
        },
        'cameras': {
            'dslr': {},
            'mirrorless': {},
            'action_cameras': {}
        },
        'mobile_devices': {
            'smartphones': {
                'android': {},
                'ios': {}
            },
            'tablets': {
                'android_tablets': {},
                'ipad': {}
            }
        }
    },
    'real_estate': {
        'residential': {
            'houses': {
                'single_family': {},
                'multi_family': {},
                'townhouses': {}
            },
            'apartments': {
                'studio': {},
                '1_bedroom': {},
                '2_bedroom': {}
            },
            'villas': {}
        },
        'commercial': {
            'offices': {
                'small_offices': {},
                'large_offices': {}
            },
            'retail_spaces': {
                'shops': {},
                'malls': {}
            },
            'warehouses': {}
        },
        'land': {
            'residential_lots': {},
            'commercial_lots': {},
            'agricultural_land': {}
        }
    },
    'other': {
        'furniture': {
            'living_room': {},
            'bedroom': {},
            'office': {},
            'outdoor': {}
        },
        'garden_tools': {
            'lawn_mowers': {},
            'trimmers': {},
            'shovels': {},
            'gardening_kits': {}
        },
        'pets': {
            'dogs': {},
            'cats': {},
            'fish': {},
            'birds': {}
        }
    }
}

# def create_categories(category_data, parent=None):
#     for title, subcategories in category_data.items():
#
#         category = Category(title=title, parent=parent)
#         category.save()
#
#         if subcategories:
#             create_categories(subcategories, parent=category)
#
#
# create_categories(category_data)

from apps.advertising.models import FieldCategory

unique_fields = {
    "brand": "str",
    "model": "str",
    "year": "int",
    "mileage": "int",
    "color": "str",
    "price": "int",
    "status": "str",
    "engine_capacity": "int",
    "battery_type": "str",
    "range_per_charge": "int",
    "type": "str",
    "wheel_size": "int",
    "frame_material": "str",
    "capacity": "int",
    "energy_source": "str",
    "warranty": "int",
    "motor_power": "int",
    "energy_consumption": "int",
    "fuel_type": "str",
    "heating_power": "int",
    "screen_size": "int",
    "resolution": "str",
    "output_power": "int",
    "processor": "str",
    "ram": "int",
    "storage": "int",
    "gpu": "str",
    "internal_storage": "int",
    "camera_specifications": "str",
    "refresh_rate": "int",
    "area": "int",
    "rooms": "int",
    "bathrooms": "int",
    "year_built": "int",
    "property_type": "str",
    "location": "str",
    "usage": "str",
    "material": "str",
    "quantity": "int",
    "breed": "str",
    "age": "int",
    "health_status": "str"
}

# # ء FieldCategory
# field_categories = [FieldCategory(title=key,  type_field=value)for key, value in unique_fields.items()]
#
#
# try:
#     FieldCategory.objects.bulk_create(field_categories)
#     print("Field categories created successfully.")
# except Exception as e:
#     print(f"Error creating field categories: {e}")
#

category_data = {
    'vehicles': {
        'compact': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'mid_size': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'full_size': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'compact_suv': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'midsize_suv': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'full_size_suv': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'light_trucks': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'heavy_trucks': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'minivans': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'cargo_vans': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'sport_bikes': {"brand", "model", "year", "mileage", "color", "engine_capacity", "price"},
        'cruisers': {"brand", "model", "year", "mileage", "color", "engine_capacity", "price"},
        'touring_bikes': {"brand", "model", "year", "mileage", "color", "engine_capacity", "price"},
        'sedans': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'suvs': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'trucks': {"brand", "model", "year", "mileage", "color", "engine_capacity", "fuel_type", "price"},
        'mountain_bikes': {"brand", "model", "year", "mileage", "color", "engine_capacity", "price"},
        'road_bikes': {"brand", "model", "year", "mileage", "color", "engine_capacity", "price"},
        'hybrid_bikes': {"brand", "model", "year", "mileage", "color", "engine_capacity", "price"}
    },
    'home_appliances': {
        'double_door': {"brand", "capacity", "price", "energy_source", "warranty"},
        'single_door': {"brand", "capacity", "price", "energy_source", "warranty"},
        'side_by_side': {"brand", "capacity", "price", "energy_source", "warranty"},
        'mini_fridge': {"brand", "capacity", "price", "energy_source", "warranty"},
        'convection': {"brand", "capacity", "price", "energy_source", "warranty"},
        'grill': {"brand", "capacity", "price", "energy_source", "warranty"},
        'solo': {"brand", "capacity", "price", "energy_source", "warranty"},
        'built_in': {"brand", "capacity", "price", "energy_source", "warranty"},
        'countertop': {"brand", "capacity", "price", "energy_source", "warranty"},
        'hand_blender': {"brand", "price", "warranty", "power"},
        'table_blender': {"brand", "price", "warranty", "power"},
        'juicer': {"brand", "price", "warranty", "power"},
        'front_load': {"brand", "price", "warranty", "capacity"},
        'top_load': {"brand", "price", "warranty", "capacity"},
        'semi_auto': {"brand", "price", "warranty", "capacity"},
        'robot_vacuum': {"brand", "price", "warranty", "power"},
        'upright_vacuum': {"brand", "price", "warranty", "power"},
        'canister_vacuum': {"brand", "price", "warranty", "power"},
        'window_ac': {"brand", "price", "warranty", "power"},
        'split_ac': {"brand", "price", "warranty", "power"},
        'portable_ac': {"brand", "price", "warranty", "power"},
        'ceramic_heater': {"brand", "price", "warranty", "heating_power"},
        'oil_heater': {"brand", "price", "warranty", "heating_power"},
        'fan_heater': {"brand", "price", "warranty", "heating_power"}
    },
    'electronics': {
        '4k': {"brand", "screen_size", "price", "resolution"},
        '1080p': {"brand", "screen_size", "price", "resolution"},
        'smart_tv': {"brand", "screen_size", "price", "resolution"},
        'lcd_tv': {"brand", "screen_size", "price", "resolution"},
        'plasma_tv': {"brand", "screen_size", "price", "resolution"},
        'home_theater': {"brand", "output_power", "price"},
        'soundbar': {"brand", "output_power", "price"},
        'portable_speakers': {"brand", "output_power", "price"},
        'gaming': {"brand", "processor", "ram", "storage", "price"},
        'business': {"brand", "processor", "ram", "storage", "price"},
        'ultrabooks': {"brand", "processor", "ram", "storage", "price"},
        'all_in_one': {"brand", "processor", "ram", "storage", "price"},
        'gaming_desktops': {"brand", "processor", "ram", "storage", "price"},
        'dslr': {"brand", "camera_specifications", "price"},
        'mirrorless': {"brand", "camera_specifications", "price"},
        'action_cameras': {"brand", "camera_specifications", "price"},
        'android': {"brand", "processor", "ram", "storage", "price"},
        'ios': {"brand", "processor", "ram", "storage", "price"},
        'android_tablets': {"brand", "processor", "ram", "storage", "price"},
        'ipad': {"brand", "processor", "ram", "storage", "price"}
    },
    'real_estate': {
        'single_family': {"price", "area", "rooms", "bathrooms", "year_built"},
        'multi_family': {"price", "area", "rooms", "bathrooms", "year_built"},
        'townhouses': {"price", "area", "rooms", "bathrooms", "year_built"},
        'studio': {"price", "area", "rooms", "bathrooms", "year_built"},
        '1_bedroom': {"price", "area", "rooms", "bathrooms", "year_built"},
        '2_bedroom': {"price", "area", "rooms", "bathrooms", "year_built"},
        'villas': {"price", "area", "rooms", "bathrooms", "year_built"},
        'small_offices': {"price", "area", "rooms", "bathrooms", "year_built"},
        'large_offices': {"price", "area", "rooms", "bathrooms", "year_built"},
        'shops': {"price", "area", "rooms", "bathrooms", "year_built"},
        'malls': {"price", "area", "rooms", "bathrooms", "year_built"},
        'warehouses': {"price", "area", "rooms", "bathrooms", "year_built"},
        'residential_lots': {"price", "area"},
        'commercial_lots': {"price", "area"},
        'agricultural_land': {"price", "area"}
    },
    'other': {
        'living_room': {"material", "color", "quantity"},
        'bedroom': {"material", "color", "quantity"},
        'office': {"material", "color", "quantity"},
        'outdoor': {"material", "color", "quantity"},
        'lawn_mowers': {"brand", "type", "price"},
        'trimmers': {"brand", "type", "price"},
        'shovels': {"brand", "type", "price"},
        'gardening_kits': {"brand", "quantity", "price"},
        'dogs': {"breed", "age", "health_status"},
        'cats': {"breed", "age", "health_status"},
        'fish': {"breed", "age", "health_status"},
        'birds': {"breed", "age", "health_status"}
    }
}
# field_objeect = []
# for parent in category_data.values():
#     print(parent)
#     for chail in parent.keys():
#         print(chail)
#         cat_id = Category.objects.filter(title=chail).first()
#         field = list(parent[chail])
#         print(field)
#         fields = FieldCategory.objects.filter(title__in=field)
#         for fieldies in fields:
#             field_objeect.append(CategoryField(category_id=cat_id, fieldcategory_id=fieldies))
# CategoryField.objects.bulk_create(field_objeect)
from apps.advertising.models import Advertising
from django.utils import timezone
from datetime import timedelta
advertise=Advertising.objects.all().update(expires_at=timezone.now()+timedelta(minutes=1))