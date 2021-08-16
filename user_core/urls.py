from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from . import views

router = DefaultRouter()
router.register(r'user', views.CustomUserViewSet)

app_name = "user_core"

urlpatterns = [
  path('register/', views.UserView.as_view(), name="register"),
  re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+).(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
  path('', include(router.urls))
]