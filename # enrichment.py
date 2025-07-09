# enrichment.py
import pandas as pd
import random

print(random.randint(1, 10))  # prints a random number between 1 and 10


def enrich_leads(df):
    sizes = ["Small", "Medium", "Large"]
    # ...