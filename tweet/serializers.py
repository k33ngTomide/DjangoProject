from rest_framework import serializers

from tweet.models import Tweet, Comment


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'text', 'last_update']

    # id = serializers.IntegerField()
    # text = serializers.CharField(max_length=200)
    # last_update = serializers.DateTimeField()


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # tweet = TweetSerializer()
    # tweet = serializers.StringRelatedField()

    # tweet = serializers.HyperlinkedRelatedField(
    #     'tweet-detail', queryset=Tweet.objects.all()
    # )

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'commented_on', 'tweet']
