# Generated by Django 2.2.15 on 2020-09-14 05:18

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Advertisement')),
                ('ad_link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('click_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('total_click_count', models.IntegerField(default=0)),
                ('total_view_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='APIs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('details', models.CharField(blank=True, default='', max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('set_time', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banner_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('image', models.ImageField(null=True, upload_to='Banner')),
                ('link', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('content', models.CharField(blank=True, default='', max_length=264, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('non_verified_user_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('ip_address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone_number', models.CharField(default='', max_length=100, null=True)),
                ('address', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('category_id', models.IntegerField(default=-1)),
                ('active', models.BooleanField(default=False)),
                ('level', models.CharField(default='First', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('non_verified_user_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField(blank=True, null=True)),
                ('reply', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('non_verified_user_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('logo', models.ImageField(null=True, upload_to='Logo')),
                ('address', models.TextField(blank=True, default='', max_length=1500, null=True)),
                ('icon', models.ImageField(null=True, upload_to='Icon')),
                ('Facebook', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('twitter', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('linkedin', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('youtube', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('help_center', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('About', models.CharField(blank=True, default='', max_length=5000, null=True)),
                ('policy', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100000), blank=True, default=list, null=True, size=None)),
                ('terms_condition', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100000), blank=True, default=list, null=True, size=None)),
                ('slogan', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('cookies', models.CharField(blank=True, default='', max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('sender_email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=10000, null=True)),
                ('is_attended', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupon_code', models.CharField(blank=True, max_length=264, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('start_from', models.DateField(auto_now_add=True)),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_type', models.CharField(blank=True, default='Taka', max_length=100, null=True)),
                ('value', models.FloatField(blank=True, default=1.0, null=True)),
                ('dates', models.DateTimeField(auto_now_add=True)),
                ('role_id', models.IntegerField(blank=True, default=-1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='discount_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(blank=True, choices=[('FLAT', 'Flat'), ('FLASH', 'Flash'), ('WHOLESALE', 'Wholesale')], max_length=264, null=True)),
                ('amount', models.FloatField(default=0, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('max_amount', models.FloatField(default=0, null=True)),
                ('group_product_id', models.IntegerField(null=True)),
                ('product_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_backend', models.CharField(default='django.core.mail.backends.smtp.EmailBackend', max_length=64)),
                ('email_host', models.CharField(default='smtp.gmail.com', max_length=64)),
                ('email_port', models.IntegerField(default=587)),
                ('Tls_value', models.BooleanField(default=True)),
                ('email_host_user', models.EmailField(max_length=254)),
                ('email_host_password', models.CharField(max_length=264)),
                ('Ssl_value', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=264, null=True)),
                ('ans', models.CharField(blank=True, max_length=3000, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, default=list, null=True, size=None)),
                ('title', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('startdate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('flashsellname', models.CharField(blank=True, max_length=120, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(default='', max_length=64, null=True)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Cancelled', 'Cancelled'), ('Not Ordered', 'Not Ordered')], default='Unpaid', max_length=155, null=True)),
                ('delivery_status', models.CharField(blank=True, choices=[('To pay', 'To pay'), ('To ship', 'To ship'), ('Received', 'Received'), ('Not Ordered', 'Not Ordered'), ('Cancelled', 'Cancelled')], default='To ship', max_length=155, null=True)),
                ('admin_status', models.CharField(blank=True, choices=[('Processing', 'Processing'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Processing', max_length=155, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('ip_address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('checkout_status', models.BooleanField(blank=True, default=False, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('non_verified_user_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('coupon', models.BooleanField(blank=True, default=False, null=True)),
                ('coupon_code', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('product_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('total_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('unit_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('total_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('unit_point', models.FloatField(blank=True, default=0.0, null=True)),
                ('total_point', models.FloatField(blank=True, default=0.0, null=True)),
                ('product_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('product_color', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('product_size', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('product_unit', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Barcode_img', models.CharField(max_length=264, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('product_id', models.IntegerField(null=True)),
                ('Barcode', models.CharField(max_length=264, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=-1)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content', models.CharField(blank=True, default='', max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None)),
                ('product_id', models.IntegerField(default=-1)),
                ('view_count', models.IntegerField(blank=True, default=0, null=True)),
                ('click_count', models.IntegerField(blank=True, default=0, null=True)),
                ('cart_count', models.IntegerField(blank=True, default=0, null=True)),
                ('sales_count', models.IntegerField(blank=True, default=0, null=True)),
                ('non_verified_user', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None)),
                ('dates', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.FloatField(blank=True, default=0.0, null=True)),
                ('product_id', models.IntegerField(default=-1)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=-1)),
                ('price', models.FloatField(default=0.0)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('currency_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=-1)),
                ('size', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('unit', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('weight', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('color', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='Profile_Img')),
                ('phone_number', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='', max_length=1)),
                ('address', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('non_verified_user_id', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_reviews')),
                ('rating', models.IntegerField(blank=True, choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent')], null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='RolesPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleType', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('roleDetails', models.CharField(blank=True, default='', max_length=264, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.FloatField(blank=True, default=0.0, null=True)),
                ('vat', models.FloatField(blank=True, default=0.0, null=True)),
                ('role_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('point_value', models.FloatField(blank=True, default=1.0, null=True)),
                ('point_converted_value', models.FloatField(blank=True, default=0.0, null=True)),
                ('theme_id', models.IntegerField(blank=True, default=-1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(default=-1)),
                ('sub_category_id', models.IntegerField(default=-1)),
                ('title', models.CharField(blank=True, default='None', max_length=120, null=True)),
                ('active', models.BooleanField(default=False)),
                ('level', models.CharField(default='Second', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('children', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=120, null=True), blank=True, default=list, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_id', models.IntegerField(default=-1)),
                ('title', models.CharField(blank=True, default='None', max_length=120, null=True)),
                ('active', models.BooleanField(default=False)),
                ('level', models.CharField(default='Third', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sub_sub_category_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=264, null=True)),
                ('details', models.CharField(blank=True, default='', max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sender_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('receiver_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('department', models.CharField(blank=True, default='', max_length=255)),
                ('complain', models.TextField(blank=True, default='')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CLOSED', 'Closed')], default='pending', max_length=155)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='TicketReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.IntegerField(default=-1)),
                ('reply', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True, default=-1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.FloatField(default=0, null=True)),
                ('point', models.FloatField(default=0, null=True)),
                ('dates', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(default=-1, null=True)),
                ('ip_id', models.IntegerField(default=-1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified_user_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('non_verified_user_id', models.IntegerField(blank=True, default=-1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=-1)),
                ('title', models.CharField(default='', max_length=120)),
                ('sale_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('active', models.BooleanField(default=True)),
                ('inventory', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_suplier', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(default='', max_length=64)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('sub_category_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('sub_sub_category_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=250)),
                ('brand', models.CharField(blank=True, default='', max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('key_features', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, null=True, size=None)),
                ('is_deleted', models.BooleanField(default=False)),
                ('properties', models.BooleanField(default=True)),
                ('is_group', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
