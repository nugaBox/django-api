from django.db import models


class Users(models.Model):
    user_id = models.CharField(max_length=50, null=True)
    user_nm = models.CharField(max_length=200, null=True)
    user_info = models.TextField()

    class Meta:
        managed = True
        db_table = 'api_user'


class ApiHist(models.Model):
    req_method = models.CharField(max_length=200, unique=False, null=True)
    req_url = models.CharField(max_length=200, unique=False, null=True)
    req_params = models.CharField(max_length=1000, unique=False, null=True)
    req_data = models.TextField(null=True)
    req_time = models.DateTimeField(null=True)
    res_code = models.CharField(max_length=200, unique=False, null=True)
    res_msg = models.CharField(max_length=200, unique=False, null=True)
    res_data = models.TextField(null=True)
    res_time = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'api_history'