# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class PlayerStatsItem(Item):
    Player = Field()
    Season = Field()
    Age = Field()
    Team = Field()
    League = Field()
    Position = Field()
    Games_Played = Field()
    Games_Started = Field()
    Minutes_Played = Field()
    Field_Goals = Field()
    Field_Goals_Attempted = Field()
    Field_Goals_Percentage = Field()
    Three_pointers_made = Field()
    Three_pointers_attempted = Field()
    Three_pointers_percentage = Field()
    Two_pointers_made = Field()
    Two_pointers_attempted = Field()
    Two_pointers_percentage = Field()
    Effective_FG = Field()
    Free_throws_made = Field()
    Free_throws_attempted = Field()
    Offensive_Rebounds = Field()
    Defensive_Rebounds = Field()
    Total_Rebounds = Field()
    Assists = Field()
    Steals = Field()
    Blocks = Field()
    Turnovers = Field()
    Personal_Fouls = Field()
    Points = Field()
    pass