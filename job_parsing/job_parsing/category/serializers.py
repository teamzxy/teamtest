from category.models import parsing
from rest_framework import serializers

class parsingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = parsing
        fields = ['id','post_name','post_path','post_category']



