# Generated by Django 4.2.19 on 2025-02-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]
