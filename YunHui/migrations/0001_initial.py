# Generated by Django 2.0.7 on 2018-08-23 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.IntegerField(blank=True, default=0, null=True, verbose_name='云回成功总数')),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='帖子id')),
                ('post_id', models.CharField(max_length=20, verbose_name='楼层数id')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('username', models.CharField(max_length=200, verbose_name='用户名')),
                ('is_fans', models.BooleanField(default=False, verbose_name='是粉丝')),
                ('fname', models.CharField(max_length=20, verbose_name='贴吧名')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('time', models.CharField(max_length=20, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='贴吧名')),
                ('fid', models.CharField(max_length=20, verbose_name='贴吧id')),
                ('level_id', models.IntegerField(default=0, null=True, verbose_name='当前等级')),
                ('cur_score', models.IntegerField(default=0, null=True, verbose_name='当前经验')),
                ('is_sign', models.BooleanField(default=False, verbose_name='是否签到')),
            ],
        ),
        migrations.CreateModel(
            name='Tieba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='贴吧名')),
                ('fid', models.CharField(max_length=20, verbose_name='贴吧id')),
                ('tid', models.CharField(max_length=20, verbose_name='帖子id')),
                ('isLou', models.BooleanField(default=False, verbose_name='是否楼中楼')),
                ('floor', models.CharField(blank=True, max_length=20, null=True, verbose_name='楼层数')),
                ('qid', models.CharField(blank=True, max_length=20, null=True, verbose_name='楼层数id')),
                ('time', models.IntegerField(default=5, verbose_name='回复间隔')),
                ('success', models.IntegerField(default=0, null=True, verbose_name='成功次数')),
                ('fail', models.IntegerField(default=0, null=True, verbose_name='失败次数')),
                ('stop', models.BooleanField(default=False, verbose_name='是否暂停')),
                ('stop_times', models.IntegerField(default=0, null=True, verbose_name='暂停次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='插入时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bduss', models.CharField(max_length=192, verbose_name='BDUSS')),
                ('username', models.CharField(editable=False, max_length=30, unique=True, verbose_name='贴吧用户名')),
                ('token', models.CharField(editable=False, max_length=200, unique=True, verbose_name='个人TOKEN')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('flag', models.IntegerField(default=0, null=True, verbose_name='新用户')),
                ('i_type', models.BooleanField(default=True, verbose_name='云回模式')),
            ],
        ),
        migrations.AddField(
            model_name='tieba',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YunHui.User', verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='sign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YunHui.User', verbose_name='所属用户'),
        ),
    ]
