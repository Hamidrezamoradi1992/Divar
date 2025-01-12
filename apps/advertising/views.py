from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from apps.core.permissions import SiteAdmin, SuperUser
from apps.core.tasks import send_email
from datetime import timedelta
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from itertools import chain
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from apps.advertising.models import Advertising, Category, City, State, Image, SaveValueField
from apps.advertising.serializers import (AllAdvertisingViewSerializer,
                                          MainFieldCategorySerializer,
                                          MainCategorySerializer,
                                          AddAdvertisingSerializer,
                                          AddAdvertisingImageSerializer,
                                          MainSaveValueFieldSerializer,
                                          MainStateSerializer,
                                          MainCitySerializer,
                                          AdminAdvertisingViewSerializer,
                                          AllAdvertiseViewSerializer,
                                          AllRetrieveAdvertisingViewSerializer,
                                          filterCategorySerializer, AcceptedAdvertisingSerializer)
from .utils.validate_ladder_advertising import ValidateLadderAdvertising
from ..favorite.models import Favorite
from ..payment.models import Order, OrderItem

# Create your views here.
"""all advertising"""


class DetailAdvertiseView(RetrieveAPIView):
    """
      - view all advertising

            {
                "id": 1,
                "title": "hamid1",
                "description": "hamid moradi 1992",
                "price": 2000.0,
                "image": [
                    {
                        "id": 1,
                        "alt": "advertising_image",
                        "content_type": 10,
                        "instance_id": 1,
                        "file": "/storage/media/file_field/images.png"
                    },
                    {
                        "id": 2,
                        "alt": "advertising_image",
                        "content_type": 10,
                        "instance_id": 1,
                        "file": "/storage/media/file_field/images_1.jpeg"
                    },
                    {
                        "id": 3,
                        "alt": "advertising_image",
                        "content_type": 10,
                        "instance_id": 1,
                        "file": "/storage/media/file_field/2.jpg"
                    },
                    {
                        "id": 4,
                        "alt": "advertising_image",
                        "content_type": 10,
                        "instance_id": 1,
                        "file": "/storage/media/file_field/images.jpeg"
                    },
                    {
                        "id": 5,
                        "alt": "advertising_image",
                        "content_type": 10,
                        "instance_id": 1,
                        "file": "/storage/media/file_field/1.jpeg"
                    },
                    {
                        "id": 6,
                        "alt": "advertising_image",
                        "content_type": 10,
                        "instance_id": 1,
                        "file": "/storage/media/file_field/1_OCCx7FI.jpeg"
                    }
                ],
                "category": {
                    "id": 6,
                    "title": "pearent 2.4",
                    "parent": {
                        "id": 5,
                        "title": "parent 2.3",
                        "parent": {
                            "id": 4,
                            "title": "p[arent 2.2",
                            "parent": {
                                "title": "",
                                "free": false,
                                "fields": [],
                                "price": null,
                                "image": null
                            },
                            "free": true,
                            "fields": [],
                            "price": 0.0,
                            "image": null
                        },
                        "free": true,
                        "fields": [],
                        "price": 0.0,
                        "image": null
                    }
                },
                "state": {
                    "id": 1,
                    "title": "tehran",
                    "area_code": "021"
                },
                "city": {
                    "id": 1,
                    "state": 1,
                    "title": "tehran"
                },
                "vlue_field": [
                    {
                        "value": "123",
                        "name_field": "field1 int",
                        "field_type": "int"
                    },
                    {
                        "value": "12.35",
                        "name_field": "field 2     float",
                        "field_type": "float"
                    },
                    {
                        "value": "hamid1992",
                        "name_field": "field3 str",
                        "field_type": "str"
                    }
                ],
                "address": {
                    "massage": "is user not authentication"
                }
            }




    """
    queryset = Advertising.objects.archive()
    serializer_class = AllRetrieveAdvertisingViewSerializer
    permission_classes = []


from rest_framework.pagination import PageNumberPagination



