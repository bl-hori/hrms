# Generated by Django 4.2.5 on 2023-09-09 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, null=True, unique=True, verbose_name='社員番号')),
                ('email', models.CharField(max_length=255, null=True, unique=True, verbose_name='メールアドレス')),
                ('name_sei', models.CharField(max_length=255, null=True, verbose_name='姓')),
                ('name_sei_hira', models.CharField(max_length=255, null=True, verbose_name='姓_ひらがな')),
                ('name_sei_kana', models.CharField(max_length=255, null=True, verbose_name='姓_カタカナ')),
                ('name_mei', models.CharField(max_length=255, null=True, verbose_name='名')),
                ('name_mei_hira', models.CharField(max_length=255, null=True, verbose_name='名_ひらがな')),
                ('name_mei_kana', models.CharField(max_length=255, null=True, verbose_name='名_カタカナ')),
                ('department_code', models.CharField(max_length=255, null=True, verbose_name='組織番号')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '従業員',
                'verbose_name_plural': '従業員',
            },
        ),
    ]
