from flask import Flask, request
from flask_restplus import Api, Resource, fields
import workflow

flask_app = Flask(__name__)
api = Api(app=flask_app)

name_space = api.namespace('main', description='Main APIs')

resource_fields = api.model('Resource', {
  'account': fields.String(required=True, description='...', example='an example'),
  'name': fields.String(required=True, description='...', example='an example'),
  'email': fields.String(required=True, description='...', example='an example'),
})

@name_space.route("/")
class MainClass(Resource):
    def get(self):
        return {
            "status": "success"
        }

    @api.expect(resource_fields, validate=True)
    def post(self):
        payload = api.payload
        print(payload)
        return {'data': workflow.execute_workflow(payload["account"], payload["name"], payload["email"])}


if __name__ == '__main__':
    flask_app.run()