# # swagger
class AllAdvertisingView(ListAPIView):
    """
      - view all advertising


        [
            {
                "id": 23,
                "title": "dfasf222",
                "price": 222.0,
                "image": {
                    "alt": "",
                    "content_type": null,
                    "instance_id": null,
                    "file": null
                },
                "favorite": false
            },
            ...
        ]

    """
    queryset = Advertising.objects.is_diffusion()
    serializer_class = AllAdvertiseViewSerializer
    pagination_class = PageNumberPagination
    permission_classes = []

    def get_queryset(self):
        ladder = ValidateLadderAdvertising.get_ladder_advertising(categories_id=None)
        if ladder is not None:
            advertising2 = list(chain(ladder, list(Advertising.objects.is_diffusion())))
        else:
            advertising2 = Advertising.objects.is_diffusion()
        advertising2 = list({ad.id: ad for ad in advertising2}.values())
        return advertising2


# swagger
# class ViewAdvertisingForCategory(APIView):
#     """
#       - view all advertising
#
#
#         {
#
#
#              {
#
#                       "id": 1,
#                       "title": "advertise1",
#                       "description": "name",
#                       "price": 25000.0,
#                       "image": [],
#                       "diffusion": true,
#                       "category": {
#                           "title": "hamid1",
#                           "parent": null,
#                           "free": true,
#                           "fields":
#
#                           [
#
#                               {
#
#                                   "id": 6,
#                                   "title": "value1",
#                                   "type_field": "int",
#                                   "mandatory": true
#                               },
#
#                               {
#
#                                   "id": 7,
#                                   "title": "value2",
#                                   "type_field": "int",
#                                   "mandatory": true
#                               },
#
#                               {
#
#                                   "id": 8,
#                                   "title": "value3",
#                                   "type_field": "int",
#                                   "mandatory": true
#                               }
#                           ],
#
#                           "price": 0.0
#                       },
#
#                       "state":
#
#                       {
#                           "id": 1,
#                           "title": "tehran",
#                           "area_code": "021"
#                       },
#
#                       "city":
#
#                       {
#
#                           "id": 1,
#                           "state": 1,
#                           "title": "tehran"
#                       },
#
#                       "vlue_field":
#
#                       [
#
#                           {
#
#                               "id": 4,
#                               "advertising": 1,
#                               "category": 11,
#                               "field": 8,
#                               "value": "123",
#                               "name_field": "value3"
#                           }
#                       ],
#
#
#                       "address":
#                       [
#
#                           {
#
#                               "id": 4,
#                               "email": "11@gmail.com",
#                               "phone": null,
#                               "is_kyc": false,
#                               "address": null
#                           }
#                       ]
#              }
#         }
#
#
#     """
#     serializer_class = AllAdvertisingViewSerializer
#     permission_classes = []
#
#     def get(self, request, category_id=None, *args, **kwargs):
#         if category_id is not None:
#             if Category.objects.filter(pk=category_id).exists():
#                 category = Category.objects.get(pk=category_id)
#                 categories = category.get_descendants(include_self=True)
#                 advertising = Advertising.objects.filter(category__in=categories).order_by('-created_at')
#                 ladder = ValidateLadderAdvertising.get_ladder_advertising(categories_id=categories)
#                 if ladder is not None:
#                     advertising2 = list(chain(ladder, list(advertising)))
#                 else:
#                     advertising2 = advertising
#
#                 serializer = self.serializer_class(advertising2, many=True)
#                 serializer.context['request'] = request
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_404_NOT_FOUND)


"""all advertising"""


# swagger

class AddAdvertiseView(APIView):
    """
        - create new advertising
            - input

            {

                'title': ['name'],
                'price': '96555',
                'description': 'name',
                'category': '5',
                'state': '1',
                'city': '1',
                'user': '2'
             }


            - accepted

                {

                    'advertise': '25'
                }

            - reject

                {

                    'error': {--------------------------}
                }


    """
    permission_classes = []

    # add new advertising
    def post(self, request):
        serializer = AddAdvertisingSerializer(data=request.data)
        if serializer.is_valid():
            advertise = serializer.save()
            return Response({'advertise': advertise.id}, status=status.HTTP_200_OK)
        print(serializer.data)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# swagger
