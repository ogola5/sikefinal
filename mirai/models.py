from django.utils import timezone
from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
from decimal import Decimal
# Create your models here.

class Company(models.Model):
    cName = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="images", blank=True)
    cUrl = models.CharField(max_length=50)
    bank_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        db_table = "company"

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField(default=timezone.now)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    class Meta:
        db_table = "payment"

class Employee(models.Model):
    eFname = models.CharField(max_length=50)
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    emonthly_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    etax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    einsurance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    epension = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_pay_date = models.DateField(default=timezone.now)
    last_pay_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payroll = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = "employee"

    def create_payment(self):
        monthly_pay = self.emonthly_salary
        gross_pay = monthly_pay
        tax = self.etax 
        insurance = self.einsurance
        pension = self.epension 
        net_pay = gross_pay - tax - insurance - pension

        return net_pay

    def process_payment(self):
        payment = Payment.objects.create(
            employee=self,
            amount=self.create_payment(),
            date=timezone.now()
        )

        self.last_pay_date = timezone.now().date()
        self.last_pay_amount = payment.amount
        self.save()
