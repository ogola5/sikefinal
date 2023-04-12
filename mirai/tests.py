from django.test import TestCase
from mirai.models import Company, Employee
from unittest.mock import patch
# from mirai.mpesa import MpesaClient

class EmployeePaymentTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            cName='My Company',
            cEmail='info@mycompany.com',
            cUrl='http://www.mycompany.com',
            bank_balance=10000
        )
        self.employee = Employee.objects.create(
            eFname='John',
            eLname='Doe',
            eCompany=self.company,
            eEmail='johndoe@mycompany.com',
            ePhone='0734567890',
            emonthly_salary=5000.00,
            evalue_per_hour=10.00,
            extra_per_hour=2.00,
            etax=500.00,
            einsurance=500.00,
            epension=200.00
        )

    def test_process_payment_sufficient_funds(self):
        self.assertEqual(self.company.bank_balance, 10000.00)
        self.assertEqual(self.employee.last_pay_amount, 0.00)

        # Ensure that payment is processed when there are sufficient funds
        self.employee.process_payment()
        self.assertEqual(self.employee.last_pay_amount, 3820.00)
        self.assertEqual(self.employee.last_pay_date, self.employee.last_pay_date)

        # Ensure that the account balance is updated after payment is processed
        self.company.refresh_from_db()
        self.assertEqual(self.company.bank_balance, 10000.00)

    def test_process_payment_insufficient_funds(self):
        self.assertEqual(self.company.bank_balance, 10000.00)
        self.assertEqual(self.employee.last_pay_amount, 0.00)

        # Reduce account balance to trigger an insufficient funds scenario
        self.company.bank_balance = 200.00
        self.company.save()
        self.assertEqual(self.company.bank_balance, 200.00)

        # Ensure that payment is not processed when there are insufficient funds
        self.employee.process_payment()
        self.assertEqual(self.employee.last_pay_amount, 3820.00)
        self.assertEqual(self.employee.last_pay_date, self.employee.last_pay_date)

        # Ensure that the account balance is unchanged after payment is not processed
        self.company.refresh_from_db()
        self.assertEqual(self.company.bank_balance, 200.00)


# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase, override_settings
# from django.core import mail
# from unittest import mock
# from datetime import date, timedelta
# from freezegun import freeze_time
# from mirai.tasks import process_payroll
# from mirai.models import Employee, Payment, Company


# class ProcessPayrollTestCase(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Create test data
#         cls.company = Company.objects.create(
#             cName='Delta private security',
#             bank_balance=100000.00
#         )
#         cls.employee = Employee.objects.create(
#             eFname='Paul',
#             eLname='Gitonga',
#             last_pay_date=date.today() - timedelta(days=30),
#             payroll=1000.00
#         )

#     @freeze_time('2022-04-09')
#     @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
#     def test_process_payroll(self):
#         # Call the Celery task
#         result = process_payroll.delay()

#         # Check the result
#         self.assertEqual(result.get()['status'], 'success')
#         self.assertEqual(result.get()['num_processed'], 1)
#         self.assertEqual(result.get()['total_amount'], 1000)

#         # Check that the employee's last_pay_date and last_pay_amount were updated
#         employee = Employee.objects.get(id=self.employee.id)
#         self.assertEqual(employee.last_pay_date, date.today())
#         self.assertEqual(employee.last_pay_amount, 1000)

#         # Check that a Payment object was created
#         payment = Payment.objects.first()
#         self.assertEqual(payment.employee, self.employee)
#         self.assertEqual(payment.amount, 1000)
#         self.assertEqual(payment.date, date.today())

#         # Check that the company's bank_balance was updated
#         company = Company.objects.get(id=self.company.id)
#         self.assertEqual(company.bank_balance, 9000)

#         # Check that no email was sent
#         self.assertEqual(len(mail.outbox), 0)

#     @freeze_time('2022-04-09')
#     @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
#     @mock.patch('myapp.models.Company.bank_balance', return_value=0)
#     def test_process_payroll_insufficient_funds(self, mock_bank_balance):
#         # Call the Celery task
#         result = process_payroll.delay()

#         # Check the result
#         self.assertEqual(result.get()['status'], 'failure')

#         # Check that the employee's last_pay_date and last_pay_amount were not updated
#         employee = Employee.objects.get(id=self.employee.id)
#         self.assertEqual(employee.last_pay_date, date.today() - timedelta(days=30))
#         self.assertEqual(employee.last_pay_amount, 1000)

#         # Check that no Payment object was created
#         payment = Payment.objects.all()
#         self.assertEqual(len(payment), 0)

#         # Check that the company's bank_balance was not updated
#         company = Company.objects.get(id=self.company.id)
#         self.assertEqual(company.bank_balance, 100000)

#         # Check that an email was sent
#         self.assertEqual(len(mail.outbox), 1)
#         self.assertEqual(mail.outbox[0].subject, 'Payment Processing Failed')
#         self.assertEqual(mail.outbox[0].body, 'Not enough funds in company bank account to process payment for employee John Doe.')


# from django.test import TestCase
# from django.utils import timezone
# from unittest.mock import patch
# from freezegun import freeze_time
# from mirai.models import Company, Employee

# class TestEmployeePayment(TestCase):
#     def setUp(self):
#         self.company = Company.objects.create(
#             cName='Test Company',
#             cEmail='test@test.com',
#             cUrl='http://www.test.com'
#         )

#         self.employee = Employee.objects.create(
#             eFname='Test',
#             eLname='Employee',
#             eCompany=self.company,
#             eEmail='test@test.com',
#             ePhone='1234567890',
#             emonthly_salary=5000,
#             evalue_per_hour=10,
#             extra_per_hour=2,
#             etax=0.2,
#             einsurance=0.1,
#             epension=0.1,
#             last_pay_date=timezone.now().date(),
#             last_pay_amount=2000,
#             payroll=3000
#         )

#     @patch('mirai.models.Payment.objects.create')
#     @freeze_time("2022-01-01")
#     def test_create_payment(self, mock_create_payment):
#         net_pay = self.employee.create_payment()
#         mock_create_payment.return_value.amount = net_pay
#         self.employee.process_payment()

#         self.assertEqual(self.employee.last_pay_date, timezone.now().date())
#         self.assertEqual(self.employee.last_pay_amount, net_pay)
