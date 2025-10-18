from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Categories(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="категория")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)
    image = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение категории")
    count = models.IntegerField(verbose_name="номер категории")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = '1 Категория'
        verbose_name_plural = '1 Категории'


class NameCategories(models.Model):
    id_cat = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Из какого категории")
    title = models.CharField(max_length=100, verbose_name="название предмета")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id_cat} | {self.title}"

    class Meta:
        verbose_name = '2 Предмет '
        verbose_name_plural = '2 Предметы категории'


class Raz(models.Model):
    categori = models.ForeignKey(NameCategories, on_delete=models.CASCADE, verbose_name="Из какого предмета")
    name = models.CharField(max_length=250, verbose_name="раздел предмета")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self):
        return f"{self.categori} | {self.name}"

    class Meta:
        verbose_name = '3 Раздел'
        verbose_name_plural = '3 Раздел предмета'


class Glav(models.Model):
    razdel = models.ForeignKey(Raz, on_delete=models.CASCADE, verbose_name="Из какого раздела")
    name = models.CharField(max_length=250, verbose_name="глава раздела")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    def __str__(self):
        return f"{self.razdel} | {self.name}"

    class Meta:
        verbose_name = '4 Глава'
        verbose_name_plural = '4 Глава раздела'


class Theme(models.Model):
    id_glav = models.ForeignKey(Glav, on_delete=models.CASCADE, verbose_name="Из какого глава")
    theme = models.TextField(verbose_name="Тема:")
    full_text = RichTextField(verbose_name="Тексе:")
    slug = models.SlugField(help_text='Поля автоматический заполняется!', null=True, blank=True)

    displayFields = ["theme"];
    searchFields = ["theme"];
    filterFields = ["id_glav"];
    def __str__(self) -> str:
        return f"{self.id_glav} | {self.theme}"

    class Meta:
        verbose_name = '5 Тема'
        verbose_name_plural = '5 Тема главы'


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название новости")
    text = RichTextField(verbose_name="Текст:")
    img = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение новость", blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="дата новость 'автоматически заполняется'")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '6 Новость'
        verbose_name_plural = '6 Новости'


class About(models.Model):
    img = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение работника")
    fio = models.CharField(max_length=255, verbose_name="Фамилия, Имя, Отечества")
    slug = models.SlugField(help_text='Поля автоматический заполняется!')
    special = models.CharField(max_length=255, verbose_name="специалисть")
    phone = PhoneNumberField(unique=True, verbose_name='Телефон номер', blank=True)
    rezume = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d', verbose_name="резюме необезательно")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = '7 О нас'
        verbose_name_plural = '7 О нас'
class Program(models.Model):
    img = models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="Изображение программа")
    name = models.CharField(max_length=500, verbose_name="Название программа")
    info = models.CharField(max_length=1000, verbose_name="Описание")
    link = models.CharField(max_length=1000, verbose_name="Ссылка источника")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '8 Программа'
        verbose_name_plural = '8 Программы'
class Laborant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Фамилия имя лаборанта:")
    info = models.CharField(max_length=1000, verbose_name="Описание, может быть группа лаборантта и так далее...")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '9 Лаборант'
        verbose_name_plural = '9 Лаборант'
class Kabinet(models.Model):
    id_laborant = models.ForeignKey(Laborant,on_delete=models.CASCADE, verbose_name="Выберите лаборант:")
    name = models.CharField(max_length=500, verbose_name="Название кабинетта:")
    info = models.CharField(max_length=1000, verbose_name="Описание...")
    def __str__(self):
        return f"{self.id_laborant} | {self.name}"
    class Meta:
        verbose_name = '10 Лаборант кабинет'
        verbose_name_plural = '10 Лаборант кабиненты'
class Computers(models.Model):
    id_kabinet = models.ForeignKey(Kabinet, on_delete=models.CASCADE, verbose_name="Из какого кабинента")
    name = models.CharField(max_length=100, verbose_name="Название компьютер")
    invb = models.CharField(max_length=15, verbose_name="ИНВ системный блок")
    invm = models.CharField(max_length=15, verbose_name="ИНВ монитор")
    hard = models.CharField(max_length=15, verbose_name="Размер жеский диск")
    cart = models.CharField(max_length=15, verbose_name="Размер видео карта")
    ram = models.CharField(max_length=15, verbose_name="Размер оперативный память")
    filterFields = ["id_kabinet"];
    search = ["name","invb","invm","id_kabinet"];
    searchFields = [search]
    def __str__(self):
        return f"{self.id_kabinet} | {self.name} |  инвСБ: {self.invb} | инвМ: {self.invm} | Жеский диск: {self.hard}гб | ОЗУ: {self.ram}гб | Видео карта: {self.cart}гб "
    class Meta:
        verbose_name = '11 Лаборант компьютер'
        verbose_name_plural = '11 Лаборант компьютеры'
