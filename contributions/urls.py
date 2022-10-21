from .views import MonthlyContributionViewSet,MerryGoRoundContributionViewSet
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()

routes.register('monthlycontribution', MonthlyContributionViewSet)
routes.register('merrygoroundcontribution', MerryGoRoundContributionViewSet)

urlpatterns = [
    
    
]

urlpatterns += routes.urls
