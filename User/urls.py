from django.urls import path
from . import views

urlpatterns = [
    path('', views.userDashboard, name='userdashboard'),
    path('CourseIntro/<int:course_id>/', views.userCourseIntro, name="courseIntro"),
    path('CourseLesson/<int:c_id>', views.userCourseLesson, name="courseLesson"),
    path('userProfile/', views.userprofile, name='userprofile'),
    path('userProfileEdit/', views.userProfileEdit, name='userprofileedit'),
    path('userCFP/', views.userCfp, name="usercfp"),
    path('userQuizz/<int:w_id>/', views.userQuizz, name="userquizz"),
    path('userResult/', views.userResult, name="userResult"),
    path('pricing/', views.pricing, name="pricing"),
]
