# Showdown Data
import src.showdown as showdown

import math
import os

OUTPUT_DIRECTORY = "out"
OUTPUT_FILENAME = "battle_frontier_generator_trainer_class_mons.h"

eevees = [
    "jolteon", "flareon", "umbreon",
    "leafeon", "sylveon", "glaceon",
    "espeon", "vaporean", "eevee",
]

regis = [
    "regirock", "regice", "registeel",
    "regigigas", "regidrago", "regieleki"
]

trainer_classes = [
    'TRAINER_CLASS_HIKER',
    # 'TRAINER_CLASS_TEAM_AQUA',
    'TRAINER_CLASS_PKMN_BREEDER',
    'TRAINER_CLASS_COOLTRAINER',
    'TRAINER_CLASS_BIRD_KEEPER',
    'TRAINER_CLASS_COLLECTOR',
    'TRAINER_CLASS_SWIMMER_M',
    # 'TRAINER_CLASS_TEAM_MAGMA',
    'TRAINER_CLASS_EXPERT',
    # 'TRAINER_CLASS_AQUA_ADMIN',
    'TRAINER_CLASS_BLACK_BELT',
    # 'TRAINER_CLASS_AQUA_LEADER',
    'TRAINER_CLASS_HEX_MANIAC',
    'TRAINER_CLASS_AROMA_LADY',
    'TRAINER_CLASS_RUIN_MANIAC',
    # 'TRAINER_CLASS_INTERVIEWER',
    'TRAINER_CLASS_TUBER_F',
    'TRAINER_CLASS_TUBER_M',
    'TRAINER_CLASS_LADY',
    'TRAINER_CLASS_BEAUTY',
    'TRAINER_CLASS_RICH_BOY',
    'TRAINER_CLASS_POKEMANIAC',
    'TRAINER_CLASS_GUITARIST',
    'TRAINER_CLASS_KINDLER',
    'TRAINER_CLASS_CAMPER',
    'TRAINER_CLASS_PICNICKER',
    'TRAINER_CLASS_BUG_MANIAC',
    'TRAINER_CLASS_PSYCHIC',
    'TRAINER_CLASS_GENTLEMAN',
    # 'TRAINER_CLASS_ELITE_FOUR',
    # 'TRAINER_CLASS_LEADER',
    'TRAINER_CLASS_SCHOOL_KID',
    # 'TRAINER_CLASS_SR_AND_JR',
    # 'TRAINER_CLASS_WINSTRATE',
    'TRAINER_CLASS_POKEFAN',
    'TRAINER_CLASS_YOUNGSTER',
    # 'TRAINER_CLASS_CHAMPION',
    'TRAINER_CLASS_FISHERMAN',
    'TRAINER_CLASS_TRIATHLETE',
    'TRAINER_CLASS_DRAGON_TAMER',
    'TRAINER_CLASS_NINJA_BOY',
    'TRAINER_CLASS_BATTLE_GIRL',
    'TRAINER_CLASS_PARASOL_LADY',
    'TRAINER_CLASS_SWIMMER_F',
    # 'TRAINER_CLASS_TWINS',
    'TRAINER_CLASS_SAILOR',
    'TRAINER_CLASS_COOLTRAINER_2',
    # 'TRAINER_CLASS_MAGMA_ADMIN',
    # 'TRAINER_CLASS_RIVAL',
    'TRAINER_CLASS_BUG_CATCHER',
    'TRAINER_CLASS_PKMN_RANGER',
    # 'TRAINER_CLASS_MAGMA_LEADER',
    'TRAINER_CLASS_LASS',
    # 'TRAINER_CLASS_YOUNG_COUPLE',
    # 'TRAINER_CLASS_OLD_COUPLE',
    # 'TRAINER_CLASS_SIS_AND_BRO',
    # 'TRAINER_CLASS_SALON_MAIDEN',
    # 'TRAINER_CLASS_DOME_ACE',
    # 'TRAINER_CLASS_PALACE_MAVEN',
    # 'TRAINER_CLASS_ARENA_TYCOON',
    # 'TRAINER_CLASS_FACTORY_HEAD',
    # 'TRAINER_CLASS_PIKE_QUEEN',
    # 'TRAINER_CLASS_PYRAMID_KING',
    # 'TRAINER_CLASS_RS_PROTAG',
]


def convert_const_to_camel(const):
    parts = const.split('_')
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

# Convert move name to MOVE_NAME


def get_species_constant(species_name):
    constant = species_name.upper()

    constant = constant.replace(" ", "_").replace("-", "_")
    constant = constant.replace("’", "").replace(
        ":", "").replace("%", "").replace(".", "")

    return f"SPECIES_{constant}"


def is_tagged(species, tag):
    return "tags" in species and tag in species["tags"]


def is_forme(species, forme):
    return "forme" in species and species["forme"] == forme


