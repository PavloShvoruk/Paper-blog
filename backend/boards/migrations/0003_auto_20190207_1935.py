# Generated by Django 2.1.5 on 2019-02-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190118_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='description',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(),
        ),
    ]
