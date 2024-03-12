# reminders/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reminder
from .serializers import ReminderSerializer

@api_view(['POST'])
def create_reminder(request):
    """
    API endpoint to create a reminder.
    """
    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        print(serializer,"90990")
     
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

