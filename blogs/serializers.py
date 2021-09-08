from .models import Blogs
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our BlogSerializer
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogs
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']