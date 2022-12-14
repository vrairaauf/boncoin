# Generated by Django 3.2.10 on 2022-02-01 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0023_auto_20220201_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.AddField(
            model_name='conversation',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marwacoin.message'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='tache',
            field=models.CharField(choices=[('reception', 'reception'), ('destination', 'destination')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('vente', 'vente'), ('location', 'location'), ('donation', 'donation'), ('echange', 'echange')], default='vente', max_length=255),
        ),
    ]
