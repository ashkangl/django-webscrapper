from rest_framework import serializers
from .models import PageModel

class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PageModel
        fields = "__all__"