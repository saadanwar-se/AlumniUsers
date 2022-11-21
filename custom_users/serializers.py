from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from custom_users.models import Custom_Users, Post, AlumniData, Announcements


class Custom_Users_Serializers(serializers.Serializer):
    roll_no = serializers.CharField()
    password = serializers.CharField()


class Post_Saving_User(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'


class Alumni_Teacher_Login_Serializers(serializers.Serializer):
    uuid = serializers.CharField()
    password = serializers.CharField()


class Register_User_Serializer(serializers.Serializer):
    roll_no = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = serializers.CharField()
    password = serializers.CharField()


class Profile_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        exclude = ("password", "role",)


class User_Search_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        exclude = ('password',)


class Registeratrion_Alumni_Teacher_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = ('id', 'username')


class Post_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['custom_users']


class Single_User_Search_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'


class Get_Alumni_Achievements_Serializers(serializers.ModelSerializer):
    class Meta:
        model = AlumniData
        fields = '__all__'


class Get_Announcements(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'
