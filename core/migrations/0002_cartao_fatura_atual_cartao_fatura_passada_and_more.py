# Generated by Django 4.1.3 on 2022-11-06 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartao',
            name='fatura_atual',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartao',
            name='fatura_passada',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartao',
            name='limite',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=9),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('motivo', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tipo', models.CharField(max_length=10)),
                ('forma', models.CharField(max_length=50)),
                ('mes', models.DecimalField(decimal_places=0, max_digits=2)),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cartao')),
            ],
        ),
    ]
