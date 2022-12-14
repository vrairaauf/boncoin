# Generated by Django 3.2.10 on 2022-03-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0041_auto_20220330_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cause',
            field=models.CharField(choices=[('Suggérer une fonctionnalité', 'Suggérer une fonctionnalité'), ('Signaler un probléme', 'Signaler un probléme'), ('Un contract de partenariat', 'Un contract de partenariat')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='contenu',
            field=models.TextField(default="aucun desrioption de produit veiller contacter le responsable du produit pour plusieur d'inforamation", null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='etat',
            field=models.CharField(choices=[('presq neuf', 'presq neuf'), ('occasion', 'occasion'), ('neuf', 'neuf'), ('bon état', 'bon état')], default='normal', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('échange', 'échange'), ('vente', 'vente'), ('donation', 'donation'), ('louer', 'louer')], default='vente', max_length=255),
        ),
    ]
