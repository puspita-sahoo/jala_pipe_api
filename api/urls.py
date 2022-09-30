from django.urls import path
from .models import Product, Cart, CartProduct
from . import views
from .views import ProductAPIView, CartAPIView, CartProductAPIView



urlpatterns = [
    # path('api/', include("api.urls")),

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("product", views.ProductAPIView)
router.register("cart", views.CartAPIView)
router.register("cartproduct", views.CartProductAPIView)

app_name = "api"
urlpatterns = router.urls + urlpatterns
 



