import numpy as np
from numpy import random


commonChance = 0.0
uncommonChance = 0.0
rareChance = 0.0
specialChance = 0.0 
chanceList = list((commonChance, uncommonChance, rareChance, specialChance))



ancestryCommonList = list(("Goblin", "Human", "Dwarf", "Elf", "Halfling", "Half-Elf", "Gnome", "Leshy", "Orc"))
ancestryUncommonList = list(("Azarketi", "Catfolk", "Fetchling", "Hobgoblin", "Kholo", "Kitsune", "Kobold", "Lizardfolk",
                              "Nagaji","Ratfolk", "Samsaran", "Tengu", "Tripkee", "Vanara", "Vishkanya", "Ghoran"))
ancestryRareList = list(("Anadi", "Automaton", "Awakened Animal", "Conrasue", "Fleshwarp", "Goloma", "Kashrishi", "Poppet",
                          "Sarangay", "Shisk", "Shoony", "Sprite", "Strix", "Surki", "Yaoguai"))
ancestrySpecialList = []
ancestryList = []

classCommonList = list(("Alchemist", "Fighter", "Barbarian", "Investigator", "Ranger", "Rogue", "Monk", "Swashbuckler"))
classUncommonList = list(("Druid", "Bard", "Kineticist", "Champion", "Cleric", "Magus", "Sorcerer",
                           "Summoner", "Thaumaturge", "Witch", "Wizard"))
classRareList = list(("Animist", "Oracle", "Psychic", "Inventor", "Gunslinger", "Exemplar"))
classSpecialList = ["None"]
classList = []
backgroundCommonList = list(("Acrobat", "Archeologist", "Artisan", "Artist", "Astrologer", "Barber", "Barkeep", "Barrister", "Bookkeeper",
                        "Charlatan", "Cook", "Courier", "Criminal", "Cultist", "Detective", "Driver", "Emissary",
                        "Entertainer", "Farmhand", "Farmsteader", "Field Medic", "Fire Warden", "Gambler", "Gossip",
                        "Guard", "Herbalist", "Hermit", "Hunter", "Insurgent", "Jeweler", "Junker", "Laborer", "Merchant", "Miner",
                        "Night Watch", "Navigator", "Nomad", "Outrider", "Pilgrim", "Root Worker", "Runner", "Sabateur", "Sailor", "Scavenger",
                        "Scout", "Servant", "Squire", "Preacher", "Vendor", "Dancer", "Warrior", "Mercenary"))
backgroundUncommonList = list(("Acolyte", "Alloysmith", "Back-Alley Doctor", "Cannoneer", "Codebreaker", "Curandero", "Dendrologist",
                        "Deputy", "Eagle Hunter", "Eidolon Contract", "Favored", "Fireworks Performer", "Fortune Teller",
                        "Free Spirit", "Grave Robber", "Hired Killer", "Hounded Thief", "Magical Merchant", "Martial Disciple", "Musical Prodigy",
                        "Noble", "Librarian", "Ocean Diver", "Prisoner", "Notary", "Gravetender", "Scholar", "Seet", "Spotter", "Teacher", "Trailblazer",
                        "Gladiator", "Bounty Hunter"))
backgroundRareList = list(("Astrological Augur", "Beast Blessed", "Blessed", "Chosen One", "Cursed", "Dauntless", "Doomcaller", "Eclipseborn",
                        "Elementally Infused", "Energy Scarred", "False Medium", "Fated Rival", "Feral Child", "Feybound", "Gunsmith", 
                        "Harrow Chosen", "Haunted", "Magical Experiment", "Magical Misfit", 
                        "Mechanical Symbiosis", "Occult Librarian", "Once Bitten", "Royalty", "Runaway Noble", "Sheriff", "Spell Seeker"))
backgroundSpecialList = ["None"]
backgroundList = []


describeCommonList = list(("wears a unique scent", "has a unique hairstyle", "has a unique grin", "doesn't like something that most people would like", "displays an heirloom", 
                        "has a particular presence about them",))
describeUncommonList = list(("wears a cape", "has an unusual haircolor", "has a striking eye color", "is good with a sword",))
describeRareList = list(("has a missing limb",))


personalityCommonList = list(())
personalityUncommonList = list(())
personalityRareList = list(())


motiveCommonList = list(())
motiveUncommonList = list(())
motiveRareList = list(())
motiveSpecialList = ["None"]
motiveList = []


allyChance = 5*random.rand()

def listMaker(common, uncommon, rare, special, chances: float) -> list:
    output = []
    templist = [common, uncommon, rare, special]
    for sublist in templist:
        threshold = 1 - chances[templist.index(sublist)]
        for item in sublist:
            roll = random.rand()
            if roll > threshold:
                output.append(item)    
    if output != []:
        return output
    else:
        return [common[random.randint(len(common))]]
    

def pickChoice(input: list):
    indexChoice = random.randint(len(input))
    return input[indexChoice]
    

def generate_npc_character():
    """Generate and return a random NPC character as a string: 'Ancestry, class, background'."""
    chanceList_ancestry = [0.6, 0.2, 0.05, 0.0]
    ancestryList = listMaker(ancestryCommonList, ancestryUncommonList, ancestryRareList, ancestrySpecialList, chanceList_ancestry)
    
    chanceList_class = [0.3, 0.1, 0.025, 0.3]
    classList = listMaker(classCommonList, classUncommonList, classRareList, classSpecialList, chanceList_class)
    
    chanceList_background = [0.3, 0.1, 0.025, 0.5]
    backgroundList = listMaker(backgroundCommonList, backgroundUncommonList, backgroundRareList, backgroundSpecialList, chanceList_background)

    finalAncestry = pickChoice(ancestryList)
    finalClass = pickChoice(classList)
    finalBackground = pickChoice(backgroundList)

    if finalAncestry == 'None':
        finalAncestry = pickChoice(ancestryCommonList)
    if finalClass == 'None':
        finalClass = pickChoice(classCommonList)
    if finalBackground == 'None':
        finalBackground = pickChoice(backgroundCommonList)

    return f"{finalAncestry}, {finalClass}, {finalBackground}"
