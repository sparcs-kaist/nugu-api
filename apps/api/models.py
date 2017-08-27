from django.utils import timezone
'''
from sqlalchemy import (Column, String, DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
'''
from django.db import models


NUGU_FIELDS = [
    {'id': 'name', 'name': '이름', 'hint': '뀨냥이'},
    {'id': 'is_private', 'name': '외부 비공개', 'hint': 'true'},
    {'id': 'is_developer', 'name': '개발자인가', 'hint': 'false'},
    {'id': 'is_designer', 'name': '디자이너인가', 'hint': 'false'},
    {'id': 'is_undergraduate', 'name': '학부생인가', 'hint': '0 or 1'},
    {'id': 'ent_year', 'name': '학번', 'hint': '14'},
    {'id': 'org', 'name': '소속'},
    {'id': 'email', 'name': '이메일'},
    {'id': 'phone', 'name': '전화번호', 'hint': '010-xxxx-xxxx'},
    {'id': 'birth', 'name': '생일', 'hint': '1996-01-01'},
    {'id': 'dorm', 'name': '기숙사'},
    {'id': 'lab', 'name': '랩'},
    {'id': 'home_add', 'name': '집주소'},
    {'id': 'github_id', 'name': 'Github ID'},
    {'id': 'linkedin_url', 'name': 'LinkedIn URL'},
    {'id': 'behance_url', 'name': 'Behance URL'},
    {'id': 'facebook_id', 'name': 'Facebook ID'},
    {'id': 'twitter_id', 'name': 'Twitter ID'},
    {'id': 'battlenet_id', 'name': 'Battlenet ID'},
    {'id': 'website', 'name': '홈페이지'},
    {'id': 'blog', 'name': '블로그'},
    {'id': 'created_on', 'name': '생성일', 'readonly': True},
    {'id': 'updated_on', 'name': '수정일', 'readonly': True},
]

NUGU_FIELD_NAMES = [field['id'] for field in NUGU_FIELDS
                    if not field.get('readonly', False)]


class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    is_private = models.BooleanField(default=True)
    is_developer = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    is_undergraduate = models.BooleanField(default=True)
    ent_year = models.CharField(max_length=255, null=True)
    org = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    birth = models.CharField(max_length=255, null=True)
    dorm = models.CharField(max_length=255, null=True)
    lab = models.CharField(max_length=255, null=True)
    home_add = models.CharField(max_length=255, null=True)
    github_id = models.CharField(max_length=255, null=True)
    linkedin_url = models.CharField(max_length=255, null=True)
    behance_url = models.CharField(max_length=255, null=True)
    facebook_id = models.CharField(max_length=255, null=True)
    twitter_id = models.CharField(max_length=255, null=True)
    battlenet_id = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    blog = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)