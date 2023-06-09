# Generated by Django 3.2.9 on 2023-04-12 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cName', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('cEmail', models.EmailField(max_length=254)),
                ('cLogo', models.ImageField(blank=True, upload_to='images')),
                ('cUrl', models.CharField(max_length=50)),
                ('bank_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eFname', models.CharField(max_length=50)),
                ('eLname', models.CharField(max_length=50)),
                ('eEmail', models.EmailField(max_length=254)),
                ('ePhone', models.CharField(max_length=50)),
                ('emonthly_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('etax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('einsurance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('epension', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('last_pay_date', models.DateField(default=django.utils.timezone.now)),
                ('last_pay_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payroll', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('eCompany', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mirai.company')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirai.employee')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
