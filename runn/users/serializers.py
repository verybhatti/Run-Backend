from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("__all__")
        
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    def update(self,instance,validated_data):
        instance.phone_Number=validated_data.get('Phone Number',instance.phone_Number)
        instance.save()
        return instance