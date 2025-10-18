# from django.contrib import admin
# from .models import *
#
#
# class CategoriesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#
#
# class NameCategiriesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#
#
# class RazAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#
#
# class GlavAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#
# class ThemeAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("theme",)}
#     list_display = Theme.displayFields
#     search_fields = Theme.searchFields
#     list_filter = Theme.filterFields
#
# class AboutAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("fio",)}
#
# class ComputerAdmin(admin.ModelAdmin):
#     list_filter = Computers.filterFields
#     search_fields = ['name', 'invb', 'invm', 'id_kabinet__name']
#
#
# admin.site.register(Categories, CategoriesAdmin)
# admin.site.register(NameCategories, CategoriesAdmin)
# admin.site.register(Raz, RazAdmin)
# admin.site.register(Glav, GlavAdmin)
# admin.site.register(Theme, ThemeAdmin)
# admin.site.register(News)
# admin.site.register(About, AboutAdmin)
# admin.site.register(Program)
# admin.site.register(Laborant)
# admin.site.register(Kabinet)
# admin.site.register(Computers, ComputerAdmin)



from django.contrib import admin
from .models import (
    Categories, NameCategories, Raz, Glav, Theme,
    News, About, Program, Laborant, Kabinet, Computers
)

# ----------- ВСПОМОГАТЕЛЬНЫЕ INLINES -----------

class NameCategoriesInline(admin.TabularInline):
    model = NameCategories
    extra = 1
    show_change_link = True


class RazInline(admin.TabularInline):
    model = Raz
    extra = 1
    show_change_link = True


class GlavInline(admin.TabularInline):
    model = Glav
    extra = 1
    show_change_link = True


class ThemeInline(admin.TabularInline):
    model = Theme
    extra = 1
    show_change_link = True


class KabinetInline(admin.TabularInline):
    model = Kabinet
    extra = 1
    show_change_link = True


class ComputersInline(admin.TabularInline):
    model = Computers
    extra = 1
    show_change_link = True

# ----------- ОСНОВНЫЕ МОДЕЛИ -----------

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'count')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [NameCategoriesInline]


@admin.register(NameCategories)
class NameCategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_cat')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RazInline]


@admin.register(Raz)
class RazAdmin(admin.ModelAdmin):
    list_display = ('name', 'categori')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GlavInline]


@admin.register(Glav)
class GlavAdmin(admin.ModelAdmin):
    list_display = ('name', 'razdel')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ThemeInline]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme', 'id_glav')
    prepopulated_fields = {'slug': ('theme',)}
    search_fields = ['theme', 'full_text']
    list_filter = ['id_glav']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ['title']
    date_hierarchy = 'date'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('fio', 'special', 'phone')
    prepopulated_fields = {'slug': ('fio',)}


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ['name']


@admin.register(Laborant)
class LaborantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [KabinetInline]


@admin.register(Kabinet)
class KabinetAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_laborant')
    inlines = [ComputersInline]


@admin.register(Computers)
class ComputersAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_kabinet', 'invb', 'invm', 'hard', 'ram', 'cart')
    search_fields = ('name', 'invb', 'invm')
    list_filter = ('id_kabinet',)

