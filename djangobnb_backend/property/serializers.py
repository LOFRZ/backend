from rest_framework import serializers

from .models import Property, Reservation
from useraccount.serializers import UserDetailSerializer


class PropertiesListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True, many=False)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord'
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class ReservationsListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializer(read_only=True, many=False)

    class Meta:
        model = Reservation
        fields = (
            'id',
            'start_date',
            'end_date',
            'number_of_nights',
            'total_price',
            'property',
        )
