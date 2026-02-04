from django.urls import path
from . import views

urlpatterns = [
    path('/', views.my_porfolio, name='portfolio'),
    path('download-cv/', views.download_cv, name='download-cv'),
    path('contact-form/', views.contact_view, name='contact-form')
]


