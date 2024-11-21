from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from apps.advertising.models import Advertising,SaveValueField,Category,FieldCategory,City,State
from apps.advertising.serializers import AllAdvertisingViewSerializer


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

