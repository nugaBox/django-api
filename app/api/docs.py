from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .apis import *
from .utils import *


# swagger_auto_schema
swagger_schema_example = swagger_auto_schema(
    tags=[api_dict[0].get('tags')],
    method=api_dict[0].get('operation')[0].get('method'),
    operation_id=api_dict[0].get('operation')[0].get('id'),
    operation_summary=api_dict[0].get('operation')[0].get('desc'),
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'id', 'pw'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'id': openapi.Schema(type=openapi.TYPE_STRING),
            'pw': openapi.Schema(type=openapi.TYPE_STRING),
        },
        example={
            'name': '테스트',
            'id': 'test',
            'pw': 'testpw',
        }
    ),
    responses={
        "200": openapi.Response(
            description="Successful response",
            examples={
                "application/json": {
                    "code": "9000",
                    "msg": "Success",
                    "time": now_datetime(),
                }
            }
        ),
    }
)
