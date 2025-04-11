from django.shortcuts import render
 
# Create your views here.
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import AzureOpenAI
import os
from .models import Message
 
class ChatbotView(APIView):
    def post(self, request):
        try:
            # Ensure JSON data is present
            if not request.data:
                return Response({"error": "Empty request body"}, status=status.HTTP_400_BAD_REQUEST)
 
            data = request.data  # DRF automatically handles JSON parsing
            user_message = data.get("message")
 
            if not user_message:
                return Response({"error": "Message field is required"}, status=status.HTTP_400_BAD_REQUEST)
 
            # save user message to database
            Message.objects.create(sender='user',text=user_message)

            # Initialize Azure OpenAI client
            client = AzureOpenAI(
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version="2024-02-01"
            )
 
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-35-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )

            bot_reply = response.choices[0].message.content
 
            # Save bot reply to database
            Message.objects.create(sender="bot", text=bot_reply)
 
            return Response({"response": bot_reply}, status=status.HTTP_200_OK)
 
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 