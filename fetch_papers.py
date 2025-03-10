import requests
import pandas as pd
import typer
import rich
from rich.console import Console

console = Console()

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query: str, filename: str = None, debug: bool = False):
    """
    Fetches research papers from PubMed based on a user query.
    Extracts relevant fields and saves them as a CSV file.
    """
    console.print(f"🔍 Searching for papers with query: [bold cyan]{query}[/bold cyan]")

    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Adjust as needed
    }

    response = requests.get(PUBMED_API_URL, params=params)

    if response.status_code != 200:
        console.print(f"[bold red]❌ Error: Failed to fetch papers. Status Code: {response.status_code}[/bold red]")
        return
    
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    if not paper_ids:
        console.print("[yellow]⚠ No papers found for this query.[/yellow]")
        return
    
    # Fetch detailed information
    details_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    details_response = requests.get(DETAILS_API_URL, params=details_params)
    details_data = details_response.json()

    papers = []
    for paper_id in paper_ids:
        paper_info = details_data.get("result", {}).get(paper_id, {})
        papers.append({
            "PubmedID": paper_id,
            "Title": paper_info.get("title", "N/A"),
            "Publication Date": paper_info.get("pubdate", "N/A"),
            "Company Affiliation(s)": "N/A",  # Needs extra logic to filter affiliations
            "Corresponding Author Email": "N/A"  # Needs extra API or parsing
        })

    df = pd.DataFrame(papers)

    if filename:
        df.to_csv(filename, index=False)
        console.print(f"[green]✅ Results saved to {filename}[/green]")
    else:
        console.print(df.to_string())

if __name__ == "__main__":
    typer.run(fetch_papers)
