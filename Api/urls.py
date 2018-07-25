from django.urls import path
from .views import Category_Viewset, Payment_Viewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', Category_Viewset, base_name='Category')

router.register('payment', Payment_Viewset, base_name='Payment')
urlpatterns = router.urls
