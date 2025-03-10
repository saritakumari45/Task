import argparse
import logging
import pandas as pd
from pubmed.api import fetch_pubmed_papers
from pubmed.parser import extract_company_authors

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on a query.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (CSV)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.info(f"Fetching papers for query: {args.query}")
    papers = fetch_pubmed_papers(args.query)

    if not papers:
        print("No papers found.")
        return

    filtered_papers = extract_company_authors(papers)
    df = pd.DataFrame(filtered_papers)

    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(df)

if __name__ == "__main__":
    main()
