from django.urls import path
from .views import ValidateLicenceView

urlpatterns = [
    path('validate-licence/<uuid:uuid>/', ValidateLicenceView.as_view(), name='validate_licence'),
]
