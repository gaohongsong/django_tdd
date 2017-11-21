# -*- coding: utf-8 -*-
import json

from django.test import TestCase
from django.test import Client


class ClientTestCase(TestCase):
    """测试类"""

    def setUp(self):
        """初始化数据
        """
        self.c = Client()

        # 强制进行CSRF检查
        self.csrf_client = Client(enforce_csrf_checks=True)

    def test_get_api(self):
        """测试样例
        """
        resp = self.c.get('/api/get_info/', {'open_id': 'test'})
        print resp

        # 测试返回码
        self.assertEqual(resp.status_code, 200)

        # 测试返回数据是否正
        resp = json.loads(resp.content)
        self.assertIs(resp.get('result'), True)

    def test_post(self):
        """测试POST
        """

        # 403 error
        resp = self.csrf_client.post('/api/update_info/', {'app_code': 'test'})
        self.assertEqual(resp.status_code, 403)
        self.assertIs('CSRF' in resp.content, True)
        # self.assertContains(resp, 'CSRF')

        # post multipart/form-data
        resp = self.c.post('/api/update_info/', {'app_code': 'test'})
        self.assertEqual(resp.status_code, 200)
        resp = json.loads(resp.content)
        print resp.get('data')

        # post json data
        resp = self.c.post(
            '/api/update_info/',
            json.dumps({'app_code': 'test1', 'secure_key': 'test'}),
            content_type='application/json'
        )
        print resp

        # 测试返回码
        self.assertEqual(resp.status_code, 200)

        # def test_qy_user_info(self):
        #     response = self.c.get('/apiy_user_info/')
        #     print response
        #     self.assertRedirects(response)

        def test_login(self):
            """测试登录
            """

    def test_redirect(self):
        resp = self.c.get('/api/home/')
        print resp
        self.assertRedirects(resp, '/api/get_info/')

