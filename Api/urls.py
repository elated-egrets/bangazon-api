from django.urls import path
from .views import Category_Viewset, Payment_Viewset, User_Viewset, User_Viewset, Order_Viewset, Product_Viewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', Category_Viewset, base_name='Category')
router.register('payment', Payment_Viewset, base_name='Payment')
router.register('user', User_Viewset, base_name='user')
router.register('order', Order_Viewset, base_name="order")
router.register('product', Product_Viewset, base_name="product")
urlpatterns = router.urls
