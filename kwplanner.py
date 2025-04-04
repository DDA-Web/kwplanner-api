from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.v14.enums.types.keyword_plan_network import KeywordPlanNetworkEnum

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

    result = []
    for idx, idea in enumerate(response):
        if idx >= 21:
            break
        metrics = idea.keyword_idea_metrics
        saisonnalite = [
            {
                "mois": MONTHS_FR.get(month_data.month, "Inconnu"),
                "volume": month_data.monthly_searches
            }
            for month_data in metrics.monthly_search_volumes
        ]
        result.append({
            "mot_cle": idea.text,
            "volume_moyen": metrics.avg_monthly_searches,
            "concurrence": metrics.competition.name.capitalize(),
            "saisonnalite": saisonnalite
        })

    return result
