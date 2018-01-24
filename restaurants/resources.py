from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from restaurants.models import Restaurant, RestaurantType


class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurant'
        authorization = Authorization()


class RestaurantTypeResource(ModelResource):
    class Meta:
        queryset = RestaurantType.objects.all()
        resource_name = 'restaurant_type'
        authorization = Authorization()

