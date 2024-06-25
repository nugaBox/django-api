from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import *
from .serializers import *
from .utils import *
from .docs import *


@swagger_schema_example
@api_view(['POST'])
def user_register(request):
    """
    사용자를 등록합니다
    """
    error_yn = 'N'
    error_code = '9000'
    error_msg = ''
    res_data = None
    req_time = now_datetime()
    logger_request(request)

    try:
        # param
        try:
            name = request.data['name']
            id = request.data['id']
            pw = request.data['pw']
            if not name or not id or not pw:
                error_yn = 'Y'
                error_code = '9100'
        except:
            error_yn = 'Y'
            error_code = '9100'

        # # Example: DB에서 기존 User 체크
        # check_user = Users.objects.filter(user_id=id)
        # if check_user.exists():
        #     error_yn = 'Y'
        #     error_code = '9101'
        # else:
        #     # User가 존재하지 않으면 데이터 저장
        #     save_data = {
        #         'user_info': 'Example Information'
        #     }
        #     serializer = UserSerializer(data=save_data)
        #     if serializer.is_valid():
        #         serializer.save()
        #     else:
        #         error_yn = 'Y'
        #         error_code = '9500'
        #         error_msg = serializer.errors

        # response
        if error_yn == 'N':
            response = {'code': error_code}
            # api_hist_add(request, req_time, response)
            return JsonResponse(api_msg(response['code']), status=200)
        else:
            response = {'code': error_code, 'msg': error_msg, 'data': res_data}
            # api_hist_add(request, req_time, response)
            return JsonResponse(api_msg(response['code'], response['msg'], response['data']), status=200)
    except Exception as e:
        logger.error(e)
        response = {'code': '9403', 'msg': str(e), 'data': res_data}
        # api_hist_add(request, req_time, response)
        return JsonResponse(api_msg(response['code'], response['msg'], response['data']), status=200)