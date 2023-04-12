from rest_framework import serializers
from .models import *

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'timestamp']
