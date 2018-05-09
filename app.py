#!/usr/bin/python
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.errorhandler(404)
def custom400(error):
    return make_response(jsonify({'message': "Error! Wrong request"}), 404)

@app.route('/directeam', methods=['GET'])

def main():
	return make_response(jsonify({'message':"I'm Alive!"}))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)



