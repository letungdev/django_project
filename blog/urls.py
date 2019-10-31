from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('about_us/',views.about_us, name = "about-us"),
    path('',views.homepage, name = "home-page"),
    path('home/',views.homepage, name = "home-page"),
    path('blogs/',views.blogs, name = "blog-page"),
    path('contact_us/',views.contact_us, name = "contact-page"),
    path('course_detail/1',views.course_detail, name = "details-page"),
    path('course_detail/2',views.course_detail2, name = "details-page"),
    path('course/',views.course_detail, name = "details-page"),
    path('investories/',views.invest, name = "invest-page"),
    path('students/',views.students, name = "students-page"),


]