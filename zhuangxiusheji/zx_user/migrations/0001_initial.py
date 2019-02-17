# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-09 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
                ('account_passWord', models.CharField(max_length=40)),
                ('account_mail', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=20)),
                ('company_num', models.CharField(max_length=30)),
                ('account_describe', models.TextField(max_length=2000)),
                ('examine', models.CharField(choices=[('W', '审核中'), ('Y', '审核通过'), ('N', '未通过')], default='W', max_length=20)),
                ('casefor', models.TextField(default='', max_length=200)),
                ('if_passed', models.BooleanField(default=False)),
                ('style', models.CharField(choices=[('O', '欧美风格'), ('D', '东方风格')], max_length=30)),
                ('paice_range', models.CharField(choices=[('0-5000', '5000元以下'), ('5000-10000', '5000到10000元'), ('10000-', '10000元以上')], max_length=30)),
            ],
            options={
                'db_table': 'company_user',
                'ordering': ['id'],
            },
            managers=[
                ('comanyUsers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='company_images/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zx_user.Company_User')),
            ],
            options={
                'db_table': 'company_images',
            },
        ),
        migrations.CreateModel(
            name='Ordinary_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
                ('account_passWord', models.CharField(max_length=40)),
                ('account_mail', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'ordinary_user',
                'ordering': ['id'],
            },
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
    ]