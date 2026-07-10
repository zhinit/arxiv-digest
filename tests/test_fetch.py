import re
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

import pytest
from src.fetch import parse_date_range, parse_response, build_query

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <opensearch:totalResults>2</opensearch:totalResults>
  <opensearch:startIndex>0</opensearch:startIndex>
  <opensearch:itemsPerPage>10</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/abs/2301.00001v1</id>
    <title>Deep Learning for Audio Signal Processing</title>
    <summary>We present a novel approach to audio classification using
    convolutional neural networks and digital signal processing techniques.</summary>
    <author><name>Alice Smith</name></author>
    <author><name>Bob Jones</name></author>
    <published>2023-01-01T00:00:00Z</published>
    <arxiv:primary_category term="cs.SD" />
    <category term="cs.SD" />
    <category term="eess.AS" />
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2301.00002v1</id>
    <title>Prediction Markets and Gambling Behavior</title>
    <summary>A psychological study of decision-making in prediction markets
    and its relationship to gambling tendencies.</summary>
    <author><name>Carol White</name></author>
    <published>2023-01-02T00:00:00Z</published>
    <arxiv:primary_category term="econ.GN" />
    <category term="econ.GN" />
  </entry>
</feed>"""

EMPTY_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <opensearch:totalResults>0</opensearch:totalResults>
  <opensearch:startIndex>0</opensearch:startIndex>
  <opensearch:itemsPerPage>10</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/</id>
    <title></title>
    <summary></summary>
  </entry>
</feed>"""


class TestParseDateRange:
    def test_past_week(self):
        start, end = parse_date_range("past week")
        now = datetime.now(timezone.utc)
        week_ago = now - timedelta(days=7)
        assert start.startswith(week_ago.strftime("%Y%m%d"))
        assert end.startswith(now.strftime("%Y%m%d"))

    def test_past_month(self):
        start, end = parse_date_range("past month")
        now = datetime.now(timezone.utc)
        month_ago = now - timedelta(days=30)
        assert start.startswith(month_ago.strftime("%Y%m%d"))
        assert end.startswith(now.strftime("%Y%m%d"))

    def test_explicit_range(self):
        start, end = parse_date_range("20230101-20230131")
        assert start == "202301010000"
        assert end == "202301312359"

    def test_invalid_range(self):
        with pytest.raises(ValueError, match="Invalid date_range"):
            parse_date_range("last year")

    def test_explicit_range_format(self):
        start, end = parse_date_range("20240601-20240615")
        assert re.match(r"^\d{12}$", start)
        assert re.match(r"^\d{12}$", end)


class TestParseResponse:
    def test_parse_two_entries(self):
        papers, total = parse_response(SAMPLE_XML)
        assert total == 2
        assert len(papers) == 2

        p1 = papers[0]
        assert p1["title"] == "Deep Learning for Audio Signal Processing"
        assert "convolutional neural networks" in p1["abstract"]
        assert p1["authors"] == ["Alice Smith", "Bob Jones"]
        assert p1["link"] == "http://arxiv.org/abs/2301.00001v1"
        assert "cs.SD" in p1["categories"]
        assert "eess.AS" in p1["categories"]
        assert p1["published"] == "2023-01-01T00:00:00Z"

        p2 = papers[1]
        assert p2["title"] == "Prediction Markets and Gambling Behavior"
        assert p2["authors"] == ["Carol White"]

    def test_empty_results(self):
        papers, total = parse_response(EMPTY_XML)
        assert total == 0
        assert len(papers) == 0


class TestBuildQuery:
    def test_single_topic(self):
        query = build_query(["AI"], "20230101-20230131")
        assert 'all:"AI"' in query
        assert "submittedDate:" in query

    def test_multiple_topics(self):
        query = build_query(["AI", "DSP"], "20230101-20230131")
        assert "OR" in query
        assert 'all:"AI"' in query
        assert 'all:"DSP"' in query

    def test_phrase_topic(self):
        query = build_query(["predictive markets"], "past week")
        assert 'all:"predictive markets"' in query
