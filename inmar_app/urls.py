from django.urls import path, include
from .views import StoreView, add_store, get_store_by_id, update_store, delete_store

urlpatterns = [
    path('', StoreView.as_view(), name='storeview'),
    path('add', add_store, name='add'),
    path('<int:id>', get_store_by_id, name='get_by_id'),
    path('update', update_store, name='update'),
    path('delete/<int:id>', delete_store, name='delete'),

]