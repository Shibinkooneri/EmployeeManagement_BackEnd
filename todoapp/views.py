from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from .serializers import UserSer,TodoSer
from .models import TodoModel
from rest_framework import authentication,permissions

class SignupViewset(ViewSet):
    def create(self,request):
        ser=UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'User created'})
        return Response({'msg':'Failed to create'})

class TodoMViewset(ModelViewSet):
    serializer_class=TodoSer
    queryset=TodoModel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        ser=TodoSer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({'msg':'ToDo Added'})
        return Response({'msg':'Failed'})
    
    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        todo=TodoModel.objects.get(id=id)
        todo.delete()
        return Response({"msg":"Deleted"})
