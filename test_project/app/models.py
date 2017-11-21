# -*- coding: utf-8 -*-
from django.db import models
from django.utils.crypto import get_random_string


class SecureInfo(models.Model):
    app_code = models.CharField(max_length=255)
    secure_key = models.CharField(max_length=255)

    def __unicode__(self):
        print self.app_code

    @staticmethod
    def create_test_data(n):
        SecureInfo.objects.bulk_create(
            [SecureInfo(app_code=get_random_string(), secure_key=get_random_string()) for i in range(n)]
        )

    class Meta:
        db_table = "secure_info"
        app_label = 'app'
        verbose_name = u'SecureInfo'
