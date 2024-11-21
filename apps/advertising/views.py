from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from itertools import chain
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from apps.advertising.models import Advertising, SaveValueField, Category, FieldCategory, City, State
from apps.advertising.serializers import AllAdvertisingViewSerializer, MainFieldCategorySerializer, \
    MainCategorySerializer
from .utils.validate_ladder_advertising import ValidateLadderAdvertising


# Create your views here.
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
                print('ladder', ladder)
                if ladder is not None:
                    advertising2 = list(chain(ladder, advertising))
                    print(advertising2)
                else:
                    advertising2 = advertising
                    print(advertising2)
                serializer = self.serializer_class(advertising2, many=True)
                serializer.context['request'] = request
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)


class AddAdvertiseView(APIView):
    serializer_class = AllAdvertisingViewSerializer
    permission_classes = []

    def get(self,request,category_id=None):
        if category_id is not None:
            category = Category.objects.filter(pk=category_id)
            if category.exists():
                category = Category.objects.get(pk=category_id).fields.all()
                if category:
                    serializers=MainFieldCategorySerializer(category, many=True)
                    return Response(serializers.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        image=request.data['image']
        value=request.data['value']
        advertise=request.data['advertise']
        category=request.data['category']
        print(image)
        print(value)
        print(advertise)
        print(category)
        pass

class ViewAllCategory(ListAPIView):
    serializer_class = MainCategorySerializer
    permission_classes = []
    queryset=Category.objects.all()