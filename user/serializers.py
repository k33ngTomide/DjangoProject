from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializers


class UserSerializer(BaseUserCreateSerializers):
    class Meta(BaseUserCreateSerializers.Meta):
        fields = ['username', 'email', 'password', 'first_name', "last_name"]
