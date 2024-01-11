from classes.pirate import Pirate
from classes.ninja import Ninja

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
michelangelo.show_stats()

# jack_sparrow.defense(michelangelo)
jack_sparrow.show_stats()

jack_sparrow.cannonball_attack(michelangelo)
michelangelo.show_stats()

michelangelo.blowgun_attack(jack_sparrow)
jack_sparrow.show_stats()

michelangelo.blowgun_attack(jack_sparrow)
jack_sparrow.show_stats()

michelangelo.blowgun_attack(jack_sparrow)
jack_sparrow.show_stats()

michelangelo.blowgun_attack(jack_sparrow)
jack_sparrow.show_stats()

michelangelo.attack(jack_sparrow)
michelangelo.show_stats()