class UploadAdvertiseImageView(APIView):
    """
        - upload image
            -input

                {

                    'advertising': ['89'],
                    'image':
                        [
                            <InMemoryUploadedFile: 2.jpg (image/jpeg)>,
                            <InMemoryUploadedFile: 2.jpg (image/jpeg)>,
                            <InMemoryUploadedFile: 2.jpg (image/jpeg)>,
                            <InMemoryUploadedFile: 2.jpg (image/jpeg)>,
                            <InMemoryUploadedFile: 2.jpg (image/jpeg)>,
                            <InMemoryUploadedFile: 2.jpg (image/jpeg)>
                        ]
                }

            - out put add image

                - accepted

                        {

                            'massage':'compliant add image'
                        }


                - reject

                     {
                        'error': 'advertising error'
                     }

                    {

                    'error': {--------------------------}
                    }
    """

    permission_classes = []
    parser_classes = [MultiPartParser, FileUploadParser]
    serializer_class = AddAdvertisingImageSerializer

    def post(self, request):
        content_type = ContentType.objects.get(model='advertising')
        advertising = Advertising.objects.archive().filter(pk=request.data['advertising']).exists()
        if advertising:
            for image in request.FILES.getlist('image'):
                data_type = {
                    'file': image,
                    'content_type': content_type.id,
                    'instance_id': request.data['advertising']}
                serializer = self.serializer_class(data=data_type, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'massage': 'compliant add image'}, status=status.HTTP_200_OK)
        return Response({'error': 'advertising error'}, status=status.HTTP_400_BAD_REQUEST)


