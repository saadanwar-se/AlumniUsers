from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from custom_users.models import Custom_Users, Post, AlumniData, Announcements, Fund_Raise


class Custom_Users_Serializers(serializers.Serializer):
    roll_no = serializers.CharField()
    password = serializers.CharField()


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
        fields = ("picture", "email", "phone_number", "bio", "social_github",
                  "social_linkedin", "social_website", "social_twitter", "social_youtube",
                  "instagram",)


class User_Search_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        exclude = ('password',)


class Registeratrion_Alumni_Teacher_Deletion_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'


class Registeratrion_Alumni_Teacher(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        exclude = ("picture",)


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


class Fund_Raise_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Fund_Raise
        exclude = ['custom_users']


class Owners(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'


class All_Posts(serializers.ModelSerializer):
    custom_users = Owners(read_only=True)
    picture_url = serializers.SerializerMethodField(method_name='get_picture_url')

    class Meta:
        model = Post
        exclude = ['picture']
        # fields = ['custom_users', 'picture', 'title', 'description']

    def get_picture_url(self, post):
        request = self.context.get('request')
        if not post.picture:
            return ""
        else:
            picture_url = post.picture.url
            return request.build_absolute_uri(picture_url)


class Student_Block_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = ("is_blocked",)

