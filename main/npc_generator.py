import numpy as np
from numpy import random



### weighted multipliers for rarity. Updated in method or by TODO user input
commonChance = 0.0
uncommonChance = 0.0
rareChance = 0.0
specialChance = 0.0 
chanceList = list((commonChance, uncommonChance, rareChance, specialChance))   #specialChance is for anything not listed as a rarity, such as "No Class"


### possible ancestries to choose from
ancestryCommonList = list(("Goblin", "Human", "Dwarf", "Elf", "Halfling", "Half-Elf", "Gnome", "Leshy", "Orc"))
ancestryUncommonList = list(("Azarketi", "Catfolk", "Fetchling", "Hobgoblin", "Kholo", "Kitsune", "Kobold", "Lizardfolk",
                              "Nagaji","Ratfolk", "Samsaran", "Tengu", "Tripkee", "Vanara", "Vishkanya", "Ghoran"))   #in this setting Athamaru, Minotaur, Wayang, and Centaur have been moved to rare. Merfolk are not considered for NPC generation
ancestryRareList = list(("Anadi", "Automaton", "Awakened Animal", "Conrasue", "Fleshwarp", "Goloma", "Kashrishi", "Poppet",
                          "Sarangay", "Shisk", "Shoony", "Sprite", "Strix", "Surki", "Yaoguai"))   #in this setting Ghoran and Vishkanya have been moved to uncommon. Skeleton are not considered.
ancestrySpecialList = [] #there probably aren't ancestries that aren't listed above that are a good fit for random generation. Empty, only used for conformity with other lists
ancestryList = []


### possible classes to choose from
# for this setting, divine casters and champions have been moved to uncommon. Other full casters have been moved to uncommon or rare.
classCommonList = list(("Alchemist", "Fighter", "Barbarian", "Investigator", "Ranger", "Rogue", "Monk", "Swashbuckler"))
classUncommonList = list(("Druid", "Bard", "Kineticist", "Champion", "Cleric", "Magus", "Sorcerer",
                           "Summoner", "Thaumaturge", "Witch", "Wizard"))
classRareList = list(("Animist", "Oracle", "Psychic", "Inventor", "Gunslinger", "Exemplar"))
classSpecialList = ["None"] #most antagonists will use a class framework
classList = []
###TODO make all these classes Objects to help determin HP, AC, and Saves using basic "low/mid/high" descriptors, maybe some hallmark abilities


### possible background the NPC may have, mostly from background options for PCs
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
#Jobs that should heighten chance of being an Antagonist: "Cultist", "Criminal", "Doomcaller", "False Medium", "Fated Rival", "Grave Robber", "Harrow Chosen", "Hired Killer"


### generic descriptors of the NPCs appearance
describeCommonList = list(("wears a unique scent", "has a unique hairstyle", "has a unique grin", "doesn't like something that most people would like", "displays an heirloom", 
                        "has a particular presence about them",))
describeUncommonList = list(("wears a cape", "has an unusual haircolor", "has a striking eye color", "is good with a sword",))
describeRareList = list(("has a missing limb",))


### generic personality quirks the NPC may have
personalityCommonList = list(())
personalityUncommonList = list(())
personalityRareList = list(())


### generic driving force the NPC may have
motiveCommonList = list(())
motiveUncommonList = list(())
motiveRareList = list(())
motiveSpecialList = ["None"]
motiveList = []


### weight for deciding whether the NPC serves as an antagonist, ally, or neutral
allyChance = 5*random.rand() #most NPCs should be neutral, expected use is <1 is ally, >1 and <4 is neutral, >5 is antagonist but may use normal distribution instead





###TODO make a "Player Party" object and use it to influence DCs and Levels of the NPC

### function: reroll, update, and print


def listMaker(common, uncommon, rare, special, chances: float) -> list: ### create final lists of options for picking the character
    output = []
    templist = [common, uncommon, rare, special]
    for sublist in templist:
        threshold = 1 - chances[templist.index(sublist)] # the chance of an item being added to a final list is based on the rarity threshold percentages
        for item in sublist:
            roll = random.rand()
            if roll > threshold:
                output.append(item)    
    if output != []:
        return output
    else:
        # If no items were selected, return a random choice from the common list for more variety
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

    # Ensure no field is 'None'
    if finalAncestry == 'None':
        finalAncestry = pickChoice(ancestryCommonList)
    if finalClass == 'None':
        finalClass = pickChoice(classCommonList)
    if finalBackground == 'None':
        finalBackground = pickChoice(backgroundCommonList)

    return f"{finalAncestry}, {finalClass}, {finalBackground}"

# Remove the call to main() to avoid side effects on import