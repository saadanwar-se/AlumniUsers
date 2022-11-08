from django.urls import path
from custom_users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('login/', views.Student_Login_Api.as_view(), name='user_login'),
                  path('loginalumni/', views.Alumni_Login_Api.as_view(), name='user_login'),
                  path('register/', views.Register_User_Api.as_view(), name='user_registration'),
                  path('profile/<str:pk>/', views.Student_Profile_Api.as_view(), name='user_making_profile'),
                  path('name/', views.Users_Search_List.as_view(), name='users_searching'),
                  path('registeralumni/', views.Register_Alumni_Api.as_view(), name='alumni_registration'),
                  path('post/', views.Post_Saving.as_view(), name='post_saving')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
