import uuid
from custom_users.models import Custom_Users
from rest_framework import response, status


def register_new_user(data):
    """
    Register New Student
    """

    if not Custom_Users.objects.filter(username=data['roll_no']).exists():
        user_obj = Custom_Users.objects.create(
            username=data['roll_no'],
            role=data['role'],
            name=data['first_name'] + data['last_name'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        user_obj.set_password(data['password'])
        user_obj.save()
        return response.Response(
            data={
                'message': 'You have registered successfully.'
            },
            status=status.HTTP_201_CREATED
        )
    else:
        return response.Response(
            data={'message': "User already exist with this roll_no."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def all_fields(user):
    """
    Returning All Fields Of Login User
    """
    data = {
        "roll_no": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "bio": user.bio,
        "social_github": user.social_github,
        "social_linkedin": user.social_linkedin,
        "social_twitter": user.social_twitter,
        "social_youtube": user.social_youtube,
        "social_website": user.social_website,
        "phone_number": user.phone_number,
        "role": user.role,
    }
    return data


def all_fields_patch(user):
    """
    Returning All Fields Of Student for patch request
    """
    data = {
        "roll_no": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "bio": user.bio,
        "social_github": user.social_github,
        "social_linkedin": user.social_linkedin,
        "social_twitter": user.social_twitter,
        "social_youtube": user.social_youtube,
        "social_website": user.social_website,
        "role": user.role,
        "phone_number": user.phone_number,
        "instagram": user.instagram
    }
    return data


def generating_uuid():
    """
    uuid:return:
    """
    var = uuid.uuid4()
    return str(var)[:13]


def generating_dict_for_alumni(data):
    """
    :param data: 
    :return: dictionary for alumni registration and returning to the front-end  
    """""
    dict_for_alumni = {
        "name": data['first_name'] + data['last_name'],
        "username": generating_uuid(),
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "email": data['email'],
        "bio": data['bio'],
        "social_github": data['social_github'],
        "social_linkedin": data['social_linkedin'],
        "social_twitter": data['social_twitter'],
        "social_youtube": data['social_youtube'],
        "social_website": data['social_website'],
        "company_name": data['company_name'],
        "designation": data['designation'],
        "role": data['role']
    }
    return dict_for_alumni


def register_alumni_user(data):
    """
    Register New Alumni
    """
    returing_dict = generating_dict_for_alumni(data)
    user_obj = Custom_Users.objects.create(**returing_dict)
    user_obj.set_password(data['password'])
    user_obj.save()
    return response.Response(
        data={
            'message': 'Alumni has been registered successfully.',
            'data': returing_dict,
        },
        status=status.HTTP_201_CREATED
    )


def register_teacher(data):
    """
    Register New Teacher
    """
    returing_dict = generating_dict_for_teacher(data)
    user_obj = Custom_Users.objects.create(**returing_dict)
    user_obj.set_password(data['password'])
    user_obj.save()
    return response.Response(
        data={
            'message': 'Teacher has been registered successfully.',
            'data': returing_dict,
        },
        status=status.HTTP_201_CREATED
    )


def generating_dict_for_teacher(data):
    """
    :param data: 
    :return: dictionary for teacher registration and returning to the front-end  
    """""
    dict_for_alumni = {
        "name": data['first_name'] + data['last_name'],
        "username": generating_uuid(),
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "email": data['email'],
        "bio": data['bio'],
        "social_github": data['social_github'],
        "social_linkedin": data['social_linkedin'],
        "social_twitter": data['social_twitter'],
        "social_youtube": data['social_youtube'],
        "social_website": data['social_website'],
        "company_name": data['company_name'],
        "designation": data['designation'],
        "role": data['role']
    }
    return dict_for_alumni


def generating_all_fields_for_alumni(alumni):
    """
    Returning All Fields Of Login User
    """
    data = {
        "uuid": alumni.username,
        "first_name": alumni.first_name,
        "last_name": alumni.last_name,
        "email": alumni.email,
        "bio": alumni.bio,
        "social_github": alumni.social_github,
        "social_linkedin": alumni.social_linkedin,
        "social_twitter": alumni.social_twitter,
        "social_youtube": alumni.social_youtube,
        "social_website": alumni.social_website,
        "role": alumni.role,
    }
    return data


def generating_all_fields_for_teacher(teacher):
    """
    Returning All Fields Of Login Teacher
    """
    data = {
        "uuid": teacher.username,
        "first_name": teacher.first_name,
        "last_name": teacher.last_name,
        "email": teacher.email,
        "short_intro": teacher.short_intro,
        "bio": teacher.bio,
        "social_github": teacher.social_github,
        "social_linkedin": teacher.social_linkedin,
        "social_twitter": teacher.social_twitter,
        "social_youtube": teacher.social_youtube,
        "social_website": teacher.social_website,
        "role": teacher.role,
        "is_teacher": teacher.is_teacher,
    }
    return data
