# Generated by Django 5.2 on 2025-04-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=30, verbose_name='Отчество')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('date_of_hire', models.DateField(verbose_name='Дата приема на работу')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
