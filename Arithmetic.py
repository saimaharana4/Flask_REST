from flask_restful import Api, Resource
from flask import Flask, jsonify, request

app = Flask(__name__)
api =Api(app)

def checkPostedData(postedData, func):
    if (func =="add" or func =="sub" or  func =="mul"  ):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif(func =="div"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        postData=request.get_json()
        #Step 1: Verify the param
        status_code = checkPostedData(postData,"add")
        if (status_code != 200):
            retJson={
                "Message": "An Error Occur",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x:int= postData["x"]
        y:int = postData["y"]
        ret =x+y
        retMap = {
            "Message":ret,
            "Status Code" : 200

        }
        return jsonify(retMap)


class Sub(Resource):
    def post(self):
        postData=request.get_json()
        #Step 1: Verify the param
        status_code = checkPostedData(postData,"sub")
        if (status_code != 200):
            retJson={
                "Message": "An Error Occur",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x:int= postData["x"]
        y:int = postData["y"]
        ret =x-y
        retMap = {
            "Message":ret,
            "Status Code" : 200

        }
        return jsonify(retMap)

class Mul(Resource):
    def post(self):
        postData=request.get_json()
        #Step 1: Verify the param
        status_code = checkPostedData(postData,"mul")
        if (status_code != 200):
            retJson={
                "Message": "An Error Occur",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x:int= postData["x"]
        y:int = postData["y"]
        ret =x*y
        retMap = {
            "Message":ret,
            "Status Code" : 200

        }
        return jsonify(retMap)

class Div(Resource):
    def post(self):
        postData=request.get_json()
        #Step 1: Verify the param
        status_code = checkPostedData(postData,"div")
        if (status_code != 200):
            retJson={
                "Message": "An Error Occur",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x:int= postData["x"]
        y:int = postData["y"]
        ret =x/y
        retMap = {
            "Message":ret,
            "Status Code" : 200

        }
        return jsonify(retMap)


@app.route('/')
def hello_world():
    
    return "Hello Sai"

api.add_resource(Add,"/add")
api.add_resource(Sub,"/sub")
api.add_resource(Mul,"/mul")
api.add_resource(Div,"/div")

if __name__ =="__main__":
    app.run(debug=True)