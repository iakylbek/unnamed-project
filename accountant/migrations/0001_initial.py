# Generated by Django 3.1.5 on 2021-04-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailySalesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(db_index=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=15)),
                ('orders', models.IntegerField()),
                ('total_orders', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthlySalesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(db_index=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=15)),
                ('orders', models.IntegerField()),
                ('total_orders', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WeeklySalesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(db_index=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=15)),
                ('orders', models.IntegerField()),
                ('total_orders', models.IntegerField()),
            ],
        ),
    ]
