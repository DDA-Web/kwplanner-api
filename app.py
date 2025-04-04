from flask import Flask, request, jsonify
from kwplanner import keyword_ideas  # On importe la fonction principale
from google.ads.googleads.client import GoogleAdsClient

app = Flask(__name__)

# Charge le client Google Ads
client = GoogleAdsClient.load_from_storage("google-ads.yaml")

# Paramètres par défaut pour la France
CUSTOMER_ID = "9240222537"  # 🔁 Remplace par ton vrai ID client
LOCATION_IDS = [1000]      # France
LANGUAGE_ID = 1000         # Français

@app.route("/kwplanner", methods=["GET"])
def run_kwplanner():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Paramètre 'keyword' manquant"}), 400
    
    try:
        results = keyword_ideas(client, CUSTOMER_ID, LOCATION_IDS, LANGUAGE_ID, [keyword])
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
