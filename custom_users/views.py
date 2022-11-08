from django.contrib.auth import authenticate
from rest_framework import response, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from custom_users.services import register_new_user, all_fields, register_alumni_user, generating_all_fields_for_alumni
from custom_users.serializers import Custom_Users_Serializers, Register_User_Serializer, Profile_Serializers, \
    User_Search_Serializers, Post_Saving_Serializers, Register_Alumni_Serializers, Alumni_Serializers
from custom_users.models import Custom_Users


# Create your views here.


class Register_User_Api(APIView):
    """
    Register New User
    """

    def post(self, request):
        try:
            data = request.data
            serializer = Register_User_Serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                data = register_new_user(serializer.validated_data)
                return data

        except Exception as e:
            return response.Response(
                data={'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )


class Student_Login_Api(APIView):
    """
    Login User
    """
    def post(self, request):
        try:
            data = request.data
            serializer = Custom_Users_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                roll_no = serializer.validated_data['roll_no']
                password = serializer.validated_data['password']
                user = authenticate(username=roll_no, password=password)
                data = all_fields(user)
                refresh_token = RefreshToken.for_user(user)
                token = str(refresh_token.access_token)
                refresh_token = str(refresh_token)

                return response.Response({
                    'token': token,
                    'refresh_token': refresh_token,
                    'data': data,
                },
                    status=status.HTTP_200_OK
                )
        except:
            return response.Response(
                {'message': "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )


class Student_Profile_Api(APIView):
    """
        Updating Registered User
    """
    authentication_classes = [JWTAuthentication]

    def patch(self, request, pk):
        obj = Custom_Users.objects.get(username=pk)
        serializer = Profile_Serializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                'data': 'The User has been successfully data in User Profile',
            },
                status=status.HTTP_201_CREATED
            )
        else:
            return response.Response(serializer.errors)


class Users_Search_List(ListAPIView):
    """
        Users Searching Api
    """
    authentication_classes = [JWTAuthentication]

    queryset = Custom_Users.objects.all()
    serializer_class = User_Search_Serializers
    filter_backends = [SearchFilter]
    search_fields = ['^name']


class Register_Alumni_Api(APIView):
    """
        Registering the Alumni Users
    """

    def post(self, request):
        try:
            data = request
            data = request.data
            serializer = Register_Alumni_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                data = register_alumni_user(serializer.validated_data)
                return data

        except Exception as e:
            return response.Response(
                data={'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )


class Alumni_Login_Api(APIView):
    """
    Login Alumni
    """
    def post(self, request):
        try:
            data = request.data
            serializer = Alumni_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                uuid = serializer.validated_data['uuid']
                password = serializer.validated_data['password']
                alumni = authenticate(username=uuid, password=password)
                data = generating_all_fields_for_alumni(alumni)
                refresh_token = RefreshToken.for_user(alumni)
                token = str(refresh_token.access_token)
                refresh_token = str(refresh_token)

                return response.Response({
                    'token': token,
                    'refresh_token': refresh_token,
                    'data': data,
                },
                    status=status.HTTP_200_OK
                )
        except:
            return response.Response(
                {'message': "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )


class Post_Saving(APIView):
    """
    Saving the POSTS
    """
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        data = request.data
        serializer = Post_Saving_Serializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({
            'data': serializer.data,
        },
            status=status.HTTP_201_CREATED
        )
