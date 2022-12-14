from django.urls import path
from custom_users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('register/', views.Student_Register.as_view(), name='student_registration'),
                  path('login/', views.Student_Login_Api.as_view(), name='user_login'),
                  path('profile/<str:pk>/', views.Student_Profile_Api.as_view(), name='updating_student_profile'),
                  path('name/', views.Users_Search_List.as_view(), name='users_searching'),
                  path('registeralumni/', views.Register_Alumni_Api.as_view(), name='alumni_registration'),
                  path('loginalumni/', views.Alumni_Login_Api.as_view(), name='user_login'),
                  path('post/', views.Post_Saving.as_view(), name='post_saving'),
                  path('getuser/<str:pk>/', views.Get_Single_User.as_view(), name='search_single_user'),
                  path('sachievements/', views.Save_Alumni_Achievements.as_view(), name='save_alumni_achievements'),
                  path('gachievements/', views.Get_Alumni_Achievements.as_view(), name='get_alumni_achievements'),
                  path('sannouncements/', views.Save_Announcments.as_view(), name='save_announcements'),
                  path('gannouncements/', views.Get_Announcments.as_view(), name='get_announcements'),
                  path('teacherregister/', views.Register_Teacher.as_view(), name='teacher_registration'),
                  path('teacherlogin/', views.Teacher_Login_Api.as_view(), name='teacher_login'),
                  path('allposts/', views.Posts.as_view(), name='fetching_all_posts'),
                  path('fundraise/', views.Raising_Fund.as_view(), name='fund_raising'),
                  path('delete/<str:pk>/', views.Delete_Student.as_view(), name='delete_user'),
                  path('block/<str:pk>/', views.Block_Student.as_view(), name='blocking_student'),
                  path('getfundraises/', views.All_FundsRaise_Post.as_view(), name='getting_all_fundraises_posts'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
