# Generated by Django 2.2 on 2019-04-09 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=20)),
                ('property_address', models.CharField(max_length=20)),
                ('property_city', models.CharField(choices=[('Kanpur', 'Kanpur'), ('New Delhi', 'New Delhi'), ('Ghaziabad', 'Ghaziabad'), ('Chandigarh', 'Chandigarh')], max_length=20)),
                ('property_states', models.CharField(choices=[('Uttar Pradesh', 'Uttar Pradesh'), ('Delhi', 'Delhi'), ('Karnataka', 'Karnataka'), ('Punjab', 'Punjab')], max_length=20)),
                ('property_pin', models.IntegerField()),
                ('property_price', models.IntegerField()),
                ('property_bedroom', models.IntegerField()),
                ('property_bathroom', models.IntegerField()),
                ('property_sq_feet', models.IntegerField()),
                ('property_lot_size', models.IntegerField(default=0)),
                ('property_garage', models.IntegerField(default=0)),
                ('property_is_published', models.BooleanField(default=True)),
                ('property_listing_date', models.DateField(auto_now_add=True)),
                ('property_description', models.TextField(blank=True, max_length=200)),
                ('photo_main', models.ImageField(default='property_images/default/home.jpg', upload_to='property_images/')),
                ('photo1', models.ImageField(blank=True, upload_to='property_images/')),
                ('photo2', models.ImageField(blank=True, upload_to='property_images/')),
                ('photo3', models.ImageField(blank=True, upload_to='property_images/')),
                ('photo4', models.ImageField(blank=True, upload_to='property_images/')),
                ('photo5', models.ImageField(blank=True, upload_to='property_images/')),
                ('photo6', models.ImageField(blank=True, upload_to='property_images/')),
                ('property_poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]