from flask import Flask, request, jsonify
import os
from kwplanner import keyword_ideas
from google.ads.googleads.client import GoogleAdsClient

app = Flask(__name__)

# Charger les identifiants depuis les variables d'environnement
credentials = {
    "developer_token": os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN"),
    "client_id": os.environ.get("GOOGLE_ADS_CLIENT_ID"),
    "client_secret": os.environ.get("GOOGLE_ADS_CLIENT_SECRET"),
    "refresh_token": os.environ.get("GOOGLE_ADS_REFRESH_TOKEN"),
    "login_customer_id": os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
    "use_proto_plus": True,
    "token_uri": os.environ.get("GOOGLE_ADS_TOKEN_URI")
}

# Initialiser le client Google Ads
client = GoogleAdsClient.load_from_dict(credentials)

# Définir les paramètres fixes
LOCATION_IDS = [1000]  # France
LANGUAGE_ID = 1000     # Français

@app.route("/kwplanner", methods=["GET"])
def run_kwplanner():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Paramètre 'keyword' manquant"}), 400

    try:
        results = keyword_ideas(client, credentials["login_customer_id"], LOCATION_IDS, LANGUAGE_ID, [keyword])
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
