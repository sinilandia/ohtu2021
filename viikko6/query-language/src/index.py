from statistics import Statistics
from player_reader import PlayerReader
from matchers import *

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = query.hasAtLeast(30, "goals").playsIn("EDM").build()

    for player in stats.matches(matcher):
        print(player)
    

if __name__ == "__main__":
    main()
