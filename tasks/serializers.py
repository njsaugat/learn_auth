from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    user=UserSerializer(read_only=True)
    class Meta:
        model=Task
        fields='__all__'

    def create(self,validated_data):
        user=self.context['request'].user
        
        task_instance=Task.objects.create(user=user,**validated_data)
        return task_instance