import requests


class Superhero:
    def __init__(self, name):
        self.name = name
        self.intelligence = self.get_intelligence()

    def get_intelligence(self):
        headers = {'Accept': 'application/json'}
        resp = requests.get(URL, headers=headers)

        if resp.status_code == 200:
            for hero in resp.json():
                if hero.get('name') == self.name:
                    self.intelligence = hero.get('powerstats').get('intelligence')
                    break

        return self.intelligence


def head_intellegence(heroes):
    heroes_dict = {}

    for hero in heroes:
        heroes_dict[hero.name] = hero.intelligence

    sorted_dict = dict(sorted(heroes_dict.items(), key=lambda item: item[1], reverse=True))

    return list(sorted_dict.keys())[0]


URL = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

Hulk = Superhero('Hulk')
Captain_America = Superhero('Captain America')
Thanos = Superhero('Thanos')

print(head_intellegence([Hulk, Captain_America, Thanos]))