# swagger
class AddFieldAdvertiseView(APIView):
    """
        - add field advertising and get field category advertising
            - method GET

            [

                {
                    'id': 1,
                    'title':
                    'field 1 int',
                    'type_field': 'int',
                    'mandatory': True
                }
                .
                .
                .
                .
                {
                }
            ]

            - reject

                {

                    'massage':'category not found'
                }


                {

                    'massage':'BAD REQUEST'
                }


            - method POST

                {

                    'field 1 int': '415',
                    'field 2 str': 'hamid',
                    'field 3 float': '12.3',
                    'field 4 bool': 'on',
                    'category': '4',
                    'advertising': '91'
                }

    - reject

                {

                    'error':[---------------------]
                }


        - accepted

                {

                    'massage': 'compliant add field'
                }


    """
    parser_classes = [MultiPartParser, FormParser]

    # get field category
    def get(self, request, category_id=None):
        if category_id is not None:
            category = Category.objects.filter(pk=category_id)
            if category.exists():
                category = Category.objects.get(pk=category_id).fields.all()
                if category:
                    serializers = MainFieldCategorySerializer(category, many=True)
                    return Response(serializers.data, status=status.HTTP_200_OK)
                return Response({'massage': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'massage': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        category = Category.objects.get(pk=request.data['category']).fields.all().values_list('title', 'id')
        for field in category:
            dict_query = {
                'advertising': request.data['advertising'],
                'category': request.data['category'],
                'field': field[1],
                'value': request.data[field[0]],
            }
            serializer = MainSaveValueFieldSerializer(data=dict_query, partial=True)
            if serializer.is_valid():
                try:
                    serializer.save()
                except Exception as e:
                    field = SaveValueField.objects.filter(advertising=dict_query['advertising'],
                                                          category=dict_query['category'], ).delete()
                    return Response({'error': serializer.errors}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response({'massage': 'compliant add field'}, status=status.HTTP_200_OK)


# @method_decorator(cache_page(10), name='dispatch')

# swagger
class AllCategoryView(APIView):
    """
    - get all categories
        - method GET

    [

        {
        "id": 63,
        "title": "electronics",
        "parent": {
            "title": "",
            "free": false,
            "fields": [],
            "price": null,
            "image": null
        },
        "free": true,
        "fields": [],
        "price": 0.0,
        "image": "/storage/media/kyc/_kyc_images/images_3.png"
        },...

    ]

    - requesst : https//domain/advertising/api/add/advertise/all_category/{category_id}
        - method GET
        [

        {
        "id": 63,
        "title": "electronics",
        "parent": {
            "title": "",
            "free": false,
            "fields": [],
            "price": null,
            "image": null
        },
        "free": true,
        "fields": [],
        "price": 0.0,
        "image": "/storage/media/kyc/_kyc_images/images_3.png"
        },...

    ]

    """
    serializer_class = MainCategorySerializer
    queryset = Category.objects.all()
    permission_classes = []

    def get(self, request, category_id=None):
        print('re', request)
        if category_id is not None:
            if Category.objects.filter(pk=category_id).exists():
                category = Category.objects.filter(parent_id=category_id)
                print(category)
                serializers = self.serializer_class(category, many=True)
                return Response(serializers.data, status=status.HTTP_200_OK)

        else:
            category = Category.objects.filter(parent_id=None)
            print(category)
            category_id_parent = Category.objects.all().values_list('parent_id',
                                                                    flat=True)
            categories = [i for i in category if i.id in category_id_parent]
            serializers = self.serializer_class(categories, many=True)
            return Response(serializers.data,
                            status=status.HTTP_200_OK)
        return Response({'massage': 'dont category'},
                        status=status.HTTP_404_NOT_FOUND)


# swagger
# @method_decorator(cache_page(10), name='dispatch')
class AllStateView(ListAPIView):
    """
    - all state in db

        - method GET

        [

            {

                "id": 1,
                "title": "tehran",
                "area_code": "021"
            },

            {

                "id": 2,
                "title": "name",
                "area_code": "068"
            }
        ]

    """
    permission_classes = []
    serializer_class = MainStateSerializer
    queryset = State.objects.all()
    pagination_class = None


# swagger
# @method_decorator(cache_page(10), name='dispatch')
class AllCityView(APIView):
    """
    - all state in db

        - method GET

        [

            {

                "id": 2,
                "state": 2,
                "title": "name"
            }
        ]

    """
    serializer_class = MainCitySerializer
    permission_classes = []

    def get(self, request, state_id=None):
        if state_id is not None:
            stata = State.objects.filter(pk=state_id).values_list('id', flat=True)
            if stata.exists():
                city = City.objects.filter(state__in=stata)
                serializers = self.serializer_class(city, many=True)
                return Response(serializers.data,
                                status=status.HTTP_200_OK)
        return Response({'massage': "NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)


""" start admin panel advertising"""


# swagger
class AdvertisingPublishedView(APIView):
    """
        - all published advertising
         - method GET  (is a)

         [
              {
             "id": 16,
             "title": "rgfg",
             "description": "sdfasf",
             "image": {
                 "alt": "",
                 "content_type": null,
                 "instance_id": null,
                 "file": null
             },
             "category": {
                 "id": 12,
                 "title": "light_trucks",
                 "free": false,
                 "price": 330.0,
                 "image": null
             },
             "is_active": true,
             "is_deleted": false,
             "diffusion": true,
             "expires_at": "2024-12-14T22:15:18.747253+03:30"
            },
            ...
         ]

    """

    serializer_class = AdminAdvertisingViewSerializer

    def get(self, request):
        userid = request.user.id
        if userid:
            queryset = Advertising.objects.filter(user=userid, diffusion=True)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'massage': 'user not define'}, status=status.HTTP_400_BAD_REQUEST)


# swagger
class AdvertisingFavoriteView(APIView):
    """
        - get all favorites
            - method GET

            [
                {
                    "id": 9,
                    "title": "jafar46",
                    "description": "Price cannot be greater than 0 for free categories.       jafar",
                    "image": {
                        "alt": "",
                        "content_type": null,
                        "instance_id": null,
                        "file": null
                    },
                    "category": {
                        "id": 116,
                        "title": "agricultural_land",
                        "free": true,
                        "fields": [],
                        "price": 0.0,
                        "image": null
                    },
                    "is_active": true,
                    "is_deleted": false,
                    "diffusion": true,
                    "expires_at": "2025-01-11T21:28:58.923525+03:30"
                }
            ]

    """
    serializer_class = AdminAdvertisingViewSerializer

    def get(self, request):
        user = request.user.id
        favorite = Favorite.objects.filter(user_id=user).values_list('advertising_id', flat=True)
        if favorite.exists():
            advertising = Advertising.objects.filter(pk__in=favorite)
            serializer = self.serializer_class(advertising, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'massage': 'user not favorites '}, status=status.HTTP_400_BAD_REQUEST)


# swagger
class AdvertisingAllView(APIView):
    """
        - all state in db
        - method GET
        [

            {
            "id": 15,
            "title": "office",
            "description": "very good so good location",
            "image": {
                "id": 23,
                "alt": "advertising_image",
                "content_type": 10,
                "instance_id": 15,
                "file": "/storage/media/file_field/images_1.png"
            },
            "category": {
                "id": 108,
                "title": "large_offices",
                "free": false,
                "price": 360.0,
                "image": null
            },
            "is_active": true,
            "is_deleted": false,
            "diffusion": true,
            "expires_at": "2025-01-11T21:40:17.754721+03:30"
            }
        ]

    """
    serializer_class = AdminAdvertisingViewSerializer

    def get(self, request):
        userid = request.user.id
        if userid:
            queryset = Advertising.objects.archive().filter(user=userid)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'massage': 'user not define'}, status=status.HTTP_400_BAD_REQUEST)


