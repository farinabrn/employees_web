# Generated by Django 2.2.4 on 2019-09-02 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20190901_2004'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='employee',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='deleted',
        ),
    ]
