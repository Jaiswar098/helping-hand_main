# Generated by Django 4.1.7 on 2023-04-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='cover_letter/')),
                ('education', models.CharField(blank=True, max_length=15, null=True, verbose_name='Highest Education ')),
                ('mark_hs', models.CharField(blank=True, max_length=10, null=True, verbose_name='HighSchool Marks')),
                ('mark_grad', models.CharField(blank=True, max_length=10, null=True, verbose_name='Graduation Marks')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
