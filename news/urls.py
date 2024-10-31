from django.urls import path
from .views import  HomeNews, NewsByCategory, ViewNews, CreateNews

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
]

#http://127.0.0.1:8000/news/{path}/