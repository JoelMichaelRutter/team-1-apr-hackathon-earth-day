# Generated by Django 3.2 on 2022-04-23 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('plastics', 'plastics'), ('cardboard', 'cardboard'), ('glass', 'glass'), ('metal', 'metal'), ('electronics', 'electronics'), ('organic_waste', 'organic_waste')], default=None, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recycle_actions', to='profiles.userprofile')),
            ],
        ),
    ]