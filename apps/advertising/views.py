from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
from itertools import chain
from rest_framework.generics import ListAPIView
from rest_framework import status
from apps.advertising.models import Advertising,  Category,  City, State
from apps.advertising.serializers import AllAdvertisingViewSerializer, MainFieldCategorySerializer, \
    MainCategorySerializer
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


class AddAdvertiseView(APIView):
    serializer_class = AllAdvertisingViewSerializer
    permission_classes = []

    def get(self, request, category_id=None):
        if category_id is not None:
            category = Category.objects.filter(pk=category_id)
            if category.exists():
                category = Category.objects.get(pk=category_id).fields.all()
                if category:
                    serializers = MainFieldCategorySerializer(category, many=True)
                    return Response(serializers.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self,request):
        print(request.data)
        return Response(status=status.HTTP_200_OK)

# @method_decorator(cache_page(60*60*24), name='dispatch')
class AllCategoryView(APIView):
    serializer_class = MainCategorySerializer
    queryset = Category.objects.all()
    permission_classes = []

    def get(self, request, category_id=None):
        print('dasdasdasdasd')
        if category_id is not None:
            if Category.objects.filter(pk=category_id).exists():
                category = Category.objects.filter(parent_id=category_id)g
                serializers = self.serializer_class(category, many=True)
                return Response(serializers.data, status=status.HTTP_200_OK)

        else:
            category = Category.objects.filter(parent_id=None)
            category_id_parent = Category.objects.all().values_list('parent_id',
                                                                    flat=True)
            categories = [i for i in category if i.id in category_id_parent]
            print('categories',categories)
            serializers = self.serializer_class(categories, many=True)
            return Response(serializers.data,
                            status=status.HTTP_200_OK)
        return Response({'massage': 'dont category'},
                        status=status.HTTP_404_NOT_FOUND)


from .serializers import MainStateSerializer, MainCitySerializer


# swagger
@method_decorator(cache_page(60*60*24), name='dispatch')
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
@method_decorator(cache_page(60*60*24), name='dispatch')
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
            stata=State.objects.filter(pk=state_id).values_list('id', flat=True)
            if stata.exists():
                city = City.objects.filter(state__in=stata)
                serializers = self.serializer_class(city, many=True)
                return Response(serializers.data,
                                status=status.HTTP_200_OK)
        return Response({'massage': "NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
