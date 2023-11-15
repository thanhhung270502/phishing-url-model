import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import encode_sample

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument("url")

validate_model = pickle.load(open('./rf_tfidf', 'rb'))

class ValidationEndPoint(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        args = parser.parse_args()
        url = args.get("url")
        
        encode_url = encode_sample.Encode.convertURL(url)
        url_features = [encode_url]
        predict_value = validate_model.predict(url_features)
        print(predict_value[0])

        return {
            "encode_url": encode_url,
            "result": "Legit",
        } if predict_value[0] == 1 else {
            "encode_url": encode_url,
            "result": "Phishing",
        }


api.add_resource(ValidationEndPoint, '/api/v1/phishingURL')

if __name__ == '__main__':
    app.run(debug=True)
    
    url = 'https://www.google.com/'
    encode_url = encode_sample.Encode.convertURL(url)
    url_features = [encode_url]
    predict_value = validate_model.predict(url_features)
    print(predict_value)
