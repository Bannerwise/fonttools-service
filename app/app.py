import subset
import convert
import health
from logger import log
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

log.info("STARTING FONT-SERVICE")

@app.route("/subset", methods=["POST"])
def handleSubset():
    try:
        text = request.json["text"]
        font = request.json["font"]
        log.info("SUBSETTING:: text: " + text)
        subsetFont = subset.subsetFont(font, text)
        log.info("DONE SUBSETTING:: text: " + text)
        return make_response(jsonify(subsetFont), 200)
    except:
        log.warn("subsetting font went wrong ")
        return make_response(jsonify(error="subsetting went wrong"), 500)

@app.route("/convert", methods=["POST"])
def handleConvert():
    try:
        kind = request.json["type"]
        font = request.json["font"]
        log.info("CONVERTING:: kind: " + kind)
        converted = convert.convertFont(font, kind)
        return make_response(jsonify(converted), 200)
    except:
        log.warn("converting font went wrong")
        return make_response(jsonify(error="converting went wrong"), 500)

@app.route("/health", methods=["GET"])
def handleHealth():
    return make_response(jsonify(health.getHealth()), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
