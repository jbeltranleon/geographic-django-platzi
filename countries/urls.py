from django.contrib import admin
from django.urls import path

from countries.views import (HomeView, UniformView,
                             CountryDetailView,CountryIdDetailView)

urlpatterns = [
    path("countries/<int:id>/", CountryIdDetailView.as_view(), name="country_id_detail"),
    path("countries/<code>/", CountryDetailView.as_view(), name="country_code_detail"),
]