# Main Process
if __name__ == '__main__':

    # Get showdown data files
    MOVES, POKEMON = showdown.get_showdown_data()

    # List of valid Pokemon
    # Excludes alt. Formes, etc.
    pokemon = []

    # Loop over species ids
    for speciesId in POKEMON:
        species = POKEMON[speciesId]

        # Base forme for species
        if "baseSpecies" in species:
            if "forme" in species:
                forme = species["forme"]
                if not (forme == "Alola" or forme == "Galar" or forme == "Hisui" or forme == "Paldea"):
                    continue  # Skip non-regional variants

        # Add species id to list
        pokemon.append(speciesId)

    # Class species table
    classes = {}
    classes_lookup = {}
    for trainer_class in trainer_classes:
        classes[trainer_class] = []
        classes_lookup[trainer_class] = convert_const_to_camel(
            f"G_SPECIES_LIST_{trainer_class}")

    # Lookup table of species which have appeared
    # in at least one facility class species list
    coverage = {}

    # Set all defaults to zero
    for speciesId in pokemon:
        species = POKEMON[speciesId]
        coverage[speciesId] = 0

        for type in species["types"]:
            # Most Common Types
            if type == "Normal":
                for trainer_class in trainer_classes:  # All Trainer Classes
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Water":
                for trainer_class in ["TRAINER_CLASS_POKEFAN", "TRAINER_CLASS_COOLTRAINER", "TRAINER_CLASS_COOLTRAINER_2", "TRAINER_CLASS_GENTLEMAN", "TRAINER_CLASS_TUBER_M", "TRAINER_CLASS_TUBER_F", "TRAINER_CLASS_SWIMMER_M", "TRAINER_CLASS_SWIMMER_F", "TRAINER_CLASS_FISHERMAN", "TRAINER_CLASS_SAILOR", "TRAINER_CLASS_COLLECTOR", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_LADY", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_PKMN_BREEDER", "TRAINER_CLASS_DRAGON_TAMER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Fire":
                for trainer_class in ["TRAINER_CLASS_POKEFAN", "TRAINER_CLASS_COOLTRAINER", "TRAINER_CLASS_COOLTRAINER_2", "TRAINER_CLASS_GENTLEMAN", "TRAINER_CLASS_COLLECTOR", "TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_LADY", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_PKMN_BREEDER", "TRAINER_CLASS_DRAGON_TAMER", "TRAINER_CLASS_CAMPER", "TRAINER_CLASS_PICNICKER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Grass":
                for trainer_class in ["TRAINER_CLASS_POKEFAN", "TRAINER_CLASS_COOLTRAINER", "TRAINER_CLASS_COOLTRAINER_2", "TRAINER_CLASS_GENTLEMAN", "TRAINER_CLASS_AROMA_LADY", "TRAINER_CLASS_COLLECTOR", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_LADY", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_CAMPER", "TRAINER_CLASS_PICNICKER", "TRAINER_CLASS_PKMN_BREEDER", "TRAINER_CLASS_PKMN_RANGER", "TRAINER_CLASS_LASS", "TRAINER_CLASS_YOUNGSTER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Electric":
                for trainer_class in ["TRAINER_CLASS_POKEFAN", "TRAINER_CLASS_COOLTRAINER", "TRAINER_CLASS_COOLTRAINER_2", "TRAINER_CLASS_GENTLEMAN", "TRAINER_CLASS_BEAUTY", "TRAINER_CLASS_PARASOL_LADY", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_CAMPER", "TRAINER_CLASS_PICNICKER", "TRAINER_CLASS_PKMN_BREEDER", "TRAINER_CLASS_COLLECTOR", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_SCHOOL_KID", "TRAINER_CLASS_LASS", "TRAINER_CLASS_YOUNGSTER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Flying" or "Levitate" in species["abilities"].values():
                for trainer_class in ["TRAINER_CLASS_POKEFAN", "TRAINER_CLASS_BIRD_KEEPER", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_LADY", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_CAMPER", "TRAINER_CLASS_PICNICKER", "TRAINER_CLASS_PKMN_BREEDER", "TRAINER_CLASS_PSYCHIC", "TRAINER_CLASS_PKMN_RANGER", "TRAINER_CLASS_SCHOOL_KID", "TRAINER_CLASS_LASS", "TRAINER_CLASS_YOUNGSTER", "TRAINER_CLASS_SCHOOL_KID"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            # Regular Types
            elif type == "Fighting":
                for trainer_class in ["TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_HIKER", "TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_SAILOR", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_NINJA_BOY", "TRAINER_CLASS_PKMN_RANGER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Poison":
                for trainer_class in ["TRAINER_CLASS_HEX_MANIAC", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_CAMPER", "TRAINER_CLASS_PICNICKER", "TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_DRAGON_TAMER", "TRAINER_CLASS_NINJA_BOY"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Ground":
                for trainer_class in ["TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_HIKER", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_NINJA_BOY"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Rock" or is_forme(species, "Hisui") or is_tagged(species, "Paradox"):
                for trainer_class in ["TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_HIKER", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_NINJA_BOY"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Bug":
                for trainer_class in ["TRAINER_CLASS_PKMN_RANGER", "TRAINER_CLASS_CAMPER", "TRAINER_CLASS_PICNICKER", "TRAINER_CLASS_BUG_CATCHER", "TRAINER_CLASS_BUG_MANIAC", "TRAINER_CLASS_FISHERMAN", "TRAINER_CLASS_SCHOOL_KID", "TRAINER_CLASS_LASS", "TRAINER_CLASS_YOUNGSTER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Ghost":
                for trainer_class in ["TRAINER_CLASS_HEX_MANIAC", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_DRAGON_TAMER", "TRAINER_CLASS_NINJA_BOY", "TRAINER_CLASS_YOUNGSTER", "TRAINER_CLASS_GENTLEMAN"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Steel":
                for trainer_class in ["TRAINER_CLASS_COOLTRAINER", "TRAINER_CLASS_COOLTRAINER_2", "TRAINER_CLASS_GENTLEMAN", "TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_HIKER", "TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_DRAGON_TAMER"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Psychic":
                for trainer_class in ["TRAINER_CLASS_BEAUTY", "TRAINER_CLASS_PARASOL_LADY", "TRAINER_CLASS_AROMA_LADY", "TRAINER_CLASS_HEX_MANIAC", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_LADY", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_PSYCHIC"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Ice":
                for trainer_class in ["TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_BEAUTY", "TRAINER_CLASS_PARASOL_LADY", "TRAINER_CLASS_TUBER_M", "TRAINER_CLASS_TUBER_F", "TRAINER_CLASS_SWIMMER_M", "TRAINER_CLASS_SWIMMER_F", "TRAINER_CLASS_FISHERMAN", "TRAINER_CLASS_TRIATHLETE"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Dark":
                for trainer_class in ["TRAINER_CLASS_HEX_MANIAC", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_GUITARIST", "TRAINER_CLASS_KINDLER", "TRAINER_CLASS_BATTLE_GIRL", "TRAINER_CLASS_BLACK_BELT", "TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_DRAGON_TAMER", "TRAINER_CLASS_NINJA_BOY"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            elif type == "Fairy":
                for trainer_class in ["TRAINER_CLASS_POKEFAN", "TRAINER_CLASS_BEAUTY", "TRAINER_CLASS_PARASOL_LADY", "TRAINER_CLASS_AROMA_LADY", "TRAINER_CLASS_TRIATHLETE", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_LADY", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_LASS"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1
            # Rarest Type
            elif type == "Dragon":
                for trainer_class in ["TRAINER_CLASS_COOLTRAINER", "TRAINER_CLASS_COOLTRAINER_2", "TRAINER_CLASS_GENTLEMAN", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_POKEMANIAC", "TRAINER_CLASS_DRAGON_TAMER", "TRAINER_CLASS_NINJA_BOY"]:
                    classes[trainer_class].append(speciesId)
                    coverage[speciesId] += 1

        # Special cases for specific trainer classes

        # Regirock / Regice / Registeel
        if speciesId in regis:
            for trainer_class in ["TRAINER_CLASS_RUIN_MANIAC", "TRAINER_CLASS_EXPERT", "TRAINER_CLASS_PSYCHIC"]:
                classes[trainer_class].append(speciesId)
                coverage[speciesId] += 1

        if speciesId in eevees:
            for trainer_class in ["TRAINER_CLASS_LADY", "TRAINER_CLASS_RICH_BOY", "TRAINER_CLASS_BEAUTY"]:
                classes[trainer_class].append(speciesId)
                coverage[speciesId] += 1

    print(f"Generating output content ...")

    # Create output content
    output = [
        "// File Auto-Generated By bfg-helper-scripts (get_trainer_class_mons.py)",
        "// Repository Link: https://github.com/damon-murdoch/bfg-helper-scripts",
        "// Warning: Some moves may need to be renamed or removed depending on your project!",
        "",
        "const u16 * gBattleFrontierTrainerClassSpeciesLookup[TRAINER_CLASS_COUNT] = {"
    ]

    # Loop over the trainer classes
    for trainer_class in trainer_classes:
        output.append(
            f"\t[{trainer_class}] = {classes_lookup[trainer_class]},")

    output.append("};\n\n")

    for trainer_class in trainer_classes:
        class_list = sorted(list(set(classes[trainer_class])))
        output.append(
            f"const u16 {classes_lookup[trainer_class]}[{len(class_list)}] = " + "{")
        for speciesId in class_list:
            species = POKEMON[speciesId]
            constant = get_species_constant(species["name"])
            output.append(f"\t{constant},")

        output.append("};\n")

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    outpath = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILENAME)

    print(f"Writing results to file '{outpath}' ...")

    with open(outpath, "w+", encoding="utf8") as f:
        f.write("\n".join(output))

    print("Results saved successfully!")
