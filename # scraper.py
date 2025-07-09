# scraper.py
import pandas as pd

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

if __name__ == "__main__":
    leads = scrape_leads()
    print(leads)