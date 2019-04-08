from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "root get. Hello!"

# @app.route('/reply', methods=['GET'])
# def reply():
#     answer = "route reply is got! \n"
#     result = {
#       "Content-Type": "application/json",
#       "Answer":{"Text": answer}
#     }
#     return jsonify(result)

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "route post. keyword is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
