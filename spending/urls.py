from django.urls import path

from spending.views import RegisterView
from spending.views import GetMeView
from spending.views import ExpenseListCreateView
from spending.views import ExpenseRetriveUpdateDeleteView
from spending.views import ExpenseSummaryView
from spending.views import BudgetPlanView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path("register/",RegisterView.as_view()),
    path("me/",GetMeView.as_view()),
    path("expense/",ExpenseListCreateView.as_view()),
    path("expense/<int:pk>/",ExpenseRetriveUpdateDeleteView.as_view()),
    path("expense/summary/",ExpenseSummaryView.as_view()),
    path("expense/budget/",BudgetPlanView.as_view()),


    path("token/",ObtainAuthToken.as_view()),
    
]