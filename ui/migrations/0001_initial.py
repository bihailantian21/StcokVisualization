# Generated by Django 2.1.8 on 2020-04-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MajorNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField(null=True)),
                ('pubtime', models.CharField(max_length=24)),
                ('src', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('bprice', models.CharField(max_length=10)),
                ('bvolume', models.CharField(max_length=10)),
                ('btime', models.DateField(auto_now_add=True)),
                ('issold', models.BooleanField(default=False)),
                ('aprice', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockBasic',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('industry', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=10)),
                ('pb', models.CharField(max_length=10)),
                ('pe', models.CharField(max_length=10)),
                ('esp', models.CharField(max_length=10)),
                ('bvps', models.CharField(max_length=10)),
                ('totals', models.CharField(max_length=10)),
                ('outstanding', models.CharField(max_length=10)),
                ('totalAssets', models.CharField(max_length=10)),
                ('liquidAssets', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StockRank',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('changepercent', models.CharField(max_length=10)),
                ('trade', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='用户', max_length=10)),
                ('passwd', models.CharField(max_length=16, null=True)),
                ('auth', models.CharField(default='5', max_length=1)),
                ('email', models.CharField(max_length=32, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=10, null=True)),
                ('createtime', models.DateField(auto_now_add=True)),
                ('verifycode', models.CharField(default='000000', max_length=6)),
                ('verifydeadline', models.CharField(default='0', max_length=10)),
                ('selfstocks', models.TextField(default='sh;sz;cyb;hs300;zxb', null=True)),
                ('selfrecords', models.TextField(null=True)),
            ],
        ),
    ]
