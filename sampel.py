from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import User

class OTPLoginView(TokenObtainPairView):
    def post(self, request):
        username = request.data.get('username')
        otp = request.data.get('otp')
        user = User.objects.get(username=username)
        # بررسی اعتبار OTP (با مقایسه با OTP ذخیره شده)
        # ...
        if otp_is_valid:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)