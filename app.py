import os
from google.ads.googleads.client import GoogleAdsClient
from flask import Flask, request, jsonify
from kwplanner import keyword_ideas

app = Flask(__name__)

credentials = {
    "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
    "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
    "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
    "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
    "use_proto_plus": True,
}

client = GoogleAdsClient.load_from_dict(credentials)

@app.route('/keywords', methods=['GET'])
def keywords():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required."}), 400

    keyword_results = keyword_ideas(client, query)
    return jsonify(keyword_results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)), debug=True)
