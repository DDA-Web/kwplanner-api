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
        "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
        "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
        "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
        "login_customer_id": os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
        "token_uri": os.getenv("GOOGLE_ADS_TOKEN_URI"),
        "use_proto_plus": True
    }

    try:
        client = GoogleAdsClient.load_from_dict(credentials)
        customer_id = os.getenv("CUSTOMER_ID")
        location_ids = ["2250"]  # France
        language_id = "1002"      # Français

        resultats = keyword_ideas(client, customer_id, location_ids, language_id, [query])
        return jsonify(resultats)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)