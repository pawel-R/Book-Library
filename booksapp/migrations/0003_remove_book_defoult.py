# Generated by Django 2.2.7 on 2019-11-15 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0002_book_defoult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='defoult',
        ),
    ]