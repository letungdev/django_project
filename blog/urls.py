from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('ve-dien-gia/',views.about_us, name = "about-us"),
    path('',views.homepage, name = "home-page"),
    path('trang-chu/',views.homepage, name = "home-page"),
    path('dien-dan/',views.blogs, name = "blog-page"),
    path('lien-he/',views.contact_us, name = "contact-page"),
    path('chi-tiet-khoa-hoc/1',views.course_detail, name = "details-page"),
    path('chi-tiet-khoa-hoc/2',views.course_detail2, name = "details-page"),
    path('khoa-hoc/',views.course_detail, name = "details-page"),
    path('dau-tu/',views.invest, name = "invest-page"),
    path('hoc-vien/',views.students, name = "students-page"),


]