# Generated by Django 4.2 on 2023-04-20 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=255)),
                ('Name', models.TextField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('s_desc', models.TextField(max_length=255)),
                ('p_desc', models.TextField(max_length=255)),
                ('creat', models.CharField(max_length=255)),
                ('s_price', models.CharField(max_length=255)),
                ('p_price', models.TextField(max_length=255)),
                ('satus', models.TextField(default='active')),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('company_email', models.CharField(blank=True, max_length=255, null=True)),
                ('business_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_type', models.CharField(blank=True, max_length=255, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='image/patient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=255)),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_type', models.TextField(max_length=255)),
                ('Account_name', models.TextField(max_length=255)),
                ('Acount_code', models.TextField(max_length=255)),
                ('Account_desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_type', models.TextField(max_length=255)),
                ('Account_name', models.TextField(max_length=255)),
                ('Acount_code', models.TextField(max_length=255)),
                ('Account_desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaxItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interstate', models.CharField(choices=[('IGST0[0%]', 'IGST0[0%]'), ('IGST5[5%]', 'IGST5[5%]'), ('IGST12[12%]', 'IGST12[12%]'), ('IGST18[18%]', 'IGST18[18%]'), ('IGST28[28%]', 'IGST28[28%]')], max_length=255)),
                ('intrastate', models.CharField(choices=[('GST0[0%]', 'GST0[0%]'), ('GST5[5%]', 'GST5[5%]'), ('GST12[12%]', 'GST12[12%]'), ('GST18[18%]', 'GST18[18%]'), ('GST28[28%]', 'GST28[28%]')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='customer_details',
        ),
        migrations.AddField(
            model_name='additem',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.purchase'),
        ),
        migrations.AddField(
            model_name='additem',
            name='sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.sales'),
        ),
        migrations.AddField(
            model_name='additem',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.taxitem'),
        ),
        migrations.AddField(
            model_name='additem',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.unit'),
        ),
        migrations.AddField(
            model_name='additem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
