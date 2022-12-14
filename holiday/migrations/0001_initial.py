# Generated by Django 4.1.1 on 2022-09-21 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolliyDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.CharField(choices=[('데이', '데이'), ('이브닝', '이브닝'), ('시차', '시차'), ('휴일', '휴일')], max_length=10)),
                ('note', models.CharField(blank=True, max_length=256)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
