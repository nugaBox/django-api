import time
import json
import logging
import hashlib
import base64
import inspect
import jwt
from datetime import datetime, timedelta
from django.http import JsonResponse
from collections import OrderedDict
from .serializers import ApiHistSerializer


# 로깅 설정
logger = logging.getLogger('api')


# API CODE 및 메시지
API_CODE_MSG = {
    # Success
    '9000': 'Success',
    '9001': 'Generated',
    '9002': 'Updated',
    # Bad Request
    '9100': 'Missing required request parameters',
    '9101': 'Already Existing Users',
    # Unauthorized
    '9401': 'Unauthorized request',
    # Server Error
    '9500': 'Internal server error'
}


# 성공 API CODE
API_CODE_SUCCESS = ['9000', '9001', '9002', '9003', '9004']


# 함수명 얻기
def get_operation():
    caller_frame = inspect.currentframe().f_back
    file_name = caller_frame.f_code.co_filename
    function_name = caller_frame.f_code.co_name

    return function_name


# 현재 시간 출력
def now_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


# API 요청 이력 추가
def api_hist_add(request, req_time, response):
    # data 저장할 내용
    history_data = {
        'req_time': req_time,
        'req_method': request.method,
        'req_url': str(request.path_info),
        'res_time': now_datetime(),
        'res_code': response['code'],
        'res_data': str(response['data'])
    }

    # request parmeter
    if request.query_params:
        req_path = ''
        req_params = request.query_params
        for idx, key in enumerate(req_params):
            if idx == 0:
                req_path += key + '=' + req_params.get(key)
            else:
                req_path += '&' + key + '=' + req_params.getlist(key)
        history_data['req_params'] = req_path

    # request data
    if request.data:
        history_data['req_data'] = str(request.data)

    # 응답 메시지
    if response['msg'] is None:
        history_data['res_msg'] = API_CODE_MSG[history_data['res_code']]
    else:
        history_data['res_msg'] = response['msg']

    # data 저장할 값 포맷 일치 확인
    serializer = ApiHistSerializer(data=history_data)
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(api_msg('9124', serializer.errors), status=200)


# API 응답 메시지 작성
def api_msg(code, msg=None, data=None):
    res_msg = ""
    log_msg = ""
    # 응답 시간
    res_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


    # 로그 메시지
    if msg is None or msg == "":
        log_msg = API_CODE_MSG[code]
    else:
        log_msg = msg
    log_dict = {
        "code": code,
        "msg": log_msg,
        "time": res_time,
    }

    # Example : 응답용 메시지 구분
    res_dict = log_dict
    # if code in API_CODE_SUCCESS:
    #     res_msg = 'Success'
    # else:
    #     res_msg = 'Error'
    # res_dict = {
    #     "code": code,
    #     "msg": res_msg,
    #     "time": res_time,
    # }

    if data is not None:
        res_dict['data'] = data
        log_dict['data'] = data

    if code in API_CODE_SUCCESS:
        logger.info('response: ' + json.dumps(log_dict))
    else:
        logger.error('response: ' + json.dumps(log_dict))
    return res_dict


# Request 로그
def logger_request(request):
    logger.info(request)
    if request.method == 'POST':
        logger.info('request: ' + str(request.data))
