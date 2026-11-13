import scrapy
from pathlib import Path


class RankingsSpider(scrapy.Spider):
    name = "rankings"
    allowed_domains = ["www.wtatennis.com"]
    start_urls = ["https://www.wtatennis.com/rankings/singles"]

    def parse(self, response):
        filename = "wta_singles_rankings.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename} from {response.url}")

        rows = response.xpath(
            '//table[contains(@class, "js-rankings-list")]'
            '/tbody[contains(@class, "js-rankings-body")]'
            '/tr[contains(@class, "player-row")]'
        )
        if not rows:
            self.logger.warning("No ranking rows found at %s", response.url)
            return

        for row in rows:
            yield {
                "ranking": row.xpath(
                    'normalize-space(.//span[contains(@class, "player-row__rank")]/text())'
                ).get(),
                "name": row.xpath(
                    'normalize-space(.//span[contains(@class, "player-cell__name")]/text())'
                ).get(),
                "country": row.xpath(
                    'normalize-space(.//span[contains(@class, "player-cell__country")]/text())'
                ).get(),
                "age": row.xpath(
                    'normalize-space(.//td[contains(@class, "player-row__cell--age")]/text())'
                ).get(),
                "points": (
                    row.xpath(
                        'normalize-space(.//td[contains(@class, "player-row__cell--points")]/text())'
                    )
                    .get(default="")
                    .replace(",", "")
                ),
            }
