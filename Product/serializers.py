import json
import serpy
from rest_framework import serializers
#from user_profile.models import User
from Intense.models import (
    Category, Product , Variation ,GroupProduct,Comment,CommentReply,Reviews,User,Category,
     Product, Variation , GroupProduct,ProductImage,
     ProductPrice,discount_product,ProductCode,ProductSpecification,ProductPoint
)
from drf_extra_fields.fields import Base64ImageField
from django.db.models import Avg


from rest_framework import serializers
from rest_framework import fields
from django.utils import timezone
from django.conf import settings
from django.forms.models import model_to_dict
import requests


host_prefix = "https://"
host_name = host_prefix+settings.ALLOWED_HOSTS[0]

site_path = "https://tango99.herokuapp.com/"
#site_path = "http://127.0.0.1:8000/"

#------------------------ product---------------------------

class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			"id",
			"title",
			"price",
		]


# class ProductSerializer(serializers.ModelSerializer):
#     seller=serializers.SerializerMethodField(method_name='get_seller')



#     class Meta:
#         model = Product
#         fields=[
#             'id',
#             'seller',
#             'category_id',
#             'title',
#             'brand',
#             'image',
#             'description',
#             'quantity',
#             'properties',
#             'is_deleted',
#             "key_features" ,
            
#         ]
 
#     def get_seller(self, obj):
#         return obj.seller


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(method_name='get_images')
    new_price = serializers.SerializerMethodField(method_name='get_new_price')
    old_price = serializers.SerializerMethodField(method_name='get_old_price')
    specification = serializers.SerializerMethodField(method_name='get_specification')


    #comment_name = serializers.SerializerMethodField(method_name='get_name')
    class Meta:
        model = Product
        fields = ('id','title','old_price','new_price','images','specification')

    def get_images(self,instance):
        try:

            replys = ProductImage.objects.filter(product_id=instance.id).values()

        except:
            replys = None

        if replys:
            list_result = [entry for entry in replys] 

        else:
            list_result = []
    
        return list_result


    def get_old_price(self,instance):

        old_price = 0 


        try:


            p_price = ProductPrice.objects.filter(product_id = instance.id).last()

        except:

            p_price = None 


        if p_price is not None:

            old_price =p_price.price

        else:
            old_price = 0


        float_total = format(old_price, '0.2f')
        return float_total



    def get_new_price(self,instance):

        new_price = 0
        discount = 0  


        try:


            p_price = ProductPrice.objects.filter(product_id = instance.id).last()

        except:

            p_price = None 


        if p_price is not None:

            new_price =p_price.price

            try:

                p_discount = discount_product.objects.filter(product_id = instance.id).last()

            except:

                p_discount = None


            if p_discount is not None:

                discount = p_discount.amount
                discount_start_date = p_discount.start_date
                discount_end_date = p_discount.end_date
                current_date = timezone.now().date()

                if (current_date >= discount_start_date) and (current_date <= discount_end_date):

                    new_price = new_price - discount

                else:
                    discount =0 
                    new_price = new_price - discount

            else:
                discount = 0
                new_price = new_price - discount




        else:

            new_price = 0
            


        float_total = format(new_price, '0.2f')
        return float_total


    def get_specification(self,instance):

        arr =  {'colors':[],'sizes':[],'units':[]}


        
        try:


            p_spec = ProductSpecification.objects.filter(product_id = instance.id)

        except:

            p_spec = None 


        if p_spec is not None:

            colors = list(p_spec.values_list('color',flat=True).distinct())
            sizes = list(p_spec.values_list('size',flat=True).distinct())
            units = list(p_spec.values_list('unit',flat=True).distinct())

            arr =  {'colors':colors,'sizes':sizes,'units':units}

            return arr

        else:

            return arr





class SearchSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(method_name='get_images')
    new_price = serializers.SerializerMethodField(method_name='get_new_price')
    old_price = serializers.SerializerMethodField(method_name='get_old_price')
    specification = serializers.SerializerMethodField(method_name='get_specification')
    ratings = serializers.SerializerMethodField(method_name='get_ratings')


    #comment_name = serializers.SerializerMethodField(method_name='get_name')
    class Meta:
        model = Product
        fields = ('id','title','old_price','new_price','brand','images','specification','ratings')

    def get_images(self,instance):
        try:

            replys = ProductImage.objects.filter(product_id=instance.id).values()

        except:
            replys = None

        if replys:
            list_result = [entry for entry in replys] 

        else:
            list_result = []
    
        return list_result


    def get_old_price(self,instance):

        old_price = 0 


        try:


            p_price = ProductPrice.objects.filter(product_id = instance.id).last()

        except:

            p_price = None 


        if p_price is not None:

            old_price =p_price.price

        else:
            old_price = 0


        float_total = format(old_price, '0.2f')
        return float_total



    def get_new_price(self,instance):

        new_price = 0
        discount = 0  


        try:


            p_price = ProductPrice.objects.filter(product_id = instance.id).last()

        except:

            p_price = None 


        if p_price is not None:

            new_price =p_price.price

            try:

                p_discount = discount_product.objects.filter(product_id = instance.id).last()

            except:

                p_discount = None


            if p_discount is not None:

                discount = p_discount.amount
                discount_start_date = p_discount.start_date
                discount_end_date = p_discount.end_date
                current_date = timezone.now().date()

                if (current_date >= discount_start_date) and (current_date <= discount_end_date):

                    new_price = new_price - discount

                else:
                    discount =0 
                    new_price = new_price - discount

            else:
                discount = 0
                new_price = new_price - discount




        else:

            new_price = 0
            


        float_total = format(new_price, '0.2f')
        return float_total


    def get_specification(self,instance):

        arr =  {'colors':[],'sizes':[],'units':[]}


        
        try:


            p_spec = ProductSpecification.objects.filter(product_id = instance.id)

        except:

            p_spec = None 


        if p_spec is not None:

            colors = list(p_spec.values_list('color',flat=True).distinct())
            sizes = list(p_spec.values_list('size',flat=True).distinct())
            units = list(p_spec.values_list('unit',flat=True).distinct())

            arr =  {'colors':colors,'sizes':sizes,'units':units}

            return arr

        else:

            return arr


    def get_ratings(self,instance):


        product_id = instance.id
        #site_path = "https://tango99.herokuapp.com/"

        url = site_path+ "product/ratings/"+str(product_id)+"/"
        values = requests.get(url).json()
        return values



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= [
            "id",
            "title",
            'active',
            'timestamp'

            ]

class GroupProductSerialyzer(serializers.ModelSerializer):
    #count =serializers.SerializerMethodField(method_name='get_Products_ids')
    class Meta:
        model= GroupProduct
        fields = [
            'id',
            "products_ids",
            'title',
            
            'startdate',
            'enddate',
            'flashsellname',
            'active',
            'timestamp',
            'product_id'
        ]
 
    # def get_Products_ids(self, obj):
    #     return len(obj.products_ids)


class SerpyProductSerializer(serpy.Serializer):
    seller = serpy.StrField()
    category = serpy.StrField()
    title = serpy.StrField()
    price = serpy.FloatField()
    image = serpy.StrField()
    description = serpy.StrField()
    quantity = serpy.IntField()
    views = serpy.IntField()

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # read_only_fields = ('id', 'seller', 'category', 'title', 'price', 'image', 'description', 'quantity', 'views',)

#------------Comment Serializers---------------
class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField(method_name='get_replies')
    comment_name = serializers.SerializerMethodField(method_name='get_name')
    class Meta:
        model = Comment
        fields = ('id','comment','date_created','product_id','user_id','non_verified_user_id','comment_name','replies',)

    def get_replies(self,instance):

        replys = CommentReply.objects.filter(comment_id=instance.id).values()
        list_result = [entry for entry in replys]

    
        return list_result

    def get_name(self,instance):
            user_id = instance.user_id
            non_verified_user_id = instance.non_verified_user_id
            comment_name=""
            
    
            if user_id is not None:
                user_id = int(user_id)
                non_verified_user_id =0

            else:
                non_verified_user_id = non_verified_user_id
                user_id = 0

            

            if non_verified_user_id == 0:


                try:


                    name = User.objects.filter(id=user_id).last()
                except:
                    name = None
                if name is not None:
                    comment_name = name.username
                    return comment_name
                else:
                    
                    return comment_name

            else:

                comment_name = "Anonymous"
                return comment_name



class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = ('id','comment_id','reply','date_created','user_id','non_verified_user_id','name')


#------------Review Serializers--------------------
class ReviewsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')
    image_link = serializers.SerializerMethodField(method_name='get_image')
    print("coming to serializer")
    class Meta:
        model = Reviews
        fields = ('id','product_id','user_id','non_verified_user_id','name','content','image','image_link','rating','date_created')

    def get_name(self,instance):
            user_id = instance.user_id
            non_verified_user_id = instance.non_verified_user_id
            comment_name=""
            
    
            if user_id is not None:
                user_id = int(user_id)
                non_verified_user_id =0

            else:
                non_verified_user_id = non_verified_user_id
                user_id = 0

            

            if non_verified_user_id == 0:


                try:


                    name = User.objects.filter(id=user_id).last()
                except:
                    name = None
                if name is not None:
                    comment_name = name.username
                    return comment_name
                else:
                    
                    return comment_name

            else:

                comment_name = "Anonymous"
                return comment_name


    def get_image(self,instance):

        #print("Coming here2")

        try:
            logo_image = Reviews.objects.get(id=instance.id)
        except:
            logo_image = None

        if logo_image is None:
            #print("Coming here3")
            return ""

        else:
            if logo_image.image:

                logo = logo_image.image

                return "{0}{1}".format(host_name,logo.url)

            else:

                return ""

            





