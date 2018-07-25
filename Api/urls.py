from django.urls import path
from .views import Category_Viewset, User_Viewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', Category_Viewset, base_name='Category')
router.register('user', User_Viewset, base_name='user')
urlpatterns = router.urls
