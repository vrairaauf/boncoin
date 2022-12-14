# Generated by Django 3.2.10 on 2022-02-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0037_auto_20220209_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='nom',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cause',
            field=models.CharField(choices=[('Signaler un probléme', 'Signaler un probléme'), ('Suggérer une fonctionnalité', 'Suggérer une fonctionnalité'), ('Un contract de partenariat', 'Un contract de partenariat')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('échange', 'échange'), ('louer', 'louer'), ('donation', 'donation'), ('vente', 'vente')], default='vente', max_length=255),
        ),
    ]
