import workflow
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful_swagger import swagger

app = Flask(__name__)
api = Api(app)

api = swagger.docs(Api(app), apiVersion='0.1')

class WorkflowAPI(Resource):
    @swagger.operation(
        notes='some really good notes',
        parameters=[
            {
              "name": "body",
              "description": "blueprint object that needs to be added. YAML.",
              "required": True,
              "allowMultiple": False,
              "paramType": "body"
            }
          ],
        responseMessages=[
            {
              "code": 201,
              "message": "Created. The URL of the created blueprint should be in the Location header"
            },
          ]
        )
    def post(self):
        json_data = request.get_json(force=True)
        return {'data': workflow.execute_workflow(json_data["param1"], json_data["param2"], json_data["param3"])}


api.add_resource(WorkflowAPI, '/workflow')

if __name__ == '__main__':
    app.run()
