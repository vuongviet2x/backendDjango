
from django.urls import path, re_path, include
from . import views
# from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('account',views.AccountViewSet,basename='account')
router.register('document',views.DocumentViewSet)
# router.register('document_rack_group/<int:group_rack_id>',views.get_specific_document_group_rack)
router.register('operation',views.OperationViewSet)
router.register('users',views.UserViewSet)
router.register('borrow',views.BorrowViewSet)
router.register('history',views.HistoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('document_rack_group/<int:group_rack_id>',views.get_specific_document_group_rack),
]
