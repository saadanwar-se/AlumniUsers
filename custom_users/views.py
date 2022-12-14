from django.contrib.auth import authenticate
from rest_framework import response, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from custom_users.services import register_new_user, all_fields, register_alumni_user, generating_all_fields_for_alumni, \
    register_teacher, all_fields_patch
from custom_users.serializers import Custom_Users_Serializers, Register_User_Serializer, Profile_Serializers, \
    User_Search_Serializers, Post_Serializers, Registeratrion_Alumni_Teacher_Deletion_Serializers, \
    Alumni_Teacher_Login_Serializers, \
    Single_User_Search_Serializers, Get_Alumni_Achievements_Serializers, Get_Announcements, Fund_Raise_Serializers, \
    All_Posts, Student_Block_Serializers,Registeratrion_Alumni_Teacher
from custom_users.models import Custom_Users, AlumniData, Announcements, Post, Fund_Raise
from .custompermissions import BlockUser

# Create your views here.


class Student_Register(APIView):
    """
    Register University Student
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
    University Student Login
    """

    def post(self, request):
        try:
            data = request.data
            serializer = Custom_Users_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                roll_no = serializer.validated_data['roll_no']
                password = serializer.validated_data['password']
                user = authenticate(username=roll_no, password=password)
                if user.is_blocked != True:
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
                else:
                    return response.Response({
                        "message":"user is blocked"
                    },
                        status=status.HTTP_406_NOT_ACCEPTABLE
                    )
        except Exception as e:
            return response.Response(
                {'message': serializer.errors},
            )


class Student_Profile_Api(APIView):
    """
        Updating the Registered University Student
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, BlockUser]

    def patch(self, request, pk):
        try:
            instance = Custom_Users.objects.get(username=pk)
            serializer = Profile_Serializers(instance, data=request.data)
            serializer.is_valid()
            Custom_Users.objects.filter(username=pk).update(**serializer.validated_data)
            obj = Custom_Users.objects.get(username=pk)
            data = all_fields_patch(obj)
            return response.Response({
                'message': 'The User has been successfully Updated',
                'data': data,
            },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return response.Response(
                {"message":e},
            )


class Users_Search_List(ListAPIView):
    """
        Users Searching Api
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, BlockUser]

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
            data = request.data
            serializer = Registeratrion_Alumni_Teacher(data=data)
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
            serializer = Alumni_Teacher_Login_Serializers(data=data)
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
        except Exception as e:
            return response.Response(
                data={'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )


class Post_Saving(APIView):
    """
    Saving the POSTS
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, BlockUser]

    def post(self, request):
        try:
            data = request.data
            serializer = Post_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                Post.objects.create(
                    custom_users=request.user, picture=serializer.validated_data['picture'],
                    title=serializer.validated_data['title'], description=serializer.validated_data['description']
                )
                return response.Response({
                    'data': "Post created successfully."
                },
                    status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return response.Response(
                data={'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )


class Get_Single_User(APIView):
    """
        Single User Searching
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, BlockUser]

    def get(self, request, pk):
        obj = Custom_Users.objects.get(id=pk)
        serializer = Single_User_Search_Serializers(obj, many=False)
        return response.Response({
            'data': serializer.data,
        },
            status=status.HTTP_200_OK
        )


class Save_Alumni_Achievements(APIView):
    """
    Saviing the acheivements of an alumni
    """

    def post(self, request):
        serializer = Get_Alumni_Achievements_Serializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(
                data={
                    'message': 'Alumni achievements has been registered successfully.',
                },
                status=status.HTTP_201_CREATED
            )


class Get_Alumni_Achievements(ListAPIView):
    """
    Getting the acheivements of all alumni's
    """
    queryset = AlumniData.objects.all()
    serializer_class = Get_Alumni_Achievements_Serializers


class Save_Announcments(APIView):
    """
    Saviing the announcments
    """

    def post(self, request):
        serializer = Get_Announcements(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(
                data={
                    'message': 'Announcements has been registered successfully.',
                },
                status=status.HTTP_201_CREATED
            )


class Get_Announcments(ListAPIView):
    """
    Getting all the announcements
    """
    queryset = Announcements.objects.all()
    serializer_class = Get_Announcements


class Register_Teacher(APIView):
    """
        Registering the Teachers
    """

    def post(self, request):
        try:
            data = request.data
            serializer = Registeratrion_Alumni_Teacher(data=data)
            if serializer.is_valid(raise_exception=True):
                data = register_teacher(serializer.validated_data)
                return data

        except Exception as e:
            return response.Response(
                data={'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )


class Teacher_Login_Api(APIView):
    """
    Teacher Login
    """

    def post(self, request):
        try:
            data = request.data
            serializer = Alumni_Teacher_Login_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                uuid = serializer.validated_data['uuid']
                password = serializer.validated_data['password']
                teacher = authenticate(username=uuid, password=password)
                data = generating_all_fields_for_alumni(teacher)
                refresh_token = RefreshToken.for_user(teacher)
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


class Posts(APIView):
    """
    Showing all Posts of users
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            posts = Post.objects.all().order_by('-id')
            serializer = All_Posts(posts, many=True, context={'request': request})
            return response.Response({
                'data': serializer.data
            },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return response.Response(
                data={'error': e},
            )


class Raising_Fund(APIView):
    """
    Saving the Raising Funds data
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            serializer = Fund_Raise_Serializers(data=data)
            if serializer.is_valid(raise_exception=True):
                Fund_Raise.objects.create(
                    custom_users=request.user,
                    title=serializer.validated_data['title'],
                    description=serializer.validated_data['description'],
                    amount=serializer.validated_data['amount'],
                    account_no=serializer.validated_data['account_no'],
                    bank_name=serializer.validated_data['bank_name'],
                )
                return response.Response({
                    'message': "Fund Raising Post has been saved"
                },
                    status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return response.Response(
                data={'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )


class Delete_Student(DestroyAPIView):
    """
    Deleting the Student who violates the rules
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Custom_Users.objects.all()
    serializer_class = Registeratrion_Alumni_Teacher_Deletion_Serializers


class Block_Student(APIView):
    """
        Blocking the University Student
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            instance = Custom_Users.objects.get(username=pk)
            serializer = Student_Block_Serializers(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return response.Response({
                    'message': 'The User has been succesfully blocked',
                },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return response.Response(
                {"message": e},
            )


class All_FundsRaise_Post(APIView):
    """
    Showing all Posts of Fund Raising
    """

    def get(self, request):
        try:
            posts = Fund_Raise.objects.all().order_by('-id')
            serializer = Fund_Raise_Serializers(posts, many=True)
            return response.Response({
                'data': serializer.data
            },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return response.Response(
                data={'error': e},
            )
