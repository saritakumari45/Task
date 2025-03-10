import re
from typing import List, Dict

COMPANY_KEYWORDS = ["pharmaceutical", "biotech", "inc", "ltd", "corp", "gmbh"]

def extract_company_authors(papers: List[Dict]) -> List[Dict]:
    """Filters authors affiliated with a pharmaceutical or biotech company."""
    for paper in papers:
        paper["Non-academic Author(s)"] = []
        paper["Company Affiliation(s)"] = []
        for author in paper.get("Authors", []):
            affiliation = author.get("affiliation", "")
            if any(keyword in affiliation.lower() for keyword in COMPANY_KEYWORDS):
                paper["Non-academic Author(s)"].append(author["name"])
                paper["Company Affiliation(s)"].append(affiliation)

    return papers
