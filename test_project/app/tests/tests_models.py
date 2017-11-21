import sys

from django.test import TestCase

from app.models import SecureInfo


class SecureInfoTest(TestCase):
    def setUp(self):
        SecureInfo.objects.bulk_create(
            SecureInfo(app_code=i, secure_key=i) for i in range(10)
        )

    def tearDown(self):
        print sys._getframe().f_code.co_name
        print SecureInfo.objects.count()

    @classmethod
    def tearDownClass(cls):
        print sys._getframe().f_code.co_name
        print SecureInfo.objects.count()

    def test_crud(self):
        test_secure = SecureInfo.objects.create(app_code='one', secure_key="12345")
        self.assertEqual(test_secure.app_code, 'one')
        test_secure.app_code = 'two'
        test_secure.save()
        self.assertEqual(test_secure.app_code, 'two')
        test_secure.delete()

        with self.assertRaises(SecureInfo.DoesNotExist) as err:
            SecureInfo.objects.get(app_code='two')

        print err.exception
