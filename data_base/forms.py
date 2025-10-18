from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class NameCategoriesForm(forms.ModelForm):
    class Meta:
        model = NameCategories
        fields = '__all__'
        widgets = {
            'id_cat': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class RazForm(forms.ModelForm):
    class Meta:
        model = Raz
        fields = '__all__'
        widgets = {
            'categori': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class GlavForm(forms.ModelForm):
    class Meta:
        model = Glav
        fields = '__all__'
        widgets = {
            'razdel': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'
        widgets = {
            'id_glav': forms.Select(attrs={'class': 'form-control'}),
            'theme': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'full_text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите текст темы...'}),

        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': CKEditorWidget(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control'}),
            'special': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'rezume': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        # Специальная форма для быстрого добавления тем
class QuickThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['id_glav', 'theme', 'full_text']
        widgets = {
            'id_glav': forms.Select(attrs={'class': 'form-control'}),
            'theme': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Введите тему...'}),
            'full_text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите текст темы...'}),
        }
