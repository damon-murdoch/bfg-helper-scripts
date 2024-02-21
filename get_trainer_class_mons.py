# Showdown Data
import src.showdown as showdown

facility_classes = [
  'FACILITY_CLASS_HIKER', # 0x0
  'FACILITY_CLASS_AQUA_GRUNT_M', # 0x1
  'FACILITY_CLASS_PKMN_BREEDER_F', # 0x2
  'FACILITY_CLASS_COOLTRAINER_M', # 0x3
  'FACILITY_CLASS_BIRD_KEEPER', # 0x4
  'FACILITY_CLASS_COLLECTOR', # 0x5
  'FACILITY_CLASS_AQUA_GRUNT_F', # 0x6
  'FACILITY_CLASS_SWIMMER_M', # 0x7
  'FACILITY_CLASS_MAGMA_GRUNT_M', # 0x8
  'FACILITY_CLASS_EXPERT_M', # 0x9
  'FACILITY_CLASS_BLACK_BELT', # 0xa
  'FACILITY_CLASS_AQUA_LEADER_ARCHIE', # 0xb
  'FACILITY_CLASS_HEX_MANIAC', # 0xc
  'FACILITY_CLASS_AROMA_LADY', # 0xd
  'FACILITY_CLASS_RUIN_MANIAC', # 0xe
  'FACILITY_CLASS_INTERVIEWER', # 0xf
  'FACILITY_CLASS_TUBER_F', # 0x10
  'FACILITY_CLASS_TUBER_M', # 0x11
  'FACILITY_CLASS_COOLTRAINER_F', # 0x12
  'FACILITY_CLASS_LADY', # 0x13
  'FACILITY_CLASS_BEAUTY', # 0x14
  'FACILITY_CLASS_RICH_BOY', # 0x15
  'FACILITY_CLASS_EXPERT_F', # 0x16
  'FACILITY_CLASS_POKEMANIAC', # 0x17
  'FACILITY_CLASS_MAGMA_GRUNT_F', # 0x18
  'FACILITY_CLASS_GUITARIST', # 0x19
  'FACILITY_CLASS_KINDLER', # 0x1a
  'FACILITY_CLASS_CAMPER', # 0x1b
  'FACILITY_CLASS_PICNICKER', # 0x1c
  'FACILITY_CLASS_BUG_MANIAC', # 0x1d
  'FACILITY_CLASS_PSYCHIC_M', # 0x1e
  'FACILITY_CLASS_PSYCHIC_F', # 0x1f
  'FACILITY_CLASS_GENTLEMAN', # 0x20
  'FACILITY_CLASS_ELITE_FOUR_SIDNEY', # 0x21
  'FACILITY_CLASS_ELITE_FOUR_PHOEBE', # 0x22
  'FACILITY_CLASS_LEADER_ROXANNE', # 0x23
  'FACILITY_CLASS_LEADER_BRAWLY', # 0x24
  'FACILITY_CLASS_LEADER_TATE_AND_LIZA', # 0x25
  'FACILITY_CLASS_SCHOOL_KID_M', # 0x26
  'FACILITY_CLASS_SCHOOL_KID_F', # 0x27
  'FACILITY_CLASS_SR_AND_JR', # 0x28
  'FACILITY_CLASS_POKEFAN_M', # 0x29
  'FACILITY_CLASS_POKEFAN_F', # 0x2a
  'FACILITY_CLASS_YOUNGSTER', # 0x2b
  'FACILITY_CLASS_CHAMPION_WALLACE', # 0x2c
  'FACILITY_CLASS_FISHERMAN', # 0x2d
  'FACILITY_CLASS_CYCLING_TRIATHLETE_M', # 0x2e
  'FACILITY_CLASS_CYCLING_TRIATHLETE_F', # 0x2f
  'FACILITY_CLASS_RUNNING_TRIATHLETE_M', # 0x30
  'FACILITY_CLASS_RUNNING_TRIATHLETE_F', # 0x31
  'FACILITY_CLASS_SWIMMING_TRIATHLETE_M', # 0x32
  'FACILITY_CLASS_SWIMMING_TRIATHLETE_F', # 0x33
  'FACILITY_CLASS_DRAGON_TAMER', # 0x34
  'FACILITY_CLASS_NINJA_BOY', # 0x35
  'FACILITY_CLASS_BATTLE_GIRL', # 0x36
  'FACILITY_CLASS_PARASOL_LADY', # 0x37
  'FACILITY_CLASS_SWIMMER_F', # 0x38
  'FACILITY_CLASS_TWINS', # 0x39
  'FACILITY_CLASS_SAILOR', # 0x3a
  'FACILITY_CLASS_WALLY', # 0x3b
  'FACILITY_CLASS_BRENDAN', # 0x3c
  'FACILITY_CLASS_BRENDAN_2', # 0x3d
  'FACILITY_CLASS_BRENDAN_3', # 0x3e
  'FACILITY_CLASS_MAY', # 0x3f
  'FACILITY_CLASS_MAY_2', # 0x40
  'FACILITY_CLASS_MAY_3', # 0x41
  'FACILITY_CLASS_PKMN_BREEDER_M', # 0x42
  'FACILITY_CLASS_BUG_CATCHER', # 0x43
  'FACILITY_CLASS_PKMN_RANGER_M', # 0x44
  'FACILITY_CLASS_PKMN_RANGER_F', # 0x45
  'FACILITY_CLASS_MAGMA_LEADER_MAXIE', # 0x46
  'FACILITY_CLASS_LASS', # 0x47
  'FACILITY_CLASS_YOUNG_COUPLE', # 0x48
  'FACILITY_CLASS_OLD_COUPLE', # 0x49
  'FACILITY_CLASS_SIS_AND_BRO', # 0x4a
  'FACILITY_CLASS_STEVEN', # 0x4b
  'FACILITY_CLASS_SALON_MAIDEN_ANABEL', # 0x4c
  'FACILITY_CLASS_DOME_ACE_TUCKER', # 0x4d
  'FACILITY_CLASS_RED', # 0x4e
  'FACILITY_CLASS_LEAF', # 0x4f
  'FACILITY_CLASS_RS_BRENDAN', # 0x50
  'FACILITY_CLASS_RS_MAY' # 0x51
]

def convert_const_to_camel(const):
    parts = const.split('_')
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

# Convert move name to MOVE_NAME
def get_species_constant(species_name):
    constant = species_name.upper()

    constant = constant.replace(" ", "_").replace("-", "_")
    constant = constant.replace("'", "").replace(":","").replace("%","")
    
    return f"SPECIES_{constant}"

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
                    continue # Skip non-regional variants

        # Add species id to list
        pokemon.append(speciesId)

    # Class species table
    classes = {}
    classes_lookup = {}
    for facility_class in facility_classes:
        classes[facility_class] = []
        classes_lookup[facility_class] = convert_const_to_camel(f"G_SPECIES_LIST_{facility_class}")

    # Lookup table of species which have appeared
    # in at least one facility class species list
    coverage = {}

    # Set all defaults to zero
    for speciesId in pokemon:
        coverage[speciesId] = 0

    # TODO: GENERATE LOOKUP
        
    # Sort ratings from highest to lowest
    coverage_sorted = sorted(coverage.items(), key=lambda x: x[1], reverse=True)

    print(coverage_sorted)