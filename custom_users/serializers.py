from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from custom_users.models import Custom_Users, Post


class Custom_Users_Serializers(serializers.Serializer):
    roll_no = serializers.CharField()
    password = serializers.CharField()


class Post_Saving_User(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'

    # def is_valid(self, raise_exception=False):
    #     return "s"


class Alumni_Serializers(serializers.Serializer):
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


class Register_Alumni_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = '__all__'


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Custom_Users
        fields = ('id', 'username')


class Post_Saving_Serializers(serializers.ModelSerializer):
    custom_users = CustomUserSerializers(read_only=True)
    # user_name = serializers.SerializerMethodField()

    # def get_user_name(self, obj):
    #     return obj.custom_users.username

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        # get user
        user = Custom_Users.objects.get(id=self.context['request'].user.id)
        # create post against user
        post_instance = Post.objects.create(custom_users=user, **validated_data)
        return post_instance

