from filters import HeroFilter

class RaceFilter(HeroFilter):
    def filter_by_race(self, race_name):
        filtered_heroes = super().filter_by_race(race_name)
        return filtered_heroes

if __name__ == "__main__":
    race_filter = RaceFilter()

    race_name = "goblin"  # Pode ser qualquer outra raça, exemplo: "human"
    filtered_heroes = race_filter.filter_by_race(race_name)

    print(f"Heróis da raça {race_name}:")
    for hero in filtered_heroes:
        print(f"Nome: {hero['localized_name']}, ID: {hero['id']}")
