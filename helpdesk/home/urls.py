from django.urls import path
from home import views

urlpatterns = [
    path("sms", views.sms, name="sms"),
    path('hello/', views.HelloView.as_view(), name='hello'),
]