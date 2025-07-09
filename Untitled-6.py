with open('app.py', 'w') as f:
    f.write("""
# Your code here
print("Hello from app.py")
""")

import streamlit as st
import pandas as pd
# from scraper import scrape_leads
# from enrichment import enrich_leads
# from scoring import score_leads

# Define the functions directly within this cell

def scrape_leads():
    """
    Simulate scraping lead data from a SaaS lead platform.
    Returns a DataFrame with basic lead info.
    """
    data = [
        {"company": "TechNova", "industry": "SaaS", "website": "technova.com", "location": "NY", "contact_email": "contact@technova.com"},
        {"company": "HealthPlus", "industry": "Healthcare", "website": "healthplus.io", "location": "CA", "contact_email": "info@healthplus.io"},
        {"company": "EduSmart", "industry": "Education", "website": "edusmart.edu", "location": "TX", "contact_email": "hello@edusmart.edu"},
        {"company": "FinEdge", "industry": "Fintech", "website": "finedge.com", "location": "NY", "contact_email": "sales@finedge.com"},
        {"company": "RetailPro", "industry": "Retail", "website": "retailpro.com", "location": "WA", "contact_email": "support@retailpro.com"},
    ]
    df = pd.DataFrame(data)
    return df

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
        # Add dummy data for missing columns to avoid errors
        company_size = row.get('company_size', 'Small') # Default to 'Small'
        funding_stage = row.get('funding_stage', 'Seed') # Default to 'Seed'
        social_media_activity = row.get('social_media_activity', 'Low') # Default to 'Low'

        score += size_score_map.get(company_size, 0)
        score += funding_score_map.get(funding_stage, 0)
        score += social_score_map.get(social_media_activity, 0)
        score += industry_score_map.get(row['industry'], 0)
        scores.append(score)

    df['lead_score'] = scores
    return df.sort_values(by='lead_score', ascending=False)


st.title("Caprae Capital - Enhanced Lead Generation Tool")

st.markdown("""
This tool simulates scraping leads, enriching data, and scoring leads to prioritize high-value sales prospects.
""")

if st.button("Run Lead Generation Pipeline"):
    with st.spinner("Scraping leads..."):
        leads = scrape_leads()
    st.success(f"Scraped {len(leads)} leads.")

    # with st.spinner("Enriching leads..."):
    #     enriched_leads = enrich_leads(leads)
    # st.success("Leads enriched with company size, funding stage, and social media activity.")

    with st.spinner("Scoring leads..."):
        # Use the leads DataFrame directly since enrichment is skipped
        scored_leads = score_leads(leads)
    st.success("Leads scored and prioritized.")

    st.subheader("Leads with Scores")
    st.dataframe(scored_leads)

    csv = scored_leads.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name='scored_leads.csv', mime='text/csv')
else:
    st.info("Click the button above to start the lead generation process.")