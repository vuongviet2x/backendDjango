from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, permissions, generics, status
from .models import Account, Document, Operation,User, Rack_group, Borrowing, History
from .serializers import AccountSerializer, DocumentSerializer, OperationSerializer, UserSerializer, BorrowSerializer, HistorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from rest_framework import permissions, authentication
# Create your views here.

# class UserRackViewSet(viewsets.ModelViewSet, generics.CreateAPIView, generics.RetrieveAPIView,generics.ListAPIView):
#     data = Rack_group.objects.select_related('user_id_Rackgroup').values_list('id')
#     print(data.query)
#     serializer_class = UserRackSerializer
class UserViewSet(viewsets.ModelViewSet, generics.CreateAPIView, generics.RetrieveAPIView,generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowSerializer
class HistoryViewSet(viewsets.ModelViewSet, generics.CreateAPIView, generics.RetrieveAPIView,generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class AccountViewSet(viewsets.ModelViewSet,generics.ListAPIView,generics.CreateAPIView,generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.filter(active=True)
    serializer_class = DocumentSerializer

    @swagger_auto_schema(
        operation_description='API dung de an mot bai viet tu phia client',
        responses={
            status.HTTP_200_OK: DocumentSerializer()
        }
    )
    @action(methods=['post'],detail=True, url_path="hide-lesson", url_name="hide-lesson")
    def hide_lesson(self,request,pk):
        try:
            l=Document.objects.get(pk=pk)
            l.active= False
            l.save()
        except Document.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=DocumentSerializer(l).data,status=status.HTTP_200_OK)

    # @action(methods=['get'], detail=True, url_path="group-rack", url_name="group-rack")
    # def hide_lesson(self, request, pk):
    #     try:
    #         l = Document.objects.get(group_rack_id=pk)
    #         l.active = False
    #         l.save()
    #     except Document.DoesNotExits:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     return Response(data=DocumentSerializer(l).data, status=status.HTTP_200_OK)
@api_view(('GET',))
def get_specific_document_group_rack(request, group_rack_id):
    try:
        print('group document id....')
        queryset = Document.objects.filter(group_rack_id=group_rack_id)
        serializer = DocumentSerializer(queryset,many=True)
    except DocumentSerializer.DoesNotExits:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)

        # serializer_class = DocumentSerializer

    # @swagger_auto_schema(
    #     operation_description='API dung de an mot bai viet tu phia client',
    #     responses={
    #         status.HTTP_200_OK: DocumentSerializer()
    #     }
    # )
    # @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    # def hide_lesson(self, request, pk):
    #     try:
    #         l = Document.objects.get(pk=pk)
    #         l.active = False
    #         l.save()
    #     except Document.DoesNotExits:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     return Response(data=DocumentSerializer(l).data, status=status.HTTP_200_OK)
def index(request):
    return render(request, template_name='api/index.html',context = { 'name': 'Pham QUy'})