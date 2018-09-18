from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insert, name="insert"),
    path('add', views.add, name="add"),
    path('disp', views.disp, name="disp"),
    path('csv', views.download_csv, name="csv"),
    path('pdf', views.download_pdf, name="pdf"),
    path('json',views.download_json, name="json"),
    path('excel',views.download_excel, name="excel")
]

