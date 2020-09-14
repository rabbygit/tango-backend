from rest_framework import serializers
from Intense.models import Category,Sub_Category,Sub_Sub_Category
from django.contrib.auth.models import User
#from Cart.models import ProductPoint
from django.utils import timezone
from colour import Color
import requests
from django.urls import reverse,reverse_lazy
#from Intense.Integral_apis import ratings
import json

site_path = "http://127.0.0.1:8000/"





class CategorySerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField(method_name='get_cat')
  
    class Meta:
        model = Category
        fields = ('id','category_id','title','active','level','children')

    def get_cat(self,instance):

        details = Sub_Category.objects.filter(category_id=instance.id).order_by('timestamp').values()
        list_result = [entry for entry in details]
        print(list_result[0]['title'])
        for i in range(len(list_result)):
            sub_id = list_result[i]['id']
            #fetch the titles of sub ids
            subsub = Sub_Sub_Category.objects.filter(sub_category_id = sub_id).order_by('timestamp')
            sub_sub_categories = list(subsub.values_list('title',flat=True).distinct())
            sub_sub_ids = list(subsub.values_list('id',flat=True).distinct())
            sub_subs = list(subsub.values_list('sub_sub_category_id',flat=True).distinct())
            sub_sub_levels = list(subsub.values_list('level',flat=True))
            datas =[]
            for j in range (len(sub_sub_categories)):
                data = {'id':sub_sub_ids[j] ,'sub_sub_category_id':sub_subs[j] ,'title':sub_sub_categories[j],'level':sub_sub_levels[j]}
                datas.append(data)
            list_result[i]['children'] = datas
    

        return list_result


            



# --------------------- Product Discount ---------------------

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = "__all__"
        #fields=("name", "email")



class Sub_Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Sub_Category
        fields = "__all__"
        #fields=("name", "email")






   
   
        



    










     








