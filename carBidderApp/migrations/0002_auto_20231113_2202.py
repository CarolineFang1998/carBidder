# Generated by Django 3.1.7 on 2023-11-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carBidderApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.CharField(max_length=11)),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('seller_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('buyer_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('num_of_seller_rating', models.IntegerField(blank=True, null=True)),
                ('num_of_buyer_rating', models.IntegerField(blank=True, null=True)),
                ('is_allowed_chat', models.IntegerField(blank=True, null=True)),
                ('is_allow_list', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'USERS',
            },
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
