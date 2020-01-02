from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from ..models import Post
from rest_framework.decorators import action
from rest_framework.response import Response

class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.upvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'upvotes': post.upvotes
        })

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.downvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'downvotes': post.downvotes
        })