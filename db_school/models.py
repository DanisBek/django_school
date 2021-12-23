from django.db import models


class Director(models.Model):
    title = models.CharField(verbose_name='ФИО', max_length=225)
    image = models.ImageField(upload_to='image/Director', blank=True, null=True)
    cell_number = models.CharField(verbose_name='Номер телефона',max_length=225)
    def __str__(self):
        return self.title

class Zauchi(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=225)
    image = models.ImageField(upload_to='image/Zauchi', blank=True, null=True)
    cell_number = models.CharField(verbose_name='Номер телефона', max_length=225)


class Teachers(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=225)
    address = models.CharField(verbose_name='Адрес',max_length=225)
    cell_number = models.CharField(verbose_name='Номер телефона',max_length=225)
    image = models.ImageField(upload_to='image/Teachers', blank=True, null=True)


class Classes(models.Model):
    letter_class = models.CharField(verbose_name='буква класс', max_length=225)
    class_number = models.IntegerField(verbose_name='Номер класса')
    class_teacher = models.ForeignKey(Teachers,verbose_name='классный руководитель',on_delete=models.CASCADE)


class Lesssons(models.Model):
    title = models.CharField(verbose_name='название урока', max_length=225)
    class_teacher = models.ForeignKey(Teachers, verbose_name='классный руководитель', on_delete=models.CASCADE)


class Pupils(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=225)
    class_letter = models.ForeignKey(Classes, verbose_name='класс', on_delete=models.CASCADE)
    parents_number = models.CharField(verbose_name='Номер родителей',max_length=225)
    address = models.CharField(verbose_name='Адрес',max_length=225)
    image_students = models.ImageField(verbose_name='Фото',upload_to='image/Pupils')


class School(models.Model):
    director = models.ForeignKey(Director,verbose_name='директор', on_delete=models.CASCADE)
    zauchi = models.ForeignKey(Zauchi,verbose_name='завуч',on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teachers,verbose_name='учителя',on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes,verbose_name='классы', on_delete=models.CASCADE)
    lessons = models.ForeignKey(Lesssons,verbose_name='уроки', on_delete=models.CASCADE)
    pupils = models.ForeignKey(Pupils,verbose_name='ученики', on_delete=models.CASCADE)