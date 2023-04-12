# # from celery import shared_task
# # from django.utils import timezone
# # from .models import Employee

# # @shared_task
# # def process_payroll():
# #     today = timezone.now().date()
# #     employees = Employee.objects.filter(last_pay_date__lte=today)

# #     for employee in employees:
# #         # Calculate pay and deductions
# #         monthly_pay = employee.emonthly_salary
# #         extra_time_pay = employee.extra_time_rate * monthly_pay
# #         gross_pay = monthly_pay + extra_time_pay
# #         tax = employee.tax_rate * gross_pay
# #         insurance = employee.insurance_rate * gross_pay
# #         net_pay = gross_pay - tax - insurance

# #         # Process payment
# #         payment = Payment.objects.create(
# #             employee=employee,
# #             amount=net_pay,
# #             date=t

# from celery import shared_task
# from django.utils import timezone
# from django.core.mail import mail_admins
# from .models import Employee, Payment

# @shared_task
# def process_payroll(batch_size=100):
#     try:
#         today = timezone.now().date()
#         employees = Employee.objects.filter(last_pay_date__lte=today)

#         total_amount = 0
#         num_processed = 0
#         for batch_start in range(0, employees.count(), batch_size):
#             batch_end = batch_start + batch_size
#             batch = employees[batch_start:batch_end]

#             for employee in batch:
#                 # Calculate pay and deductions using create_payment method
#                 net_pay = employee.create_payment()

#                 # Process payment
#                 payment = Payment.objects.create(
#                     employee=employee,
#                     amount=net_pay,
#                     date=today
#                 )

#                 total_amount += net_pay
#                 num_processed += 1

#         # Update last_pay_date and last_pay_amount for each employee
#         employees.update(last_pay_date=today, last_pay_amount=F('payroll'))

#         # Send email notification to admin
#         message = f"Payroll processing complete. {num_processed} employees processed for a total amount of {total_amount:.2f}."
#         mail_admins(subject="Payroll Processing Complete", message=message)

#         return {'status': 'success', 'num_processed': num_processed, 'total_amount': total_amount}
#     except Exception as e:
#         # Log any exceptions and send email notification to admin
#         message = f"Payroll processing failed with error: {str(e)}"
#         print(message)
#         mail_admins(subject="Payroll Processing Failed", message=message)
#         return {'status': 'failure', 'error': str(e)}

# from celery import shared_task
# from django.utils import timezone
# from django.core.mail import mail_admins
# from .models import Employee, Payment

# @shared_task
# def process_payroll(batch_size=100):
#     try:
#         today = timezone.now().date()
#         employees = Employee.objects.filter(last_pay_date__lte=today)

#         total_amount = 0
#         num_processed = 0
#         for batch_start in range(0, employees.count(), batch_size):
#             batch_end = batch_start + batch_size
#             batch = employees[batch_start:batch_end]

#             for employee in batch:
#                 # Calculate pay and deductions using create_payment method
#                 net_pay = employee.create_payment()

#                 # Process payment
#                 payment = Payment.objects.create(
#                     employee=employee,
#                     amount=net_pay,
#                     date=today
#                 )

#                 # Update last_pay_date for the employee
#                 employee.last_pay_date = today

#                 # Update last_pay_amount for the employee
#                 employee.last_pay_amount = net_pay
#                 employee.save()

#                 total_amount += net_pay
#                 num_processed += 1

#         # Send email notification to admin
#         message = f"Payroll processing complete. {num_processed} employees processed for a total amount of {total_amount:.2f}."
#         mail_admins(subject="Payroll Processing Complete", message=message)

#         return {'status': 'success', 'num_processed': num_processed, 'total_amount': total_amount}
#     except Exception as e:
#         # Log any exceptions and send email notification to admin
#         message = f"Payroll processing failed with error: {str(e)}"
#         print(message)
#         mail_admins(subject="Payroll Processing Failed", message=message)
#         return {'status': 'failure', 'error': str(e)}
