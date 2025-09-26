from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password')
    def validate_password(self, value):
        validate_password(value); return value
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','balance')
        read_only_fields = ('id','username','email','balance')
class TopUpSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    def validate_amount(self, v):
        if v<=0: raise serializers.ValidationError("Amount must be positive.")
        return v
