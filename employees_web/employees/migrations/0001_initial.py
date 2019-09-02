# Generated by Django 2.2.4 on 2019-09-02 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hiring_date', models.DateTimeField(verbose_name='hiring date')),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
                ('cell_phone', models.IntegerField()),
                ('role', models.CharField(choices=[('STD', 'base employee'), ('MGR', 'manager'), ('SRMGR', 'senior manager'), ('PRES', 'president')], default='STD', max_length=25)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinate', to='employees.Employee')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employees',
            },
        ),
    ]
