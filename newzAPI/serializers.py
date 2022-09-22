from rest_framework import serializers

from newz.models import LatestNewsModel

class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNewsModel
        fields = ('id', 'post_data', 'pub_date', 'custom_post')