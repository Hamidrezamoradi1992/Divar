from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.conf import settings
from apps.payment.models import Order, OrderItem
from apps.payment.serializers import AddLadderToOrderSerializer
import json
import requests


# Create your views here.
class AddToOrderForLadderView(APIView):
    serializer_class = AddLadderToOrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PayOrderView(APIView):
    permission_classes = []

    def post(self, request):
        order_id = int(request.data.get('order_id'))
        try:
            order = Order.objects.get(pk=order_id)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        order.is_paid = True
        order.is_completed = True
        order.save(update_fields=['is_paid', 'is_completed'])
        orderItems = OrderItem.objects.filter(order=order)
        for order_item in orderItems:
            advertise = order_item.advertise
            if order_item.title == 'ladder':
                advertise.ladder = True
            else:
                advertise.payed = True
            advertise.save()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)

# amount = 1000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080//comment/verify/'
#
#
# def send_request(request):
#     print(request.method)
#     if request.method == 'GET':
#         if settings.SANDBOX:
#             sandbox = 'sandbox'
#         else:
#             sandbox = 'www'
#         ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
#         ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
#         ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
#         data = {
#             "MerchantID": settings.MERCHANT,
#             "Amount": amount,
#             "Description": description,
#             "Phone": phone,
#             "CallbackURL": CallbackURL,
#         }
#         data = json.dumps(data)
#         # set content length by data
#         headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#         try:
#             response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
#             print(response.status_code)
#             print(response.headers)
#
#             if response.status_code == 200:
#                 response = response.json()
#                 if response['Status'] == 100:
#                     return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
#                             'authority': response['Authority']}
#                 else:
#                     return {'status': False, 'code': str(response['Status'])}
#             return response
#
#         except requests.exceptions.Timeout:
#             return {'status': False, 'code': 'timeout'}
#         except requests.exceptions.ConnectionError:
#             return {'status': False, 'code': 'connection error'}
#
# def verify(authority):
#         data = {
#             "MerchantID": settings.MERCHANT,
#             "Amount": amount,
#             "Authority": authority,
#         }
#         data = json.dumps(data)
#         # set content length by data
#         headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#         response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
#
#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'RefID': response['RefID']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response
