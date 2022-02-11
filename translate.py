# cd $HOME/github.com/loicbourgois/PokeWorld && python translate.py

path = "pokemon_en_fr/pokemon_en_fr_utf8.csv"
path_2 = "Defs/ThingDefs_Races/Races_Pokemon.xml"

with open(path_2) as races:
    content_races = races.read()
    with open(path, 'r') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            abc = line.strip().split(";")
            en = abc[1]
            fr = abc[2]
            print(i, en, fr)
            content_races = content_races.replace(f"<label>{en}</label>", f"<label>{fr}</label>").replace(f"<labelPlural>{en}</labelPlural>", f"<labelPlural>{fr}</labelPlural>")
    f = open("Defs/ThingDefs_Races/Races_Pokemon_fr.xml", "w")
    f.write(content_races)
    f.close()

# print("bob")
