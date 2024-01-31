from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

class TaskView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    

        
        
