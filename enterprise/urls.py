from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"enterprise", views.EnterpriseViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"ratings", views.RatingViewSet)

app_name = "enterprise"

urlpatterns = [
  path("", include(router.urls)),
  path("categories/", views.CategoryListView.as_view()),
  path("categories/<int:pk>/subcategories/", views.SubcategoryListView.as_view())
]