# Generated by Django 4.0.1 on 2022-01-09 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('users_assigned', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('background', multiselectfield.db.fields.MultiSelectField(choices=[('FIN', 'Finance'), ('STF', 'Staffing'), ('OP', 'Operations')], max_length=10)),
                ('priority', multiselectfield.db.fields.MultiSelectField(choices=[('LOW', 'Low'), ('MED', 'Medium'), ('HIGH', 'High'), ('VHIGH', 'Very High')], max_length=18)),
                ('probability_percentage', multiselectfield.db.fields.MultiSelectField(choices=[(1, '10%'), (2, '20%'), (3, '30%'), (4, '40%'), (5, '50%'), (6, '60%'), (7, '70%'), (8, '80%'), (9, '90%'), (10, '100%')], max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user_assigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
