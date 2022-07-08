from django.urls import path
from .views import PartyView

urlpatterns = [
    path('parties/', PartyView.as_view()),
    path('parties/<str:type>', PartyView.as_view()),
    path('put_party/<int:id>', PartyView.as_view()),
]