from django.db import models


class Contact(models.Model):
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name='Номер дома')
    email = models.EmailField(unique=True)

    class Meta:
#        abstract = True
        verbose_name = "Конакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=100, verbose_name="Название продукта")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выпуска")

    def __str__(self):
        return self.name


class Factory(Contact):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    name = models.CharField(max_length=100, verbose_name="Название завода")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name


class Stores(Contact):
    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    name = models.CharField(max_length=100, verbose_name="Название сети")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    supplier = models.ForeignKey(Factory, verbose_name="Поставщик", on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name="Задолженность перед поставщиком")

    def __str__(self):
        return self.name


class IndividualEntrepreneur(Contact):
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    name = models.CharField(max_length=100, verbose_name="Имя индивидуального предпринимателя")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    supplier = models.ForeignKey(Factory, verbose_name="Поставщик", on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name="Задолженность перед поставщиком")

    def __str__(self):
        return self.name