# swagger
class AdvertisingAllForPaymentView(APIView):
    """
        - all for payment in db
            - method GET

                    "datas": [
                                {
                                    "id": 7,
                                    "title": "jafar",
                                    "description": "Price cannot be greater than 0 for free categories.",
                                    "image": {
                                        "id": 15,
                                        "alt": "advertising_image",
                                        "content_type": 10,
                                        "instance_id": 7,
                                        "file": "/storage/media/file_field/mlp-img-perf-2024-camaro_Vzck5z1.webp"
                                    },
                                    "category": {
                                        "id": 12,
                                        "title": "light_trucks",
                                        "free": false,
                                        "price": 330.0,
                                        "image": null
                                    },
                                    "is_active": true,
                                    "is_deleted": false,
                                    "diffusion": true,
                                    "expires_at": "2025-01-11T21:32:55.802474+03:30"
                                }
                            ],
                    "order": 20,
                    "total": 40.0

    """
    serializer_class = AdminAdvertisingViewSerializer

    def get(self, request):
        userid = request.user

        orders = Order.objects.filter(user=userid, is_completed=False)

        if orders.exists():
            order_item = OrderItem.objects.filter(order__in=orders).values_list('advertise_id', flat=True)
            advertise = Advertising.objects.archive().filter(pk__in=order_item)
            # queryset = Advertising.objects.archive().filter(user=userid, payed=False)
            serializer = self.serializer_class(advertise, many=True)
            total_price = orders.first().total_order_price
            return Response({"datas": serializer.data,
                             "order": orders.values_list('id', flat=True).first(),
                             "total": total_price
                             }, status=status.HTTP_200_OK)
        return Response({'massage': 'user not define'}, status=status.HTTP_400_BAD_REQUEST)


""""end admin panel advertising"""
"""filter advertising"""


