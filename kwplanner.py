from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.v14.enums.types import KeywordPlanNetworkEnum

CUSTOMER_ID = "9240222537"  # Ton ID client Google Ads

location_ids = ["2250"]  # France
language_id = "1002"     # Français

MONTHS_FR = {
    1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril",
    5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août",
    9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"
}

def keyword_ideas(client, customer_id, location_ids, language_id, keywords):
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = client.get_service("GoogleAdsService").language_constant_path(language_id)
    request.geo_target_constants.extend(
        [client.get_service("GoogleAdsService").geo_target_constant_path(loc_id) for loc_id in location_ids]
    )

    request.keyword_plan_network = KeywordPlanNetworkEnum.KeywordPlanNetwork.GOOGLE_SEARCH_AND_PARTNERS

    request.keyword_seed.keywords.extend(keywords)

    response = keyword_plan_idea_service.generate_keyword_ideas(request=request)

    print(f"\n🚀 Résultats pour : {keywords[0]}")
    print(f"{'-'*40}")

    for idx, idea in enumerate(response):
        if idx >= 21:  # Mot-clé demandé + 20 suggestions
            break

        metrics = idea.keyword_idea_metrics

        # Affichage mot clé principal + 20 suggestions
        print(f"\n🔑 Mot-clé : {idea.text}")
        print(f"📊 Volume moyen mensuel : {metrics.avg_monthly_searches}")
        print(f"🎯 Concurrence : {metrics.competition.name.capitalize()}")

        # Saisonnière mensuelle
        print("📅 Saisonnière mensuelle :")
        for month_data in metrics.monthly_search_volumes:
            month_name = MONTHS_FR.get(month_data.month, "Mois inconnu")
            print(f"  - {month_name}: {month_data.monthly_searches} recherches")

if __name__ == "__main__":
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    keyword = input("\n🔎 Entre le mot-clé à analyser : ")
    keyword_ideas(client, CUSTOMER_ID, location_ids, language_id, [keyword])
