from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadedImageSerializer
from .ocr import extract_text

# Create your views here.
def index(request):
    return render(request,'index.html')


class OCRUploadView(APIView):
    parser_classes=[MultiPartParser,FormParser]

    def post(self,request):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            file_path=serializer.instance.file.path
            text=extract_text(file_path)
            return Response({"text":text})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
