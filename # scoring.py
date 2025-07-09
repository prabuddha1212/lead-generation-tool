# scoring.py

def score_leads(df):
    """
    Assign scores to leads based on company size, funding stage, industry relevance, and social media activity.
    Higher score means higher priority.
    """
    size_score_map = {"Small": 1, "Medium": 3, "Large": 5}
    funding_score_map = {
        "Pre-Seed": 1,
        "Seed": 2,
        "Series A": 4,
        "Series B": 5,
        "Series C": 5,
        "Public": 3,
    }
    social_score_map = {"Low": 1, "Medium": 3, "High": 5}

    # Industry priority: SaaS and Fintech highest, others moderate
    industry_score_map = {"SaaS": 5, "Fintech": 5, "Healthcare": 3, "Education": 2, "Retail": 1}

    scores = []
    for _, row in df.iterrows():
        score = 0
        score += size_score_map.get(row['company_size'], 0)
        score += funding_score_map.get(row['funding_stage'], 0)
        score += social_score_map.get(row['social_media_activity'], 0)
        score += industry_score_map.get(row['industry'], 0)
        scores.append(score)

    df['lead_score'] = scores
    return df.sort_values(by='lead_score', ascending=False)
