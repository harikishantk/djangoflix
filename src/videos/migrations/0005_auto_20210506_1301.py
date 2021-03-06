# Generated by Django 3.2 on 2021-05-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_videoproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published Video', 'verbose_name_plural': 'Published Videos'},
        ),
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
