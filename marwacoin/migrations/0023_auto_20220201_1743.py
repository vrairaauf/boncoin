# Generated by Django 3.2.10 on 2022-02-01 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marwacoin', '0022_auto_20220201_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('participant', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='expediteur',
        ),
        migrations.AlterField(
            model_name='contact',
            name='cause',
            field=models.CharField(choices=[('la deuxiem echoix', 'la deuxiem choices'), ('demande une partenaire', 'demande une partenaire')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='operation',
            field=models.CharField(choices=[('vente', 'vente'), ('echange', 'echange'), ('donation', 'donation'), ('location', 'location')], default='vente', max_length=255),
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marwacoin.conversation'),
        ),
    ]
