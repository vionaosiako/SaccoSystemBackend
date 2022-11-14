from .views import MerryGoRoundContributionViewSet, getMonthlyContribution, getMonthlyContributionDetails
from rest_framework.routers import DefaultRouter
from django.urls import path



routes = DefaultRouter()

# routes.register('monthlycontribution', MonthlyContributionViewSet)
routes.register('merrygoroundcontribution', MerryGoRoundContributionViewSet)

urlpatterns = [
    path('monthlycontribution/',getMonthlyContribution,name='monthlycontribution'),
    path('monthlycontribution/<int:id>', getMonthlyContributionDetails),
    
]

urlpatterns += routes.urls
