# Generated by Django 5.0.7 on 2024-08-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids'), ('Baby', 'Baby'), ('Sports', 'Sports')], default='men', max_length=10),
        ),
    ]
