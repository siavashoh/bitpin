from rest_framework.serializers import ModelSerializer
from django.db.models import Avg, Count
from content.models import Content, Rate


class ContentSerializer(ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        rates = Rate.objects.filter(content__id=instance.id)
        rate_avg = rates.aggregate(Avg('rate')).get("rate__avg")
        rate_count = rates.aggregate(Count('user')).get("user__count")
        ret['avg_rate'] = rate_avg if rate_avg else 0
        ret['users_rated_count'] = rate_count if rate_count else 0

        user_rate = rates.filter(user=instance.user).first()
        if user_rate:
            ret['user_rate'] = user_rate.rate
        return ret

    class Meta:
        model = Content
        fields = ['title', 'context', 'user']


class RateSerializer(ModelSerializer):

    def create(self, validated_data):
        content = validated_data['content']
        user = validated_data['user']
        rate = Rate.objects.filter(user=user, content__id=content.id).first()
        if rate:
            rate.rate=validated_data['rate']
            rate.save()
            return rate
        return super().create(validated_data)

    class Meta:
        model = Rate
        fields = ["rate", "content", 'user']
