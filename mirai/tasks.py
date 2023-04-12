from celery import shared_task
from django.utils import timezone
from django.core.mail import mail_admins
from django.db.models import F, Sum
from .models import Employee, Payment, Company


@shared_task
def process_payroll(batch_size=100):
    try:
        today = timezone.now().date()
        employees = Employee.objects.filter(last_pay_date__lte=today)

        company = Company.objects.first()  # get the first company instance

        total_amount = 0
        num_processed = 0
        for batch_start in range(0, employees.count(), batch_size):
            batch_end = batch_start + batch_size
            batch = employees[batch_start:batch_end]

            for employee in batch:
                # Calculate pay and deductions using create_payment method
                net_pay = employee.create_payment()

                # Check if company has enough money in bank account
                if company.bank_balance >= net_pay:
                    # Process payment
                    payment = Payment.objects.create(
                        employee=employee,
                        amount=net_pay,
                        date=today
                    )

                    total_amount += net_pay
                    num_processed += 1

                    # Deduct payment amount from company bank balance
                    company.bank_balance -= net_pay
                    company.save()
                else:
                    # Send email notification to admin if company doesn't have enough money
                    message = f"Not enough funds in company bank account to process payment for employee {employee.eFname} {employee.eLname}."
                    mail_admins(subject="Payment Processing Failed", message=message)

        # Update last_pay_date and last_pay_amount for each employee
        employees.update(last_pay_date=today, last_pay_amount=F('payroll'))

        # Send email notification to admin
        message = f"Payroll processing complete. {num_processed} employees processed for a total amount of {total_amount:.2f}."
        mail_admins(subject="Payroll Processing Complete", message=message)

        return {'status': 'success', 'num_processed': num_processed, 'total_amount': total_amount}
    except Exception as e:
        # Log any exceptions and send email notification to admin
        message = f"Payroll processing failed with error: {str(e)}"
        print(message)
        mail_admins(subject="Payroll Processing Failed", message=message)
        return {'status': 'failure', 'error': str(e)}
