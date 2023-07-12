from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ContactForm
from .serializers import ContactFormSerializer


class ContactFormView(APIView):
    def get(self, request):
        contacts = ContactForm.objects.all()
        serializer = ContactFormSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Form submitted successfully!'}, status=201)
        else:
            return Response(serializer.errors, status=400)
