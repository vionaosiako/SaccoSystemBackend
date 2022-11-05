from .views import MonthlyContributionViewSet,MerryGoRoundContributionViewSet, getMonthlyContribution
from rest_framework.routers import DefaultRouter
from django.urls import path



routes = DefaultRouter()

routes.register('monthlycontribution', MonthlyContributionViewSet)
routes.register('merrygoroundcontribution', MerryGoRoundContributionViewSet)

urlpatterns = [
    path('monthlycontribution/',getMonthlyContribution,name='monthlycontribution')
    
]

urlpatterns += routes.urls
