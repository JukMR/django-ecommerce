# Generated by Django 3.1.7 on 2021-03-09 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('description_text', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.items')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Object',
        ),
    ]
