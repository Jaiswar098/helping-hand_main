# Generated by Django 4.1.7 on 2023-05-10 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_job'),
        ('jobseeker', '0003_remove_person_mark_grad_remove_person_mark_hs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('accepted', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.job')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.person')),
            ],
        ),
    ]
