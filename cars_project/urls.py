from django.urls import path
from cars.views import CarList, CarDetail
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('cars/', CarList.as_view()),
    path('mashinalar/<int:pk>/', CarDetail.as_view())

]
