tableString = """Language

Typical Speakers

Script

Common

Humans

Common

Dwarvish

Dwarves

Dwarvish

Elvish

Elves

Elvish

Giant

Ogres, giants

Dwarvish

Gnomish

Gnomes

Dwarvish

Goblin

Goblinoids

Dwarvish

Halfling

Halflings

Common

Orc

Orcs

Dwarvish

Exotic Languages

Language

Typical Speakers

Script

Abyssal

Demons

Infernal

Celestial

Celestials

Celestial

Draconic

Dragons, dragonborn

Draconic

Deep Speech

Aboleths, cloakers

—

Infernal

Devils

Infernal

Primordial

Elementals

Dwarvish

Sylvan

Fey creatures

Elvish

Undercommon

Underworld traders

Elvish"""

splits = tableString.split("\n\n")

# insertBlanksAt = list(range(12, (21)*12,12))
# for i in range(len(insertBlanksAt)):
# 	splits.insert(insertBlanksAt[i]-i, "")

out = open('src/mdsrd5/tables/languages.csv', 'w')

counter = 0
newLineAt = 2

for split in splits:
	out.write("\"" + split.strip() + "\"")
	
	if counter == newLineAt:
		out.write("\n")
		counter = 0
	else:
		out.write(",")
		counter += 1

out.close()
