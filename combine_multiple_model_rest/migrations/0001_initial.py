# Generated by Django 3.2.7 on 2021-09-29 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('model1_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('model1_item_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('model2_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('model2_item_name', models.CharField(max_length=50)),
                ('model1_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combine_multiple_model_rest.model1')),
            ],
        ),
    ]
