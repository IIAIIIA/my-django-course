from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from newsproject import settings
from .forms import NewsForm
from .models import News, Category

# CBV - class based views
# Create your views here.

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'all_news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(HomeNews):
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')

# Пример использования SMTP сервера
# def send_message(request):
#     if request.method == 'POST':
#         form = None
#         if form.is_vaid():
#             send_application(form.cleaned_data['first_name'], form.cleaned_data['last_name'])
#
# def send_application(first_name, second_name):
#     application = f'''Заравствуйте, {first_name} {second_name}'''
#     send_mail(f'Письмо для проверки SMTP сервера', application, settings.EMAIL_HOST_USER, ['fpk@bsac.by'])