class ProductReviewSerializer(serializers.ModelSerializer):
    total_no_of_ratings = serializers.SerializerMethodField(method_name='total_ratings')
    total_no_of_reviews = serializers.SerializerMethodField(method_name='total_reviews')
    average_ratings = serializers.SerializerMethodField(method_name='average_rating')
    each_ratings = serializers.SerializerMethodField(method_name='each_rating')
    class Meta:
        model = Reviews
        fields = ('product_id','total_no_of_ratings','total_no_of_reviews','average_ratings','each_ratings')

    def total_ratings(self,instance):
        try:

            product = Reviews.objects.filter(product_id=instance.product_id).count()

        except:

            product = None

        if product:
            return int(product)

        else:

            return 0

       

        

    def total_reviews(self,instance):
        try:

            product = Reviews.objects.filter(product_id=instance.product_id).count()

        except:

            product = None

        if product:
            return int(product)

        else:

            return 0




    def average_rating(self,instance):


	
        num = 0



        try:

            product = Reviews.objects.filter(product_id=instance.product_id)

        except:

            product = None


        if product:

            product_count = Reviews.objects.filter(product_id=instance.product_id).count()
            review_ids = product.values_list('rating' , flat = True)
            total_count = 0
            #print(len(review_ids))

            for i in range(len(review_ids)):

                total_count += int(review_ids[i])

            average = total_count/product_count


            num1 = int(average)
            num2 = average%1
            if num2>0.5:
                num2=1
            elif num2 == 0.5:
                num2=0.5
            else:
                num2=0

            #print(num2)

            num = num1 + num2

            return num

        else:


            num = 0

            return num
            


       

      

    def each_rating(self,instance):

        sum_one = 0
        sum_two = 0
        sum_three = 0
        sum_four = 0
        sum_five =0 

        try:
            product = Reviews.objects.filter(product_id=instance.product_id)
            review_ids = product.values_list('rating' , flat = True)

            for i in range(len(review_ids)):
                if review_ids[i] == 1:
                    sum_one += 1

                elif review_ids[i] == 2:
                    sum_two += 1


                elif review_ids[i] == 3:
                    sum_three += 1


                elif review_ids[i] == 4:
                    sum_four += 1

                else:
                    sum_five += 1



            nums = [{"rating":1,"count":sum_one},{"rating":2,"count":sum_two},{"rating":3,"count":sum_three},{"rating":4,"count":sum_four},{"rating":5,"count":sum_five}]




        except:
            product = None

        if product:
            return nums

        else:
            return ""


# ---------------------------- Product Code ------------------

class ProductCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCode
        fields = "__all__"

class ScannerProductSerializer(serializers.ModelSerializer):
    scan_product_id = serializers.SerializerMethodField('scanned_product_value')

    class Meta:
        model = ProductCode
        fields = ('scan_product_id','date')

    def scanned_product_value(self,obj):
        return obj.product_id

#---------------------------- Group Product----------------------

class AllGroupProductSerialyzer (serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField(method_name='get_product')
    images = serializers.SerializerMethodField(method_name='get_images')
    Group_data = serializers.SerializerMethodField(method_name='get_group_info')
    price = serializers.SerializerMethodField(method_name='get_price')

    specification = serializers.SerializerMethodField(method_name='get_specification')
    point = serializers.SerializerMethodField(method_name='get_point')
    discount = serializers.SerializerMethodField(method_name='get_discount')
    
    code = serializers.SerializerMethodField(method_name='get_code')
    
    class Meta:
        model = Product
        fields = ('product_details','Group_data','price','specification','point','discount','images','code')
        #fields = ('product_details','images','price','specification','code','discount','point')

    def get_images(self,instance):
        try:

            Images = ProductImage.objects.filter(product_id=instance.id).values()

        except:
            Images = None

        if Images:
            list_result = [entry for entry in Images] 

        else:
            list_result = []
    
        return list_result

    def get_product (self,instance):
        
        try:
            values= Product.objects.filter(id=instance.id).values()[0]
            return values
        except:
            return ''

    def get_group_info (self,instance):
        
        try:
          
            values= GroupProduct.objects.filter(product_id=instance.id).values()[0]
            return values
        except:
            return ''
       

    def get_price (self,instance):
    
        try:
            values= ProductPrice.objects.filter(product_id=instance.id).values()[0]
            return values
        except:
            return " "

    def get_specification (self,instance):
        try:
            values= ProductSpecification.objects.filter(product_id=instance.id).values()[0]
            return values
        except:
            return " "

    def get_code (self,instance):
        try:
            values= ProductCode.objects.filter(product_id=instance.id).values()[0]
            return values
        except:
            return " "

    def get_discount (self,instance):
        try:
            values= discount_product.objects.filter(product_id=instance.id).values()[0]
            return values
        except:
            return " "

    def get_point (self,instance):
        try:
            values= ProductPoint.objects.filter(product_id=instance.id).values()[0]
            return values
        except:
            return " "

