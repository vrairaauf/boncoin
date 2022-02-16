# Generated by Django 3.2.10 on 2022-02-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0017_auto_20220201_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cause',
            field=models.CharField(choices=[('demande une partenaire', 'demande une partenaire'), ('la deuxiem echoix', 'la deuxiem choices')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('donation', 'donation'), ('location', 'location'), ('echange', 'echange'), ('vente', 'vente')], default='vente', max_length=255),
        ),
    ]