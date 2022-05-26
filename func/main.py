# Jormungandr - Onboarding
from src.domain.exceptions import ErrorOnSendAuditLog, ErrorOnUpdateUser, ErrorOnFindUser
from src.domain.enums.code import InternalCode
from src.domain.response.model import ResponseModel
from src.services.jwt import JwtService
from src.services.suitability import SuitabilityService

# Standards
from http import HTTPStatus

# Third party
from etria_logger import Gladsheim
from flask import Flask, request
from asgiref.wsgi import WsgiToAsgi
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)


@app.route('/create_suitability')
async def create_suitability_profile():
    jwt = request.headers.get("x-thebes-answer")
    unique_id = await JwtService.decode_jwt_and_get_unique_id(jwt=jwt)
    msg = "Jormungandr-Onboarding::create_suitability_profile::"
    msg_error = "Unexpected error occurred"
    try:
        success = await SuitabilityService.create(unique_id=unique_id)
        response = ResponseModel(
            success=success,
            message="Suitability profile successfully created",
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except ErrorOnFindUser as ex:
        Gladsheim.error(error=ex, message=f"{msg}Error on trying to get user in mongo_db")
        response = ResponseModel(
            success=False, code=InternalCode.INTERNAL_SERVER_ERROR, message=msg_error
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except ErrorOnUpdateUser as ex:
        Gladsheim.error(error=ex, message=f"{msg}Error on trying to update user in mongo_db")
        response = ResponseModel(
            success=False, code=InternalCode.INTERNAL_SERVER_ERROR, message=msg_error
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except ErrorOnSendAuditLog as ex:
        Gladsheim.error(error=ex, message=f"{msg}error on send log to audit service")
        response = ResponseModel(
            success=False, code=InternalCode.INTERNAL_SERVER_ERROR, message=msg_error
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except Exception as ex:
        Gladsheim.error(error=ex, message=f"{msg}Unexpected error occurred")
        response = ResponseModel(
            success=False, code=InternalCode.INTERNAL_SERVER_ERROR, message=msg_error
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response


asyncio.run(serve(asgi_app, Config()))
