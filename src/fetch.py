import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

ARXIV_API_URL = "http://export.arxiv.org/api/query"
MAX_RESULTS_PER_REQUEST = 2000
REQUEST_DELAY = 3

ATOM_NS = "http://www.w3.org/2005/Atom"
ARXIV_NS = "http://arxiv.org/schemas/atom"
OPENSEARCH_NS = "http://a9.com/-/spec/opensearch/1.1/"


def parse_date_range(date_range: str) -> tuple[str, str]:
    now = datetime.now(timezone.utc)

    if date_range == "past week":
        start = now - timedelta(days=7)
    elif date_range == "past month":
        start = now - timedelta(days=30)
    elif re.match(r"^\d{8}-\d{8}$", date_range):
        start_str, end_str = date_range.split("-")
        start = datetime.strptime(start_str, "%Y%m%d").replace(tzinfo=timezone.utc)
        end = datetime.strptime(end_str, "%Y%m%d").replace(tzinfo=timezone.utc)
        end = end.replace(hour=23, minute=59, second=59)
        return start.strftime("%Y%m%d0000"), end.strftime("%Y%m%d2359")
    else:
        raise ValueError(
            f"Invalid date_range: {date_range!r}. "
            "Use 'past week', 'past month', or 'YYYYMMDD-YYYYMMDD'."
        )

    return start.strftime("%Y%m%d0000"), now.strftime("%Y%m%d2359")


def build_query(topics: list[str], date_range: str) -> str:
    date_start, date_end = parse_date_range(date_range)

    keyword_parts = []
    for topic in topics:
        escaped = topic.replace('"', "")
        keyword_parts.append(f'all:"{escaped}"')
    keyword_query = " OR ".join(keyword_parts)

    query = f"({keyword_query}) AND submittedDate:[{date_start} TO {date_end}]"
    return query


def parse_entry(entry: ET.Element) -> dict:
    title = entry.findtext(f"{{{ATOM_NS}}}title", "").strip()
    title = re.sub(r"\s+", " ", title)

    abstract = entry.findtext(f"{{{ATOM_NS}}}summary", "").strip()
    abstract = re.sub(r"\s+", " ", abstract)

    authors = [
        name.text.strip()
        for author in entry.findall(f"{{{ATOM_NS}}}author")
        if (name := author.find(f"{{{ATOM_NS}}}name")) is not None and name.text
    ]

    link = entry.findtext(f"{{{ATOM_NS}}}id", "").strip()

    categories = []
    for cat in entry.findall(f"{{{ARXIV_NS}}}primary_category"):
        term = cat.get("term", "")
        if term:
            categories.append(term)
    for cat in entry.findall(f"{{{ATOM_NS}}}category"):
        term = cat.get("term", "")
        if term and term not in categories:
            categories.append(term)

    published = entry.findtext(f"{{{ATOM_NS}}}published", "").strip()

    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "link": link,
        "categories": categories,
        "published": published,
    }


def parse_response(xml_text: str) -> tuple[list[dict], int]:
    root = ET.fromstring(xml_text)
    total = int(root.findtext(f"{{{OPENSEARCH_NS}}}totalResults", "0"))
    entries = root.findall(f"{{{ATOM_NS}}}entry")
    papers = [parse_entry(e) for e in entries]
    # arXiv returns a single entry with empty title when there are no results
    papers = [p for p in papers if p["title"]]
    return papers, total


def fetch_papers(topics: list[str], date_range: str) -> list[dict]:
    query = build_query(topics, date_range)
    all_papers = []
    start = 0

    while True:
        params = urllib.parse.urlencode({
            "search_query": query,
            "start": start,
            "max_results": MAX_RESULTS_PER_REQUEST,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        url = f"{ARXIV_API_URL}?{params}"

        with urllib.request.urlopen(url) as resp:
            xml_text = resp.read().decode("utf-8")

        papers, total = parse_response(xml_text)
        all_papers.extend(papers)

        start += MAX_RESULTS_PER_REQUEST
        if start >= total or not papers:
            break

        time.sleep(REQUEST_DELAY)

    return all_papers
