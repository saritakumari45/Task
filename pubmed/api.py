import requests
import logging
from typing import Dict, List, Optional

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_pubmed_papers(query: str, max_results: int = 50) -> Optional[List[Dict]]:
    """Fetches papers from PubMed based on a query."""
    search_url = f"{BASE_URL}/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    
    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if "esearchresult" not in data or "idlist" not in data["esearchresult"]:
            logging.warning("No results found.")
            return None

        paper_ids = data["esearchresult"]["idlist"]
        return fetch_paper_details(paper_ids)
    
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetches details for a list of PubMed paper IDs."""
    details_url = f"{BASE_URL}/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    
    response = requests.get(details_url, params=params)
    response.raise_for_status()
    data = response.json()
    
    papers = []
    for paper_id in paper_ids:
        if paper_id in data.get("result", {}):
            paper = data["result"][paper_id]
            papers.append({
                "PubmedID": paper_id,
                "Title": paper.get("title", "N/A"),
                "Publication Date": paper.get("pubdate", "N/A"),
                "Authors": paper.get("authors", [])
            })
    return papers
