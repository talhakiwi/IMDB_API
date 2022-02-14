from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    length_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
    
    # calculate lenght of name
    def get_length_name(self,objects):
        return len(objects.name)
    
    # # object level validation    
    # def validate(self, data):
    #     if data['name'] ==  data['description']:
    #         raise serializers.ValidationError("Title and name should be diffrent! ")
    #     return data
    
    # # feild level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
        

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short! ")
    
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value
        
    