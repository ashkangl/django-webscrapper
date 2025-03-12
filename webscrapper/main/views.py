from django.shortcuts import render
from rest_framework.views import APIView
from .models import PageModel
from .serializers import PageSerializers
from rest_framework.response import Response
from rest_framework import status
from .utils import website_scrapper
from .serializers import serializers

class PageScrapperViews(APIView):
    def get(self,request,pk=None):
        if pk:
            try:
                page = PageModel.objects.get(pk=pk)
            except PageModel.DoesNotExist:
                return Response({"error":"Not Found!"},status=status.HTTP_404_NOT_FOUND)
            serializer = PageSerializers(page)
            return Response(serializer.data)
        else:
            pages = PageModel.objects.all()
            serializer = PageSerializers(pages,many=True)
            return Response(serializer.data)

    def post(self,request):
        url = request.data.get('url')
        scrapped_data = website_scrapper(url)
        if scrapped_data:
            content = PageModel.objects.create(
                title = scrapped_data['title'],
                body = scrapped_data['body'],
            )
            serializers = PageSerializers(content)
            return Response(serializers.data,status=status.HTTP_201_CREATED,content_type='application/json')
        else:
            return Response({"error":"Scrapped Failed!"},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk=None):
        if pk:
            try:
                page = PageModel.objects.get(pk=pk)
                page.delete()
            except PageModel.DoesNotExist:
                return Response({"error":"Not Found!"},status=status.HTTP_404_NOT_FOUND)
        else:
            page = PageModel.objects.all().delete()

        return Response({"message":"Delete success"},status=status.HTTP_204_NO_CONTENT)
