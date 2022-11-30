from rest_framework import serializers 

from .models import Cat 

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        # tell it what fields I want to show
        # with dunder all (double under scores before and after)
        fields = '__all__'
        # tell it which model to reference
        model = Cat