class FilterAdvertising(APIView):
    """
    - all filter advertising
        - request /advertising/api/add/advertise/filter/category/{category_id}
        - method GET
        [
             {
                 "id": 16,
                 "title": "rgfg",
                 "price": 62.0,
                 "image": {
                     "alt": "",
                     "content_type": null,
                     "instance_id": null,
                     "file": null
                 }
             },
             {
                 "id": 7,
                 "title": "jafar",
                 "price": 360.0,
                 "image": {
                     "id": 15,
                     "alt": "advertising_image",
                     "content_type": 10,
                     "instance_id": 7,
                     "file": "/storage/media/file_field/mlp-img-perf-2024-camaro_Vzck5z1.webp"
                 }
             }
        ]

        - request /advertising/api/add/advertise/filter/category/
        - method post

        request{
            {
                'title': [''],
                'city': ['None'],
                'province': ['None'],
                'category': ['']
            }
        }

    -response

          [
             {
                 "id": 16,
                 "title": "rgfg",
                 "price": 62.0,
                 "image": {
                     "alt": "",
                     "content_type": null,
                     "instance_id": null,
                     "file": null
                 }
             },
             {
                 "id": 7,
                 "title": "jafar",
                 "price": 360.0,
                 "image": {
                     "id": 15,
                     "alt": "advertising_image",
                     "content_type": 10,
                     "instance_id": 7,
                     "file": "/storage/media/file_field/mlp-img-perf-2024-camaro_Vzck5z1.webp"
                 }
             }
        ]

    """
    permission_classes = []

    def get(self, request, category_id=None):
        if category_id:
            if not (serializer := cache.get(f'category:{category_id}')):
                category = Category.objects.get(pk=category_id)
                categories = category.get_descendants(include_self=True)
                advertising_category = Advertising.objects.is_diffusion().filter(category_id=category_id)
                ladder = ValidateLadderAdvertising.get_ladder_advertising(categories_id=categories)
                if ladder is not None:
                    advertising2 = list(chain(ladder, list(advertising_category)))
                else:
                    advertising2 = advertising_category
                advertising2 = list({ad.id: ad for ad in advertising2}.values())
                serializer = filterCategorySerializer(advertising2, many=True, context=request).data
                cache.set(f'category:{category_id}', serializer, 5)
            return Response(serializer, status=status.HTTP_200_OK)
        return Response({'massage': "NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        titles = None if (c := request.data['title']) in ['None', ''] else c
        category = None if (c := request.data['category']) in ['None', ''] else int(c)
        province = None if (c := request.data['province']) in ['None', ''] else int(c)
        city = None if (c := request.data['city']) in ['None', ''] else int(c)
        filters = Q()

        cache_key = f'{titles},{category},{province},{city}'
        if not (serializer_data := cache.get(cache_key)):
            print('apps.advertise.view.FilterAdvertising,post:', cache.get(cache_key))
            if category:
                categories = Category.objects.get(pk=int(category))
                cat = categories.get_descendants(include_self=False)
                filters &= Q(category__in=cat) if len(cat) > 0 else Q(category_id=category)

            if titles:
                filters &= Q(title__icontains=titles)
            if city:
                filters &= Q(city_id=city)
            if province:
                filters &= Q(state_id=province)

            advertising = Advertising.objects.is_diffusion().filter(filters)
            serializer = filterCategorySerializer(advertising, many=True, context=request)
            serializer_data = serializer.data
            cache.set(cache_key, serializer_data, 30)

        return Response(serializer_data, status=status.HTTP_200_OK)


"""end filter advertising"""
"""remove Advertising"""


class DestroyAdvertising(APIView):

    def post(self, request):
        advertising = int(request.data['advertising'])
        print(advertising)
        advertise = Advertising.objects.filter(pk=advertising)
        if advertise.exists():
            image = Image.objects.filter(content_type=ContentType.objects.get(model='advertising'),
                                         instance_id=advertising)
            save_field = SaveValueField.objects.filter(advertising_id=advertising)
            if save_field.exists():
                save_field.delete()
                image.delete()
                advertise.delete()
            if image.exists():
                image.delete()
                advertise.delete()

            advertise.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        return Response({'massage': 'delete advertising failed'}, status=status.HTTP_400_BAD_REQUEST)


"""advertise accepted"""


class AcceptSiteAdminAdvertising(APIView):
    permission_classes = [SiteAdmin]

    def get(self, request):
        advertise = Advertising.objects.archive().filter(diffusion=False, payed=True)
        serializer = AcceptedAdvertisingSerializer(
            advertise,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        advertise_id = int(request.data['advertise'])
        user_id = int(request.data['user'])
        try:
            advertise = Advertising.objects.get(pk=advertise_id)
        except Exception as e:
            return Response({'massage': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        advertise.diffusion = True
        advertise.created_at = timezone.now()
        advertise.expires_at = timezone.now() + timedelta(days=30)
        advertise.save(update_fields=['diffusion', 'created_at', 'expires_at'])
        emails = advertise.user.email
        send_email.delay(subject='Advertise Accepted', to_email=[emails],
                         context='Your ad is advertise displayed on our website for 30 days.')
        return Response({'massage': 'Accepted'}, status=status.HTTP_200_OK)

    def post(self, request):
        advertise_id = int(request.data['advertise'])
        try:
            advertise = Advertising.objects.get(pk=advertise_id)
        except Exception as e:
            return Response({'massage': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        advertise.diffusion = False
        advertise.is_active = False
        advertise.payed = False
        advertise.is_deleted = True
        advertise.save(update_fields=['diffusion', 'is_active', 'payed', 'is_deleted'])
        emails = advertise.user.email

        send_email.delay(subject='Advertise rejected', to_email=[emails], context='Your ad is advertise rejected ')

        return Response({'massage': 'Accepted'}, status=status.HTTP_200_OK)
