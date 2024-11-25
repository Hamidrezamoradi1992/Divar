from django.contrib.contenttypes.models import ContentType

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from itertools import chain
from rest_framework.generics import ListAPIView
from rest_framework import status
from apps.advertising.models import Advertising, Category, City, State
from apps.advertising.serializers import (AllAdvertisingViewSerializer,
                                          MainFieldCategorySerializer,
                                          MainCategorySerializer,
                                          AddAdvertisingSerializer,
                                          AddAdvertisingImageSerializer,
                                          MainSaveValueFieldSerializer,
                                          MainStateSerializer,
                                          MainCitySerializer, AdminAdvertisingViewSerializer)
from .utils.validate_ladder_advertising import ValidateLadderAdvertising


# Create your views here.

# swagger
class AllAdvertisingView(ListAPIView):
    """
      - view all advertising


        {


             {

                      "id": 1,
                      "title": "advertise1",
                      "description": ";lkjhgfdgvbjhnkm",
                      "price": 25000.0,
                      "image": [],
                      "diffusion": true,
                      "category": {
                          "title": "hamid1",
                          "parent": null,
                          "free": true,
                          "fields":

                          [

                              {

                                  "id": 6,
                                  "title": "value1",
                                  "type_field": "int",
                                  "mandatory": true

                              },

                              {

                                  "id": 7,
                                  "title": "value2",
                                  "type_field": "int",
                                  "mandatory": true

                              },

                              {

                                  "id": 8,
                                  "title": "value3",
                                  "type_field": "int",
                                  "mandatory": true

                              }

                          ],

                          "price": 0.0

                      },

                      "state":

                      {
                          "id": 1,
                          "title": "tehran",
                          "area_code": "021"

                      },

                      "city":

                      {

                          "id": 1,
                          "state": 1,
                          "title": "tehran"

                      },

                      "vlue_field":

                      [

                          {

                              "id": 4,
                              "advertising": 1,
                              "category": 11,
                              "field": 8,
                              "value": "123",
                              "name_field": "value3"

                          }

                      ],


                      "address":
                      [

                          {

                              "id": 4,
                              "email": "11@gmail.com",
                              "phone": null,
                              "is_kyc": false,
                              "address": null

                          }

                      ]

             }

        }


    """
    queryset = Advertising.objects.all().order_by('-created_at')
    serializer_class = AllAdvertisingViewSerializer
    permission_classes = []


# swagger
class ViewAdvertisingForCategory(APIView):
    """
      - view all advertising


        {


             {

                      "id": 1,
                      "title": "advertise1",
                      "description": ";lkjhgfdgvbjhnkm",
                      "price": 25000.0,
                      "image": [],
                      "diffusion": true,
                      "category": {
                          "title": "hamid1",
                          "parent": null,
                          "free": true,
                          "fields":

                          [

                              {

                                  "id": 6,
                                  "title": "value1",
                                  "type_field": "int",
                                  "mandatory": true

                              },

                              {

                                  "id": 7,
                                  "title": "value2",
                                  "type_field": "int",
                                  "mandatory": true

                              },

                              {

                                  "id": 8,
                                  "title": "value3",
                                  "type_field": "int",
                                  "mandatory": true

                              }

                          ],

                          "price": 0.0

                      },

                      "state":

                      {
                          "id": 1,
                          "title": "tehran",
                          "area_code": "021"

                      },

                      "city":

                      {

                          "id": 1,
                          "state": 1,
                          "title": "tehran"

                      },

                      "vlue_field":

                      [

                          {

                              "id": 4,
                              "advertising": 1,
                              "category": 11,
                              "field": 8,
                              "value": "123",
                              "name_field": "value3"

                          }

                      ],


                      "address":
                      [

                          {

                              "id": 4,
                              "email": "11@gmail.com",
                              "phone": null,
                              "is_kyc": false,
                              "address": null

                          }

                      ]

             }

        }


    """
    serializer_class = AllAdvertisingViewSerializer
    permission_classes = []

    def get(self, request, category_id=None, *args, **kwargs):
        if category_id is not None:
            if Category.objects.filter(pk=category_id).exists():
                category = Category.objects.get(pk=category_id)
                categories = category.get_descendants(include_self=True)
                advertising = Advertising.objects.filter(category__in=categories).order_by('-created_at')
                ladder = ValidateLadderAdvertising.get_ladder_advertising(categories)
                if ladder is not None:
                    advertising2 = list(chain(ladder, advertising))
                else:
                    advertising2 = advertising
                serializer = self.serializer_class(advertising2, many=True)
                serializer.context['request'] = request
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)


# swagger

@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class AddAdvertiseView(APIView):
    """
        - create new advertising
            - input

            {

                'title': ['asdasd'],
                'price': '96555',
                'description': 'sdasda',
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
        advertising = Advertising.objects.filter(pk=request.data['advertising']).exists()
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

    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

    # get field catefory
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
                serializer.save()
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return Response({'massage': 'compliant add field'}, status=status.HTTP_200_OK)


@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class AllCategoryView(APIView):
    serializer_class = MainCategorySerializer
    queryset = Category.objects.all()
    permission_classes = []

    def get(self, request, category_id=None):
        if category_id is not None:
            if Category.objects.filter(pk=category_id).exists():
                category = Category.objects.filter(parent_id=category_id)
                serializers = self.serializer_class(category, many=True)
                return Response(serializers.data, status=status.HTTP_200_OK)

        else:
            category = Category.objects.filter(parent_id=None)
            category_id_parent = Category.objects.all().values_list('parent_id',
                                                                    flat=True)
            categories = [i for i in category if i.id in category_id_parent]
            serializers = self.serializer_class(categories, many=True)
            return Response(serializers.data,
                            status=status.HTTP_200_OK)
        return Response({'massage': 'dont category'},
                        status=status.HTTP_404_NOT_FOUND)


# swagger
@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
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
                "title": "karaj",
                "area_code": "068"

            }

        ]

    """
    serializer_class = MainStateSerializer
    queryset = State.objects.all()


# swagger
@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class AllCityView(APIView):
    """
    - all state in db

        - method GET

        [

            {

                "id": 2,
                "state": 2,
                "title": "karaj"

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


class AdvertisingPublishedView(APIView):
    serializer_class = AdminAdvertisingViewSerializer
    def get(self, request):
        userid=request.user.id
        if userid:
            queryset=Advertising.objects.filter(user=userid,diffusion=True)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'massage':'user not define'}, status=status.HTTP_400_BAD_REQUEST)



""""end admin panel advertising"""
