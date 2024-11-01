from django import forms
from django.core.exceptions import ValidationError

from .models import News
import re


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

    def clean_is_published(self):
        if self.cleaned_data['is_published']:
            return self.cleaned_data['is_published']
        raise ValidationError('Статус публикации должен быть подтверждён')
