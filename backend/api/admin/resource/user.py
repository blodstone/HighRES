import jwt
import os
from datetime import datetime, timedelta
from backend.model.user import User
from flask_restful import Resource, abort
from flask import request, jsonify


class UserResource(Resource):
    def post(self):
        data = request.get_json()
        user = User.authenticate(**data)
        if not user:
            abort(401, message='Invalid credentials', authenticated=False)
        token = jwt.encode({
            'sub': user.email,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=30)
            # TODO: This is a hack until the pythonanywhere server issue resolved
        }, os.getenv('SECRET_KEY')
        )
        return jsonify({'token': token.decode('UTF-8')})
