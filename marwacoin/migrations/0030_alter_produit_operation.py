# Generated by Django 3.2.10 on 2022-02-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0029_auto_20220203_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('vente', 'vente'), ('location', 'location'), ('echange', 'echange'), ('donation', 'donation')], default='vente', max_length=255),
        ),
    ]