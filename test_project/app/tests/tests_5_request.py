# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import User

from app.views import get_info, home


class RequestTestCase(TestCase):
    """测试类"""

    def setUp(self):
        """初始化数据
        """

        self.factory = RequestFactory()
        self.uin = '836324475'
        self.skey = 'test'

        self.user = User.objects.create_user(username=self.uin)

    def test_get(self):
        """测试样例
        """
        request = self.factory.get('/api/get_info/')
        print request

        # 设置cookies
        request.COOKIES = {
            'uin': self.uin,
            'skey': self.skey
        }

        resp = get_info(request)
        print 'get_info', resp.content
        # 测试返回码
        self.assertEqual(resp.status_code, 200)

    def test_get_user_info(self):
        request = self.factory.get('/api/get_info/')
        print request

        # 设置user对象
        request.user = self.user

        resp = home(request)
        print 'test_get_user_info', resp.content
        # 测试返回码
        # self.assertEqual(resp.status_code, 200)
