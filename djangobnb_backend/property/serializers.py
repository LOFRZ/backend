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
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url  # Plus besoin de `request`
        return None


class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True)
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
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url  # Cloudinary fournit une URL publique
        return None


class ReservationsListSerializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'id', 'start_date', 'end_date', 'number_of_nights', 'total_price', 'property'
        )

    def get_property(self, obj):
        # Important : context passé ici pour inclure l'image_url
        return PropertiesDetailSerializer(obj.property, context=self.context).data
