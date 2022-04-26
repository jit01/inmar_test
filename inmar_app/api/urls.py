from django.urls import path
from rest_framework import routers

from .views import StoreView, get_data, LocationView, DepartmentView, CategoryView, SubCategoryView

"""
Router for location, department, category and subcategory to update via view-set
"""
router = routers.SimpleRouter()
router.register(r'location', LocationView)
router.register(r'department', DepartmentView)
router.register(r'category', CategoryView)
router.register(r'subcategory', SubCategoryView)


urlpatterns = [
    path('store', StoreView.as_view(), name='store'),
    path('location/<int:location>/department', get_data, name='location'),
    path('location/<int:location>/department/<int:department>/category',
         get_data, name='department'),
    path('location/<int:location>/department/<int:department>/category/<int:category>/subcategory',
         get_data, name='category'),
    path('location/<int:location>/department/<int:department>/category/<int:category>/subcategory/<int:subcategory>',
         get_data, name='subcategory'),
] + router.urls
