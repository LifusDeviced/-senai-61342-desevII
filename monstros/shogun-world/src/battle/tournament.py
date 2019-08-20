import json
from src.characters.senshi import Senshi
from src.battle.tatakai import Tatakai

file = open("../characters/theSixteen.json", "r")
theSixteen = file.read()
theSixteen = json.loads(theSixteen)
senshis = []
i = 0

while(i <= 15):
	oneSenshi = theSixteen[i]
	senshi = Senshi(oneSenshi["name"], oneSenshi["category"], oneSenshi["attack"], oneSenshi["defense"], oneSenshi["speed"], oneSenshi["health"], oneSenshi["expertise"], oneSenshi["level"])
	senshis.append(senshi)
	i += 1

Tatakai.tournament(senshis)

