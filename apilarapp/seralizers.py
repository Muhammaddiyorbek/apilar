from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class BookSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=('id','title','subtitle','content','author','isbn','price',)

    def validate(self,data):
        title=data.get('title',None)
        author = data.get('author', None)

        # title validate
        if not title.isalpha():
            raise ValidationError(
                {'status':False,
                 'message':'Kitob sarlavhasi harflardan iborat bolishi kerak!'}
            )

        # title va author validate
        if Books.objects.filter(title=title,author=author).exists():
            raise ValidationError(
                {'status':False,
                 'message':'Bunday nomdagi kitob bor!'}
            )
        return data

