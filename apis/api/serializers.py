import traceback

from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from .models import Account, Document, Operation,User,Borrowing, History
# class UserRackSerializer(ModelSerializer):
#     class Meta:
#
class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields= ["email","password","username","role","created_at"]

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ["id","name","author","created_at","rack_id_Document","active","group_rack_id"]

class BorrowSerializer(ModelSerializer):
    class Meta:
        model = Borrowing
        fields= ["id","document_id","date_borrowed","date_returned"]
class OperationSerializer(ModelSerializer):
    class Meta:
        model = Operation
        fields = ["rack_id_Operation","open_specific_rack","handlemoving","ventilate","guide_light","group_id"]
class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields= ["action","created_at"]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= ['id','first_name','last_name','email','username','password']
    def create(self, validated_data):
            """
            We have a bit of extra checking around this in order to provide
            descriptive messages when something goes wrong, but this method is
            essentially just:

                return ExampleModel.objects.create(**validated_data)

            If there are many to many fields present on the instance then they
            cannot be set until the model is instantiated, in which case the
            implementation is like so:

                example_relationship = validated_data.pop('example_relationship')
                instance = ExampleModel.objects.create(**validated_data)
                instance.example_relationship = example_relationship
                return instance

            The default implementation also does not handle nested relationships.
            If you want to support writable nested relationships you'll need
            to write an explicit `.create()` method.
            """
            if validated_data['password']:
                validated_data['password'] = make_password(validated_data['password'])
            raise_errors_on_nested_writes('create', self, validated_data)

            ModelClass = self.Meta.model

            # Remove many-to-many relationships from validated_data.
            # They are not valid arguments to the default `.create()` method,
            # as they require that the instance has already been saved.
            info = model_meta.get_field_info(ModelClass)
            many_to_many = {}
            for field_name, relation_info in info.relations.items():
                if relation_info.to_many and (field_name in validated_data):
                    many_to_many[field_name] = validated_data.pop(field_name)

            try:
                instance = ModelClass._default_manager.create(**validated_data)
            except TypeError:
                tb = traceback.format_exc()
                msg = (
                    'Got a `TypeError` when calling `%s.%s.create()`. '
                    'This may be because you have a writable field on the '
                    'serializer class that is not a valid argument to '
                    '`%s.%s.create()`. You may need to make the field '
                    'read-only, or override the %s.create() method to handle '
                    'this correctly.\nOriginal exception was:\n %s' %
                    (
                        ModelClass.__name__,
                        ModelClass._default_manager.name,
                        ModelClass.__name__,
                        ModelClass._default_manager.name,
                        self.__class__.__name__,
                        tb
                    )
                )
                raise TypeError(msg)

            # Save many-to-many relationships after the instance is created.
            if many_to_many:
                for field_name, value in many_to_many.items():
                    field = getattr(instance, field_name)
                    field.set(value)

            return instance
    def update(self, instance, validated_data):
            raise_errors_on_nested_writes('update', self, validated_data)
            info = model_meta.get_field_info(instance)

            # Simply set each attribute on the instance, and then save it.
            # Note that unlike `.create()` we don't need to treat many-to-many
            # relationships as being a special case. During updates we already
            # have an instance pk for the relationships to be associated with.
            if validated_data['password']:
                validated_data['password'] = make_password(validated_data['password'])
            m2m_fields = []
            for attr, value in validated_data.items():
                if attr in info.relations and info.relations[attr].to_many:
                    m2m_fields.append((attr, value))
                else:
                    setattr(instance, attr, value)

            instance.save()

            # Note that many-to-many fields are set after updating instance.
            # Setting m2m fields triggers signals which could potentially change
            # updated instance and we do not want it to collide with .update()
            for attr, value in m2m_fields:
                field = getattr(instance, attr)
                field.set(value)

            return instance