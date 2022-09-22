from re import T
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from newz.models import LatestNewsModel
from .serializers import LatestNewsSerializer


# # Create your views here.

class LatestNewsAPIView(APIView):

    def get(self, request):
        '''
        Method to GET all posts
        '''
        try:
            latestNews_instance = LatestNewsModel.objects.all().order_by('id')
            serializer = LatestNewsSerializer(latestNews_instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except LatestNewsModel.DoesNotExist:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


class NewsAPIView(APIView):

    def get_object(self, post_id):
        '''
        Helper method to get the object with given post_id
        '''
        try:
            data = LatestNewsModel.objects.filter(id=post_id)
            return data
        except LatestNewsModel.DoesNotExist:
            return None

    # 1. Retrieve
    def get(self, request, post_id, *args, **kwargs):
        '''
        Retrieves the Post with given post_id
        '''
        post_instance = self.get_object(post_id)
        if not post_instance:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LatestNewsSerializer(post_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Update
    def post(self, request, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        post_instance = LatestNewsModel()

        data = {
            'id': request.data.get('id'),
            'post_data': request.data,
            'pub_date': request.data.get('pub_date'),
            'custom_post': True
        }
        serializer = LatestNewsSerializer(
            instance=post_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Update
    def put(self, request, post_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        post_instance = LatestNewsModel.objects.get(id=post_id)
        if not post_instance:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        post_obj = {
            "id": post_instance.id,
            "post_data": post_instance.post_data,
            "pub_date": post_instance.pub_date,
            "custom_post": post_instance.custom_post
        }
        data = {
            **post_obj,
            'post_data': request.data,
            'pub_date': request.data.get('pub_date') or post_obj['pub_date']
        }
        serializer = LatestNewsSerializer(
            instance=post_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. Delete
    def delete(self, request, post_id, *args, **kwargs):
        '''
        Deletes the post item with given post_id if exists
        '''
        post_instance = self.get_object(post_id)
        if not post_instance or not post_instance.first().custom_post:
            return Response(
                {"res": "Cannot delete post. Post is not a custom post"},
                status=status.HTTP_400_BAD_REQUEST
            )
        post_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
