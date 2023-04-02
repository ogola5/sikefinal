from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BankAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountType
        fields = ['name', 'maximum_withdrawal_amount', 'annual_interest_rate', 'interest_calculation_per_year']

class UserBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserBankAccount
        fields = ['user', 'account_type', 'account_no', 'gender', 'birth_date', 'balance', 'interest_start_date', 'initial_deposit_date'] 

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['user', 'street_address', 'city', 'postal_code', 'country']         