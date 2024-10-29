from django.urls import path, include
from .views import index, get_category

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category')
]

#http://127.0.0.1:8000/news/{path}/