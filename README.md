# WTA Tennis Rankings Scraper

This project uses [Scrapy](https://scrapy.org/) to collect the current WTA
women's singles rankings from the
[WTA singles rankings page](https://www.wtatennis.com/rankings/singles).

For each ranking row, the spider extracts:

- Ranking
- Player name
- Country code
- Age
- Points

It also saves a copy of the downloaded page as `wta_singles_rankings.html` in
the current working directory.

## Requirements

- Python 3
- Scrapy (listed in `requirements.txt`)

## Install

From the project root:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Run and export JSON

The Scrapy project configuration is in the `wtatennis` directory. From the
project root, run:

```bash
cd wtatennis
scrapy crawl rankings -O rankings.json
```

The spider writes the extracted records to `wtatennis/rankings.json`, with one
JSON object per player. `-O` overwrites the output file if it already exists.
To append to an existing JSON Lines file instead, use lowercase `-o`:

```bash
scrapy crawl rankings -o rankings.json
```

The spider relies on CSS class names in the WTA page's HTML; if the site changes
its markup, the XPath selectors in
[`rankings.py`](wtatennis/wtatennis/spiders/rankings.py) may need updating.
