# Generated by Django 3.2.10 on 2022-02-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0016_auto_20220201_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('cause', models.CharField(choices=[('la deuxiem echoix', 'la deuxiem choices'), ('demande une partenaire', 'demande une partenaire')], max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lire', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('location', 'location'), ('vente', 'vente'), ('echange', 'echange'), ('donation', 'donation')], default='vente', max_length=255),
        ),
    ]