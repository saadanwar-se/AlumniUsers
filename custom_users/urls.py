from django.urls import path
from custom_users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('login/', views.Student_Login_Api.as_view(), name='user_login'),
                  path('loginalumni/', views.Alumni_Login_Api.as_view(), name='user_login'),
                  path('register/', views.Student_Register.as_view(), name='student_registration'),
                  path('profile/<str:pk>/', views.Student_Profile_Api.as_view(), name='user_making_profile'),
                  path('name/', views.Users_Search_List.as_view(), name='users_searching'),
                  path('registeralumni/', views.Register_Alumni_Api.as_view(), name='alumni_registration'),
                  path('post/', views.Post_Saving.as_view(), name='post_saving'),
                  path('getuser/<str:pk>/', views.Get_Single_User.as_view(), name='search_single_user'),
                  path('sachievements/', views.Save_Alumni_Achievements.as_view(), name='save_alumni_achievements'),
                  path('gachievements/', views.Get_Alumni_Achievements.as_view(), name='get_alumni_achievements'),
                  path('sannouncements/', views.Save_Announcments.as_view(), name='save_announcements'),
                  path('gannouncements/', views.Get_Announcments.as_view(), name='get_announcements'),
                  path('teacherregister/', views.Register_Teacher.as_view(), name='teacher_registration'),
                  path('teacherlogin/', views.Teacher_Login_Api.as_view(), name='teacher_registration'),
                  path('allposts/', views.Posts.as_view(), name='post_saving'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
