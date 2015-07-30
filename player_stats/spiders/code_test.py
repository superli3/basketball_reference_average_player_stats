__author__ = 'Jeff'


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from player_stats.items import PlayerStatsItem

class BaseSpider(BaseSpider):
    name = "players_stats2"
    allowed_domains = ["basketball-reference.com"]
    start_urls =  ["http://www.basketball-reference.com/players/j/jamesle01.html"]
    download_delay = 30

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('')
        items = []
        for titles in titles:
            item = PlayerStatsItem()
            item ["Season"] = titles.select("td[1]/a/text()").extract()
            item ["Age"] = titles.select("td[2]/text()").extract()
            item ["Team"] = titles.select("td[3]/a/text()").extract()
            item ["League"] = titles.select("td[4]/a/text()").extract()
            item ["Position"] = titles.select("td[5]/text()").extract()
            item ["Games_Played"] = titles.select("td[6]/text()").extract()
            item ["Games_Started"] = titles.select("td[7]/text()").extract()
            item ["Minutes_Played"] = titles.select("td[8]/text()").extract()
            item ["Field_Goals"] = titles.select("td[9]/text()").extract()
            item ["Field_Goals_Attempted"] = titles.select("td[10]/text()").extract()
            item ["Field_Goals_Percentage"] = titles.select("td[11]/text()").extract()
            item ["Three_pointers_made"] = titles.select("td[12]/text()").extract()
            item ["Three_pointers_attempted"] = titles.select("td[13]/text()").extract()
            item ["Three_pointers_percentage"] = titles.select("td[14]/text()").extract()
            item ["Two_pointers_made"] = titles.select("td[15]/text()").extract()
            item ["Two_pointers_attempted"] = titles.select("td[16]/text()").extract()
            item ["Two_pointers_percentage"] = titles.select("td[17]/text()").extract()
            item ["Effective_FG"] = titles.select("td[18]/text()").extract()
            item ["Free_throws_made"] = titles.select("td[19]/text()").extract()
            item ["Free_throws_attempted"] = titles.select("td[20]/text()").extract()
            item ["Offensive_Rebounds"] = titles.select("td[21]/text()").extract()
            item ["Defensive_Rebounds"] = titles.select("td[22]/text()").extract()
            item ["Total_Rebounds"] = titles.select("td[23]/text()").extract()
            item ["Assists"] = titles.select("td[24]/text()").extract()
            item ["Steals"] = titles.select("td[25]/text()").extract()
            item ["Blocks"] = titles.select("td[26]/text()").extract()
            item ["Turnovers"] = titles.select("td[27]/text()").extract()
            item ["Personal_Fouls"] = titles.select("td[28]/text()").extract()
            item ["Points"] = titles.select("td[29]/text()").extract()
            items.append(item)
        return items
