from django.contrib.auth.decorators import login_required
from .models import (Categories, NameCategories, Raz, Glav, Theme, News,
                     About, Program, Laborant, Kabinet, Computers)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

categories = Categories.objects.all()  # Program
nameDisipline = NameCategories.objects.all()  # python
razdelDisipline = Raz.objects.all()      # django
glavDisipline = Glav.objects.all()      # glav
themeDisipline = Theme.objects.all()
news = News.objects.all()
laborants = About.objects.all()
programm = Program.objects.all()

@login_required
# Главная страница админки
def dashboard(request):
    stats = {
        'categories_count': Categories.objects.count(),
        'themes_count': Theme.objects.count(),
        'news_count': News.objects.count(),
        'staff_count': About.objects.count(),
    }

    recent_news = News.objects.order_by('-date')[:5]
    recent_themes = Theme.objects.all()[:5]

    return render(request, 'adm/dashboard.html', {
        'stats': stats,
        'recent_news': recent_news,
        'recent_themes': recent_themes,
    })


# Базовый класс для CRUD операций
class BaseCRUDView:
    model = None
    form_class = None
    template_name = None
    list_display = []

    def get_success_url(self):
        # Используйте правильное пространство имен
        model_name = self.model.__name__.lower()
        return reverse_lazy(f'adm:{model_name}_list')

# CRUD для Categories
class CategoriesListView(BaseCRUDView, ListView):
    model = Categories
    template_name = 'adm/categories_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Categories.objects.all().order_by('count')


class CategoriesCreateView(BaseCRUDView, CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'adm/categories_form.html'


class CategoriesUpdateView(BaseCRUDView, UpdateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'adm/categories_form.html'


class CategoriesDeleteView(BaseCRUDView, DeleteView):
    model = Categories
    template_name = 'adm/confirm_delete.html'

# CRUD для NameCategories
class NameCategoriesListView(BaseCRUDView, ListView):
    model = NameCategories
    template_name = 'adm/namecategories_list.html'
    context_object_name = 'namecategories'

class NameCategoriesCreateView(BaseCRUDView, CreateView):
    model = NameCategories
    form_class = NameCategoriesForm
    template_name = 'adm/namecategories_form.html'

class NameCategoriesUpdateView(BaseCRUDView, UpdateView):
    model = NameCategories
    form_class = NameCategoriesForm
    template_name = 'adm/namecategories_form.html'

class NameCategoriesDeleteView(BaseCRUDView, DeleteView):
    model = NameCategories
    template_name = 'adm/confirm_delete.html'

# CRUD для Raz
class RazListView(BaseCRUDView, ListView):
    model = Raz
    template_name = 'adm/raz_list.html'
    context_object_name = 'razs'

class RazCreateView(BaseCRUDView, CreateView):
    model = Raz
    form_class = RazForm
    template_name = 'adm/raz_form.html'

class RazUpdateView(BaseCRUDView, UpdateView):
    model = Raz
    form_class = RazForm
    template_name = 'adm/raz_form.html'

class RazDeleteView(BaseCRUDView, DeleteView):
    model = Raz
    template_name = 'adm/confirm_delete.html'

# CRUD для Glav
class GlavListView(BaseCRUDView, ListView):
    model = Glav
    template_name = 'adm/glav_list.html'
    context_object_name = 'glavs'

class GlavCreateView(BaseCRUDView, CreateView):
    model = Glav
    form_class = GlavForm
    template_name = 'adm/glav_form.html'

class GlavUpdateView(BaseCRUDView, UpdateView):
    model = Glav
    form_class = GlavForm
    template_name = 'adm/glav_form.html'

class GlavDeleteView(BaseCRUDView, DeleteView):
    model = Glav
    template_name = 'adm/confirm_delete.html'


# CRUD для Theme с улучшенными функциями
class ThemeListView(BaseCRUDView, ListView):
    model = Theme
    template_name = 'adm/theme_list.html'
    context_object_name = 'themes'
    paginate_by = 20

    def get_queryset(self):
        queryset = Theme.objects.all().select_related('id_glav__razdel__categori__id_cat')
        search_query = self.request.GET.get('search', '')
        glav_filter = self.request.GET.get('glav', '')

        if search_query:
            queryset = queryset.filter(
                Q(theme__icontains=search_query) |
                Q(full_text__icontains=search_query)
            )

        if glav_filter:
            queryset = queryset.filter(id_glav_id=glav_filter)

        return queryset.order_by('id_glav')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['glavs'] = Glav.objects.all()
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_glav'] = self.request.GET.get('glav', '')
        return context


class ThemeCreateView(BaseCRUDView, CreateView):
    model = Theme
    form_class = ThemeForm
    template_name = 'adm/theme_form.html'


class ThemeUpdateView(BaseCRUDView, UpdateView):
    model = Theme
    form_class = ThemeForm
    template_name = 'adm/theme_form.html'


class ThemeDeleteView(DeleteView):
    model = Theme
    template_name = 'adm/confirm_delete.html'
    success_url = reverse_lazy('adm:theme_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Тема успешно удалена!')
        return super().delete(request, *args, **kwargs)


# Функция для быстрого добавления тем
def quick_add_theme(request):
    if request.method == 'POST':
        form = QuickThemeForm(request.POST)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.save()
            messages.success(request, f'Тема "{theme.theme[:50]}..." успешно добавлена!')
            return redirect('adm:theme_list')
    else:
        form = QuickThemeForm()

    return render(request, 'adm/quick_add_theme.html', {'form': form})


# Функция для массового создания тем
def bulk_add_themes(request):
    if request.method == 'POST':
        glav_id = request.POST.get('glav')
        themes_text = request.POST.get('themes_text')

        if glav_id and themes_text:
            glav = get_object_or_404(Glav, id=glav_id)
            themes_list = [t.strip() for t in themes_text.split('\n') if t.strip()]

            created_count = 0
            for i, theme_text in enumerate(themes_list):
                if theme_text:
                    Theme.objects.create(
                        id_glav=glav,
                        theme=theme_text,
                        full_text=f"<p>{theme_text}</p>",
                    )
                    created_count += 1

            messages.success(request, f'Успешно создано {created_count} тем!')
            return redirect('adm:theme_list')

    glavs = Glav.objects.all()
    return render(request, 'adm/bulk_add_themes.html', {'glavs': glavs})


# CRUD для News
class NewsListView(BaseCRUDView, ListView):
    model = News
    template_name = 'adm/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10


class NewsCreateView(BaseCRUDView, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'adm/news_form.html'


class NewsUpdateView(BaseCRUDView, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'adm/news_form.html'


class NewsDeleteView(BaseCRUDView, DeleteView):
    model = News
    template_name = 'adm/confirm_delete.html'


# CRUD для About
class AboutListView(BaseCRUDView, ListView):
    model = About
    template_name = 'adm/about_list.html'
    context_object_name = 'staff_list'


class AboutCreateView(BaseCRUDView, CreateView):
    model = About
    form_class = AboutForm
    template_name = 'adm/about_form.html'


class AboutUpdateView(BaseCRUDView, UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'adm/about_form.html'


class AboutDeleteView(BaseCRUDView, DeleteView):
    model = About
    template_name = 'adm/confirm_delete.html'


# API функции для AJAX
def get_glavs_by_razdel(request, razdel_id):
    glavs = Glav.objects.filter(razdel_id=razdel_id).values('id', 'name')
    return JsonResponse(list(glavs), safe=False)


def get_razdels_by_category(request, category_id):
    razdels = Raz.objects.filter(categori_id=category_id).values('id', 'name')
    return JsonResponse(list(razdels), safe=False)

