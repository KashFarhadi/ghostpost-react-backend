from rest_framework.serializers import HyperlinkedModelSerializer
from ..models import Post

class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_at', 'upvotes', 'downvotes', 'type_of_post', 'score')
        