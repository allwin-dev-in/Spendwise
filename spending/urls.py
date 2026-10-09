from django.urls import path

from spending.views import RegisterView
from spending.views import GetMeView
from spending.views import ExpenseListCreateView
from spending.views import ExpenseRetriveUpdateDeleteView

urlpatterns=[
    path("register/",RegisterView.as_view()),
    path("me/",GetMeView.as_view()),
    path("expense/",ExpenseListCreateView.as_view()),
    path("expense/<int:pk>/",ExpenseRetriveUpdateDeleteView.as_view())    
]