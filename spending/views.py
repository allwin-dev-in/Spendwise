from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions


from spending.serializers import SignupSerializer
from spending.serializers import ExpenseSerializer
from spending.models import Expense
from spending.permissions import IsOwner

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignupSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class GetMeView(APIView):

    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        user_data=request.user
        qs=User.objects.get(username=user_data)
        ser_inst=SignupSerializer(qs)
        return Response(data=ser_inst.data)


class ExpenseListCreateView(APIView):
    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Expense.objects.filter(owner=request.user)
        serializer_instance=ExpenseSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=ExpenseSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(owner=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class ExpenseRetriveUpdateDeleteView(APIView):

    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def get(self,request,pk=None):
        instance=get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance=ExpenseSerializer(instance)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        instance=get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,instance)
        form_data=request.data
        serializer_instance=ExpenseSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        instance=get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,instance)
        instance.delete()
        return Response({"message":"Data Deleted ..."})


