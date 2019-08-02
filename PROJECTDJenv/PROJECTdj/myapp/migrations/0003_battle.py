# Generated by Django 2.2.3 on 2019-08-02 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_champ'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dom_but', models.IntegerField()),
                ('ext_but', models.IntegerField()),
                ('cham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Champ')),
                ('dom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Domicile')),
                ('ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Exterieure')),
            ],
        ),
    ]