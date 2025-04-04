from flask import Flask, request, jsonify
from google.ads.googleads.client import GoogleAdsClient
from kwplanner import keyword_ideas
import os

app = Flask(__name__)

@app.route("/keywords", methods=["GET"])
def get_keywords():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Paramètre 'q' manquant."}), 400

    credentials = {
        "developer_token": os.getenv("DEVELOPER_TOKEN"),
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": os.getenv("REFRESH_TOKEN"),
        "use_proto_plus": True,
        "login_customer_id": os.getenv("LOGIN_CUSTOMER_ID")
    }

    try:
        client = GoogleAdsClient.load_from_dict(credentials)
        customer_id = os.getenv("CUSTOMER_ID")
        location_ids = ["2250"]
        language_id = "1002"

        resultats = keyword_ideas(client, customer_id, location_ids, language_id, [query])
        return jsonify(resultats)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))


