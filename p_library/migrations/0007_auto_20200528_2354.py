# Generated by Django 3.0.5 on 2020-05-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20200528_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='foto',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='media', verbose_name='Ссылка картинки'),
        ),
    ]
