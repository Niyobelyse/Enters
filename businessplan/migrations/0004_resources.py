# Generated by Django 4.1.2 on 2022-11-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplan', '0003_rename_business_businessdetail_delete_business1'),
    ]

    operations = [
        migrations.CreateModel(
            name='resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=255)),
                ('proposedresource', models.CharField(max_length=255)),
                ('purchaseditem', models.CharField(max_length=255)),
            ],
        ),
    ]