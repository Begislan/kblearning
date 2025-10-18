from django.urls import path
from . import views

app_name = 'adm'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Categories URLs
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('categories/create/', views.CategoriesCreateView.as_view(), name='categories_create'),
    path('categories/<int:pk>/edit/', views.CategoriesUpdateView.as_view(), name='categories_edit'),
    path('categories/<int:pk>/delete/', views.CategoriesDeleteView.as_view(), name='categories_delete'),

    # NameCategories URLs
    path('namecategories/', views.NameCategoriesListView.as_view(), name='namecategories_list'),
    path('namecategories/create/', views.NameCategoriesCreateView.as_view(), name='namecategories_create'),
    path('namecategories/<int:pk>/edit/', views.NameCategoriesUpdateView.as_view(), name='namecategories_edit'),
    path('namecategories/<int:pk>/delete/', views.NameCategoriesDeleteView.as_view(), name='namecategories_delete'),

    # Raz URLs
    path('raz/', views.RazListView.as_view(), name='raz_list'),
    path('raz/create/', views.RazCreateView.as_view(), name='raz_create'),
    path('raz/<int:pk>/edit/', views.RazUpdateView.as_view(), name='raz_edit'),
    path('raz/<int:pk>/delete/', views.RazDeleteView.as_view(), name='raz_delete'),

    # Glav URLs
    path('glav/', views.GlavListView.as_view(), name='glav_list'),
    path('glav/create/', views.GlavCreateView.as_view(), name='glav_create'),
    path('glav/<int:pk>/edit/', views.GlavUpdateView.as_view(), name='glav_edit'),
    path('glav/<int:pk>/delete/', views.GlavDeleteView.as_view(), name='glav_delete'),

    # Theme URLs с улучшенными функциями
    path('themes/', views.ThemeListView.as_view(), name='theme_list'),
    path('themes/create/', views.ThemeCreateView.as_view(), name='theme_create'),
    path('themes/quick-add/', views.quick_add_theme, name='theme_quick_add'),
    path('themes/bulk-add/', views.bulk_add_themes, name='theme_bulk_add'),
    path('themes/<int:pk>/edit/', views.ThemeUpdateView.as_view(), name='theme_edit'),
    path('themes/<int:pk>/delete/', views.ThemeDeleteView.as_view(), name='theme_delete'),

    # News URLs
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),

    # About URLs
    path('about/', views.AboutListView.as_view(), name='about_list'),
    path('about/create/', views.AboutCreateView.as_view(), name='about_create'),
    path('about/<int:pk>/edit/', views.AboutUpdateView.as_view(), name='about_edit'),
    path('about/<int:pk>/delete/', views.AboutDeleteView.as_view(), name='about_delete'),

    # API URLs
    path('api/glavs/<int:razdel_id>/', views.get_glavs_by_razdel, name='api_glavs'),
    path('api/razdels/<int:category_id>/', views.get_razdels_by_category, name='api_razdels'),
]