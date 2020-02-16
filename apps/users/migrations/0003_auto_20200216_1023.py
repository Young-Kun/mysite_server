# Generated by Django 3.0.3 on 2020-02-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200215_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verifycode',
            options={'verbose_name': '验证码', 'verbose_name_plural': '验证码'},
        ),
        migrations.RemoveField(
            model_name='verifycode',
            name='mobile',
        ),
        migrations.AddField(
            model_name='verifycode',
            name='account',
            field=models.CharField(default='', max_length=125, verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='verifycode',
            name='account_type',
            field=models.CharField(choices=[('email', '邮箱'), ('mobile', '手机')], default='email', max_length=6, verbose_name='账号类型'),
        ),
    ]
