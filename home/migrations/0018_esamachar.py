# Generated by Django 3.1.4 on 2021-03-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_notice_board_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='eSamachar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievement')),
                ('desc', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
