# Generated by Django 5.0.2 on 2024-02-24 14:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reply_content', models.TextField()),
                ('group_id', models.BigIntegerField(null=True)),
                ('reply_depth', models.BigIntegerField(default=1)),
                ('reply_private_status', models.BooleanField(choices=[(True, '비밀 댓글'), (False, '일반 댓글')], default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.post')),
            ],
            options={
                'db_table': 'tbl_reply',
                'ordering': ['-id'],
            },
        ),
    ]