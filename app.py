import subset
import convert
import health
from logger import log
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

log.info("starting subset service..")

@app.route("/subset", methods=["POST"])
def handleSubset():
    try:
        text = request.json['text']
        font = request.json['font']
        # fontName = request.json['fontName']
        # log.info('SUBSETTING:: fontName: ' + fontName + ' text: ' + text)
        log.info('SUBSETTING:: text: ' + text)
        print text
        print font
        # print fontName
        subsetFont = subset.subsetFont(font, text)
        print subsetFont
        return make_response(jsonify(subsetFont), 200)
    except:
        log.warn("subsetting font went wrong", request)
        return make_response(jsonify(error="subsetting went wrong"), 500)

@app.route("/convert", methods=["POST"])
def handleConvert():
    try:
        print request.json
        kind = request.json['type']
        font = request.json['font']
        log.info('CONVERTING:: kind: ' + kind)
        print kind
        print font
        converted = convert.convertFont(font, kind)
        print converted
        return make_response(jsonify(converted), 200)
    except:
        log.warn("converting font went wrong")
        return make_response(jsonify(error="converting went wrong"), 500)

@app.route("/health", methods=["GET"])
def handleHealth():
    return make_response(jsonify(health.getHealth()), 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9097)
