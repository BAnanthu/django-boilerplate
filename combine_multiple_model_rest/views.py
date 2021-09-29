from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from django.views import View

from combine_multiple_model_rest.serializers import Model1Serializer, Model2Serializer


# SINGLE FORM DATA SAVED TO TWO MODELS RELATED BY FOREGINKEY
class CombineModelPost(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        data1 = {'model1_item_name': request.data['model1_item_name']}
        data2 = {'model2_item_name': request.data['model2_item_name'],
                 'model1_item_id': request.data['model1_item_id']}
        serializer1 = Model1Serializer(data=data1)
        serializer2 = Model2Serializer(data=data2)
        if serializer1.is_valid():
            serializer1.save()
            response1 = serializer1.data
            if serializer2.is_valid():
                serializer2.save()
                response2 = serializer2.data
                return Response({'detail': [response1, response2]}, status=status.HTTP_201_CREATED)

        else:
            return Response({'error': [serializer1.errors or serializer2.errors]}, status=status.HTTP_400_BAD_REQUEST)

        # OUTPUT
        # {
        #     "detail": [
        #         {
        #             "model1_item_id": 6,
        #             "model1_item_name": "hello"
        #         },
        #         {
        #             "model2_item_id": 2,
        #             "model2_item_name": "hello2",
        #             "model1_item_id": 6
        #         }
        #     ]
        # }
