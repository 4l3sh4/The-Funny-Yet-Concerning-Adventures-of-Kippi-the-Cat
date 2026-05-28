# ******************************************************************************************************
# Program: THE_FUNNY_YET_CONCERNING_ADVENTURES_OF_KIPPI_THE_CAT.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL9L
# Year: 2023/24 Trimester 1
# Names: ALESHA NOOR | AMIRAH BALQIS | ARIANA FALISYA
# ******************************************************************************************************

#we use this to do all the random chances that is involved in our game. makes it more fun, hehe!
import random
#we use this so that our players can quit the game gracefully!
import os
#for our save files!
import json

game_state = True
intro_screen = True
game_start = False
continue_game = False

while game_state == True:
    #kippi
    #dictionary ver.
    kippi_stats_dictionary = {'LVL': 0, 'EXP' : 0, 'EXP TO LVL UP' : 1, 'HP': 10, 'ATK': 3, 'DEF': 1, 'SPD' : 1}

    #list ver.
    kippi_stats_perm = list(kippi_stats_dictionary.values()) #limit, important for level up, doesn't change when kippi gets attacked
    kippi_stats = list(kippi_stats_dictionary.values()) #the only stats that changes when kippi gets attacked
        
    #intro sceeen
    start_options = ['play', 'continue', 'quit']
    yes_or_no = ['yes', 'no']

    #omg we finally fixed the save function
    #explanation for what we changed:
    #deleted last_played_location (discovered that kippi_stats[0] plays the same function anyway)
    #made the introduction be able to print ONLY IF kippi's level == 0 to avoid having the player go through the intro all over again when they boot up their save file lol
    #added meanie_counter onto the list of things to be saved since it's required for the bad ending (spoilers oops)
    def load_checkpoint(file_path):
        try:
            with open(file_path, 'r') as kippi_save:
                data = kippi_save.readlines()                
                player_name = data[0].split(": ")[1].strip()
                kippi_stats = json.loads(data[1].split(": ")[1].strip())
                inventory = [item.strip() for item in data[2].split(": ")[1].split(',')] if len(data) > 2 else []
                head = [item.strip() for item in data[3].split(": ")[1].split(',')] if len(data) > 3 else []
                body = [item.strip() for item in data[4].split(": ")[1].split(',')] if len(data) > 4 else []
                feet = [item.strip() for item in data[5].split(": ")[1].split(',')] if len(data) > 5 else []
                hand = [item.strip() for item in data[6].split(": ")[1].split(',')] if len(data) > 6 else []
                meanie_counter = data[7].split(": ")[1].strip()
                return {
                    "player_name": player_name,
                    "kippi_stats": kippi_stats,
                    "inventory": inventory,
                    "head": head,
                    "body": body,
                    "feet": feet,
                    "hand": hand,
                    "meanie_counter": meanie_counter
                }
        except FileNotFoundError:
            return None
    
    while intro_screen == True:
        print("		  _______ __   __ _______   _______ __   __ __    _ __    _ __   __\n		 |       |  | |  |       | |       |  | |  |  |  | |  |  | |  | |  |\n		 |_     _|  |_|  |    ___| |    ___|  | |  |   |_| |   |_| |  |_|  |\n 		   |   | |       |   |___  |   |___|  |_|  |       |       |       |\n 		   |   | |       |    ___| |    ___|       |  _    |  _    |_     _|\n 		   |   | |   _   |   |___  |   |   |       | | |   | | |   | |   |\n 	 	   |___| |__| |__|_______| |___|   |_______|_|  |__|_|  |__| |___|\n __   __ _______ _______   _______ _______ __    _ _______ _______ ______   __    _ ___ __    _ _______ \n|  | |  |       |       | |       |       |  |  | |       |       |    _ | |  |  | |   |  |  | |       |\n|  |_|  |    ___|_     _| |       |   _   |   |_| |       |    ___|   | || |   |_| |   |   |_| |    ___|\n|       |   |___  |   |   |       |  | |  |       |       |   |___|   |_||_|       |   |       |   | __\n|_     _|    ___| |   |   |      _|  |_|  |  _    |      _|    ___|    __  |  _    |   |  _    |   ||  |\n  |   | |   |___  |   |   |     |_|       | | |   |     |_|   |___|   |  | | | |   |   | | |   |   |_| |\n  |___| |_______| |___|   |_______|_______|_|  |__|_______|_______|___|  |_|_|  |__|___|_|  |__|_______|\n   _______ ______  __   __ _______ __    _ _______ __   __ ______   _______ _______   _______ _______     \n  |   _   |      ||  | |  |       |  |  | |       |  | |  |    _ | |       |       | |       |       |\n  |  |_|  |  _    |  |_|  |    ___|   |_| |_     _|  | |  |   | || |    ___|  _____| |   _   |    ___|\n  |       | | |   |       |   |___|       | |   | |  |_|  |   |_||_|   |___| |_____  |  | |  |   |___\n  |       | |_|   |       |    ___|  _    | |   | |       |    __  |    ___|_____  | |  |_|  |    ___|\n  |   _   |       ||     ||   |___| | |   | |   | |       |   |  | |   |___ _____| | |       |   |\n  |__| |__|______|  |___| |_______|_|  |__| |___| |_______|___|  |_|_______|_______| |_______|___|\n	 ___   _ ___ _______ _______ ___   _______ __   __ _______   _______ _______ _______ \n	|   | | |   |       |       |   | |       |  | |  |       | |       |   _   |       |\n	|   |_| |   |    _  |    _  |   | |_     _|  |_|  |    ___| |       |  |_|  |_     _|\n	|      _|   |   |_| |   |_| |   |   |   | |       |   |___  |       |       | |   |\n	|     |_|   |    ___|    ___|   |   |   | |       |    ___| |      _|       | |   |\n	|    _  |   |   |   |   |   |   |   |   | |   _   |   |___  |     |_|   _   | |   |\n	|___| |_|___|___|   |___|   |___|   |___| |__| |__|_______| |_______|__| |__| |___|\n\n\n                                                   ^✦\n                                                  |||\n                                        ^----^    |||\n                                       (  •u• )   |||\n                                       |     |〵_|〵/|\n                                    _  | |   |〵__|_|\n                                    ||_!_|   〵 \n                                     ---|  T_ 〵\n                                        |  |_|_|\n                                        !_/     〵    ^\n                                   /〵  /         〵 / 〵\n                                  /  〵/           〵   〵\n\n                                          [ PLAY ]\n\n                                        [ CONTINUE ]\n\n                                          [ QUIT ]\n")
        start_input = input("[ Insert any command! ]\n")
        start_input = start_input.lower()
        while start_input not in start_options:
            start_input = input("[ Input not recognised. Please try again! ]\n")
            start_input = start_input.lower()
        if start_input == 'play':
            file_path = "kippi_save.txt"
            checkpoint_data = load_checkpoint(file_path)
            if checkpoint_data is not None:
                start_input = input("[ WARNING! You've been through an adventure in the past. Are you sure you'd like to overwrite your old save file? ]\n")
                start_input = start_input.lower()
                while start_input not in yes_or_no:
                    start_input = input("[ Input not recognised. Please try again! ]\n")
                    start_input = start_input.lower()
                if start_input == 'yes':
                    player_name = None
                    kippi_stats = list(kippi_stats_dictionary.values())
                    inventory = []                
                    head = []
                    body = []
                    feet = []
                    hand = []
                    meanie_counter = 0
                    intro_screen = False
                    game_start = True
                    game_start = True
                    continue_game = False
                elif start_input == 'no':
                    continue
            else:
                intro_screen = False
                game_start = True
                continue_game = False
        if start_input == 'continue':
            file_path = "kippi_save.txt"
            checkpoint_data = load_checkpoint(file_path)
            if checkpoint_data is not None:
                player_name = checkpoint_data["player_name"]
                kippi_stats = checkpoint_data["kippi_stats"]
                inventory = checkpoint_data["inventory"]                
                head = checkpoint_data["head"]
                body = checkpoint_data["body"]
                feet = checkpoint_data["feet"]
                hand = checkpoint_data["hand"]
                meanie_counter = checkpoint_data["meanie_counter"]
                print(f"[Welcome back, {player_name}! You are at LEVEL {kippi_stats[0]}!]")
                intro_screen = False
                game_start = True
                continue_game = True
            else:
                print(f"[Uh oh, no save file found! Starting a new game...]")
                intro_screen = False
                game_start = True
                continue_game = False
        if start_input == 'quit':
            os._exit(os.EX_OK) #os code

    while game_start == True:
            #list ver.
            kippi_stats_perm = list(kippi_stats_dictionary.values())
            kippi_stats = list(kippi_stats_dictionary.values())
            
            #enemies
            #we use dictionaries for this! i was originally gonna use lists, but bruh, it's so hard to memorise which stat is which... so yeah!
            #ariana did all of this! thank you ariana <3
            
            #Enemies of Floresta Dictionary
            skunk_stats = {'NAME' : 'SKUNK', 'HP': 3, 'ATK': 2, 'DEF': 2, 'SPD' : 3, 'EXP GAIN' : 1}
            monkey_stats = {'NAME': 'MONKEY','HP': 4,'ATK': 2,'DEF': 2,'SPD': 2,'EXP GAIN': 2}
            raven_stats = {'NAME': 'RAVEN','HP': 2,'ATK': 3,'DEF': 1,'SPD': 4,'EXP GAIN': 3}
            rhino_stats = {'NAME': 'RHINO','HP': 20,'ATK': 15,'DEF': 10,'SPD': 5,'EXP GAIN': 10}

            #Enemies of Tundra Dictionary
            penguin_stats = {'NAME': 'PENGUIN','HP':25,'ATK':10,'DEF':15,'SPD':10,'EXP GAIN':3}
            seal_stats = {'NAME': 'SEAL','HP':15,'ATK':10,'DEF':25,'SPD':10,'EXP GAIN':3}
            wolf_stats = {'NAME': 'ARCTIC WOLF','HP':10,'ATK':20,'DEF':10,'SPD':20,'EXP GAIN':5}
            bear_stats = {'NAME': 'POLAR BEAR','HP':20,'ATK':20,'DEF':15,'SPD':5,'EXP GAIN':5}
            snowman_stats = {'NAME': 'SNOWMAN', 'HP':10,'ATK':15,'DEF':30,'SPD':5,'EXP GAIN':10}
            spirit_stats = {'NAME': 'SNOWSTORM SPIRIT','HP':100,'ATK':35,'DEF':25,'SPD':40,'EXP GAIN':30}
            bigfoot_stats = {'NAME': 'ELUSIVE BIGFOOT','HP':100,'ATK':45,'DEF':25,'SPD':30,'EXP GAIN':35}

            #Enemies of Sahara Dictionary
            lizard_stats = {'NAME': 'LIZARD','HP':55,'ATK':50,'DEF':30,'SPD':65,'EXP GAIN':10}
            snake_stats = {'NAME': 'SNAKE','HP':45,'ATK':60,'DEF':25,'SPD':70,'EXP GAIN':10}
            ostrich_stats = {'NAME': 'OSTRICH','HP':25,'ATK':65,'DEF':30,'SPD':80,'EXP GAIN':15}
            coyote_stats = {'NAME': 'COYOTE','HP':30,'ATK':70,'DEF':25,'SPD':75,'EXP GAIN':15}
            tortoise_stats = {'NAME': 'TORTOISE','HP':100,'ATK':30,'DEF':50,'SPD':20,'EXP GAIN':20}
            armadillo_stats = {'NAME': 'BROBDINGNAGIAN ARMADILLO','HP':130,'ATK':50,'DEF':40,'SPD':30,'EXP GAIN':50}
            cactus_stats = {'NAME': 'COLOSSAL CACTUS','HP':110,'ATK':60,'DEF':30,'SPD':50,'EXP GAIN':55}
            behemoth_stats = {'NAME': 'BEHEMOTH OF THE DUNES','HP':130,'ATK':75,'DEF':50,'SPD':45,'EXP GAIN':75}

            #Enemies of Volcana Dictionary
            lavablob_stats = {'NAME': 'UNASSUMMING BLOB OF LAVA','HP':25,'ATK':75,'DEF':50,'SPD':50,'EXP GAIN':20}
            skeleton_stats = {'NAME': 'SKELETON','HP':100,'ATK':75,'DEF':80,'SPD':45,'EXP GAIN':30}
            wraith_stats = {'NAME': 'SMOKEY WRAITH','HP':25,'ATK':95,'DEF':100,'SPD':80,'EXP GAIN':50}
            phoenix_stats = {'NAME': 'PHOENIX','HP':50,'ATK':85,'DEF':65,'SPD':100,'EXP GAIN':50}
            hellhound_stats = {'NAME': 'HELLHOUND','HP':80,'ATK':100,'DEF':50,'SPD':70,'EXP GAIN':50}
            golem_stats ={'NAME': 'MAGMA GOLEM','HP':100,'ATK':120,'DEF':80,'SPD':50,'EXP GAIN':100}
            zealous_stats = {'NAME': 'ZEALOUS','HP':150,'ATK':150,'DEF':100,'SPD':100,'EXP GAIN':1000}

            #True Ending's Enemies Dictionary
            wizard_stats = {'NAME': 'WIZARD OF PAWZ','HP':150,'ATK':150,'DEF':100,'SPD':100,'EXP GAIN':'0'}
            zealousx_stats = {'NAME': 'ZEALOUS, THE REAL ONE','HP':75,'ATK':200,'DEF':50,'SPD':100,'EXP GAIN':'0'}

            #amirah made the items, thanks amirah! <3

            #items
            common_items = ['BOWTIE', 'SUNGLASSES', 'STRAW HAT', 'STRIPED TIE', 'MISMATCHED SOCKS', 'TUTU', 'TRAFFIC CONE', 'POTATO SACK', 'HULA HOOP', 'COCONUT SHELL','JALAPENO', 'SWEET JAPANESE CURRY', 'ASAM LAKSA', 'COTTON CANDY','ICE CREAM', 'COFFEE', 'FIZZY SODA','RUSTY FORK', 'CROOKED BAT', 'SLIPPER', 'HANGER', 'WATER GUN', 'PLASTIC SHOVEL', 'JELLYFISH NET', 'ROLLING PIN', 'TICKLE FEATHER', 'SQUEAKY HAMMER', 'RAMEN BOWL', 'KIT KAT BAR', 'SLURPEE', 'POPCORN', 'SHAWARMA', 'SPOILED MILK', 'MUSHROOM', 'BURNT BROWNIE', 'MOULDY CHEESE', 'HAY', 'ELDERBERRIES', 'PUFFERFISH']
            uncommon_items = ['JESTER’S HAT', 'SPRING BOOTS', 'FISHBOWL', 'ORIGAMI HAT', 'SQUID HAT','CAPE', 'FLAMINGO FLOATIE', 'FEATHER BOAS', 'FRILLY APRON', 'PROPELLER HAT', 'YO-YO', 'DAGGER', 'BOOMERANG', 'NUNCHUCKS', 'RUBBER CHICKEN','FIRECRACKERS', 'GLITTER BOMB', 'HUNTING SPEAR', 'SLINGSHOT', 'BOUNCY BALL']
            rare_items = ['LUMINARA LENSES', 'AMULET OF THE INFERNAL BLAZE', 'CROWN OF THE FALLEN','ECLIPSE O’CLOCK CLOAK', 'SWIFTSHADOW BOOTS', 'DURIAN', 'JAWBREAKER CANDY', 'MATCHA COOKIES', 'SWORD OF THE MIGHTY', 'STARFALL CROSSBOW', 'RUMBLESTRIKE HAMMER', 'JESTER\'S JOKER CARDS', 'WAND OF A PHOENIX’S ASHES']

            #armour
            armour_common = ['BOWTIE', 'SUNGLASSES', 'STRAW HAT', 'STRIPED TIE', 'MISMATCHED SOCKS', 'TUTU', 'TRAFFIC CONE', 'POTATO SACK', 'HULA HOOP', 'COCONUT SHELL']
            armour_uncommon = ['JESTER’S HAT', 'SPRING BOOTS', 'FISHBOWL', 'ORIGAMI HAT', 'SQUID HAT','CAPE', 'FLAMINGO FLOATIE', 'FEATHER BOAS', 'FRILLY APRON', 'PROPELLER HAT']
            armour_rare = ['LUMINARA LENSES', 'AMULET OF THE INFERNAL BLAZE', 'CROWN OF THE FALLEN','ECLIPSE O’CLOCK CLOAK', 'SWIFTSHADOW BOOTS']

            #armour categories
            head_armour = ['TRAFFIC CONE','SUNGLASSES','STRAW HAT','COCONUT SHELL','SQUID HAT',"JESTER'S HAT",'PROPELLER HAT','ORIGAMI HAT','FISHBOWL','LUMINARA LENSES','CROWN OF THE FALLEN']
            body_armour = ['HULA HOOP','BOWTIE','STRIPED TIE','TUTU','POTATO SACK','FEATHER BOAS','CAPE','FRILLY APRON','FLAMINGO FLOATIE','AMULET OF THE INFERNAL BLAZE',"ECLIPSE O' CLOCK CLOAK"]
            feet_armour = ['MISMATCHED SOCKS','SPRING BOOTS','SWIFTSHADOW BOOTS']

            #consumables
            consumables_health = ['RAMEN BOWL', 'KIT KAT BAR', 'SLURPEE', 'POPCORN', 'SHAWARMA']
            consumables_boost_common = ['JALAPENO', 'SWEET JAPANESE CURRY', 'ASAM LAKSA', 'COTTON CANDY','ICE CREAM', 'COFFEE', 'FIZZY SODA']
            consumables_boost_rare = ['DURIAN', 'JAWBREAKER CANDY', 'MATCHA COOKIES']
            consumables_worsen = ['SPOILED MILK', 'MUSHROOM', 'BURNT BROWNIE', 'MOULDY CHEESE', 'HAY', 'ELDERBERRIES', 'PUFFERFISH']

            #weapons
            weapons_common = ['RUSTY FORK', 'CROOKED BAT', 'SLIPPER', 'HANGER', 'WATER GUN', 'PLASTIC SHOVEL', 'JELLYFISH NET', 'ROLLING PIN', 'TICKLE FEATHER', 'SQUEAKY HAMMER']
            weapons_uncommon = ['YO-YO', 'DAGGER', 'BOOMERANG', 'NUNCHUCKS', 'RUBBER CHICKEN','FIRECRACKERS', 'GLITTER BOMB', 'HUNTING SPEAR', 'SLINGSHOT', 'BOUNCY BALL']
            weapons_rare = ['SWORD OF THE MIGHTY', 'STARFALL CROSSBOW', 'RUMBLESTRIKE HAMMER', 'JESTER’S JOKER CARDS', 'WAND OF A PHOENIX’S ASHES']

            #items and their descriptions
            #armour_common
            item_1 = {'ITEM':'BOWTIE', 'DESCRIPTION':"A simple, black bowtie meant to be worn at formal occasions. Wear this and you'll instantly look like a refined gentleman!", 'ATK':0, 'DEF':3, 'SPD':0}
            item_2 = {'ITEM':'SUNGLASSES', 'DESCRIPTION':'Slip on these shadees and look cooler than Tundra!', 'ATK':0, 'DEF':3, 'SPD':0}
            item_3 = {'ITEM':'STRAW HAT', 'DESCRIPTION':"It's not just a hat; it's your head's BFF in the heat!", 'ATK':0, 'DEF':5, 'SPD':0}
            item_4 = {'ITEM':'STRIPED TIE', 'DESCRIPTION':"The zany zebra of neckwear, turning yourself into a mini fashion circus!", 'ATK':0, 'DEF':3, 'SPD':0}
            item_5 = {'ITEM':'MISMATCHED SOCKS','DESCRIPTION':"Step into the unknown with mismatched socks - because life's too short to match every step!", 'ATK':0, 'DEF':5, 'SPD':5}
            item_6 = {'ITEM':'TUTU', 'DESCRIPTON':"A pink, sparkly tutu that looks a little big on you. Who said that you couldn't look fabulous while saving the world.", 'ATK':0, 'DEF':5, 'SPD':5}
            item_7 = {'ITEM':'TRAFFIC CONE', 'DESCRIPTION': "Navigate the world with this traffic cone - safety always comes first!", 'ATK':10, 'DEF':15, 'SPD':0}
            item_8 = {'ITEM':'POTATO SACK', 'DESCRIPTION':"Wear this and feel like a spud-tacular potato!", 'ATK':0, 'DEF':10, 'SPD':0}
            item_9 = {'ITEM':'HULA HOOP', 'DESCRIPTION':"Turn your waist into a dance floor and let the wiggles begin!", 'ATK':5, 'DEF':3, 'SPD':0}
            item_10 = {'ITEM':'COCONUT SHELL', 'DESCRIPTION':"Nature's most durable helmet!", 'ATK':0, 'DEF':20, 'SPD':0}
            #armour_uncommon
            item_11 = {'ITEM':"JESTER'S HAT", 'DESCRIPTION':"Your ticket to certified silliness; turning you into a conductor of chuckles!", 'ATK':10, 'DEF':5, 'SPD':15}
            item_12 = {'ITEM':'SPRING BOOTS', 'DESCRIPTION':"Strap tiny trampolines to your soles and turn every step into a hop, a skip and a jump!", 'ATK':0, 'DEF':10, 'SPD':15}
            item_13 = {'ITEM':'FISHBOWL', 'DESCRIPTION':"A surprisingly durable fishbowl. Did the owner gave up on taking care of their beloved fishies?", 'ATK':0, 'DEF':30, 'SPD':0}
            item_14 = {'ITEM':'ORIGAMI HAT', 'DESCRIPTION':"Fold here... Fold there... Ah, look! An origami hat!", 'ATK':0, 'DEF':5, 'SPD':15}
            item_15 = {'ITEM':'SQUID HAT', 'DESCRIPTION':"This silly-looking hat probably belonged to a child that might've dropped it. You decided to 'borrow' it for a while because you think it looks funky on you.", 'ATK':5, 'DEF':15, 'SPD':10}
            item_16 = {'ITEM':'CAPE', 'DESCRIPTION':"Feel like a real superhero while wearing this!", 'ATK':15, 'DEF':5, 'SPD':20}
            item_17 = {'ITEM':'FLAMINGO FLOATIE', 'DESCRIPTION':"Lounge on an inflated throne that gracefully floats you through the waves!", 'ATK':0, 'DEF':15, 'SPD':5}
            item_18 = {'ITEM':'FEATHER BOAS', 'DESCRIPTION':"Wrap a fuzzy tornado of fabulousness around your neck... that tickles you! Teehee!", 'ATK':5, 'DEF':5, 'SPD':10}
            item_19 = {'ITEM':'FRILLY APRON', 'DESCRIPTION':"You aren't going to serve any master. The only thing you'll serve is serving punches to these beasts' faces!", 'ATK':25, 'DEF':10, 'SPD':25}
            item_20 = {'ITEM':'PROPELLER HAT', 'DESCRIPTION':"Attach a mini windmill on your noggin and you might be able to fly far, far away!", 'ATK':10, 'DEF':5, 'SPD':20}
            #armour_rare
            item_21 = {'ITEM':'LUMINARA LENSES', 'DESCRIPTION':"These goggles emit a sudden, intense flash of light, momentarily blinding nearby opponents and creating an opportunity for the wearer to avoid attacks.", 'ATK':0, 'DEF':0, 'SPD':75}
            item_22 = {'ITEM':'AMULET OF THE INFERNAL BLAZE', 'DESCRIPTION':"An amulet infused with volcanic energy, granting resistance to heat-based attacks.", 'ATK':75, 'DEF':0, 'SPD':0}
            item_23 = {'ITEM':'CROWN OF THE FALLEN', 'DESCRIPTION':"A black crown that looks rusted, made from the bones of dead animals. It projects an ethereal shield that absorbs and mitigates incoming damage.", 'ATK':100, 'DEF':0, 'SPD':0}
            item_24 = {'ITEM':"ECLIPSE O'CLOCK CLOAK", 'DESCRIPTION':"A sparkling cloak that is constantly flowing due to otherworldly means. It makes the wearer nearly invisible and impervious to detection for a short period of time.", 'ATK':0, 'DEF':25, 'SPD':50}
            item_25 = {'ITEM':'SWIFTSHADOW BOOTS', 'DESCRIPTION':"A pair of black boots, decorated with sharp studs and feathers of a raven. They enable the ability to move swiftly and dodge attacks with enhanced agility, just like a raven!", 'ATK':0, 'DEF':0, 'SPD':100}
            #consumables_health
            item_26 = {'ITEM':'RAMEN BOWL', 'DESCRIPTION':"Grab a bowl of instant noodles – because nothing says 'epic quest' like noodles in a cup", 'HP':30}
            item_27 = {'ITEM':'KIT KAT BAR', 'DESCRIPTION':"Unleash the power of the breakable Kit Kat. Snap, munch, conquer!", 'HP':10}
            item_28 = {'ITEM':'SLURPEE', 'DESCRIPTION':"A gulp of brain-freezing explosion that’ll take you to a whole other world!", 'HP':15}
            item_29 = {'ITEM':'POPCORN', 'DESCRIPTION':"Toss back buttery popcorn like confetti on your quest. Warning: May attract monsters with a serious case of snack envy.", 'HP':25}
            item_30 = {'ITEM':'SHAWARMA', 'DESCRIPTION':"Wrap up your hunger in a hug of a shawarma’s– the hero's choice for a savoury adventure break. Just don't let the monsters smell the garlic sauce!", 'HP':50}
            #consumables_boost_common
            item_31 = {'ITEM':'JALAPENO', 'DESCRIPTION':"Feels like you could breathe out fire with how hot it is! Ouch!", 'ATK':5, 'DEF':0, 'SPD':0}
            item_32 = {'ITEM':'SWEET JAPANESE CURRY', 'DESCRIPTION':"Take a bite of Japanese knock-off of India’s greatest dish!", 'ATK':15, 'DEF':0, 'SPD':0}
            item_33 = {'ITEM':'ASAM LAKSA', 'DESCRIPTION':"Slurp up the tangy delight of Asam Laksa – the perfect noodle soup that gives you an extra kick with its spice!", 'ATK':30, 'DEF':0, 'SPD':0}
            item_34 = {'ITEM':'COTTON CANDY', 'DESCRIPTION':"Make yourself feel like on cloud nine with how absurdly sweet these are!", 'ATK':0, 'DEF':15, 'SPD':0}
            item_35 = {'ITEM':'ICE CREAM', 'DESCRIPTION':"Careful, don’t get a brain-freeze!", 'ATK':0, 'DEF':30, 'SPD':0}
            item_36 = {'ITEM':'COFFEE', 'DESCRIPTION':"What are these magic beans that keeps you awake?", 'ATK':0, 'DEF':15, 'SPD':0}
            item_37 = {'ITEM':'FIZZY SODA', 'DESCRIPTION':"Forget plain old drinks; this is a party popper in a can!", 'ATK':0, 'DEF':30, 'SPD':0}
            #consumables_boost_rare
            item_38 = {'ITEM':'DURIAN', 'DESCRIPTION':"Mother Nature's best mistake, gone right with a mix of custardy goodness and chaotic sweetness! Just... ignore how it smells, though.", 'ATK':50, 'DEF':0, 'SPD':0}
            item_39 = {'ITEM':'JAWBREAKER CANDY', 'DESCRIPTION':"Challenge your taste buds with a jawbreaker – the timeless candy that lasts as long as your sweet cravings.", 'ATK':0, 'DEF':50, 'SPD':0}
            item_40 = {'ITEM':'MATCHA COOKIES', 'DESCRIPTION':"You feel like a teenage girl with a crazy sweet tooth while eating these... and they’re worth it!", 'ATK':0, 'DEF':0, 'SPD':50}
            #consumables_worsen
            item_41 = {'ITEM':'SPOILED MILK', 'DESCRIPTION':"I mean... It’s only been a day since it’s expiry date... So, it must be good enough to consume, right?", 'HP':10}
            item_42 = {'ITEM':'MUSHROOM', 'DESCRIPTION':"Maybe you’ll grow twice your size if you ate this? Or even gain a new life!?", 'HP':20}
            item_43 = {'ITEM':'BURNT BROWNIE', 'DESCRIPTION':"The chocolate disaster that went on a sunbathing spree in the oven... and forgot how to brown properly!", 'HP':5}
            item_44 = {'ITEM':'MOULDY CHEESE', 'DESCRIPTION':'''As your mom always told you, “Just cut off the mouldy parts!"''', 'HP':10}
            item_45 = {'ITEM':'HAY', 'DESCRIPTION':"Ever wondered what it’d be like to have a horse’s diet?", 'HP':15}
            item_46 = {'ITEM':'ELDERBERRIES', 'DESCRIPTION':"Looks like blueberries... Must be delicious!", 'HP':30}
            item_47 = {'ITEM':'PUFFERFISH', 'DESCRIPTION':"It’s a fish, and kitfolk like fish!", 'HP':50}
            #weapon_common
            item_48 = {'ITEM':'RUSTY FORK', 'DESCRIPTION':"Don’t judge a fork by its rust!", 'ATK':10}
            item_49 = {'ITEM':'CROOKED BAT', 'DESCRIPTION':"It’s crooked... ‘cause it had a history of beating the heck out of things!", 'ATK':10}
            item_50 = {'ITEM':'SLIPPER', 'DESCRIPTION':"Knock knock, who’s there? Asian mom’s deadliest weapon, that’s what!", 'ATK':10}
            item_51 = {'ITEM':'HANGER', 'DESCRIPTION':"Ah, such cheerful childhood memories!", 'ATK':10}
            item_52 = {'ITEM':'WATER GUN', 'DESCRIPTION':"Splish, splash, it’ll kick your a —", 'ATK':10}
            item_53 = {'ITEM':'PLASTIC SHOVEL', 'DESCRIPTION':"Remember not to dig straight down!", 'ATK':10}
            item_54 = {'ITEM':'JELLYFISH NET', 'DESCRIPTION':"Reminds you of a specific cartoon that features a sponge and a starfish...", 'ATK':10}
            item_55 = {'ITEM':'ROLLING PIN', 'DESCRIPTION':"When life gets messy, the rolling pin is here to flatten the absurdity out of it!", 'ATK':10}
            item_56 = {'ITEM':'TICKLE FEATHER', 'DESCRIPTION':"“Perhaps they’ll die if I tickle them to death?” ...is what you probably thought when you rationally decided to use this as a weapon.", 'ATK':10}
            item_57 = {'ITEM':'SQUEAKY HAMMER', 'DESCRIPTION':"Squeak, squeak!", 'ATK':10}
            #weapon_uncommon
            item_58 = {'ITEM':'YO-YO', 'DESCRIPTION':"Unleash its spinning fury and watch as it entangles foes in a web of whimsy!", 'ATK':30}
            item_59 = {'ITEM':'DAGGER', 'DESCRIPTION':"A silent menace in the hands of a skilled rogue!", 'ATK':30}
            item_60 = {'ITEM':'BOOMERANG', 'DESCRIPTION':"Throw it, duck and brace yourself for its unexpected return!", 'ATK':30}
            item_61 = {'ITEM':'NUNCHUCKS', 'DESCRIPTION':"Use this to defeat your enemies... and be qualified to become the next karate kid!", 'ATK':30}
            item_62 = {'ITEM':'RUBBER CHICKEN', 'DESCRIPTION':"No — This isn’t the edible kind!", 'ATK':30}
            item_63 = {'ITEM':'FIRECRACKERS', 'DESCRIPTION':"Hmm… must be New Year’s leftovers. Might as well put some festive into the battles!", 'ATK':30}
            item_64 = {'ITEM':'GLITTER BOMB', 'DESCRIPTION':"Every battle needs a sparkling finish!", 'ATK':30}
            item_65 = {'ITEM':'HUNTING SPEAR', 'DESCRIPTION':"History’s very first “point and poke” device!", 'ATK':30}
            item_66 = {'ITEM':'SLINGSHOT', 'DESCRIPTION':"Now… Where do I find some rocks to make use of this?", 'ATK':30}
            item_67 = {'ITEM':'BOUNCY BALL', 'DESCRIPTION':"Bounce! Bounce! Bounce!", 'ATK':30}
            #weapon_rare
            item_68 = {'ITEM':'SWORD OF THE MIGHTY', 'DESCRIPTION':"A powerful, finely crafted blade, made from tungsten that was harvested from the underground caves of Tundra. It bestows unparalleled strength upon its chosen wielder.", 'ATK':100}
            item_69 = {'ITEM':'STARFALL CROSSBOW', 'DESCRIPTION':"This crossbow glows a slight blue, with its arrows resembling shooting stars that fall from sky at night. Make a wish for your enemies to be obliterated, and your arrows shall do it for you.", 'ATK':100}
            item_70 = {'ITEM':'RUMBLESTRIKE HAMMER', 'DESCRIPTION':"A hammer made from the unbreakable boulders of Sahara. It sends shockwaves through the earth with every forceful impact, creating quakes that resonate with its wielder's might.", 'ATK':100}
            item_71 = {'ITEM':"JESTER'S JOKER CARDS", 'DESCRIPTION':"Throwing cards that deal damage upon impact and release blinding confetti, adding a more whimsical touch to an already chaotic battle!", 'ATK':100}
            item_72 = {'ITEM':'PHOENIX WAND', 'DESCRIPTION':"This wand, crafted from the bones and feathers of a perished phoenix, possesses ethereal magic that redirects incoming attacks.", 'ATK':100}

            #armour_common
            item_1 = list(item_1.values())
            item_2 = list(item_2.values())
            item_3 = list(item_3.values())
            item_4 = list(item_4.values())
            item_5 = list(item_5.values())
            item_6 = list(item_6.values())
            item_7 = list(item_7.values())
            item_8 = list(item_8.values())
            item_9 = list(item_9.values())
            item_10 = list(item_10.values())
            #armour_uncommon
            item_11 = list(item_11.values())
            item_12 = list(item_12.values())
            item_13 = list(item_13.values())
            item_14 = list(item_14.values())
            item_15 = list(item_15.values())
            item_16 = list(item_16.values())
            item_17 = list(item_17.values())
            item_18 = list(item_18.values())
            item_19 = list(item_19.values())
            item_20 = list(item_20.values())
            #armour_rare
            item_21 = list(item_21.values())
            item_22 = list(item_22.values())
            item_23 = list(item_23.values())
            item_24 = list(item_24.values())
            item_25 = list(item_25.values())
            #consumables_health
            item_26 = list(item_26.values())
            item_27 = list(item_27.values())
            item_28 = list(item_28.values())
            item_29 = list(item_29.values())
            item_30 = list(item_30.values())
            #consumables_boost_common
            item_31 = list(item_31.values())
            item_32 = list(item_32.values())
            item_33 = list(item_33.values())
            item_34 = list(item_34.values())
            item_35 = list(item_35.values())
            item_36 = list(item_36.values())
            item_37 = list(item_37.values())
            #consumables_boost_rare
            item_38 = list(item_38.values())
            item_39 = list(item_39.values())
            item_40 = list(item_40.values())
            #consumables_worsen
            item_41 = list(item_41.values())
            item_42 = list(item_42.values())
            item_43 = list(item_43.values())
            item_44 = list(item_44.values())
            item_45 = list(item_45.values())
            item_46 = list(item_46.values())
            item_47 = list(item_47.values())
            #weapon_common
            item_48 = list(item_48.values())
            item_49 = list(item_49.values())
            item_50 = list(item_50.values())
            item_51 = list(item_51.values())
            item_52 = list(item_52.values())
            item_53 = list(item_53.values())
            item_54 = list(item_54.values())
            item_55 = list(item_55.values())
            item_56 = list(item_56.values())
            item_57 = list(item_57.values())
            #weapon_uncommon
            item_58 = list(item_58.values())
            item_59 = list(item_59.values())
            item_60 = list(item_60.values())
            item_61 = list(item_61.values())
            item_62 = list(item_62.values())
            item_63 = list(item_63.values())
            item_64 = list(item_64.values())
            item_65 = list(item_65.values())
            item_66 = list(item_66.values())
            item_67 = list(item_67.values())
            #weapon_rare
            item_68 = list(item_68.values())
            item_69 = list(item_69.values())
            item_70 = list(item_70.values())
            item_71 = list(item_71.values())
            item_72 = list(item_72.values())
            
            #list of lists (lol)
            inventory = []
            head = []
            body = []
            feet = []
            hand = []
            old_head_armour_stats = [0,0,0]
            old_body_armour_stats = [0,0,0]
            old_feet_armour_stats = [0,0,0]
            old_weapon_stats = [0]
            status_condition = ['BURNING', 'PARALYZED', 'FROZEN', 'INTOXICATED', 'POISONED']
            meanie_counter = 0

            #list of defines
            #we use 'define' whenever we want to re-use similar code, saves time! it also makes the code neater, which is god's gift to my eyes and my awful comprehension skills

            def level_up_checkpoint():
                file_path = "kippi_save.txt"
                file_path = os.path.abspath(file_path)

                with open(file_path, 'w') as kippi_save:
                    kippi_save.write(f"Player: {player_name}\n")
                    kippi_save.write(f"Stats: {kippi_stats}\n")
                    kippi_save.write(f"Inventory: {', '.join(inventory)}\n" if inventory else "Inventory: \n")
                    kippi_save.write(f"Head: {', '.join(head)}\n" if head else "Head: \n")
                    kippi_save.write(f"Body: {', '.join(body)}\n" if body else "Body: \n")
                    kippi_save.write(f"Feet: {', '.join(feet)}\n" if feet else "Feet: \n")
                    kippi_save.write(f"Hand: {', '.join(hand)}\n" if hand else "Hand: \n")
                    kippi_save.write(f"Meanie Points: {meanie_counter}")
            
            def level_up_mechanic():
                level_up_print = True
                while kippi_stats[1] >= kippi_stats[2]:
                    if level_up_print == True:
                        print("[ You feel somehow stronger! ]")
                        level_up_print = False
                    kippi_stats_perm[0] += 1 #level up
                    kippi_stats_perm[1] = kippi_stats[1] - kippi_stats[2] #experience points goes over to the next level
                    kippi_stats_perm[2] += 1 #amount of experience points to level up gets higher
                    kippi_stats_perm[3] += 2
                    kippi_stats_perm[4] += 1
                    kippi_stats_perm[5] += 1
                    kippi_stats_perm[6] += 1
                    kippi_stats[0] = kippi_stats_perm[0]
                    kippi_stats[1] = kippi_stats_perm[1]
                    kippi_stats[2] = kippi_stats_perm[2]
                    kippi_stats[3] = kippi_stats_perm[3]
                    kippi_stats[4] = kippi_stats_perm[4]
                    kippi_stats[5] = kippi_stats_perm[5]
                    kippi_stats[6] = kippi_stats_perm[6]
                    level_up_checkpoint()

            def wear_armour(item,inspect_items):
                if item in head_armour:
                    new_head_armour_stats = inspect_items
                elif item in body_armour:
                    new_body_armour_stats = inspect_items
                elif item in feet_armour:
                    new_feet_armour_stats = inspect_items
                elif item in weapons_common or item in weapons_uncommon or item in weapons_rare:
                    new_weapon_stats = inspect_items
                
                if item in head_armour:
                    if len(head) == 1:
                        print(f'[ {player_name} is already wearing something on his tiny head! ]')
                        decision = input(f'[ Do you want to throw away the {head[0]} and wear the {item}? ]')
                        if decision.lower() == 'yes':
                            print(f'[ {player_name} throws away the {head[0]} and wears the {item} on their tiny head! ]')
                            inventory.remove(inspect_items[0])
                            kippi_stats_perm[4] -= old_head_armour_stats[0]
                            kippi_stats_perm[5] -= old_head_armour_stats[1]
                            kippi_stats_perm[6] -= old_head_armour_stats[2]
                            kippi_stats_perm[4] += new_head_armour_stats[2]
                            kippi_stats_perm[5] += new_head_armour_stats[3]
                            kippi_stats_perm[6] += new_head_armour_stats[4]
                            old_head_armour_stats[0] = new_head_armour_stats[2]
                            old_head_armour_stats[1] = new_head_armour_stats[3]
                            old_head_armour_stats[2] = new_head_armour_stats[4]
                            head[0] = item
                        else:
                            print(f'[ {player_name} decides to leave the {item} alone. ]')
                    if not head:
                        head.append(item)
                        print(f'[ {player_name} is now wearing a {item} on their tiny head! ]')
                        inventory.remove(inspect_items[0])
                        kippi_stats_perm[4] += new_head_armour_stats[2]
                        kippi_stats_perm[5] += new_head_armour_stats[3]
                        kippi_stats_perm[6] += new_head_armour_stats[4]
                        old_head_armour_stats[0] = new_head_armour_stats[2]
                        old_head_armour_stats[1] = new_head_armour_stats[3]
                        old_head_armour_stats[2] = new_head_armour_stats[4]
                
                elif item in body_armour:
                    if len(body) == 1:
                        print(f'[ {player_name} is already wearing something on his fluffy body! ]')
                        decision = input(f'[ Do you want to throw away the {body[0]} and wear the {item}? ]')
                        if decision.lower() == 'yes':
                            print(f'[ {player_name} throws away the {body[0]} and wears the {item} on their fluffy body! ]')
                            inventory.remove(inspect_items[0])
                            kippi_stats_perm[4] -= old_body_armour_stats[0]
                            kippi_stats_perm[5] -= old_body_armour_stats[1]
                            kippi_stats_perm[6] -= old_body_armour_stats[2]
                            kippi_stats_perm[4] += new_body_armour_stats[2]
                            kippi_stats_perm[5] += new_body_armour_stats[3]
                            kippi_stats_perm[6] += new_body_armour_stats[4]
                            old_body_armour_stats[0] = new_body_armour_stats[2]
                            old_body_armour_stats[1] = new_body_armour_stats[3]
                            old_body_armour_stats[2] = new_body_armour_stats[4]
                            body[0] = item
                        else:
                            print(f'[ {player_name} decides to leave the {item} alone. ]')
                    if not body:
                        body.append(item)
                        print(f'[ {player_name} is now wearing a {item} on his tiny head! ]')
                        inventory.remove(inspect_items[0])
                        kippi_stats_perm[4] += new_body_armour_stats[2]
                        kippi_stats_perm[5] += new_body_armour_stats[3]
                        kippi_stats_perm[6] += new_body_armour_stats[4]
                        old_body_armour_stats[0] = new_body_armour_stats[2]
                        old_body_armour_stats[1] = new_body_armour_stats[3]
                        old_body_armour_stats[2] = new_body_armour_stats[4]

                elif item in feet_armour:
                    if len(feet) == 1:
                        print(f'[ {player_name} is now wearing a pair of {item} on their tiny feet! ]')
                        decision = input(f'[ Do you want to throw away the {feet[0]} and wear the {item}? ]')
                        if decision.lower() == 'yes':
                            print(f'[ {player_name} throws away the {feet[0]} and wears the {item} on their fluffy body! ]')
                            inventory.remove(inspect_items[0])
                            kippi_stats_perm[4] -= old_feet_armour_stats[0]
                            kippi_stats_perm[5] -= old_feet_armour_stats[1]
                            kippi_stats_perm[6] -= old_feet_armour_stats[2]
                            kippi_stats_perm[4] += new_feet_armour_stats[2]
                            kippi_stats_perm[5] += new_feet_armour_stats[3]
                            kippi_stats_perm[6] += new_feet_armour_stats[4]
                            old_feet_armour_stats[0] = new_feet_armour_stats[2]
                            old_feet_armour_stats[1] = new_feet_armour_stats[3]
                            old_feet_armour_stats[2] = new_feet_armour_stats[4]
                            feet[0] = item
                        else:
                            print(f'[ {player_name} decides to leave the {item} alone. ]')
                    if not feet:
                        feet.append(item)
                        print(f'[ {player_name} is now wearing a pair of {item} on their tiny feet! ]')
                        inventory.remove(inspect_items[0])
                        kippi_stats_perm[4] += new_feet_armour_stats[2]
                        kippi_stats_perm[5] += new_feet_armour_stats[3]
                        kippi_stats_perm[6] += new_feet_armour_stats[4]
                        old_feet_armour_stats[0] = new_feet_armour_stats[2]
                        old_feet_armour_stats[1] = new_feet_armour_stats[3]
                        old_feet_armour_stats[2] = new_feet_armour_stats[4]

                elif item in weapons_common or item in weapons_uncommon or item in weapons_rare:
                    if len(hand) == 1:
                        print(f'[ {player_name} is already brandishing a weapon! ]')
                        decision = input(f'[ Do you want to throw away the {hand[0]} and brandish the {item}? ]')
                        if decision.lower() == 'yes':
                            print(f'[ {player_name} throws away the {hand[0]} and brandishes the {item} proudly! ]')
                            inventory.remove(inspect_items[0])
                            kippi_stats_perm[4] -= old_weapon_stats[0]
                            kippi_stats_perm[4] += new_weapon_stats[2]
                            old_weapon_stats[0] = new_weapon_stats[2]
                            hand[0] = item
                        else:
                            print(f'[ {player_name} decides to leave the {item} alone. ]')
                    if not hand:
                        hand.append(item)
                        print(f'[ {player_name} is now brandishing a {item} as their weapon! ]')
                        inventory.remove(inspect_items[0])
                        kippi_stats_perm[4] += new_weapon_stats[2]
                        old_weapon_stats[0] = new_weapon_stats[2]

            def inventory_check():
                print("[ You decided to take a peek inside your bag... ]")
                if not inventory:
                    print("[ ...but you've got nothing inside! ]\n")
                else:
                    print("Your inventory contains:")
                    for index, item in enumerate(inventory, start=1):
                        print(f" {index}. {item}")
                    inspect_items = input("[ Would you like to INSPECT your items? ]\n")
                    inspect_items = inspect_items.lower()
                    while inspect_items not in yes_or_no:
                        inspect_items = input("[ Input not recognised. Please try again! ]\n")
                        inspect_items = inspect_items.lower()
                    if inspect_items == 'yes':
                        inspect_items = input("[ Which item would you like to INSPECT? ]\n")
                        inspect_items = inspect_items.upper()
                        while inspect_items not in inventory:
                            inspect_items = input("[ Input not recognised. Please try again! ] [ TIP: Type in the NAME of the ITEM you're trying to INSPECT! ]\n")
                            inspect_items = inspect_items.upper()
                        if inspect_items in inventory:
                            if inspect_items in armour_common or inspect_items in armour_uncommon or inspect_items in armour_rare:
                                if inspect_items == item_1[0]:
                                    inspect_items = item_1
                                elif inspect_items == item_2[0]:
                                    inspect_items = item_2
                                elif inspect_items == item_3[0]:
                                    inspect_items = item_3
                                elif inspect_items == item_4[0]:
                                    inspect_items = item_4
                                elif inspect_items == item_5[0]:
                                    inspect_items = item_5
                                elif inspect_items == item_6[0]:
                                    inspect_items = item_6
                                elif inspect_items == item_7[0]:
                                    inspect_items = item_7
                                elif inspect_items == item_8[0]:
                                    inspect_items = item_8
                                elif inspect_items == item_9[0]:
                                    inspect_items = item_9
                                elif inspect_items == item_10[0]:
                                    inspect_items = item_10
                                elif inspect_items == item_11[0]:
                                    inspect_items = item_11
                                elif inspect_items == item_12[0]:
                                    inspect_items = item_12
                                elif inspect_items == item_13[0]:
                                    inspect_items = item_13
                                elif inspect_items == item_14[0]:
                                    inspect_items = item_14
                                elif inspect_items == item_15[0]:
                                    inspect_items = item_15
                                elif inspect_items == item_16[0]:
                                    inspect_items = item_16
                                elif inspect_items == item_17[0]:
                                    inspect_items = item_17
                                elif inspect_items == item_18[0]:
                                    inspect_items = item_18
                                elif inspect_items == item_19[0]:
                                    inspect_items = item_19
                                elif inspect_items == item_20[0]:
                                    inspect_items = item_20
                                elif inspect_items == item_21[0]:
                                    inspect_items = item_21
                                elif inspect_items == item_22[0]:
                                    inspect_items = item_22
                                elif inspect_items == item_23[0]:
                                    inspect_items = item_23
                                elif inspect_items == item_24[0]:
                                    inspect_items = item_24
                                elif inspect_items == item_25[0]:
                                    inspect_items = item_25
                                print(f'[ {inspect_items[0]} ]')
                                print(f'[ {inspect_items[1]} ]\n')
                                print(f'[ ATK +{inspect_items[2]} ]')
                                print(f'[ DEF +{inspect_items[3]} ]')
                                print(f'[ SPD +{inspect_items[4]} ]\n')
                                wear_choice = input("[ Would you like to WEAR it? ]\n")
                                wear_choice = wear_choice.lower()
                                while wear_choice not in yes_or_no:
                                    wear_choice = input("[ Input not recognised. Please try again! ]\n")
                                    wear_choice = wear_choice.lower()
                                if wear_choice == 'yes':
                                    wear_armour(inspect_items[0],inspect_items)
                                    print("[ TIP: Your stats will only increase after you've LEVELED UP! ]\n")
                                elif wear_choice == 'no':
                                    delete_item = input(f"[ Would you like to THROW AWAY {inspect_items[0]}? ]\n")
                                    delete_item = delete_item.lower()
                                    while delete_item not in yes_or_no:
                                        delete_item = input("[ Input not recognised. Please try again! ]\n")
                                        delete_item = delete_item.lower()
                                    if delete_item == 'yes':
                                        inventory.remove(inspect_items[0])
                                        print(f"{inspect_items[0]} has been THROWN AWAY.")
                                    elif delete_item == 'no':
                                        pass
                            elif inspect_items in consumables_health:
                                if inspect_items == item_26[0]:
                                    inspect_items = item_26
                                elif inspect_items == item_27[0]:
                                    inspect_items = item_27
                                elif inspect_items == item_28[0]:
                                    inspect_items = item_28
                                elif inspect_items == item_29[0]:
                                    inspect_items = item_29
                                elif inspect_items == item_30[0]:
                                    inspect_items = item_30
                                print(f'[ {inspect_items[0]} ]')
                                print(f'[ {inspect_items[1]} ]')
                                eat_choice = input("[ Would you like to EAT it? ]\n")
                                eat_choice = eat_choice.lower()
                                while eat_choice not in yes_or_no:
                                    eat_choice = input("[ Input not recognised. Please try again! ]\n")
                                    eat_choice = eat_choice.lower()
                                if eat_choice == 'yes':
                                    inventory.remove(inspect_items[0])
                                    if kippi_stats[3] != kippi_stats_perm[3]:
                                        kippi_stats[3] += inspect_items[2]
                                        if kippi_stats[3] < kippi_stats_perm[3]:
                                            print(f"[ Yum, yum! {player_name}'s tummy is satisfied! ]")
                                            print(f"[ {player_name}'s health went up to {kippi_stats[3]}! ]")
                                        if kippi_stats[3] >= kippi_stats_perm[3]:
                                            kippi_stats[3] = kippi_stats_perm[3]
                                            print(f"[ {player_name} smiles as they munch on their {inspect_items[0]}! ]")
                                            print(f"[ {player_name} has fully recovered! ]")
                                    else:
                                        print(f"[ Gosh, {player_name} feels absolutely stuffed!  They only took a few bites of the {inspect_items[0]} before throwing it away! ]")
                                elif eat_choice == 'no':
                                    delete_item = input(f"[ Would you like to THROW AWAY {inspect_items[0]}? ]\n")
                                    delete_item = delete_item.lower()
                                    while delete_item not in yes_or_no:
                                        delete_item = input("[ Input not recognised. Please try again! ]\n")
                                        delete_item = delete_item.lower()
                                        if delete_item == 'yes':
                                            inventory.remove(inspect_items[0])
                                            print(f"{inspect_items[0]} has been THROWN AWAY.")
                                        elif delete_item == 'no':
                                            pass
                            elif inspect_items in consumables_boost_common or inspect_items in consumables_boost_rare:
                                if inspect_items == item_31[0]:
                                    inspect_items = item_31
                                elif inspect_items == item_32[0]:
                                    inspect_items = item_32
                                elif inspect_items == item_33[0]:
                                    inspect_items = item_33
                                elif inspect_items == item_34[0]:
                                    inspect_items = item_34
                                elif inspect_items == item_35[0]:
                                    inspect_items = item_35
                                elif inspect_items == item_36[0]:
                                    inspect_items = item_36
                                elif inspect_items == item_37[0]:
                                    inspect_items = item_37
                                elif inspect_items == item_38[0]:
                                    inspect_items = item_38
                                elif inspect_items == item_39[0]:
                                    inspect_items = item_39
                                elif inspect_items == item_40[0]:
                                    inspect_items = item_40
                                print(f'[ {inspect_items[0]} ]')
                                print(f'[ {inspect_items[1]} ]\n')
                                eat_choice = input("[ Would you like to EAT it? ]\n")
                                eat_choice = eat_choice.lower()
                                while eat_choice not in yes_or_no:
                                    eat_choice = input("[ Input not recognised. Please try again! ]\n")
                                    eat_choice = eat_choice.lower()
                                if eat_choice == 'yes':
                                    inventory.remove(inspect_items[0])
                                    print(f"[ {player_name} feels much stronger after eating the {inspect_items[0]}! ]")
                                    kippi_stats_perm[4] += inspect_items[2]
                                    kippi_stats_perm[5] += inspect_items[3]
                                    kippi_stats_perm[6] += inspect_items[4]
                                    print("[ TIP: Your stats will only increase after you've LEVELED UP! ]\n")
                                elif eat_choice == 'no':
                                    delete_item = input(f"[ Would you like to THROW AWAY {inspect_items[0]}? ]\n")
                                    delete_item = delete_item.lower()
                                    while delete_item not in yes_or_no:
                                        delete_item = input("[ Input not recognised. Please try again! ]\n")
                                        delete_item = delete_item.lower()
                                    if delete_item == 'yes':
                                        inventory.remove(inspect_items[0])
                                        print(f"{inspect_items[0]} has been THROWN AWAY.")
                                    elif delete_item == 'no':
                                        pass
                            elif inspect_items in consumables_worsen:
                                if inspect_items == item_41[0]:
                                    inspect_items = item_41
                                elif inspect_items == item_42[0]:
                                    inspect_items = item_42
                                elif inspect_items == item_43[0]:
                                    inspect_items = item_43
                                elif inspect_items == item_44[0]:
                                    inspect_items = item_44
                                elif inspect_items == item_45[0]:
                                    inspect_items = item_45
                                elif inspect_items == item_46[0]:
                                    inspect_items = item_46
                                elif inspect_items == item_47[0]:
                                    inspect_items = item_47
                                print(f'[ {inspect_items[0]} ]')
                                print(f'[ {inspect_items[1]} ]')
                                eat_choice = input("[ Would you like to EAT it? ]\n")
                                eat_choice = eat_choice.lower()
                                while eat_choice not in yes_or_no:
                                    eat_choice = input("[ Input not recognised. Please try again! ]\n")
                                    eat_choice = eat_choice.lower()
                                if eat_choice == 'yes':
                                    inventory.remove(inspect_items[0])
                                    kippi_stats[3] -= inspect_items[2]
                                    if kippi_stats[3] <= 0:
                                        print(f"[ Uh oh! {player_name} doesn't feel too good... ]")
                                        print("[ Quickly, eat something else before you faint! ]\n")
                                    if kippi_stats[3] > 0:
                                        print(f"[ Yuck! The {inspect_items[0]} does not taste great at all! ]")
                                        print(f"f[ {player_name}'s health went down to {kippi_stats[3]}! ]\n")
                                elif eat_choice == 'no':
                                    delete_item = input(f"[ Would you like to THROW AWAY {inspect_items[0]}? ]\n")
                                    delete_item = delete_item.lower()
                                    while delete_item not in yes_or_no:
                                        delete_item = input("[ Input not recognised. Please try again! ]\n")
                                        delete_item = delete_item.lower()
                                    if delete_item == 'yes':
                                        inventory.remove(inspect_items[0])
                                        print(f"{inspect_items[0]} has been THROWN AWAY.")
                                    elif delete_item == 'no':
                                        pass
                            elif inspect_items in weapons_common or inspect_items in weapons_uncommon or inspect_items in weapons_rare:
                                if inspect_items == item_48[0]:
                                    inspect_items = item_48
                                elif inspect_items == item_49[0]:
                                    inspect_items = item_49
                                elif inspect_items == item_50[0]:
                                    inspect_items = item_50
                                elif inspect_items == item_51[0]:
                                    inspect_items = item_51
                                elif inspect_items == item_52[0]:
                                    inspect_items = item_52
                                elif inspect_items == item_53[0]:
                                    inspect_items = item_53
                                elif inspect_items == item_54[0]:
                                    inspect_items = item_54
                                elif inspect_items == item_55[0]:
                                    inspect_items = item_55
                                elif inspect_items == item_56[0]:
                                    inspect_items = item_56
                                elif inspect_items == item_57[0]:
                                    inspect_items = item_57
                                elif inspect_items == item_58[0]:
                                    inspect_items = item_58
                                elif inspect_items == item_59[0]:
                                    inspect_items = item_59
                                elif inspect_items == item_60[0]:
                                    inspect_items = item_60
                                elif inspect_items == item_61[0]:
                                    inspect_items = item_61
                                elif inspect_items == item_62[0]:
                                    inspect_items = item_62
                                elif inspect_items == item_63[0]:
                                    inspect_items = item_63
                                elif inspect_items == item_64[0]:
                                    inspect_items = item_64
                                elif inspect_items == item_65[0]:
                                    inspect_items = item_65
                                elif inspect_items == item_66[0]:
                                    inspect_items = item_66
                                elif inspect_items == item_67[0]:
                                    inspect_items = item_67
                                elif inspect_items == item_68[0]:
                                    inspect_items = item_68
                                elif inspect_items == item_69[0]:
                                    inspect_items = item_69
                                elif inspect_items == item_70[0]:
                                    inspect_items = item_70
                                elif inspect_items == item_71[0]:
                                    inspect_items = item_71
                                print(f'[ {inspect_items[0]} ]')
                                print(f'[ {inspect_items[1]} ]\n')
                                print(f'[ ATK +{inspect_items[2]} ]\n')
                                wear_choice = input("[ Would you like to USE it? ]\n")
                                wear_choice = wear_choice.lower()
                                while wear_choice not in yes_or_no:
                                    wear_choice = input("[ Input not recognised. Please try again! ]\n")
                                    wear_choice = wear_choice.lower()
                                if wear_choice == 'yes':
                                    wear_armour(inspect_items[0],inspect_items)
                                    print("[ TIP: Your stats will only increase after you've LEVELED UP! ]\n")
                                elif wear_choice == 'no':
                                    delete_item = input(f"[ Would you like to THROW AWAY {inspect_items[0]}? ]\n")
                                    delete_item = delete_item.lower()
                                    while delete_item not in yes_or_no:
                                        delete_item = input("[ Input not recognised. Please try again! ]\n")
                                        delete_item = delete_item.lower()
                                    if delete_item == 'yes':
                                        inventory.remove(inspect_items[0])
                                        print(f"{inspect_items[0]} has been THROWN AWAY.")
                                    elif delete_item == 'no':
                                        pass
                    elif inspect_items == 'no':
                        pass

            def self_check():
                #kippi stats display
                print("[ STATS ]")
                print(f"LVL: {kippi_stats[0]}")
                print(f"HP: {kippi_stats[3]}/{kippi_stats_perm[3]}")
                print(f"ATK: {kippi_stats[4]}")
                print(f"DEF: {kippi_stats[5]}")
                print(f"SPD: {kippi_stats[6]}\n")
                if not head:
                    pass
                else:
                    print(f"[ {player_name} is wearing a {head[0]} on their head! ]")
                if not body:
                    pass
                else:
                    print(f"[ {player_name} is wearing a {body[0]} on their fluffy body! ]")
                if not feet:
                    pass
                else:
                    print(f"[ {player_name} is wearing {feet[0]} on their lil' feet! ]")
                if not hand:
                    pass
                else:
                    print(f"\n[ {player_name} is brandishing a {hand[0]} as their weapon! ]")
                #health check
                if kippi_stats[3] <= (kippi_stats_perm[3] / 3):
                    print(f"\n[ {player_name} is close to fainting...! ]\n")
                elif kippi_stats[3] <= (kippi_stats_perm[3] / 2):
                    print(f"\n[ {player_name} isn't doing so great... ]\n")
                else:
                    print(f"[ {player_name} is doing fine! ]\n")

            def item_drop_common(percentage):
                item_drop = random.randint(1,percentage)
                item = random.choice(common_items)
                if item_drop == 1: #item drop
                    print(f"[ A {item} was dropped! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                    if len(inventory) < 20:
                        inventory.append(item)
                    else:
                        print(f"But... Uh oh! Your backpack seems to be LOADED with too many knick-knacks! It seems like you'd have to bid goodbye to {item} then...")

            def item_drop_uncommon(percentage):
                item_drop = random.randint(1,percentage)
                item = random.choice(uncommon_items)
                if item_drop == 1: #item drop
                    print(f"[ A {item} was dropped! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                    if len(inventory) < 20:
                        inventory.append(item)
                    else:
                        print(f"But... Uh oh! Your backpack seems to be LOADED with too many knick-knacks! It seems like you'd have to bid goodbye to {item} then...")

            def item_drop_rare(percentage):
                item_drop = random.randint(1,percentage)
                item = random.choice(rare_items)
                if item_drop == 1: #item drop
                    print(f"[ A {item} was dropped! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                    if len(inventory) < 20:
                        inventory.append(item)
                    else:
                        print(f"But... Uh oh! Your backpack seems to be LOADED with too many knick-knacks! It seems like you'd have to bid goodbye to {item} then...")

            #status conditions
            def kippi_poisoned():
                print(f"[ {player_name} is {status_condition[4]}! ]")
                kippi_stats[3] -= 1
                print(f"[ {player_name}'s health went down to {kippi_stats[3]}! ]\n")

            def kippi_intoxicated():
                print(f"[ {player_name} is {status_condition[3]}! ]")
                kippi_stats[6] -= 20
                print(f"[ {player_name}'s speed went down to {kippi_stats[6]}! ]\n")

            def kippi_burned():
                print(f"[ {player_name} is {status_condition[0]}! ]")
                kippi_stats[3] -= 3
                print(f"[ {player_name}'s health went down to {kippi_stats[3]}! ]\n")
            
            def direction_mechanic():
                while deciding_direction == True :
                    direction_choice = input("[ What shall you do? ]\n[ WALK RIGHT ] [ WALK LEFT ] [ WALK FORWARD ] [ CHECK INVENTORY ] [ CHECK SELF ]\n")
                    direction_choice = direction_choice.lower()
                    while 'inventory' not in direction_choice and 'self' not in direction_choice and 'right' not in direction_choice and 'left' not in direction_choice and 'forward' not in direction_choice and not direction_choice == 'i' and not direction_choice == 's' and not direction_choice == 'r' and not direction_choice == 'l' and not direction_choice == 'f':
                            direction_choice = input("[ Uh... Your command seems to not be clear enough. Perhaps you could try again? ]\n")
                            direction_choice = direction_choice.lower()
                    if 'inventory' in direction_choice or direction_choice == 'i':
                        inventory_check()
                    elif 'self' in direction_choice or direction_choice == 's':
                        self_check()
                    elif 'right' in direction_choice or direction_choice == 'r':
                        break
                    elif 'left' in direction_choice or direction_choice == 'l':
                        break
                    elif 'forward' in direction_choice or direction_choice == 'f':
                        break
            def game_over_mechanic():
                global intro_screen
                global game_start
                print(f"[ {player_name} fainted! ]")
                print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                game_over = input("[ Would you like to try again? ]\n")
                game_over = game_over.lower()
                while game_over not in yes_or_no:
                    game_over = input("[ Input not recognised. Please try again! ]")
                    game_over = game_over.lower()
                if game_over == 'yes':
                    if os.path.exists("kippi_save.txt"):
                      os.remove("kippi_save.txt")
                    else:
                      pass
                    continue_game = False
                elif game_over == 'no':
                    game_start = False
                    intro_screen = True
                    if os.path.exists("kippi_save.txt"):
                      os.remove("kippi_save.txt")
                    else:
                      pass

            def wizard_emotes(mood):
                if mood == 'excited':
                    print("        ____\n       / .  〵\n 〵   /  o  _〵,       ____\n _   /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /         〵 〵    V  / /\n/_/|  ^ . ^   〵_〵     / /\n   ==   w     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /\n")
                elif mood == 'happy':
                    print("        ____\n       / .  〵\n 〵   /  o  _〵,       ____\n _   /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /         〵 〵    V  / /\n/_/|  o . o   〵_〵     / /\n   ==   w     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /\n")
                elif mood == 'deadpan':
                    print("        ____\n       / .  〵\n 〵   /  o  _〵,       ____\n _   /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /         〵 〵    V  / /\n/_/|  o . o   〵_〵     / /\n   ==   ^     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /\n")
                elif mood == 'angry' :
                    print("        ____\n       / .  〵\n      /  o  _〵,       ____\n     /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /         〵 〵    V  / /\n/_/|  ò . ó   〵_〵     / /\n   ==   ^     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /\n")
                elif mood == 'angrier' :
                    print("        ____\n       / .  〵\n      /  o  _〵,       ____\n     /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /         〵 〵    V  / /\n/_/|  ò . ó   〵_〵     / /\n   ==   o     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /\n")
                elif mood == 'sassy' :
                    print("        ____\n       / .  〵\n      /  o  _〵,       ____\n     /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /  -   ^  〵 〵    V  / /\n/_/|  - . -   〵_〵     / /\n   ==   `     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /\n")
                elif mood == 'sassier' :
                    print("          ____\n         / .  〵\n        /  o  _〵,       ____\n       /o . o 〵        /___.〵\n      /   o  . 〵       |   〵〵\n    _/_).___._(_〵     <^>  / /\n   / /  -   ^  〵 〵    V  / /\n  /_/|  - . -   〵_〵     / /\n     ==   `     ==       / /\n     _〵_....._/_______ / /\n    /  /〵   /〵       / /\n __|  |  |  /  |______/ /\n(  〵 | |> /   |     / /\n 〵 〵| 〵/    |    / /\n")
                elif mood == 'happier' :
                    print("          ____\n         / .  〵\n        /  o  _〵,       ____\n       /o . o 〵        /___.〵\n      /   o  . 〵       |   〵〵\n    _/_).___._(_〵     <^>  / /\n   / /         〵 〵    V  / /\n  /_/|  ^ . ^   〵_〵     / /\n     ==   w     ==       / /\n     _〵_....._/_______ / /\n    /  /〵   /〵       / /\n __|  |  |  /  |______/ /\n(  〵 | |> /   |     / /\n 〵 〵| 〵/    |    / /\n")
                elif mood == 'worried':
                    print("        ____\n       / .  〵\n      /  o  _〵,       ____\n     /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /  ,      〵 〵    V  / /\n/_/|  o . o U'〵_〵     / /\n   ==   ^     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /")
                elif mood == 'disappointed':
                    print("        ____\n       / .  〵\n      /  o  _〵,       ____\n     /o . o 〵        /___.〵\n    /   o  . 〵       |   〵〵\n  _/_).___._(_〵     <^>  / /\n / /         〵 〵    V  / /\n/_/|  u . u   〵_〵     / /\n   ==   ^     ==       / /\n   _〵_....._/_______ / /\n  /  /〵   /〵       / /\n |  |  |  /  |______/ /\n |  | |> /   |     / /\n |  | 〵/    |    / /")

            def traveller_emotes(mood):
                if mood == 'happy':
                    print("        _______\n  〵   /_____ _〵\n _    |______ __|_\n    (_______ _____)\n    / /        〵 〵\n   /_/|  ^ . ^  〵_〵\n      ==   w   ==\n       〵_ __ _/\n      / = 〵/ = 〵\n     |  |     |  |\n     |  |     |  |")
                elif mood == 'happier':
                    print("        _______\n  〵   /_____ _〵\n _    |______ __|_\n    (_______ _____)\n    / /        〵 〵\n   /_/|  ^ . ^  〵_〵\n      ==   o   ==\n       〵_ __ _/\n      / = 〵/ = 〵\n     |  |     |  |\n     |  |     |  |")
                elif mood == 'angry':
                    print("        _______\n       /_____ _〵\n      |______ __|_\n    (_______ _____)\n    / /        〵 〵\n   /_/|  o . o  〵_〵\n      ==  ___   ==\n       〵_ __ _/\n      / = 〵/ = 〵\n     |  |     |  |\n     |  |     |  |")
                elif mood == 'angrier':
                    print("        _______\n       /_____ _〵\n      |______ __|_\n    (_______ _____)\n    / /        〵 〵\n   /_/|  ò . ó  〵_〵\n      ==   -   ==\n       〵_ __ _/\n      / = 〵/ = 〵\n     |  |     |  |\n     |  |     |  |")
                elif mood == 'angriest':
                    print("        _______\n  〵   /_____ _〵\n _    |______ __|_\n    (_______ _____)\n    / /        〵 〵\n   /_/|  ò . ó  〵_〵\n      ==   O   ==\n       〵_ __ _/\n      / = 〵/ = 〵\n     |  |     |  |\n     |  |     |  |")

            def king_emotes(mood):
                if mood == 'rescued':
                    print("    WWWWWWWWW\n    |o o o o|\n   |__.___.__|\n  (______/____)\n / /  =   = 〵 〵\n/_/|  O . O  〵_〵\n   ==   O   ==\n    〵_ __ _/\n   / = 〵/ = 〵\n  |  |     |  |\n  |  |     |  |")
                elif mood == 'happy':
                    print("    WWWWWWWWW\n    |o o o o|\n   |__.___.__|\n  (______/____)\n / /  =   = 〵 〵\n/_/|  o . o  〵_〵\n   ==   w   ==\n    〵_ __ _/\n   / = 〵/ = 〵\n  |  |     |  |\n  |  |     |  |")
                elif mood == 'happier':
                    print("    WWWWWWWWW\n    |o o o o|\n   |__.___.__|\n  (______/____)\n / /  =   = 〵 〵\n/_/|  ^ . ^  〵_〵\n   ==   w   ==\n    〵_ __ _/\n   / = 〵/ = 〵\n  |  |     |  |\n  |  |     |  |")
                elif mood == 'possessed':
                    print("    WWWWWWWWW\n    |o o o o|\n   |__.___.__|\n  (______/____)\n / /  =   = 〵 〵\n/_/|  ●.●  〵_〵\n   ==  ---   ==\n    〵_ __ _/\n   / = 〵/ = 〵\n  |  |     |  |\n  |  |     |  |")
                    
            #don't ask me why i decided to add a character where their only intended purpose is to spew random armadillo facts
            #i just find it cute wheneever games include a character that's obsessed with one (1) particular subject and never shuts up about it
            def armadillo_facts_moment(fact):
                while fact <= 10 :
                    if fact == 1:
                        armadillo_fact = '''[ "Did you knowo dat Bwaziwian dwee-banded awmadiwwos wewe bewieved extinct untiw 1988? Since dan, do', weseawchews have found scattewed, smaww popuwations of dase cute wiw' cwittews. And what's mowe, animaws dat awe wwongwie bewieved extinct, such as da one I've mentioned just nowo, awe actuawwie cawwed Lazawus species! Isn't dat intewesting?" ]'''
                    elif fact == 2:
                        armadillo_fact = '''[ "Did you knowo dat Gwyptodonts wewe heaviwie awmowed, dinosauw-sized, eawwie mammaws? In 2016, scientists detewmined Gwyptodonts wewe a subfamiwie of awmadiwwos dat fiwst appeawed 35 miwwion yeaws ago! Deie became extinct awound da end of da wast ice age, whiwe daiw smawwew and mowe wightwie awmowed wewatives suwvived. Us kitfowk hunted dase two-ton animaws fow meat, do'. Deie dan cweated shewtews fwom da bonie cawapace. Isn't dat intewesting?" ]'''
                    elif fact == 3:
                        armadillo_fact = '''[ "Did you knowo dat as noctuwnaw animaws, awmadiwwos pewfowm most activities — fowaging, eating, buwwowoing, matim — at night? Duwim da daywight houws, daie spend up to 16 houws sweeping, usuawwie in buwwowos. Awmadiwwos wawewie shawe daiw buwwowos with odaw awmadiwwos, awthuff daie do shawe dam with towtoises, snakes, and even wats! When awake, awmadiwwos spend mowe time fowagim dan most mammaws. Onwie two mawsupiaws and gwound squiwwews spend mowe active time feeding! Isn't dat supew intewesting?" ]'''
                    elif fact == 4:
                        armadillo_fact = '''[ "Did you knowo dat awmadiwwos awe da onwie non-kitfowk animaws to spwead wepwosy, nowo cawwed Hansen's disease? Da bactewia dat causes da disease dwives due to da awmadiwwo's wowo bodie tempewatuwe. Reseawchews bewieve awmadiwwos acquiwed Hansen's disease fwom 15th-centuwie expwowews. Kitfowk contwact awmadiwwo-bowne Hansen's disease dwuff huntim dam ow eatim daiw meat. In some cases, kitfowk become infected fwom inhawim awmadiwwo fecaw spowes. I dink daie desewve it, to be honest. You shouwdn't eat awmadiwwos! Anyway, wasn't dat intewesting?" ]'''
                    elif fact == 5:
                        armadillo_fact = '''[ "Did you knowo dat awmadiwwos beim abwe to cuww up into tight bawws and woww awaie is actuawwie a common myth? None activewie choose to woww awaie fwom pwedatows, because day'we bwave! Da onwie awmadiwwos abwe to cuww into tight bawws awe two species bewongim to da Towypeutes genus. Dese awe commonwie knowon as da Bwaziwian and Soudawn dwee-banded awmadiwwos. Aww odaw awmadiwwo species have too manie pwates, makim dis wevew of fwexibiwitie impossibwe. Isn't dat supew intewesting?" ]'''
                    elif fact == 6:
                        armadillo_fact = '''[ "Did you knowo dat da pink faiwie awmadiwwo, knowon scientificawwie as 'Chwamyphowus twuncatus', is da smawwest awmadiwwo in da wowwd!? Named fow its pink awmow and size, it measuwes between 4 and 6 inches in wength and weighs about 3.5 ounces. In addition to da awmow on daiw back, daie have a vewticaw wump pwate used to backfiww buwwowos. Doesn't dat sound adowabwe!?" ]'''
                    elif fact == 7:
                        armadillo_fact = '''[ "Did you knowo dat da scweamim haiwie awmadiwwo, awso knowon scientificawwie as 'Chaetophwactus vewwewosus', has mowe dan awmow as a defense. Dat's because it's got a paiw of scweechim wungs! Anytime dis species pewceives a dweat, it emits extwemewie woud, awawm-wike vocawizations. Vewie scawy, ain't it?" ]'''
                    elif fact == 8:
                        armadillo_fact = '''[ "Did you knowo dat even do' awmadiwwos awweadie spend most of daiw wives sweeping, da pichi, awso scientificawwie knowon as 'Zaedyus pichiy', takes it a step fuwdaw bie hibewnatim evewie wintew! Aftew buiwdim up fat stowes and settwim dowon in a buwwowo, da pichi's bodie tempewatuwe dwops fwom 95 degwees to 58 degwees fahwenheit! Dese awmadiwwos awso entew daiwie states of towpow, a type of mini-hibewnation. Doesn't dat sound intewesting?" ]'''
                    elif fact == 9:
                        armadillo_fact = '''[ "Did you knowo dat awmadiwwo shewws awe used to make musicaw instwuments? Knowon as chawangos, dase 10-stwinged instwuments awe an integwaw pawt of twaditionaw Andean music. Whiwe daie wewe once commonwie made fwom an awmadiwwo's dwied sheww, contempowawie chawangos awe genewawwie made with wood ow sometimes cawabash gouwds. Not onwie dat, awmadiwwo shewws wewe awso used to make cawnivaw wattwes cawwed matwacas. In 2015, fowtunatewy, do', it became iwwegaw to owon ow seww new awmadiwwo matwacas! Whiwe I don't agwee with da poachim of awmadiwwos... At weast day'we used to make peopwe happy, I guess... Anyways, doesn't dat sound intewesting?" ]'''
                    elif fact == 10:
                        armadillo_fact = '''[ "Last but not weast, did you knowo dat awmadiwwos awe good swimmews and can howd daiw bweath fow 4 to 6 minutes!? Deie wawk undewwatew acwoss da bottom of stweams. When facim wawgew bodies of watew, daie guwp aiw to cweate buoyancie and dan dog paddwe. So cute!" ]'''
                    traveller_emotes('happier')
                    print(armadillo_fact)
                    dialogue_options = range(1,3)
                    for n in dialogue_options:
                        if n == 1:
                            print(f"{n}. [ Yep! ]")
                        if n == 2:
                            print(f"{n}. [ Yeah... ]\n")
                    dialogue_choice = input("[ What would you like to say to him? ]\n")
                    while dialogue_choice not in map(str, dialogue_options):
                        print('''[ "Uh... Guess we'we fwom diffewent pawts of Nyuwuwoviwwa, huh? 'Cause I can't seem to undewstand you..." ]''')
                        dialogue_choice = input("[ What would you like to say to him? ]\n")
                    if dialogue_choice == '1':
                        fact += 1
                    if dialogue_choice == '2':
                        fact = 11

            def player_attacks(kippi_attack,enemy_defense):
                print(f"[ {player_name} attacks the {enemy_stats[0]}! ]")
                if enemy_defense >= kippi_attack :
                    print(f"[ ...but the {enemy_stats[0]} didn't budge at all! ]\n")
                else:
                    enemy_stats[1] -= (kippi_attack - enemy_defense)
                    if enemy_stats[1] <= 0:
                        print(f"[ {enemy_stats[0]} fainted! ]")
                    else:
                        print(f"[ {enemy_stats[0]} health is down to {enemy_stats[1]} HP! ]\n")

            def enemy_attacks(kippi_defense,enemy_attack):
                print(f"[ The {enemy_stats[0]} attacks {player_name}! ]")
                if kippi_defense <= enemy_attack :
                    kippi_stats[3] -= (enemy_attack - kippi_defense)
                    if kippi_stats[3] <= 0:
                        print(f"[ {player_name} fainted! ]")
                    else:
                        print(f"[ {player_name}'s health is down to {kippi_stats[3]} HP! ] \n")
                else:
                    print(f"[ ...but {player_name} didn't budge at all! ]\n")

            def speed_check(kippi_speed,enemy_speed):
                random_chance = random.randint(1, 3)
                #kippi is faster than enemy
                if kippi_speed >= enemy_speed :
                    if random_chance == 1:
                        print(f"[ {player_name} manages to react first! ]\n")
                    elif random_chance == 2:
                        print(f"[ {player_name} gets the upper hand! ]\n")
                    else:
                        print(f"[ The swift lil' kitty legs of {player_name} acted on their own! ]\n")
                #enemy is faster than kippi
                if kippi_speed < enemy_speed :
                    if random_chance == 1:
                        print(f"[ {player_name} dissociated themselves from the situation for a second, and now they're being attacked! ]\n")
                    elif random_chance == 2:
                        print(f"[ {player_name} was blindsided by the enemy's swiftness! ]\n")
                    else:
                        print(f"[ {player_name} could not keep up with the enemy's actions in time! ]\n")
                    
            #skunk encounter
            def skunk_encounter():
                battle_mode = True
                signature_move_trigger = True
                poisoned_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(skunk_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than skunk
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||    〵         __/|\n  ||_!_|   |!   _  _c,     / __/\n   ---|  T |      |ó 〵___/ /\n      |  | |        〵      |\n      !__!_!         L/``〵_J")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                            break
                        if battle_input == 'fight':
                            if poisoned_check == True:
                                kippi_poisoned()
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                if poisoned_check == True:
                                    print(f"[ {player_name} doesn't feel ill anymore. Hooray! ]\n")
                                item_drop_common(50)
                                break
                            if signature_move_trigger == True:
                                skunk_moves = ['NOXIOUS SPRAY', 'SNEAKY POUNCE']
                                signature_move = random.choice(skunk_moves)
                                if signature_move == skunk_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {skunk_moves[0]}! ]")
                                    print(f"[ {player_name} feels lightheaded and... almost ill from smelling the disgusting aroma that was let out by the {enemy_stats[0]}! ]")
                                    poisoned_check = True
                                    if poisoned_check == True:
                                        kippi_poisoned()
                                    signature_move_trigger = False
                                    if kippi_stats[3] <= 0:
                                        break
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {skunk_moves[1]}! ]")
                                    print(f"[ {player_name} was heavily wounded! ]")
                                    kippi_stats[3] -= enemy_stats[2]*3
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    signature_move_trigger = False
                                    if kippi_stats[3] <= 0:
                                        break
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                    #skunk is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||    〵         __/|\n  ||_!_|   |!   _  _c,     / __/\n   ---|  T |      |ó 〵___/ /\n      |  | |        〵      |\n      !__!_!         L/``〵_J")
                        if signature_move_trigger == True:
                            skunk_moves = ['NOXIOUS SPRAY', 'NASTY POUNCE']
                            signature_move = random.choice(skunk_moves)
                            if signature_move == skunk_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {skunk_moves[0]}! ]")
                                print(f"[ {player_name} feels lightheaded and... almost ill from smelling the disgusting aroma that was let out by the {enemy_stats[0]}! ]")
                                poisoned_check = True
                                if poisoned_check == True:
                                    kippi_poisoned()
                                signature_move_trigger = False
                                if kippi_stats[3] <= 0:
                                    break
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {skunk_moves[1]}! ]")
                                print(f"[ {player_name} was heavily wounded! ]")
                                kippi_stats[3] -= enemy_stats[2]*3
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                signature_move_trigger = False
                                if kippi_stats[3] <= 0:
                                    break
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||    〵         __/|\n  ||_!_|   |!   _  _c,     / __/\n   ---|  T |      |ó 〵___/ /\n      |  | |        〵      |\n      !__!_!         L/``〵_J")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                            break
                        if battle_input == 'fight':
                            if poisoned_check == True:
                                kippi_poisoned()
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                if poisoned_check == True:
                                    print(f"[ {player_name} doesn't feel ill anymore. Hooray! ]\n")
                                item_drop_common(50)
                                break
                    break
                
            #monkey encounter
            def monkey_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                skip_turn = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(monkey_stats.values())                    
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than monkey
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"      ^----^\n     (  {face} )      〵\n     |     ||     _   ___\n  _  | |   ||       0(ò.ó)0\n  ||_!_|   |!     0===   ===0\n   ---|  T |         | _ |9\n      |  | |         || ||\n      !__!_!         CJ CJ")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                    random_chance = random.randint(1, 2)
                                    if random_chance == 1:
                                        item_drop_common(5)
                                    else:
                                        item_drop_uncommon(20)
                                    break
                                if signature_move_trigger == True:
                                    monkey_moves = ['BANANA... DISGUISED AS A GRENADE!?', 'ALLURING ACROBATICS']
                                    signature_move = random.choice(monkey_moves)
                                    if signature_move == monkey_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {monkey_moves[0]}! ]")
                                        print(f"[ Bits of a suspiciously large banana that was thrown in your direction went flying everywhere— and one particularly huge bit hit {player_name} directly into their eyeball! Ouch! ]")
                                        print(f"[ {player_name} was heavily wounded! ]")
                                        kippi_stats[3] -= enemy_stats[2]*5
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        signature_move_trigger = False
                                        if kippi_stats[3] <= 0:
                                            break
                                    else:
                                        if signature_move == monkey_moves[1]:
                                            print(f"[ {enemy_stats[0]} decided to use {monkey_moves[1]}! ]")
                                            print(f"[ {player_name} is distracted by the ever-so-graceful {monkey_moves[1]}'s moves! ]")
                                            print(f"[ {player_name}'s turn is skipped! ]")
                                            signature_move_trigger = False
                                            skip_turn = True     
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                            if kippi_stats[3] <= 0:
                                break
                    #monkey is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )      〵\n     |     ||     _   ___\n  _  | |   ||       0(ò.ó)0\n  ||_!_|   |!     0===   ===0\n   ---|  T |         | _ |9\n      |  | |         || ||\n      !__!_!         CJ CJ")
                        if signature_move_trigger == True:
                            monkey_moves = ['BANANA... DISGUISED AS A GRENADE!?', 'ALLURING ACROBATICS']
                            signature_move = random.choice(monkey_moves)
                            if signature_move == monkey_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {monkey_moves[0]}! ]")
                                print(f"[ Bits of a suspiciously large banana that was thrown in your direction went flying everywhere— and one particularly huge bit hit {player_name} directly into their eyeball! Ouch! ]")
                                print(f"[ {player_name} was heavily wounded! ]")
                                kippi_stats[3] -= enemy_stats[2]*5
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                signature_move_trigger = False
                                if kippi_stats[3] <= 0:
                                    break
                            else:
                                signature_move == monkey_moves[1]
                                print(f"[ {enemy_stats[0]} decided to use {monkey_moves[1]}! ]")
                                print(f"[ {player_name} is distracted by the ever-so-graceful {monkey_moves[1]}'s moves! ]")
                                print(f"[ {player_name}'s turn is skipped! ]\n")
                                skip_turn = True
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"      ^----^\n     (  {face} )      〵\n     |     ||     _   ___\n  _  | |   ||       0(ò.ó)0\n  ||_!_|   |!     0===   ===0\n   ---|  T |         | _ |9\n      |  | |         || ||\n      !__!_!         CJ CJ")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                    random_chance = random.randint(1, 2)
                                    if random_chance == 1:
                                        item_drop_common(5)
                                    else:
                                        item_drop_uncommon(20)
                                    break
                        else:
                            skip_turn = False
                    break

            #raven encounter
            def raven_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                skip_turn = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(raven_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than raven
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"      ^----^        〵     _\n     (  {face} )      _  _   / _〵 \n     |     ||        <ó〵/ /_\n  _  | |   ||         〵__ _/\n  ||_!_|   |!         ././\n   ---|  T |\n      |  | |\n      !__!_!")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                    random_chance = random.randint(1, 3)
                                    if random_chance == 1:
                                        item_drop_common(2)
                                    elif random_chance == 2:
                                        item_drop_uncommon(50)
                                    else:
                                        item_drop_rare(100)
                                    break
                                if signature_move_trigger == True:
                                    raven_moves = ["TALONS O' VOIDANCE", 'GALE OF GLOOMY FEATHERS']
                                    signature_move = random.choice(raven_moves)
                                    if signature_move == raven_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {raven_moves[0]}! ]")
                                        print(f"[ Ouch! {player_name} was heavily wounded! ]")
                                        kippi_stats[3] -= enemy_stats[2]*3
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        signature_move_trigger = False
                                        if kippi_stats[3] <= 0:
                                            break
                                    else:
                                        if signature_move == raven_moves[1]:
                                            print(f"[ {enemy_stats[0]} decided to use {raven_moves[1]}! ]")
                                            print(f"[ {player_name}'s turn is skipped! ]")
                                            signature_move_trigger = False
                                            skip_turn = True     
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                            if kippi_stats[3] <= 0:
                                break
                    #raven is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^        〵     _\n     (  {face} )      _  _   / _〵 \n     |     ||        <ó〵/ /_\n  _  | |   ||         〵__ _/\n  ||_!_|   |!         ././\n   ---|  T |\n      |  | |\n      !__!_!")
                        if signature_move_trigger == True:
                            raven_moves = ["TALONS O' VOIDANCE", 'GALE OF GLOOMY FEATHERS']
                            signature_move = random.choice(raven_moves)
                            if signature_move == raven_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {raven_moves[0]}! ]")
                                print(f"[ Ouch! {player_name} is heavily wounded! ]")
                                kippi_stats[3] -= enemy_stats[2]*3
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                signature_move_trigger = False
                                if kippi_stats[3] <= 0:
                                    break
                            else:
                                signature_move == raven_moves[1]
                                print(f"[ {enemy_stats[0]} decided to use {raven_moves[1]}! ]")
                                print(f"[ {player_name}'s turn is skipped! ]\n")
                                skip_turn = True
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"      ^----^        〵     _\n     (  {face} )      _  _   / _〵 \n     |     ||        <ó〵/ /_\n  _  | |   ||         〵__ _/\n  ||_!_|   |!         ././\n   ---|  T |\n      |  | |\n      !__!_!")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                random_chance = random.randint(1, 3)
                                if random_chance == 1:
                                    item_drop_common(2)
                                elif random_chance == 2:
                                    item_drop_uncommon(50)
                                else:
                                    item_drop_rare(100)
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                    break
                        else:
                            skip_turn = False
                    break
            #fixed
            #rhino encounter               
            def rhino_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                def_up_check = False
                paralyzed = False
                paralyzed_check = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(rhino_stats.values())                    
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than rhino
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if paralyzed == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                            ,-.             __\n                                          ,'   `---.___.---'  `.\n                                        ,'   ,-                 `-.___\n                                      ,'      /                       〵\n                                  , /        /                       〵〵\n                              )`._)>)        |                        〵〵\n                              `>,'    _      〵               /        | 〵\n      ^----^                    )       〵    |  |            |        |〵〵\n     (  {face} )           .   ,   /        〵   |   `.          |     | ) )\n     |     ||           〵`. 〵`-'          )-|      `.       〵      / ( (\n  _  | |   ||            〵 `-`   ó`     _/ ;〵 _    )`-.___.--〵    /   `'\n  ||_!_|   |!             `._         ,'    〵`j`.__/      〵  `.   〵\n   ---|  T |               / ,    ,'       _)〵  /`        _) ( 〵  /\n      |  | |               〵__  /        /nn_) (         /nn__〵) (\n      !__!_!                 `--'           /nn__〵             /nn__〵")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                if paralyzed_check == True:
                                    paralyzed_trigger = random.randint(1,2)
                                    if paralyzed_trigger == 1 :
                                        player_attacks(kippi_stats[4],enemy_stats[3])
                                        if enemy_stats[1] <= 0:
                                            print(f"[ {enemy_stats[0]} fainted! ]")
                                            print(f"[ {player_name} wins! ]\n")
                                            kippi_stats[1] += enemy_stats[5]
                                            print("     @%      @%         \n     `@%.  `;@%.      @@%;         \n      `@%%. `@%%    ;@@%;        \n       ;@%. :@%%  %@@%;       \n         %@bd%%%bd%%:;     \n          #@%%%%%:;;\n            %@@%::;\n            %@@(o);  . '         \n          %@@@;:(.,'         \n        `.. %@@@::;         \n           `)@o%::;         \n            %(o)::;        \n           .%@@%::;         \n           ;%@@%::;.          \n          ;%@@%%:;;;. \n     ...;%@@@%%:;;;;,. \n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(U'=w= )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                            break
                                    else:
                                            print(f"[ {player_name} is PARALYZED! The static in their body makes them unable to move a single inch! ]")
                                else:
                                    player_attacks(kippi_stats[4],enemy_stats[3])
                                    if enemy_stats[1] <= 0:
                                        print(f"[ {enemy_stats[0]} fainted! ]")
                                        print(f"[ {player_name} wins! ]\n")
                                        kippi_stats[1] += enemy_stats[5]
                                        break
                                stall_check = 0
                                if signature_move_trigger == True:
                                    rhino_moves = ['ELECTRIFYING CHARGE', 'ROCK-HARD SHIELD']
                                    signature_move = random.choice(rhino_moves)
                                    if signature_move == rhino_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {rhino_moves[0]}! ]")
                                        print(f"[ The {enemy_stats[0]} headbutted into {player_name}'s body... leaving them terribly PARALYZED! ]")
                                        paralyzed_check = True
                                        kippi_stats[4] -= 3
                                        print(f"[ {player_name}'s defenses went down to {kippi_stats[4]}! ] \n")
                                        signature_move_trigger = False
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {rhino_moves[1]}! ]")
                                        def_up_check = True
                                        turn_count = 0
                                        enemy_stats[3] += 5
                                        print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                        signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if def_up_check == True :
                                        turn_count += 1
                                        if turn_count == 3:
                                            enemy_stats[3] -= 5
                                            print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                    if kippi_stats[3] <= 0:
                                        break
                    #rhino is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        if paralyzed == False:
                            if signature_move_trigger == True:
                                rhino_moves = ['ELECTRIFYING CHARGE', 'ROCK-HARD SHIELD']
                                signature_move = random.choice(rhino_moves)
                                if signature_move == rhino_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {rhino_moves[0]}! ]")
                                        print(f"[ The {enemy_stats[0]} headbutted into {player_name}'s body... leaving them terribly PARALYZED! ]")
                                        paralyzed_check = True
                                        kippi_stats[4] -= 3
                                        print(f"[ {player_name}'s defenses went down to {kippi_stats[4]}! ] \n")
                                        signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {rhino_moves[1]}! ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 5
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 3:
                                        enemy_stats[3] -= 5
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                if kippi_stats[3] <= 0:
                                    break
                            if paralyzed == False:
                                print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                                face = random.randint(1,4)
                                if face == 1:
                                    face = '•w•'
                                elif face == 2:
                                    face = '•u•'
                                elif face == 3:
                                    face = '^W^'
                                else:
                                    face = '^u^'
                                print(f"                                            ,-.             __\n                                          ,'   `---.___.---'  `.\n                                        ,'   ,-                 `-.___\n                                      ,'      /                       〵\n                                  , /        /                       〵〵\n                              )`._)>)        |                        〵〵\n                              `>,'    _      〵               /        | 〵\n      ^----^                    )       〵    |  |            |        |〵〵\n     (  {face} )           .   ,   /        〵   |   `.          |     | ) )\n     |     ||           〵`. 〵`-'          )-|      `.       〵      / ( (\n  _  | |   ||            〵 `-`   ó`     _/ ;〵 _    )`-.___.--〵    /   `'\n  ||_!_|   |!             `._         ,'    〵`j`.__/      〵  `.   〵\n   ---|  T |               / ,    ,'       _)〵  /`        _) ( 〵  /\n      |  | |               〵__  /        /nn_) (         /nn__〵) (\n      !__!_!                 `--'           /nn__〵             /nn__〵")
                                battle_input = input(f"[ What will {player_name} do? ]\n")
                                battle_input = battle_input.lower()
                                while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                    battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                    battle_input = battle_input.lower()
                                if battle_input == 'items':
                                    inventory_check()
                                if battle_input == 'run':
                                    print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                                if battle_input == 'fight':
                                    if paralyzed_check == True:
                                        paralyzed_trigger = random.randint(1,2)
                                        if paralyzed_trigger == 1 :
                                            player_attacks(kippi_stats[4],enemy_stats[3])
                                            if enemy_stats[1] <= 0:
                                                print(f"[ {enemy_stats[0]} fainted! ]")
                                                print(f"[ {player_name} wins! ]\n")
                                                kippi_stats[1] += enemy_stats[5]
                                                break
                                        else:
                                            print(f"[ {player_name} is PARALYZED! The static in their body makes them unable to move a single inch! ]")
                                    else:
                                        player_attacks(kippi_stats[4],enemy_stats[3])
                                        if enemy_stats[1] <= 0:
                                            print(f"[ {enemy_stats[0]} fainted! ]")
                                            print(f"[ {player_name} wins! ]\n")
                                            kippi_stats[1] += enemy_stats[5]
                                            print("     @%      @%         \n     `@%.  `;@%.      @@%;         \n      `@%%. `@%%    ;@@%;        \n       ;@%. :@%%  %@@%;       \n         %@bd%%%bd%%:;     \n          #@%%%%%:;;\n            %@@%::;\n            %@@(o);  . '         \n          %@@@;:(.,'         \n        `.. %@@@::;         \n           `)@o%::;         \n            %(o)::;        \n           .%@@%::;         \n           ;%@@%::;.          \n          ;%@@%%:;;;. \n     ...;%@@@%%:;;;;,. \n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(U'=w= )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                                            break
                    break

            #penguin encounter
            def penguin_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                skip_turn = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(penguin_stats.values())                    
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than penguin
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"      ^----^\n     (  {face} )       〵\n     |     ||           __\n  _  | |   ||     -  -=(ó '.\n  ||_!_|   |!           '.-.〵\n   ---|  T |            /| 〵〵\n      |  | |            '|  | |\n      !__!_!            _〵_) :,_")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    item_drop_common(100)
                                    break
                                if signature_move_trigger == True:
                                    penguin_moves = ['SLUSHY SLIDE', 'PETRIFYING PECK']
                                    signature_move = random.choice(penguin_moves)
                                    if signature_move == penguin_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {penguin_moves[0]}! ]")
                                        print(f"[ {player_name} slips, trips and falls like a clumsy princess from {enemy_stats[0]}'s cheeky move! ]\n")
                                        kippi_stats[3] -= enemy_stats[2]*2
                                        kippi_stats[6] -= 5
                                        print(f"[ Oh no, {player_name}'s speed has reduced to {kippi_stats[6]}! ]")
                                        print(f"[ {player_name} got a concussion from falling onto the cold, hard ice! {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                        signature_move_trigger = False
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {penguin_moves[1]}! ]")
                                        kippi_stats[3] -= enemy_stats[2]*2
                                        print(f"[ Ouch! {player_name} was heavily wounded! ]")
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        print(f"[ {player_name}'s turn is skipped because {player_name} can't stop shivering! ]")
                                        signature_move_trigger = False
                                        skip_turn = True
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                            if kippi_stats[3] <= 0:
                                break
                    #penguin is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )       〵\n     |     ||           __\n  _  | |   ||     -  -=(ó '.\n  ||_!_|   |!           '.-.〵\n   ---|  T |            /| 〵〵\n      |  | |            '|  | |\n      !__!_!            _〵_) :,_")
                        if signature_move_trigger == True:
                            penguin_moves = ['SLUSHY SLIDE', 'PETRIFYING PECK']
                            signature_move = random.choice(penguin_moves)
                            if signature_move == penguin_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {penguin_moves[0]}! ]")
                                print(f"[ {player_name} slips, trips and falls like a clumsy princess from {enemy_stats[0]}'s cheeky move! ]\n")
                                kippi_stats[3] -= enemy_stats[2]*2
                                kippi_stats[6] -= 5
                                print(f"[ Oh no, {player_name}'s speed has reduced to {kippi_stats[6]}! ]")
                                print(f"[ {player_name} got a concussion from falling onto the cold, hard ice! {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                signature_move_trigger = False
                                if kippi_stats[3] <= 0:
                                    break
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {penguin_moves[1]}! ]")
                                kippi_stats[3] -= enemy_stats[2]*2
                                print(f"[ Ouch! {player_name} was heavily wounded! ]")
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                print(f"[ {player_name}'s turn is skipped because {player_name} can't stop shivering! ]")
                                skip_turn = True
                                signature_move_trigger = False
                                if kippi_stats[3] <= 0:
                                    break
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"      ^----^\n     (  {face} )       〵\n     |     ||           __\n  _  | |   ||     -  -=(ó '.\n  ||_!_|   |!           '.-.〵\n   ---|  T |            /| 〵〵\n      |  | |            '|  | |\n      !__!_!            _〵_) :,_")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    item_drop_common(100)
                                    break
                        else:
                            skip_turn = False
                    break

            #seal encounter                
            def seal_encounter():
                battle_mode = True
                signature_move_trigger = True
                def_up_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(seal_stats.values())                            
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than seal
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||     〵\n  _  | |   ||        o___C.\n  ||_!_|   |!    -   〵 ó=〵\n   ---|  T |           `-  〵_____\n      |  | |            |         〵\n      !__!_!          ./ /L._____, 〵\n                      '-'       /__/")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                item_drop_common(100)
                                break
                            if signature_move_trigger == True:
                                seal_moves = ['ABYSSAL BARK', "SHIELD O' GLACIERS"]
                                signature_move = random.choice(seal_moves)
                                if signature_move == seal_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {seal_moves[0]}! ]")
                                    print(f"[ {player_name}'s ears were blasted by the {enemy_stats[0]}'s monstrous bark!]")
                                    kippi_stats[5] -= 5
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s defence was reduced to {kippi_stats[5]}! ] \n")
                                    print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} used {seal_moves[1]}! ]")
                                    print(f"[ Ginormous glaciers erupted from the snow, and surrounds the {enemy_stats[0]}! Where did they come from!? ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 5
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 3:
                                        enemy_stats[3] -= 5
                                        print(f"[ The glaciers that were surrounding the {enemy_stats[0]}... have melted! ]")
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                if kippi_stats[3] <= 0:
                                    break
                    #seal is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||     〵\n  _  | |   ||        o___C.\n  ||_!_|   |!    -   〵 ó=〵\n   ---|  T |           `-  〵_____\n      |  | |            |         〵\n      !__!_!          ./ /L._____, 〵\n                      '-'       /__/")
                        if signature_move_trigger == True:
                                seal_moves = ['ABYSSAL BARK', "SHIELD O' GLACIERS"]
                                signature_move = random.choice(seal_moves)
                                if signature_move == seal_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {seal_moves[0]}! ]")
                                    print(f"[ {player_name}'s ears were blasted by the {enemy_stats[0]}'s monstrous bark!]")
                                    kippi_stats[5] -= 5
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s defence was reduced to {kippi_stats[5]}! ] \n")
                                    print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} used {seal_moves[1]}! ]")
                                    print(f"[ Ginormous glaciers erupted from the snow, and surrounds the {enemy_stats[0]}! Where did they come from!? ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 5
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if def_up_check == True :
                                def_counter += 1
                                if def_counter == 3:
                                    enemy_stats[3] -= 5
                                    print(f"[ The glaciers that were surrounding the {enemy_stats[0]}... have melted! ]")
                                    print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||     〵\n  _  | |   ||        o___C.\n  ||_!_|   |!    -   〵 ó=〵\n   ---|  T |           `-  〵_____\n      |  | |            |         〵\n      !__!_!          ./ /L._____, 〵\n                      '-'       /__/")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                item_drop_common(100)
                                break
                    break

            #wolf encounter
            def wolf_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                frozen_check = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(wolf_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than wolf
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f'''                   〵      ,\n                        ,,/( ,,,,,,,,,,___,,\n                  -     )       ,,,         "`,_,\n      ^----^          /( D   /                   `,\n     (  {face} )        L/7_/〵,|         /        〵\n     |     ||         ,`      `,  〵    ,|          〵\n  _  | |   ||          ,      /  /``````||      |〵, 〵__,)))\n  ||_!_|   |!                /  / |      〵〵   〵 〵,,,,,,/\n   ---|  T |                |  /  |       〵〵  )/\n      |  | |                〵 (|  )     ,,//   /\n      !__!_!                  `_)_/     ((___/"''')
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    item_drop_uncommon(20)
                                    break
                                if signature_move_trigger == True:
                                    wolf_moves = ['HOARFROST HOWL', 'MALEVOLENT MAUL']
                                    signature_move = random.choice(wolf_moves)
                                    if signature_move == wolf_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {wolf_moves[0]}! ]")
                                        print(f"[ A blast of cold air and snowflakes hit {player_name}'s body when the {enemy_stats[0]} howled! ]")
                                        print(f"[ {player_name} is frozen! ]\n")
                                        signature_move_trigger = False
                                        frozen_check = True
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {wolf_moves[1]}! ]")
                                        print(f"[ The {enemy_stats[0]}'s relentless bite has caused {player_name} to bleed profusely! ]")
                                        kippi_stats[3] -= int(enemy_stats[2]*1.5)
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                        signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if frozen_check == True:
                            for i in range(2):
                                print(f"[ {player_name} is still shivering! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                        break
                            frozen_check = False
                            print(f"[ {player_name} has gotten over the coldness! ]")
                    #wolf is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                   〵      ,\n                        ,,/( ,,,,,,,,,,___,,\n                  -     )       ,,,         "`,_,\n      ^----^          /( D   /                   `,\n     (  {face} )        L/7_/〵,|         /        〵\n     |     ||         ,`      `,  〵    ,|          〵\n  _  | |   ||          ,      /  /``````||      |〵, 〵__,)))\n  ||_!_|   |!                /  / |      〵〵   〵 〵,,,,,,/\n   ---|  T |                |  /  |       〵〵  )/\n      |  | |                〵 (|  )     ,,//   /\n      !__!_!                  `_)_/     ((___/"''')
                        if signature_move_trigger == True:
                            wolf_moves = ['HOARFROST HOWL', 'MALEVOLENT MAUL']
                            signature_move = random.choice(wolf_moves)
                            if signature_move == wolf_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {wolf_moves[0]}! ]")
                                print(f"[ A blast of cold air and snowflakes hit {player_name}'s body when the {enemy_stats[0]} howled! ]")
                                print(f"[ {player_name} is frozen! ]\n")
                                signature_move_trigger = False
                                frozen_check = True
                            else:
                                if signature_move == wolf_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {wolf_moves[1]}! ]")
                                    print(f"[ The {enemy_stats[0]}'s relentless bite has caused {player_name} to bleed profusely! ]")
                                    kippi_stats[3] -= int(enemy_stats[2]*1.5)
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f'''                   〵      ,\n                        ,,/( ,,,,,,,,,,___,,\n                  -     )       ,,,         "`,_,\n      ^----^          /( D   /                   `,\n     (  {face} )        L/7_/〵,|         /        〵\n     |     ||         ,`      `,  〵    ,|          〵\n  _  | |   ||          ,      /  /``````||      |〵, 〵__,)))\n  ||_!_|   |!                /  / |      〵〵   〵 〵,,,,,,/\n   ---|  T |                |  /  |       〵〵  )/\n      |  | |                〵 (|  )     ,,//   /\n      !__!_!                  `_)_/     ((___/"''')
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    item_drop_uncommon(20)
                                    break
                        if frozen_check == True:
                            for i in range(2):
                                print(f'''                   〵      ,\n                        ,,/( ,,,,,,,,,,___,,\n                  -     )       ,,,         "`,_,\n      ^----^          /( D   /                   `,\n     (U'>,< )        L/7_/〵,|         /        〵\n     |     ||         ,`      `,  〵    ,|          〵\n  _  | |   ||          ,      /  /``````||      |〵, 〵__,)))\n  ||_!_|   |!                /  / |      〵〵   〵 〵,,,,,,/\n   ---|  T |                |  /  |       〵〵  )/\n      |  | |                〵 (|  )     ,,//   /\n      !__!_!                  `_)_/     ((___/"''')
                                print(f"[ {player_name} is still shivering! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                        break
                            frozen_check = False
                            print(f"[ {player_name} has gotten over the coldness! ]")
                    break

            #polar bear encounter
            def bear_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                skip_turn = False
                frozen_check = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    random_chance = random.randint(1, 3)
                    #kippi is faster than bear
                    if kippi_stats[6] >= enemy_stats[4] :
                        if random_chance == 1:
                            print(f"[ {player_name} manages to react first! ]\n")
                        elif random_chance == 2:
                            print(f"[ {player_name} gets the upper hand! ]\n")
                        else:
                            print(f"[ The swift lil' kitty legs of {player_name} acted on their own! ]\n")
                    #bear is faster than kippi
                    if kippi_stats[6] < enemy_stats[4] :
                        if random_chance == 1:
                            print(f"[ {player_name} dissociated themselves from the situation for a second, and now they're being attacked! ]\n")
                        elif random_chance == 2:
                            print(f"[ {player_name} was blindsided by the enemy's swiftness! ]\n")
                        else:
                            print(f"[ {player_name} could not keep up with the enemy's actions in time! ]\n")
                    #kippi is faster than bear
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False or frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f'''                               _\n                              (〵〵 _                      ___\n                     〵      .-"`"(〵〵               _.""`   `"-.\n                            /      ` `-._        _.-"            `〵__\n                           a   a)        `-.__.-'                    `",\n                   _      /                                         `;-`\n                         /     .^                                    |\n                        ()    /  /`                                  |\n                         `---`"~``〵                                 |\n      ^----^                       〵                                |\n     (  {face} )                       〵          〵      /           /\n     |     ||                       /`,   ,      |     |           /\n  _  | |   ||                      /   "-.|      |     |         /'\n  ||_!_|   |!                     /     / |      /,__  |       /`〵\n   ---|  T |                     /    /'  |     /    `"'〵    (   〵\n      |  | |                  __/   /'    |    |        `〵    〵  〵\n      !__!_!                 (_(___/      |   |           `〵   〵__〵\n                                          /   〵           (_(___|\n                                         /     )\n                                        (_(_(__)''')
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    item_drop_uncommon(20)
                                    break
                                if signature_move_trigger == True:
                                    bear_moves = ['GRIZZLING GROWL', 'HYPERBOREAN HEADBUTT']
                                    signature_move = random.choice(bear_moves)
                                    if signature_move == bear_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {bear_moves[0]}! ]")
                                        print(f"[ The {enemy_stats[0]}'s terrifying growl made {player_name} petrified... they feel absolutely scared! ]")
                                        print(f"[ {player_name}'s turn is skipped! ]\n")
                                        signature_move_trigger = False
                                        skip_turn = True
                                    else:
                                        if signature_move == bear_moves[1]:
                                            print(f"[ {enemy_stats[0]} decided to use {bear_moves[1]}! ]")
                                            print(f"[ {enemy_stats[0]} charged head-first into {player_name}, causing them to break one or two bones in the process! ]\n")
                                            print(f"[ {player_name} is heavily wounded! ]")
                                            kippi_stats[3] -= int(enemy_stats[2]*1.5)
                                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                            print(f"[ {player_name} is frozen and unable to move! ]\n")
                                            signature_move_trigger = False
                                            frozen_check = True
                                            if kippi_stats[3] <= 0:
                                                break
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                        if frozen_check == True:
                            for i in range(2):
                                print(f'''                               _\n                              (〵〵 _                      ___\n                     〵      .-"`"(〵〵               _.""`   `"-.\n                            /      ` `-._        _.-"            `〵__\n                           a   a)        `-.__.-'                    `",\n                   _      /                                         `;-`\n                         /     .^                                    |\n                        ()    /  /`                                  |\n                         `---`"~``〵                                 |\n      ^----^                       〵                                |\n     (U'>.< )                       〵          〵      /           /\n     |     ||                       /`,   ,      |     |           /\n  _  | |   ||                      /   "-.|      |     |         /'\n  ||_!_|   |!                     /     / |      /,__  |       /`〵\n   ---|  T |                     /    /'  |     /    `"'〵    (   〵\n      |  | |                  __/   /'    |    |        `〵    〵  〵\n      !__!_!                 (_(___/      |   |           `〵   〵__〵\n                                          /   〵           (_(___|\n                                         /     )\n                                        (_(_(__)''')
                                print(f"[ {player_name} is still shivering! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                        break
                            frozen_check = False
                            print(f"[ {player_name} has gotten over the coldness! ]")
                    #bear is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                               _\n                              (〵〵 _                      ___\n                     〵      .-"`"(〵〵               _.""`   `"-.\n                            /      ` `-._        _.-"            `〵__\n                           a   a)        `-.__.-'                    `",\n                   _      /                                         `;-`\n                         /     .^                                    |\n                        ()    /  /`                                  |\n                         `---`"~``〵                                 |\n      ^----^                       〵                                |\n     (  {face} )                       〵          〵      /           /\n     |     ||                       /`,   ,      |     |           /\n  _  | |   ||                      /   "-.|      |     |         /'\n  ||_!_|   |!                     /     / |      /,__  |       /`〵\n   ---|  T |                     /    /'  |     /    `"'〵    (   〵\n      |  | |                  __/   /'    |    |        `〵    〵  〵\n      !__!_!                 (_(___/      |   |           `〵   〵__〵\n                                          /   〵           (_(___|\n                                         /     )\n                                        (_(_(__)''')
                        if signature_move_trigger == True:
                            bear_moves = ['GRIZZLING GROWL', 'HYPERBOREAN HEADBUTT']
                            signature_move = random.choice(bear_moves)
                            if signature_move == bear_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {bear_moves[0]}! ]")
                                print(f"[ The {enemy_stats[0]}'s terrifying growl made {player_name} petrified.. they feel absolutely scared! ]")
                                print(f"[ {player_name}'s turn is skipped! ]\n")
                                signature_move_trigger = False
                                skip_turn = True
                            else:
                                if signature_move == bear_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {bear_moves[1]}! ]")
                                    print(f"[ {enemy_stats[0]} charged head-first into {player_name}, causing them to break one or two bones in the process! ]\n")
                                    print(f"[ {player_name} is heavily wounded! ]")
                                    kippi_stats[3] -= int(enemy_stats[2]*1.5)
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                                    print(f"[ {player_name} is frozen and unable to move! ]\n")
                                    signature_move_trigger = False
                                    frozen_check = True
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False and frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f'''                               _\n                              (〵〵 _                      ___\n                     〵      .-"`"(〵〵               _.""`   `"-.\n                            /      ` `-._        _.-"            `〵__\n                           a   a)        `-.__.-'                    `",\n                   _      /                                         `;-`\n                         /     .^                                    |\n                        ()    /  /`                                  |\n                         `---`"~``〵                                 |\n      ^----^                       〵                                |\n     (U'>.< )                       〵          〵      /           /\n     |     ||                       /`,   ,      |     |           /\n  _  | |   ||                      /   "-.|      |     |         /'\n  ||_!_|   |!                     /     / |      /,__  |       /`〵\n   ---|  T |                     /    /'  |     /    `"'〵    (   〵\n      |  | |                  __/   /'    |    |        `〵    〵  〵\n      !__!_!                 (_(___/      |   |           `〵   〵__〵\n                                          /   〵           (_(___|\n                                         /     )\n                                        (_(_(__)''')
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    item_drop_uncommon(20)
                                    break
                        if skip_turn == True:
                            skip_turn = False
                        if frozen_check == True:
                            for i in range(2):
                                print(f'''                               _\n                              (〵〵 _                      ___\n                     〵      .-"`"(〵〵               _.""`   `"-.\n                            /      ` `-._        _.-"            `〵__\n                           a   a)        `-.__.-'                    `",\n                   _      /                                         `;-`\n                         /     .^                                    |\n                        ()    /  /`                                  |\n                         `---`"~``〵                                 |\n      ^----^                       〵                                |\n     (  {face} )                       〵          〵      /           /\n     |     ||                       /`,   ,      |     |           /\n  _  | |   ||                      /   "-.|      |     |         /'\n  ||_!_|   |!                     /     / |      /,__  |       /`〵\n   ---|  T |                     /    /'  |     /    `"'〵    (   〵\n      |  | |                  __/   /'    |    |        `〵    〵  〵\n      !__!_!                 (_(___/      |   |           `〵   〵__〵\n                                          /   〵           (_(___|\n                                         /     )\n                                        (_(_(__)''')
                                print(f"[ {player_name} is still shivering! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                        break
                            frozen_check = False
                            print(f"[ {player_name} has gotten over the coldness! ]")
                    break

            #snowman encounter                
            def snowman_encounter():
                battle_mode = True
                signature_move_trigger = True
                def_up_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(snowman_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than snowman
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                    〵         ,===.\n                   _          _|___|_\n                       __/    ".ò ó."     /__\n                        /`.   ; ._. ;   ,'〵\n      ^----^               `. .'=*=`. .'\n     (  {face} )                Y   *   Y\n     |     ||                 (  *  )\n  _  | |   ||                 .`---'.\n  ||_!_|   |!               .`   *   '.\n   ---|  T |                |    *    |\n      |  | |                (    *    )\n      !__!_!                 `._____.`''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print(" * `       *   `   *   `   *   *     *\n         `                  `         ` \n  `   *       *     *     `     *      `\n `     `        `      `      `    `\n   *     *          *      `    `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  =.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print(" * `       *   `   *   `   *   *     *\n         `                  `         ` \n  `   *       *     *     `     *      `\n `     `        `      `      `    `\n   *     *          *      `    `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  =.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                random_chance = random.randint(1, 3)
                                if random_chance == 1:
                                    item_drop_common(2)
                                elif random_chance == 2:
                                    item_drop_uncommon(20)
                                else:
                                    item_drop_rare(100)
                                break
                            if signature_move_trigger == True:
                                snowman_moves = ["BLAST O' SNOWBALLS", 'CRYSTALLIZE']
                                signature_move = random.choice(snowman_moves)
                                if signature_move == snowman_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {snowman_moves[0]}! ]")
                                    print(f"[ {player_name} was blasted by {enemy_stats[0]}'s attack!]")
                                    kippi_stats[3] -= enemy_stats[2]*3
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ] \n")
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {snowman_moves[1]}! ]")
                                    print(f"[ Looks like {enemy_stats[0]} has crystilallized its body! ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 30
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]\n")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 3:
                                        enemy_stats[3] -= 30
                                        print(f"[ The crystals that were covering the {enemy_stats[0]}... have melted! ]")
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                if kippi_stats[3] <= 0:
                                    break
                    #snowman is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        if signature_move_trigger == True:
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f'''                    〵         ,===.\n                   _          _|___|_\n                       __/    ".ò ó."     /__\n                        /`.   ; ._. ;   ,'〵\n      ^----^               `. .'=*=`. .'\n     (  {face} )                Y   *   Y\n     |     ||                 (  *  )\n  _  | |   ||                 .`---'.\n  ||_!_|   |!               .`   *   '.\n   ---|  T |                |    *    |\n      |  | |                (    *    )\n      !__!_!                 `._____.`''')
                            snowman_moves = ["BLAST O' SNOWBALLS", 'CRYSTALLIZE']
                            signature_move = random.choice(snowman_moves)
                            if signature_move == snowman_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {snowman_moves[0]}! ]")
                                print(f"[ {player_name} is blasted by {enemy_stats[0]} attack!]")
                                kippi_stats[3] -= enemy_stats[2]*3
                                kippi_stats[6] -= 10
                                print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ] \n")
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {snowman_moves[1]}! ]")
                                print(f"[ Looks like {enemy_stats[0]} has crystilallized its body! ]")
                                def_up_check = True
                                def_counter = 0
                                enemy_stats[3] += 30
                                print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]\n")
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if def_up_check == True :
                                def_counter += 1
                                if def_counter == 3:
                                    enemy_stats[3] -= 30
                                    print(f"[ The crystals that were covering the {enemy_stats[0]}... have melted! ]")
                                    print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                    〵         ,===.\n                   _          _|___|_\n                       __/    ".ò ó."     /__\n                        /`.   ; ._. ;   ,'〵\n      ^----^               `. .'=*=`. .'\n     (  {face} )                Y   *   Y\n     |     ||                 (  *  )\n  _  | |   ||                 .`---'.\n  ||_!_|   |!               .`   *   '.\n   ---|  T |                |    *    |\n      |  | |                (    *    )\n      !__!_!                 `._____.`''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print(" * `       *   `   *   `   *   *     *\n         `                  `         ` \n  `   *       *     *     `     *      `\n `     `        `      `      `    `\n   *     *          *      `    `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  =.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print(" * `       *   `   *   `   *   *     *\n         `                  `         ` \n  `   *       *     *     `     *      `\n `     `        `      `      `    `\n   *     *          *      `    `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  =.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                random_chance = random.randint(1, 3)
                                if random_chance == 1:
                                    item_drop_common(2)
                                elif random_chance == 2:
                                    item_drop_uncommon(20)
                                else:
                                    item_drop_rare(100)
                                break
                    break

            #snowstorm spirit encounter                
            def spirit_encounter():
                battle_mode = True
                signature_move_trigger = True
                def_up_check = False
                stall_check = 0
                hysteria_check = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(spirit_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than spirit
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                                          |\n                                       .*`|'*,\n                                      --- * ---\n                                       '*,|.*`\n                                          |\n\n                               .-"~.    ,;;;,    ,~"-.\n                              (     )  (  )( )  (     )\n                             ('      )();o,o*()(      `)\n                            (        ( ); v ;( )        )\n                            ('     ,( (;-`-'-;( ),     `)\n                             `(   (  )  ,   ,  (  )   )'\n                              `(     : :_,|._; :     )'\n                              ('     `---'*`---':    `)\n                              ('    /  /  |  〵 〵    `)\n      ^----^                 (     /  /   "   〵 〵     )\n     (  {face} )                `-..-'  //;      |〵 `-..-'\n     |     ||                        ))        ))\n  _  | |   ||                       (/         〵〵\n  ||_!_|   |!                       (*;~*:~*;~*;~*)\n   ---|  T |                       ('';〵' ``) ''〵'\n      |  | |\n      !__!_!''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if hysteria_check == True:
                                kippi_stats[3] -= 3
                                print(f"[ The voices in {player_name}'s head is slowly draining them of their sanity! ]")
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print(" * `       *   `   *   `   *     *\n         `                   `     ` \n  `   *       *     *      `  *     *    \n `     `        `      `      \n   *     *          *      `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (U'=.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            if signature_move_trigger == True:
                                spirit_moves = ['TEMPEST VEIL', 'WHISPERS OF HYSTERIA', 'PERMAFROST ARMOUR']
                                signature_move = random.choice(spirit_moves)
                                if signature_move == spirit_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {spirit_moves[0]}! ]")
                                    print(f'''[ "...How could thou be so blind towards your wrongdoings...?" {player_name} hears the {enemy_stats[0]} whisper. ]''')
                                    print(f"[ Veils of white smoke have surrounded the spirit... {player_name} can't see where she is! ]\n")
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                elif signature_move == spirit_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {spirit_moves[1]}! ]")
                                    print(f"[ {player_name} could hear something— someone...? Crying, creaming, and shouting endlessly in their head... It's turning them insane! ]")
                                    kippi_stats[3] -= 3
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    signature_move_trigger = False
                                    hysteria_check = True
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {spirit_moves[2]}! ]")
                                    print(f"[ {enemy_stats[0]}'s dress shone a bright, pale blue. ]")
                                    print(f'''[ "Must I show you how it feels to be powerless... such as all those creations of my land whom thou has killed?" ]''')
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 10
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]\n")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 5:
                                        enemy_stats[3] -= 10
                                        print(f"[ {enemy_stats[0]}'s dress has turned back to a simple white. ]")
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                if kippi_stats[3] <= 0:
                                    break
                    #spirit is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                                          |\n                                       .*`|'*,\n                                      --- * ---\n                                       '*,|.*`\n                                          |\n\n                               .-"~.    ,;;;,    ,~"-.\n                              (     )  (  )( )  (     )\n                             ('      )();o,o*()(      `)\n                            (        ( ); v ;( )        )\n                            ('     ,( (;-`-'-;( ),     `)\n                             `(   (  )  ,   ,  (  )   )'\n                              `(     : :_,|._; :     )'\n                              ('     `---'*`---':    `)\n                              ('    /  /  |  〵 〵    `)\n      ^----^                 (     /  /   "   〵 〵     )\n     (  {face} )                `-..-'  //;      |〵 `-..-'\n     |     ||                        ))        ))\n  _  | |   ||                       (/         〵〵\n  ||_!_|   |!                       (*;~*:~*;~*;~*)\n   ---|  T |                       ('';〵' ``) ''〵'\n      |  | |\n      !__!_!''')
                        if signature_move_trigger == True:
                                spirit_moves = ['TEMPEST VEIL', 'WHISPERS OF HYSTERIA', 'PERMAFROST ARMOUR']
                                signature_move = random.choice(spirit_moves)
                                if signature_move == spirit_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {spirit_moves[0]}! ]")
                                    print(f'''[ "...How could thou be so blind towards your wrongdoings...?" {player_name} hears the {enemy_stats[0]} whisper. ]''')
                                    print(f"[ Veils of white smoke have surrounded the spirit... {player_name} can't see where she is! ]\n")
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                elif signature_move == spirit_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {spirit_moves[1]}! ]")
                                    print(f"[ {player_name} could hear something— someone...? Crying, creaming, and shouting endlessly in their head... It's turning them insane! ]")
                                    kippi_stats[3] -= 3
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    signature_move_trigger = False
                                    hysteria_check = True
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {spirit_moves[2]}! ]")
                                    print(f"[ The {enemy_stats[0]}'s dress shone a bright, pale blue. ]")
                                    print(f'''[ "Must I show you how it feels to be powerless... such as all those creations of my land whom thou has killed?" ]''')
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 10
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]\n")
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if def_up_check == True :
                                def_counter += 1
                                if def_counter == 5:
                                    enemy_stats[3] -= 10
                                    print(f"[ The {enemy_stats[0]}'s dress has turned back to a simple white. ]")
                                    print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                                          |\n                                       .*`|'*,\n                                      --- * ---\n                                       '*,|.*`\n                                          |\n\n                               .-"~.    ,;;;,    ,~"-.\n                              (     )  (  )( )  (     )\n                             ('      )();o,o*()(      `)\n                            (        ( ); v ;( )        )\n                            ('     ,( (;-`-'-;( ),     `)\n                             `(   (  )  ,   ,  (  )   )'\n                              `(     : :_,|._; :     )'\n                              ('     `---'*`---':    `)\n                              ('    /  /  |  〵 〵    `)\n      ^----^                 (     /  /   "   〵 〵     )\n     (  {face} )                `-..-'  //;      |〵 `-..-'\n     |     ||                        ))        ))\n  _  | |   ||                       (/         〵〵\n  ||_!_|   |!                       (*;~*:~*;~*;~*)\n   ---|  T |                       ('';〵' ``) ''〵'\n      |  | |\n      !__!_!''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if hysteria_check == True:
                                kippi_stats[3] -= 3
                                print(f"[ The voices in {player_name}'s head is slowly draining them of their sanity! ]")
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print(" * `       *   `   *   `   *     *\n         `                   `     ` \n  `   *       *     *      `  *     *    \n `     `        `      `      \n   *     *          *      `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (U'=.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                break
                            stall_check = 0
                    break
            
            #bigfoot encounter                
            def bigfoot_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                frozen_check = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(bigfoot_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than bigfoot
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                        /#####〵\n                                  〵     ____\n                                 _     /    〵#|\n                                      /_  __/##|_\n                                   __(_((___ /#/  )_____\n                                  /##|o^ o__/#/  /######〵\n                                 |##|____   |_  /〵######|\n                                /〵#/ /  〵 /  |/  〵####/\n                               |####(_(___/ ___/####〵#/〵\n                              〵####|  |       |######|##|\n      ^----^                   /(##〵c_〵   c_/|######/##/\n     (  {face} )                  |##### (_(___   ' 〵######)〵\n     |     ||             ____|_#####( ( ______ #|#######/\n  _  | |   ||           ( ( ( ( 〵###_  / ) ) ) )|#####/\n  ||_!_|   |!           /       /(〵/ )〵      〵|###/____\n   ---|  T |           (       (/  /〵〵)       )         〵\n      |  | |           〵         // 〵         /_/〵_〵_〵_〵\n      !__!_!            〵_______//   〵_______/")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print(" * `       *   `   *   `   *     *\n         `                   `     ` \n  `   *       *     *      `  *     *    \n `     `        `      `      \n   *     *          *      `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (U'=.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    break
                                if signature_move_trigger == True:
                                    bigfoot_moves = ['ICICLE SPEAR', 'ICE-COLD GRASP', 'FRIGID FURY']
                                    signature_move = random.choice(bigfoot_moves)
                                    if signature_move == bigfoot_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {bigfoot_moves[0]}! ]")
                                        print(f"[ {player_name} managed to swiftly dodge the gigantic icicle spear and saved themselves from turning into the {enemy_stats[0]} next meal... but it did take a toll on {player_name}'s body! ]")
                                        kippi_stats[5] -= 5
                                        kippi_stats[6] -= 5
                                        print(f"[ {player_name}'s defence was reduced to {kippi_stats[5]}! ]")
                                        print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ]\n")
                                        signature_move_trigger = False
                                    elif signature_move == bigfoot_moves[1]:
                                        print(f"[ {enemy_stats[0]} decided to use {bigfoot_moves[1]}! ]")
                                        print(f"[ {enemy_stats[0]}'s little kitty legs start to shiver... {enemy_stats[0]}'s palms are too cold for your liking! ]")
                                        print(f"[ {player_name} is frozen! ]\n")
                                        signature_move_trigger = False
                                        frozen_check = True
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {bigfoot_moves[2]}! ]")
                                        print(f"[ {player_name} could see the veins on the {enemy_stats[0]}'s head popping! ]")
                                        enemy_stats[4] += 30
                                        print(f"[ {enemy_stats[0]}'s attack was boosted to {enemy_stats[4]}! ] \n")
                                        signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if frozen_check == True:
                            for i in range(2):
                                print(f"                                        /#####〵\n                                  〵     ____\n                                 _     /    〵#|\n                                      /_  __/##|_\n                                   __(_((___ /#/  )_____\n                                  /##|o^ o__/#/  /######〵\n                                 |##|____   |_  /〵######|\n                                /〵#/ /  〵 /  |/  〵####/\n                               |####(_(___/ ___/####〵#/〵\n                              〵####|  |       |######|##|\n      ^----^                   /(##〵c_〵   c_/|######/##/\n     (U'>.< )                  |##### (_(___   ' 〵######)〵\n     |     ||             ____|_#####( ( ______ #|#######/\n  _  | |   ||           ( ( ( ( 〵###_  / ) ) ) )|#####/\n  ||_!_|   |!           /       /(〵/ )〵      〵|###/____\n   ---|  T |           (       (/  /〵〵)       )         〵\n      |  | |           〵         // 〵         /_/〵_〵_〵_〵\n      !__!_!            〵_______//   〵_______/")
                                print(f"[ {player_name} is still shivering! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                            frozen_check = False          
                    #bigfoot is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                        /#####〵\n                                  〵     ____\n                                 _     /    〵#|\n                                      /_  __/##|_\n                                   __(_((___ /#/  )_____\n                                  /##|o^ o__/#/  /######〵\n                                 |##|____   |_  /〵######|\n                                /〵#/ /  〵 /  |/  〵####/\n                               |####(_(___/ ___/####〵#/〵\n                              〵####|  |       |######|##|\n      ^----^                   /(##〵c_〵   c_/|######/##/\n     (  {face} )                  |##### (_(___   ' 〵######)〵\n     |     ||             ____|_#####( ( ______ #|#######/\n  _  | |   ||           ( ( ( ( 〵###_  / ) ) ) )|#####/\n  ||_!_|   |!           /       /(〵/ )〵      〵|###/____\n   ---|  T |           (       (/  /〵〵)       )         〵\n      |  | |           〵         // 〵         /_/〵_〵_〵_〵\n      !__!_!            〵_______//   〵_______/")
                        if signature_move_trigger == True:
                            bigfoot_moves = ['ICICLE SPEAR', 'ICE-COLD GRASP', 'FRIGID FURY']
                            signature_move = random.choice(bigfoot_moves)
                            if signature_move == bigfoot_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {bigfoot_moves[0]}! ]")
                                print(f"[ {player_name} managed to swiftly dodge the gigantic icicle spear and saved themselves from turning into the bigfoot's next meal... but it did take a toll on {player_name}'s body! ]")
                                kippi_stats[5] -= 5
                                kippi_stats[6] -= 5
                                print(f"[ {player_name}'s defence was reduced to {kippi_stats[5]}! ]")
                                print(f"[ {player_name}'s speed was reduced to {kippi_stats[6]}! ]\n")
                                signature_move_trigger = False
                            elif signature_move == bigfoot_moves[1]:
                                print(f"[ {enemy_stats[0]} decided to use {bigfoot_moves[1]}! ]")
                                print(f"[ {enemy_stats[0]}'s little kitty legs start to shiver... {enemy_stats[0]}'s palms are too cold for your liking! ]")
                                print(f"[ {player_name} is frozen! ]\n")
                                signature_move_trigger = False
                                frozen_check = True
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {bigfoot_moves[2]}! ]")
                                print(f"[ {player_name} could see the veins on the {enemy_stats[0]}'s head popping! ]")
                                enemy_stats[4] += 30
                                print(f"[ {enemy_stats[0]}'s attack was boosted to {enemy_stats[4]}! ]\n")
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                        /#####〵\n                                  〵     ____\n                                 _     /    〵#|\n                                      /_  __/##|_\n                                   __(_((___ /#/  )_____\n                                  /##|o^ o__/#/  /######〵\n                                 |##|____   |_  /〵######|\n                                /〵#/ /  〵 /  |/  〵####/\n                               |####(_(___/ ___/####〵#/〵\n                              〵####|  |       |######|##|\n      ^----^                   /(##〵c_〵   c_/|######/##/\n     (  {face} )                  |##### (_(___   ' 〵######)〵\n     |     ||             ____|_#####( ( ______ #|#######/\n  _  | |   ||           ( ( ( ( 〵###_  / ) ) ) )|#####/\n  ||_!_|   |!           /       /(〵/ )〵      〵|###/____\n   ---|  T |           (       (/  /〵〵)       )         〵\n      |  | |           〵         // 〵         /_/〵_〵_〵_〵\n      !__!_!            〵_______//   〵_______/")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print(" * `       *   `   *   `   *     *\n         `                   `     ` \n  `   *       *     *      `  *     *    \n `     `        `      `      \n   *     *          *      `     *\n``````````````````````      ```````````\n      ^----^         /     /\n     (U'=.= )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                                    break
                        if frozen_check == True:
                            for i in range(2):
                                print(f"                                        /#####〵\n                                  〵     ____\n                                 _     /    〵#|\n                                      /_  __/##|_\n                                   __(_((___ /#/  )_____\n                                  /##|o^ o__/#/  /######〵\n                                 |##|____   |_  /〵######|\n                                /〵#/ /  〵 /  |/  〵####/\n                               |####(_(___/ ___/####〵#/〵\n                              〵####|  |       |######|##|\n      ^----^                   /(##〵c_〵   c_/|######/##/\n     (U'>.< )                  |##### (_(___   ' 〵######)〵\n     |     ||             ____|_#####( ( ______ #|#######/\n  _  | |   ||           ( ( ( ( 〵###_  / ) ) ) )|#####/\n  ||_!_|   |!           /       /(〵/ )〵      〵|###/____\n   ---|  T |           (       (/  /〵〵)       )         〵\n      |  | |           〵         // 〵         /_/〵_〵_〵_〵\n      !__!_!            〵_______//   〵_______/")
                                print(f"[ {player_name} is still shivering! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                            frozen_check = False
                    break

            #lizard encounter                
            def lizard_encounter():
                battle_mode = True
                signature_move_trigger = True
                hp_up_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(lizard_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than lizard
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |       〵\n      |  | |      _    ò--ó^^^^^^^^^^^^.________\n      !__!_!          (__/||-------||---------'\n                          ``       ``")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                item_drop_uncommon(20)
                                break
                            if signature_move_trigger == True:
                                lizard_moves = ['REGENERATE', 'WHISKING TAIL WHIP']
                                signature_move = random.choice(lizard_moves)
                                if signature_move == lizard_moves[0]:
                                    hp_up_check = True
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {lizard_moves[1]}! ]")
                                    print(f"[ Ouch! A lotta sand got into {enemy_stats[0]}'s little eyes, slowing him down! ]")
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if hp_up_check == True:
                                    if enemy_stats[1] < 25:
                                        print(f"[ {enemy_stats[0]} decided to use {lizard_moves[0]}! ]")
                                        print(f"[ {enemy_stats[0]} tore off a limb that was dragging it down! Looks metal! ]")
                                        enemy_stats[1] += 25
                                        print(f"[ {enemy_stats[0]}'s health went up to {enemy_stats[1]}! ] \n")
                                        hp_up_check = False
                                if kippi_stats[3] <= 0:
                                    break
                    #lizard is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                        /#####〵\n                                  〵     ____\n                                 _     /    〵#|\n                                      /_  __/##|_\n                                   __(_((___ /#/  )_____\n                                  /##|o^ o__/#/  /######〵\n                                 |##|____   |_  /〵######|\n                                /〵#/ /  〵 /  |/  〵####/\n                               |####(_(___/ ___/####〵#/〵\n                              〵####|  |       |######|##|\n      ^----^                   /(##〵c_〵   c_/|######/##/\n     (  {face} )                  |##### (_(___   ' 〵######)〵\n     |     ||             ____|_#####( ( ______ #|#######/\n  _  | |   ||           ( ( ( ( 〵###_  / ) ) ) )|#####/\n  ||_!_|   |!           /       /(〵/ )〵      〵|###/____\n   ---|  T |           (       (/  /〵〵)       )         〵\n      |  | |           〵         // 〵         /_/〵_〵_〵_〵\n      !__!_!            〵_______//   〵_______/")
                        if signature_move_trigger == True:
                                lizard_moves = ['REGENERATE', 'WHISKING TAIL WHIP']
                                signature_move = random.choice(lizard_moves)
                                if signature_move == lizard_moves[0]:
                                    hp_up_check = True
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {lizard_moves[1]}! ]")
                                    print(f"[ Ouch! A lotta sand got into {enemy_stats[0]}'s little eyes, slowing him down! ]")
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if hp_up_check == True:
                                if enemy_stats[1] < 25:
                                    print(f"[ {enemy_stats[0]} decided to use {lizard_moves[0]}! ]")
                                    print(f"[ {enemy_stats[0]} tore off a limb that was dragging it down! Looks metal! ]")
                                    enemy_stats[1] += 25
                                    print(f"[ {enemy_stats[0]}'s health went up to {enemy_stats[1]}! ] \n")
                                    hp_up_check = False
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |       〵\n      |  | |      _    ò--ó^^^^^^^^^^^^.________\n      !__!_!          (__/||-------||---------'\n                          ``       ``")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                item_drop_uncommon(20)
                                break
                    break

            #snake encounter                
            def snake_encounter():
                battle_mode = True
                signature_move_trigger = True
                poisoned_check = False
                stall_check = 0
                skip_turn = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(snake_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than snake
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                   〵\n      ^----^      _   __\n     (  {face} )        (òó)\n     |     ||        〵_/\n  _  | |   ||        / ^\n  ||_!_|   |!       ( (\n   ---|  T |        〵〵____\n      |  | |        (_______)\n      !__!_!       (_________()Oo")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if poisoned_check == True:
                                    kippi_poisoned()
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    item_drop_uncommon(20)
                                    if poisoned_check == True:
                                        print(f"[ {player_name} doesn't feel ill anymore. Hooray! ]\n")
                                    break
                                if signature_move_trigger == True:
                                    snake_moves = ['VENOMOUS BITE', 'COIL & CONSTRICT']
                                    signature_move = random.choice(snake_moves)
                                    if signature_move == snake_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {snake_moves[0]}! ]")
                                        print(f"[ {player_name} could feel the {enemy_stats[0]}'s venom flowing in their blood... Oh no! ]")
                                        poisoned_check = True
                                        if poisoned_check == True:
                                            kippi_poisoned()
                                        signature_move_trigger = False
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {snake_moves[1]}! ]")
                                        print(f"[ {enemy_stats[0]} embraced {player_name} in an asphyxiating hug! ]")
                                        print(f"[ {player_name}'s turn is skipped! ]")
                                        signature_move_trigger = False
                                        skip_turn = True
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                    #snake is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                   〵\n      ^----^      _   __\n     (  {face} )        (òó)\n     |     ||        〵_/\n  _  | |   ||        / ^\n  ||_!_|   |!       ( (\n   ---|  T |        〵〵____\n      |  | |        (_______)\n      !__!_!       (_________()Oo")
                        if signature_move_trigger == True:
                            snake_moves = ['VENOMOUS BITE', 'COIL & CONSTRICT']
                            signature_move = random.choice(snake_moves)
                            if signature_move == snake_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {snake_moves[0]}! ]")
                                print(f"[ {player_name} could feel the {enemy_stats[0]}'s venom flowing in their blood... Oh no! ]")
                                poisoned_check = True
                                if poisoned_check == True:
                                    kippi_poisoned()
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {snake_moves[1]}! ]")
                                print(f"[ {enemy_stats[0]} embraced {player_name} in an asphyxiating hug! ]")
                                print(f"[ {player_name}'s turn is skipped! ]")
                                skip_turn = True
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                   〵\n      ^----^      _   __\n     (  {face} )        (òó)\n     |     ||        〵_/\n  _  | |   ||        / ^\n  ||_!_|   |!       ( (\n   ---|  T |        〵〵____\n      |  | |        (_______)\n      !__!_!       (_________()Oo")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if poisoned_check == True:
                                    kippi_poisoned()
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    item_drop_uncommon(20)
                                    if poisoned_check == True:
                                        print(f"[ {player_name} doesn't feel ill anymore. Hooray! ]\n")
                                    break
                        else:
                            skip_turn = False
                    break

            #ostrich encounter                
            def ostrich_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(ostrich_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than ostrich
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                            〵\n                           _    __\n                               (òó)\n                               (/|\n                                ||\n                                ||\n                                ||,-v-,_\n                                ||〵|   /\n                            _,'=  ='-,-<\n                           / :       /  〵\n                          ( :       (   /,\n                          〵_;       〵__)\n      ^----^                 〵,_ ,   |\n     (  {face} )                 |  / 〵 |\n     |     ||                 | /   〵|\n  _  | |   ||                 ()     ()\n  ||_!_|   |!                 //     ||\n   ---|  T |                 //      ||\n      |  | |                //       ||\n      !__!_!              ,//        /〵\n                          ^^         '^^")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                item_drop_uncommon(20)
                                break
                            if signature_move_trigger == True:
                                ostrich_moves = ['PEBBLY PUNT', 'KICK OF HERCULES']
                                signature_move = random.choice(ostrich_moves)
                                if signature_move == ostrich_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {ostrich_moves[0]}! ]")
                                    print(f"[ Thousands of tiny pebbles flung in your direction when the {ostrich_moves[0]} kicked the sand towards you! How rude! ]")
                                    kippi_stats[6] -= 5
                                    print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {ostrich_moves[1]}! ]")
                                    print(f"[ {enemy_stats[0]} could swear that they could hear their skull cracking when the {enemy_stats[0]} kicked them right in the face! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+50) :
                                        kippi_stats[3] -= ((enemy_stats[2]+50) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                    #ostrich is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                            〵\n                           _    __\n                               (òó)\n                               (/|\n                                ||\n                                ||\n                                ||,-v-,_\n                                ||〵|   /\n                            _,'=  ='-,-<\n                           / :       /  〵\n                          ( :       (   /,\n                          〵_;       〵__)\n      ^----^                 〵,_ ,   |\n     (  {face} )                 |  / 〵 |\n     |     ||                 | /   〵|\n  _  | |   ||                 ()     ()\n  ||_!_|   |!                 //     ||\n   ---|  T |                 //      ||\n      |  | |                //       ||\n      !__!_!              ,//        /〵\n                          ^^         '^^")
                        if signature_move_trigger == True:
                                ostrich_moves = ['PEBBLY PUNT', 'KICK OF HERCULES']
                                signature_move = random.choice(ostrich_moves)
                                if signature_move == ostrich_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {ostrich_moves[0]}! ]")
                                    print(f"[ Thousands of tiny pebbles flung in your direction when the {ostrich_moves[0]} kicked the sand towards you! How rude! ]")
                                    kippi_stats[6] -= 5
                                    print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {ostrich_moves[1]}! ]")
                                    print(f"[ {enemy_stats[0]} could swear that they could hear their skull cracking when the {enemy_stats[0]} kicked them right in the face! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+50) :
                                        kippi_stats[3] -= ((enemy_stats[2]+50) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                            〵\n                           _    __\n                               (òó)\n                               (/|\n                                ||\n                                ||\n                                ||,-v-,_\n                                ||〵|   /\n                            _,'=  ='-,-<\n                           / :       /  〵\n                          ( :       (   /,\n                          〵_;       〵__)\n      ^----^                 〵,_ ,   |\n     (  {face} )                 |  / 〵 |\n     |     ||                 | /   〵|\n  _  | |   ||                 ()     ()\n  ||_!_|   |!                 //     ||\n   ---|  T |                 //      ||\n      |  | |                //       ||\n      !__!_!              ,//        /〵\n                          ^^         '^^")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                item_drop_uncommon(20)
                                break
                    break

            #coyote encounter
            def coyote_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                skip_turn = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(coyote_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than coyote
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                                  .\n                                                  ))\n      ^----^        〵      )〵〵                 //\n     (  {face} )              _``〵`,- '''' ''- ,,,/ /\n     |     ||     _   .---'a> , < ,<' << ,<, ' / 〵\n  _  | |   ||         `v^w   ' , << ,< ' <  <  / 〵\n  ||_!_|   |!          ````--' 〵  ,,,---''/ <' //\n   ---|  T |                    !! ;;    ( '  / 〵\n      |  | |                    !!</       〵`〵/\n      !__!_!                  <</          / /</\n                                          <</")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    item_drop_uncommon(20)
                                    break
                                if signature_move_trigger == True:
                                    coyote_moves = ['FRENZIED FERAL LACERATIONS', 'EVASIVE SWERVE']
                                    signature_move = random.choice(coyote_moves)
                                    if signature_move == coyote_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {coyote_moves[0]}! ]")
                                        print(f'''[ "WATCH OUT!" Shouts the voice in {player_name}'s head as the {enemy_stats[0]}'s about to lacerate {player_name} 'til the sand turns red. ]''')
                                        if kippi_stats[5] < (enemy_stats[2]+75) :
                                            kippi_stats[3] -= ((enemy_stats[2]+75) - kippi_stats[5])
                                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        else:
                                            print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                        signature_move_trigger = False
                                    else:
                                        signature_move == coyote_moves[1]
                                        print(f"[ {enemy_stats[0]} decided to use {coyote_moves[1]}! ]")
                                        print(f"[ {player_name} swears that they could hear the {enemy_stats[0]} laughing at them as they try to attack it! ...But to no avail! ]")
                                        print(f"[ {player_name}'s turn is skipped! ]\n")
                                        signature_move_trigger = False
                                        skip_turn = True     
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                    #coyote is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                                  .\n                                                  ))\n      ^----^        〵      )〵〵                 //\n     (  {face} )              _``〵`,- '''' ''- ,,,/ /\n     |     ||     _   .---'a> , < ,<' << ,<, ' / 〵\n  _  | |   ||         `v^w   ' , << ,< ' <  <  / 〵\n  ||_!_|   |!          ````--' 〵  ,,,---''/ <' //\n   ---|  T |                    !! ;;    ( '  / 〵\n      |  | |                    !!</       〵`〵/\n      !__!_!                  <</          / /</\n                                          <</")
                        if signature_move_trigger == True:
                            coyote_moves = ['FRENZIED FERAL LACERATIONS', 'EVASIVE SWERVE']
                            signature_move = random.choice(coyote_moves)
                            if signature_move == coyote_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {coyote_moves[0]}! ]")
                                print(f'''[ "WATCH OUT!" Shouts the voice in {player_name}'s head as the {enemy_stats[0]}'s about to lacerate {player_name} 'til the sand turns red. ]''')
                                if kippi_stats[5] < (enemy_stats[2]+75) :
                                    kippi_stats[3] -= ((enemy_stats[2]+75) - kippi_stats[5])
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                else:
                                    print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                signature_move_trigger = False
                            else:
                                signature_move == coyote_moves[1]
                                print(f"[ {enemy_stats[0]} decided to use {coyote_moves[1]}! ]")
                                print(f"[ {player_name} swears that they could hear the {enemy_stats[0]} laughing at them as they try to attack it! ...But to no avail! ]")
                                print(f"[ {player_name}'s turn is skipped! ]\n")
                                skip_turn = True
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                                  .\n                                                  ))\n      ^----^        〵      )〵〵                 //\n     (  {face} )              _``〵`,- '''' ''- ,,,/ /\n     |     ||     _   .---'a> , < ,<' << ,<, ' / 〵\n  _  | |   ||         `v^w   ' , << ,< ' <  <  / 〵\n  ||_!_|   |!          ````--' 〵  ,,,---''/ <' //\n   ---|  T |                    !! ;;    ( '  / 〵\n      |  | |                    !!</       〵`〵/\n      !__!_!                  <</          / /</\n                                          <</")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    item_drop_uncommon(20)
                                    break
                        else:
                            skip_turn = False
                    break

            #tortoise encounter                
            def tortoise_encounter():
                battle_mode = True
                signature_move_trigger = True
                def_up_check = False
                paralyzed_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(tortoise_stats.values())
                    random_chance = random.randint(1, 3)
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than tortoise
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )       〵\n     |     ||      _    _..---.--.\n  _  | |   ||         .'〵__|/ò.__)\n  ||_!_|   |!        /__.' _/ .-'〵\n   ---|  T |        (____.'.-_〵___)\n      |  | |         (_/ _)__(_〵_)〵_\n      !__!_!          (_..)--(.._)'--'")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                            break
                        if battle_input == 'fight':
                            if paralyzed_check == True:
                                paralyzed_trigger = random.randint(1,2)
                                if paralyzed_trigger == 1 :
                                    player_attacks(kippi_stats[4],enemy_stats[3])
                                    if enemy_stats[1] <= 0:
                                        print(f"[ {enemy_stats[0]} fainted! ]")
                                        print(f"[ {player_name} wins! ]\n")
                                        kippi_stats[1] += enemy_stats[5]
                                        print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                        random_chance = random.randint(1, 2)
                                        if random_chance == 1:
                                            item_drop_uncommon(20)
                                        else:
                                            item_drop_rare(100)
                                        break
                                else:
                                    print(f"[ {player_name} is PARALYZED! The static in their body makes them unable to move a single inch! ]")
                            else:
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    random_chance = random.randint(1, 2)
                                    if random_chance == 1:
                                        item_drop_uncommon(20)
                                    else:
                                        item_drop_rare(100)
                                    break
                            if signature_move_trigger == True:
                                tortoise_moves = ['QUAKING STOMP', 'LIE DOGGO']
                                signature_move = random.choice(tortoise_moves)
                                if signature_move == tortoise_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {tortoise_moves[0]}! ]")
                                    print(f"[ As the {enemy_stats[0]} stomps it's little foot onto the ground, otherworldly tremors could be felt from beneath {player_name}'s feet, leaving them scared! ]")
                                    print(f'''[ "Dis ain't no owdinawie towtoise!" {player_name} screams. ]''')
                                    print(f"[ {player_name} is paralyzed! ]")
                                    paralyzed_check = True
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {tortoise_moves[1]}! ]")
                                    print(f"[ The {enemy_stats[0]} decides to hide in its rock-hard shell! ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 50
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 3:
                                        enemy_stats[3] -= 50
                                        print(f"[ The {enemy_stats[0]} popped out from its shell! ]")
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                if kippi_stats[3] <= 0:
                                    break
                    #tortoise is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )       〵\n     |     ||      _    _..---.--.\n  _  | |   ||         .'〵__|/ò.__)\n  ||_!_|   |!        /__.' _/ .-'〵\n   ---|  T |        (____.'.-_〵___)\n      |  | |         (_/ _)__(_〵_)〵_\n      !__!_!          (_..)--(.._)'--'")
                        if signature_move_trigger == True:
                            tortoise_moves = ['QUAKING STOMP', 'LIE DOGGO']
                            signature_move = random.choice(tortoise_moves)
                            if signature_move == tortoise_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {tortoise_moves[0]}! ]")
                                print(f"[ As the {enemy_stats[0]} stomps it's little foot onto the ground, otherworldly tremors could be felt from beneath {player_name}'s feet, leaving them scared! ]")
                                print(f'''[ "Dis ain't no owdinawie towtoise!" {player_name} screams. ]''')
                                print(f"[ {player_name} is paralyzed! ]")
                                paralyzed_check = True
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {tortoise_moves[1]}! ]")
                                print(f"[ The {enemy_stats[0]} decides to hide in its rock-hard shell! ]")
                                def_up_check = True
                                def_counter = 0
                                enemy_stats[3] += 50
                                print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if def_up_check == True :
                                def_counter += 1
                                if def_counter == 3:
                                    enemy_stats[3] -= 50
                                    print(f"[ The {enemy_stats[0]} popped out from its shell! ]")
                                    print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^\n     (  {face} )       〵\n     |     ||      _    _..---.--.\n  _  | |   ||         .'〵__|/ò.__)\n  ||_!_|   |!        /__.' _/ .-'〵\n   ---|  T |        (____.'.-_〵___)\n      |  | |         (_/ _)__(_〵_)〵_\n      !__!_!          (_..)--(.._)'--'")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                            break
                        if battle_input == 'fight':
                            if paralyzed_check == True:
                                paralyzed_trigger = random.randint(1,2)
                                if paralyzed_trigger == 1 :
                                    player_attacks(kippi_stats[4],enemy_stats[3])
                                    if enemy_stats[1] <= 0:
                                        print(f"[ {enemy_stats[0]} fainted! ]")
                                        print(f"[ {player_name} wins! ]\n")
                                        kippi_stats[1] += enemy_stats[5]
                                        print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                        random_chance = random.randint(1, 2)
                                        if random_chance == 1:
                                            item_drop_uncommon(20)
                                        else:
                                            item_drop_rare(100)
                                        break
                                else:
                                    print(f"[ {player_name} is PARALYZED! The static in their body makes them unable to move a single inch! ]")
                            else:
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    random_chance = random.randint(1, 2)
                                    if random_chance == 1:
                                        item_drop_uncommon(20)
                                    else:
                                        item_drop_rare(100)
                                    break
                    break

            #armadillo encounter                
            def armadillo_encounter():
                battle_mode = True
                signature_move_trigger = True
                def_up_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(armadillo_stats.values())                    
                    random_chance = random.randint(1, 3)
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than armadillo
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                                                  @@%#@#+@%#@@@@@@                           \n                                                               @-+--=--+--*--+--+==-@                        \n                                                            @@=---*+*+==*--+--+--*-+==*%@                    \n                                                         @@--====+*++#==++-#=-*=-*-+-=-+--#@                 \n                                       %-#@            @#:-======*=*++#+=%=+=-#=-*=+-=+=++--*@               \n                                       @==-@         @=:-========*=#++#+=#==++#++#+==-#-#-=--:%              \n                                   @++@@+==-#@     #::-==========+=*++#+=++-#=*+-*+=*+%=%-#=---=%            \n                             〵      @=-%*==-#%%=----===========--++*+%++*#=%-*==#*+*+*=#-==----:+@          \n                                      @=--+#==%---===========-----+=*=**==%-#-*=-*++*=#=#===-------+@        \n                           _           @@@@#=-#*============------*-*=+*=-%-%+#==#==*=#=#=+=--------=@       \n                                        @=-----#==========--------*-*+++==#=*-*--#-=+=*+%-#----------=@      \n                                      %=#%@*---#========----------*-*=+===+=+-+=+*=*-+--*-=-----------#@     \n                                    @+=-+*:-*-=#======----===-----*-*=*======---*=-*-#=*-*-------------@     \n                                   @+=-*#-@#%-=#------=+==++==*-+++-*-+=-+-*--=-*=*=+-=%-=-===---------@     \n                                   %=-==-##+---*---==+*=+=+=+*+++++-+-+--+-+-=--==*-*=+-*=+=++====----*+@    \n                                  @--------**=-=#=--=====++++#+=-=+--::::-:-::-+:+-+-+=++++*+**+++*=-#+-*@   \n                                  %:::-=----+==+%@@@#*=:::====-+*=::=:::::::::-:::==+:=--**++#*+===##==+=%   \n                                  %::-+:--=*+@@        @#@@#=---+@#====+@ @%%%-=-::::::==--+===-@@ %=+---:#  \n      ^----^                     @+==-:-=+%@            @#+=+@ @+++==+%   ^----^=**+:::::--*%@@     @==+--:# \n     (  {face} )                    @+-:::==%               +===*  @+=+==*  ( ò-ó  )=+*=====+@           @+==+-* \n     |     ||                  #:::::-#@               @#==*   @*++==#   ||     |@@+===+@             @+-+=*#\n  _  | |   ||                                         #=-+-@   *====*  #*||   | | @_+++@               @=-=-#\n  ||_!_|   |!                                      @#*=-*++   @=--=%@+=+=!|   |_!_||--@                 =-=-*\n   ---|  T |                                     @@#=@ @@   @*-#--%    @==| T  |---=#=@               @*-=+=@\n      |  | |                                             @--*+-+:@        | |  |=*:+%=             @@:+--##@ \n      !__!_!                                             %@#+*#*          !_!__!#%           @@*-==+=+%@    \n                                                                                         @#*-==+*##          \n                                                                                  %**+##%##@@")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            kippi_stats[3] -= (enemy_stats[2] - kippi_stats[5])
                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ]\n")
                            stall_check = 0
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'=.= )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            print(f"[ {player_name} attacks the {enemy_stats[0]}! ]")
                            print(f"[ {enemy_stats[0]} health is down to {enemy_stats[1]}! ]\n")
                            if signature_move_trigger == True:
                                armadillo_moves = ['ROLL OVER', "CALL UPON THE SUN'S WRATH", 'VOLVATION']
                                signature_move = random.choice(armadillo_moves)
                                if signature_move == armadillo_moves[0]:
                                    print(f"[ The traveller shouts out... ]")
                                    print(f'''[ "{armadillo_moves[0]}!" ]''')
                                    print(f"[ The {enemy_stats[0]} rolls over in {player_name}'s direction... and {player_name} wasn't able to run away in time! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+50) :
                                        kippi_stats[3] -= ((enemy_stats[2]+50) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                                elif signature_move == armadillo_moves[1]:
                                    print(f"[ The traveller shouts out... ]")
                                    print(f'''[ "{armadillo_moves[0]}!" ]''')
                                    print(f"[ The sun is getting unbearably hot! Phew! Your vision is getting... blurry... ]")
                                    kippi_stats[5] -= 20
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s defence has reduced to {kippi_stats[5]}! ] \n")
                                    print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ The traveller shouts out... ]")
                                    print(f'''[ "{armadillo_moves[0]}!" ]''')
                                    print(f"[ The {enemy_stats[0]} rolled into a big ball... awaiting to take damage! ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 40
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 3:
                                        enemy_stats[3] -= 40
                                        print(f"[ The {enemy_stats[0]} de-balled! ]")
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                                if kippi_stats[3] <= 0:
                                    break
                    #armadillo is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                                                  @@%#@#+@%#@@@@@@                           \n                                                               @-+--=--+--*--+--+==-@                        \n                                                            @@=---*+*+==*--+--+--*-+==*%@                    \n                                                         @@--====+*++#==++-#=-*=-*-+-=-+--#@                 \n                                       %-#@            @#:-======*=*++#+=%=+=-#=-*=+-=+=++--*@               \n                                       @==-@         @=:-========*=#++#+=#==++#++#+==-#-#-=--:%              \n                                   @++@@+==-#@     #::-==========+=*++#+=++-#=*+-*+=*+%=%-#=---=%            \n                             〵      @=-%*==-#%%=----===========--++*+%++*#=%-*==#*+*+*=#-==----:+@          \n                                      @=--+#==%---===========-----+=*=**==%-#-*=-*++*=#=#===-------+@        \n                           _           @@@@#=-#*============------*-*=+*=-%-%+#==#==*=#=#=+=--------=@       \n                                        @=-----#==========--------*-*+++==#=*-*--#-=+=*+%-#----------=@      \n                                      %=#%@*---#========----------*-*=+===+=+-+=+*=*-+--*-=-----------#@     \n                                    @+=-+*:-*-=#======----===-----*-*=*======---*=-*-#=*-*-------------@     \n                                   @+=-*#-@#%-=#------=+==++==*-+++-*-+=-+-*--=-*=*=+-=%-=-===---------@     \n                                   %=-==-##+---*---==+*=+=+=+*+++++-+-+--+-+-=--==*-*=+-*=+=++====----*+@    \n                                  @--------**=-=#=--=====++++#+=-=+--::::-:-::-+:+-+-+=++++*+**+++*=-#+-*@   \n                                  %:::-=----+==+%@@@#*=:::====-+*=::=:::::::::-:::==+:=--**++#*+===##==+=%   \n                                  %::-+:--=*+@@        @#@@#=---+@#====+@ @%%%-=-::::::==--+===-@@ %=+---:#  \n      ^----^                     @+==-:-=+%@            @#+=+@ @+++==+%   ^----^=**+:::::--*%@@     @==+--:# \n     (  {face} )                    @+-:::==%               +===*  @+=+==*  ( ò-ó  )=+*=====+@           @+==+-* \n     |     ||                  #:::::-#@               @#==*   @*++==#   ||     |@@+===+@             @+-+=*#\n  _  | |   ||                                         #=-+-@   *====*  #*||   | | @_+++@               @=-=-#\n  ||_!_|   |!                                      @#*=-*++   @=--=%@+=+=!|   |_!_||--@                 =-=-*\n   ---|  T |                                     @@#=@ @@   @*-#--%    @==| T  |---=#=@               @*-=+=@\n      |  | |                                             @--*+-+:@        | |  |=*:+%=             @@:+--##@ \n      !__!_!                                             %@#+*#*          !_!__!#%           @@*-==+=+%@    \n                                                                                         @#*-==+*##          \n                                                                                  %**+##%##@@")
                        if signature_move_trigger == True:
                                armadillo_moves = ['ROLL OVER', "CALL UPON THE SUN'S WRATH", 'VOLVATION']
                                signature_move = random.choice(armadillo_moves)
                                if signature_move == armadillo_moves[0]:
                                    print(f"[ The traveller shouts out... ]")
                                    print(f'''[ "{armadillo_moves[0]}!" ]''')
                                    print(f"[ The {enemy_stats[0]} rolls over in {player_name}'s direction... and {player_name} wasn't able to run away in time! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+50) :
                                        kippi_stats[3] -= ((enemy_stats[2]+50) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                                elif signature_move == armadillo_moves[1]:
                                    print(f"[ The traveller shouts out... ]")
                                    print(f'''[ "{armadillo_moves[0]}!" ]''')
                                    print(f"[ The sun is getting unbearably hot! Phew! Your vision is getting... blurry... ]")
                                    kippi_stats[5] -= 20
                                    kippi_stats[6] -= 10
                                    print(f"[ {player_name}'s defence has reduced to {kippi_stats[5]}! ] \n")
                                    print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ The traveller shouts out... ]")
                                    print(f'''[ "{armadillo_moves[0]}!" ]''')
                                    print(f"[ The {enemy_stats[0]} rolled into a big ball... awaiting to take damage! ]")
                                    def_up_check = True
                                    def_counter = 0
                                    enemy_stats[3] += 40
                                    print(f"[ {enemy_stats[0]}'s defence has increased to {enemy_stats[3]}! ]")
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if def_up_check == True :
                                    def_counter += 1
                                    if def_counter == 3:
                                        enemy_stats[3] -= 40
                                        print(f"[ The {enemy_stats[0]} de-balled! ]")
                                        print(f"[ {enemy_stats[0]}'s defence has went back down to to {enemy_stats[3]}! ]")
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                                                  @@%#@#+@%#@@@@@@                           \n                                                               @-+--=--+--*--+--+==-@                        \n                                                            @@=---*+*+==*--+--+--*-+==*%@                    \n                                                         @@--====+*++#==++-#=-*=-*-+-=-+--#@                 \n                                       %-#@            @#:-======*=*++#+=%=+=-#=-*=+-=+=++--*@               \n                                       @==-@         @=:-========*=#++#+=#==++#++#+==-#-#-=--:%              \n                                   @++@@+==-#@     #::-==========+=*++#+=++-#=*+-*+=*+%=%-#=---=%            \n                             〵      @=-%*==-#%%=----===========--++*+%++*#=%-*==#*+*+*=#-==----:+@          \n                                      @=--+#==%---===========-----+=*=**==%-#-*=-*++*=#=#===-------+@        \n                           _           @@@@#=-#*============------*-*=+*=-%-%+#==#==*=#=#=+=--------=@       \n                                        @=-----#==========--------*-*+++==#=*-*--#-=+=*+%-#----------=@      \n                                      %=#%@*---#========----------*-*=+===+=+-+=+*=*-+--*-=-----------#@     \n                                    @+=-+*:-*-=#======----===-----*-*=*======---*=-*-#=*-*-------------@     \n                                   @+=-*#-@#%-=#------=+==++==*-+++-*-+=-+-*--=-*=*=+-=%-=-===---------@     \n                                   %=-==-##+---*---==+*=+=+=+*+++++-+-+--+-+-=--==*-*=+-*=+=++====----*+@    \n                                  @--------**=-=#=--=====++++#+=-=+--::::-:-::-+:+-+-+=++++*+**+++*=-#+-*@   \n                                  %:::-=----+==+%@@@#*=:::====-+*=::=:::::::::-:::==+:=--**++#*+===##==+=%   \n                                  %::-+:--=*+@@        @#@@#=---+@#====+@ @%%%-=-::::::==--+===-@@ %=+---:#  \n      ^----^                     @+==-:-=+%@            @#+=+@ @+++==+%   ^----^=**+:::::--*%@@     @==+--:# \n     (  {face} )                    @+-:::==%               +===*  @+=+==*  ( ò-ó  )=+*=====+@           @+==+-* \n     |     ||                  #:::::-#@               @#==*   @*++==#   ||     |@@+===+@             @+-+=*#\n  _  | |   ||                                         #=-+-@   *====*  #*||   | | @_+++@               @=-=-#\n  ||_!_|   |!                                      @#*=-*++   @=--=%@+=+=!|   |_!_||--@                 =-=-*\n   ---|  T |                                     @@#=@ @@   @*-#--%    @==| T  |---=#=@               @*-=+=@\n      |  | |                                             @--*+-+:@        | |  |=*:+%=             @@:+--##@ \n      !__!_!                                             %@#+*#*          !_!__!#%           @@*-==+=+%@    \n                                                                                         @#*-==+*##          \n                                                                                  %**+##%##@@")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            print(f"[ {player_name} attacks the {enemy_stats[0]}! ]")
                            enemy_stats[1] -= (kippi_stats[4] - enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'=.= )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            print(f"[ {enemy_stats[0]} health is down to {enemy_stats[1]}! ]\n")
                    break

            #cactus encounter                
            def cactus_encounter():
                battle_mode = True
                signature_move_trigger = True
                hp_up_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(cactus_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than cactus
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                  _   _\n                                 / '-' 〵\n                                ;       ;\n                             /'-|       |-'〵\n                            |   |_______K   |\n                            〵   '-------'  /\n                              .___.....___.'\n                                | ;  : ;|\n                               _|;__;__.|_\n                              |     Y     |    .--\n                     .--      〵__.'^'.__./   /;  〵\n                    /  ;〵      |_  ;  _|     |  ' |\n                    | ;  |     ( `(''')  )    |;   |\n                    |'   |     (  (   )  )`.  | ;  |\n                    |  ; |     (  (   )  )  ) |    |\n                    |;   |      ;`-.__.'|  /  |:  ;|\n                    | ;  |.     |;  ;   |__(__/ ;  |\n                    |   ' L_____'      ' -_   .'   /\n                    〵  '.   - _  ' ;  ;  _  -   .'\n                     '.   -     - ;  ;   .------`\n                       `--------.      ;|    〵\n                                |;  ,   |〵    〵\n                                |     ; |  `````\n                                |. ;    |\n                                | :    :|\n                                |   .   |\n                                |;   ;  |\n                                |;  ,   |\n                                |     ; |\n                                |. ;    |\n                                | :    :|\n                                |   .   |\n                                |;   ;  |\n      ^----^                    |;  ,   |\n     (  {face} )                   |     ; |\n     |     ||                   |     ; |\n  _  | |   ||                   |. ;    |\n  ||_!_|   |!                   | :    :|\n   ---|  T |                    |   .   |\n      |  | |                    |;   ;  |\n      !__!_!                    `'-----'`")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n\n\n\n\n\n\n\n             _\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'=.= )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                            if signature_move_trigger == True:
                                cactus_moves = ["BARRAGE O' THORNS", 'SPILLING SPORES', 'PHOTOSYNTHESIS']
                                signature_move = random.choice(cactus_moves)
                                if signature_move == cactus_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {cactus_moves[0]}! ]")
                                    print(f"[ Ginormous thorns shot out from the {enemy_stats[0]}'s body! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+50) :
                                        kippi_stats[3] -= ((enemy_stats[2]+50) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                                elif signature_move == cactus_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {cactus_moves[0]}! ]")
                                    print(f"[ {player_name} feels... INTOXICATED from inhaling the spores let out by the {enemy_stats[0]}! ]")
                                    kippi_stats[6] -= 20
                                    print(f"[ {player_name}'s speed went down to {kippi_stats[6]}! ]")
                                    signature_move_trigger = False
                                else:
                                    hp_up_check = True
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if hp_up_check == True:
                                    if enemy_stats[1] < 25:
                                        print(f"[ {enemy_stats[0]} decided to use {cactus_moves[2]}! ]")
                                        print(f"[ {enemy_stats[0]} soaked up the sun waves! ]")
                                        enemy_stats[1] += 50
                                        print(f"[ {enemy_stats[0]}'s health went up to {enemy_stats[1]}! ] \n")
                                        hp_up_check = False
                                if kippi_stats[3] <= 0:
                                    break
                    #cactus is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                  _   _\n                                 / '-' 〵\n                                ;       ;\n                             /'-|       |-'〵\n                            |   |_______K   |\n                            〵   '-------'  /\n                              .___.....___.'\n                                | ;  : ;|\n                               _|;__;__.|_\n                              |     Y     |    .--\n                     .--      〵__.'^'.__./   /;  〵\n                    /  ;〵      |_  ;  _|     |  ' |\n                    | ;  |     ( `(''')  )    |;   |\n                    |'   |     (  (   )  )`.  | ;  |\n                    |  ; |     (  (   )  )  ) |    |\n                    |;   |      ;`-.__.'|  /  |:  ;|\n                    | ;  |.     |;  ;   |__(__/ ;  |\n                    |   ' L_____'      ' -_   .'   /\n                    〵  '.   - _  ' ;  ;  _  -   .'\n                     '.   -     - ;  ;   .------`\n                       `--------.      ;|    〵\n                                |;  ,   |〵    〵\n                                |     ; |  `````\n                                |. ;    |\n                                | :    :|\n                                |   .   |\n                                |;   ;  |\n                                |;  ,   |\n                                |     ; |\n                                |. ;    |\n                                | :    :|\n                                |   .   |\n                                |;   ;  |\n      ^----^                    |;  ,   |\n     (  {face} )                   |     ; |\n     |     ||                   |     ; |\n  _  | |   ||                   |. ;    |\n  ||_!_|   |!                   | :    :|\n   ---|  T |                    |   .   |\n      |  | |                    |;   ;  |\n      !__!_!                    `'-----'`")
                        if signature_move_trigger == True:
                                cactus_moves = ["BARRAGE O' THORNS", 'SPILLING SPORES', 'PHOTOSYNTHESIS']
                                signature_move = random.choice(cactus_moves)
                                if signature_move == cactus_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {cactus_moves[0]}! ]")
                                    print(f"[ Ginormous thorns shot out from the {enemy_stats[0]}'s body! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+50) :
                                        kippi_stats[3] -= ((enemy_stats[2]+50) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                                elif signature_move == cactus_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {cactus_moves[0]}! ]")
                                    print(f"[ {player_name} feels... INTOXICATED from inhaling the spores let out by the {enemy_stats[0]}! ]")
                                    kippi_stats[6] -= 20
                                    print(f"[ {player_name}'s speed went down to {kippi_stats[6]}! ]")
                                    signature_move_trigger = False
                                else:
                                    hp_up_check = True
                                    signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if hp_up_check == True:
                                if enemy_stats[1] < 25:
                                    print(f"[ {enemy_stats[0]} decided to use {cactus_moves[2]}! ]")
                                    print(f"[ {enemy_stats[0]} soaked up the sun waves! ]")
                                    enemy_stats[1] += 50
                                    print(f"[ {enemy_stats[0]}'s health went up to {enemy_stats[1]}! ] \n")
                                    hp_up_check = False
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                  _   _\n                                 / '-' 〵\n                                ;       ;\n                             /'-|       |-'〵\n                            |   |_______K   |\n                            〵   '-------'  /\n                              .___.....___.'\n                                | ;  : ;|\n                               _|;__;__.|_\n                              |     Y     |    .--\n                     .--      〵__.'^'.__./   /;  〵\n                    /  ;〵      |_  ;  _|     |  ' |\n                    | ;  |     ( `(''')  )    |;   |\n                    |'   |     (  (   )  )`.  | ;  |\n                    |  ; |     (  (   )  )  ) |    |\n                    |;   |      ;`-.__.'|  /  |:  ;|\n                    | ;  |.     |;  ;   |__(__/ ;  |\n                    |   ' L_____'      ' -_   .'   /\n                    〵  '.   - _  ' ;  ;  _  -   .'\n                     '.   -     - ;  ;   .------`\n                       `--------.      ;|    〵\n                                |;  ,   |〵    〵\n                                |     ; |  `````\n                                |. ;    |\n                                | :    :|\n                                |   .   |\n                                |;   ;  |\n                                |;  ,   |\n                                |     ; |\n                                |. ;    |\n                                | :    :|\n                                |   .   |\n                                |;   ;  |\n      ^----^                    |;  ,   |\n     (  {face} )                   |     ; |\n     |     ||                   |     ; |\n  _  | |   ||                   |. ;    |\n  ||_!_|   |!                   | :    :|\n   ---|  T |                    |   .   |\n      |  | |                    |;   ;  |\n      !__!_!                    `'-----'`")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n\n\n\n\n\n\n\n             _\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'=.= )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                break
                    break

            #behemoth encounter                
            def behemoth_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                skip_turn = False
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(behemoth_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than behemoth
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                                    /|/|/|〵〵|〵\n                                                   |  | | | | | |〵\n                                                 | | |  | || || | 〵\n                                                /  | | |  || || ||||\n                                                || | | |  | | |  | 〵\n                                              |  | | |  || ||  | | |〵\n                                             /  |  | |  ||  | || | ||〵\n                                             | | | | | || |  ||   | | |\n                                             | | |    | | || |  | | ||〵\n                                            || |  | | | |  | || | | |||〵\n                                           ||  |    |   | | ||| |     | |\n                                           ||| | | |  | | |  || | | ||  |〵\n                                           | | | | |  |   | || |||| ||| |〵\n                                          /|  |  | | |  |  | | | || | ||  |\n                                          |||| | |__ |__| |__|   || | || ||〵\n                                         |_| _ --,   ,.. ,   ,.... _|_|_ || |〵\n                                         /,   ,..,    ,.,    ,.. ,   ,..-|〵| |\n      ^----^                          _ /.,    ,.,    ,,     ,...   ,...,   .〵〵\n     (  {face} )                      _ /  ,..,    ,     ,      ,.,    ,.,    _ ...〵〵〵\n     |     ||             〵     _/       ',,   ,     ,       ,     .       〵  .   .〵〵〵\n  _  | |   ||                  /     .       _--                      -〵    〵  .   ..  〵〵〵〵\n  ||_!_|   |!            _    /    ó .   __ /    _/                 ____|    〵       .       〵〵〵〵\n   ---|  T |                 /      |---  /    /---__________------    |    |---____            |  〵\n      |  | |                /    ,; /     |    |                       |nn  |       ---____     |  |\n      !__!_!                |,,,','/      /nn  |                                             ---|  |\n                              ;,,;/                                                     _______/   /\n                                                                                 --------_________/")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n\n     .*.       .*.\n   , | | ,     | |\n  ||_| |_||  , | | ,\n  `--, ,--` ||_| |_||\n     | |    `--, ,--`\n     | |       | |\n     | |       | |                 _\n```````````````| |````      ``````/_〵``\n``````^----^`````````/     /```````````\n`````(U'=.= )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````    |  ````````````````\n      |  | |     〵___〵_`__._`___`__/_\n      !__!_!        __`__/〵`__  〵\n                   /           〵\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    break
                                if signature_move_trigger == True:
                                    behemoth_moves = ['GRITTY TRAP', 'TERRAFORMATION', "SURGE O' SAND"]
                                    signature_move = random.choice(behemoth_moves)
                                    if signature_move == behemoth_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {behemoth_moves[0]}! ]")
                                        print(f"[ {player_name}'s paws suddenly got encaptured by sand that took in the form of gigantic hands... They can't move! ]")
                                        print(f"[ {player_name}'s turn is skipped! ]\n")
                                        signature_move_trigger = False
                                        skip_turn = True
                                    elif signature_move == behemoth_moves[1]:
                                        print(f"[ {enemy_stats[0]} decided to use {behemoth_moves[1]}! ]")
                                        print(f"[ A gigantic mound of sand was terraformed... and it slammed right onto {enemy_stats[0]}'s fluffy body! ]")
                                        if kippi_stats[5] < (enemy_stats[2]+25) :
                                            kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        else:
                                            print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                        signature_move_trigger = False
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {behemoth_moves[2]}! ]")
                                        print(f"[ A large sandstorm appeared out of nowhere, causing {player_name} to get a few scratches and blinding their eyes! ]")
                                        if kippi_stats[5] < (enemy_stats[2]+25) :
                                            kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        else:
                                            print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                        kippi_stats[6] -= 10
                                        print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                        signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if skip_turn == True:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            skip_turn = False
                    #behemoth is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                                                    /|/|/|〵〵|〵\n                                                   |  | | | | | |〵\n                                                 | | |  | || || | 〵\n                                                /  | | |  || || ||||\n                                                || | | |  | | |  | 〵\n                                              |  | | |  || ||  | | |〵\n                                             /  |  | |  ||  | || | ||〵\n                                             | | | | | || |  ||   | | |\n                                             | | |    | | || |  | | ||〵\n                                            || |  | | | |  | || | | |||〵\n                                           ||  |    |   | | ||| |     | |\n                                           ||| | | |  | | |  || | | ||  |〵\n                                           | | | | |  |   | || |||| ||| |〵\n                                          /|  |  | | |  |  | | | || | ||  |\n                                          |||| | |__ |__| |__|   || | || ||〵\n                                         |_| _ --,   ,.. ,   ,.... _|_|_ || |〵\n                                         /,   ,..,    ,.,    ,.. ,   ,..-|〵| |\n      ^----^                          _ /.,    ,.,    ,,     ,...   ,...,   .〵〵\n     (  {face} )                      _ /  ,..,    ,     ,      ,.,    ,.,    _ ...〵〵〵\n     |     ||             〵     _/       ',,   ,     ,       ,     .       〵  .   .〵〵〵\n  _  | |   ||                  /     .       _--                      -〵    〵  .   ..  〵〵〵〵\n  ||_!_|   |!            _    /    ó .   __ /    _/                 ____|    〵       .       〵〵〵〵\n   ---|  T |                 /      |---  /    /---__________------    |    |---____            |  〵\n      |  | |                /    ,; /     |    |                       |nn  |       ---____     |  |\n      !__!_!                |,,,','/      /nn  |                                             ---|  |\n                              ;,,;/                                                     _______/   /\n                                                                                 --------_________/")
                        if signature_move_trigger == True:
                            behemoth_moves = ['GRITTY TRAP', 'TERRAFORMATION', "SURGE O' SAND"]
                            signature_move = random.choice(behemoth_moves)
                            if signature_move == behemoth_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {behemoth_moves[0]}! ]")
                                print(f"[ {player_name}'s paws suddenly got encaptured by sand that took in the form of gigantic hands... They can't move! ]")
                                print(f"[ {player_name}'s turn is skipped! ]\n")
                                signature_move_trigger = False
                                skip_turn = True
                            elif signature_move == behemoth_moves[1]:
                                print(f"[ {enemy_stats[0]} decided to use {behemoth_moves[1]}! ]")
                                print(f"[ A gigantic mound of sand was terraformed... and it slammed right onto {enemy_stats[0]}'s fluffy body! ]")
                                if kippi_stats[5] < (enemy_stats[2]+25) :
                                    kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                else:
                                    print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {behemoth_moves[2]}! ]")
                                print(f"[ A large sandstorm appeared out of nowhere, causing {player_name} to get a few scratches and blinding their eyes! ]")
                                if kippi_stats[5] < (enemy_stats[2]+25) :
                                    kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                else:
                                    print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                kippi_stats[6] -= 10
                                print(f"[ {player_name}'s speed has reduced to {kippi_stats[6]}! ] \n")
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if skip_turn == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                                                    /|/|/|〵〵|〵\n                                                   |  | | | | | |〵\n                                                 | | |  | || || | 〵\n                                                /  | | |  || || ||||\n                                                || | | |  | | |  | 〵\n                                              |  | | |  || ||  | | |〵\n                                             /  |  | |  ||  | || | ||〵\n                                             | | | | | || |  ||   | | |\n                                             | | |    | | || |  | | ||〵\n                                            || |  | | | |  | || | | |||〵\n                                           ||  |    |   | | ||| |     | |\n                                           ||| | | |  | | |  || | | ||  |〵\n                                           | | | | |  |   | || |||| ||| |〵\n                                          /|  |  | | |  |  | | | || | ||  |\n                                          |||| | |__ |__| |__|   || | || ||〵\n                                         |_| _ --,   ,.. ,   ,.... _|_|_ || |〵\n                                         /,   ,..,    ,.,    ,.. ,   ,..-|〵| |\n      ^----^                          _ /.,    ,.,    ,,     ,...   ,...,   .〵〵\n     (  {face} )                      _ /  ,..,    ,     ,      ,.,    ,.,    _ ...〵〵〵\n     |     ||             〵     _/       ',,   ,     ,       ,     .       〵  .   .〵〵〵\n  _  | |   ||                  /     .       _--                      -〵    〵  .   ..  〵〵〵〵\n  ||_!_|   |!            _    /    ó .   __ /    _/                 ____|    〵       .       〵〵〵〵\n   ---|  T |                 /      |---  /    /---__________------    |    |---____            |  〵\n      |  | |                /    ,; /     |    |                       |nn  |       ---____     |  |\n      !__!_!                |,,,','/      /nn  |                                             ---|  |\n                              ;,,;/                                                     _______/   /\n                                                                                 --------_________/")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n\n     .*.       .*.\n   , | | ,     | |\n  ||_| |_||  , | | ,\n  `--, ,--` ||_| |_||\n     | |    `--, ,--`\n     | |       | |\n     | |       | |                 _\n```````````````| |````      ``````/_〵``\n``````^----^`````````/     /```````````\n`````(U'=.= )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````    |  ````````````````\n      |  | |     〵___〵_`__._`___`__/_\n      !__!_!        __`__/〵`__  〵\n                   /           〵\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                                    break
                        else:
                            skip_turn = False
                    break

            #lava blob
            def lavablob_encounter():
                battle_mode = True
                signature_move_trigger = True
                burned_check = False
                stall_check = 0
                def_up_check = False

                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(lavablob_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than lava blob
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^            `.\n     (  {face} )\n     |     ||        `   ,\n  _  | |   ||    .     .    ,\n  ||_!_|   |!       '      .\n   ---|  T |    `    )^( `\n      |  | |      .|Vo.oV|.  ,\n      !__!_!      ('W'W'W')_.")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if burned_check == True:
                                kippi_burned()
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                if burned_check == True:
                                    print(f"[ {player_name}'s body isn't burning anymore. Hooray! ]\n")
                                break
                            if def_up_check == True:
                                enemy_stats[3] = 4
                                def_counter += 1
                                if def_counter == 2:
                                    enemy_stats[3] = 2
                                    def_up_check = False
                            if signature_move_trigger == True:
                                lavablob_moves = ['RAIN OF EMBERS', 'SOLIDIFY']
                                signature_move = random.choice(lavablob_moves)
                                if signature_move == lavablob_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {lavablob_moves[0]}! ]")
                                    print(f"[ A particularly large chunck of magma hit {player_name} directly in the eye— Ouch! ]\n")
                                    kippi_stats[3] -= enemy_stats[2]+25
                                    burned_check = True
                                    if burned_check == True:
                                        kippi_burned()
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {lavablob_moves[1]}! ]")
                                    print(f"[ {enemy_stats[0]} transformed into a block of obsidian! ]\n")
                                    enemy_stats[3] += 50
                                    def_counter = 0
                                    print(f"[ {enemy_stats[0]}'s defence went up to {enemy_stats[3]}! ]\n")
                                    def_up_check = True
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if def_up_check == True:
                                    def_counter += 1
                                    if def_counter == 2:
                                        print(f"[ Oh, look! {enemy_stats[0]} turned back into a pile of lava! ]")
                                        enemy_stats[3] -= 50
                                        print(f"[ {enemy_stats[0]}'s defence went down to {enemy_stats[3]}! ]\n")
                                        def_up_check = False
                                if kippi_stats[3] <= 0:
                                    break
                    #lavablob is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^            `.\n     (  {face} )\n     |     ||        `   ,\n  _  | |   ||    .     .    ,\n  ||_!_|   |!       '      .\n   ---|  T |    `    )^( `\n      |  | |      .|Vo.oV|.  ,\n      !__!_!      ('W'W'W')_.")
                        if signature_move_trigger == True:
                            lavablob_moves = ['RAIN OF EMBERS', 'SOLIDIFY']
                            signature_move = random.choice(lavablob_moves)
                            if signature_move == lavablob_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {lavablob_moves[0]}! ]")
                                print(f"[ A particularly large chunck of magma hit {player_name} directly in the eye— Ouch! ]\n")
                                kippi_stats[3] -= enemy_stats[2]+25
                                burned_check = True
                                if burned_check == True:
                                    kippi_burned()
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {lavablob_moves[1]}! ]")
                                print(f"[ {enemy_stats[0]} transformed into a block of obsidian! ]\n")
                                enemy_stats[3] += 50
                                def_counter = 0
                                print(f"[ {enemy_stats[0]}'s defence went up to {enemy_stats[3]}! ]\n")
                                def_up_check = True
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if def_up_check == True:
                                def_counter += 1
                                if def_counter == 2:
                                    print(f"[ Oh, look! {enemy_stats[0]} turned back into a pile of lava! ]")
                                    enemy_stats[3] -= 50
                                    print(f"[ {enemy_stats[0]}'s defence went down to {enemy_stats[3]}! ]\n")
                                    def_up_check = False
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"      ^----^            `.\n     (  {face} )\n     |     ||        `   ,\n  _  | |   ||    .     .    ,\n  ||_!_|   |!       '      .\n   ---|  T |    `    )^( `\n      |  | |      .|Vo.oV|.  ,\n      !__!_!      ('W'W'W')_.")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if burned_check == True:
                                kippi_burned()
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                if burned_check:
                                    print(f"[ {player_name} doesn't feel ill anymore. Hooray! ]\n")
                                break
                    break

            #skeleton
            def skeleton_encounter():
                battle_mode = True
                signature_move_trigger = True
                frozen_check = False
                stall_check = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(skeleton_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than skeleton
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                         .-.\n                        (●●)\n                         |=|\n                        __|__\n                      //.=|=.〵.\n                     // .=|=. 〵.\n      ^----^        .〵 .=|=. //\n     (  {face} )        .〵(_=_)//\n     |     ||          (:| |:)\n  _  | |   ||           || ||\n  ||_!_|   |!           () ()\n   ---|  T |            || ||\n      |  | |            || ||\n      !__!_!           ==' '==")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    random_chance = random.randint(1, 3)
                                    if random_chance == 1:
                                        item_drop_common(25)
                                    elif random_chance == 2:
                                        item_drop_uncommon(50)
                                    else:
                                        item_drop_rare(100)
                                    break
                                if signature_move_trigger == True:
                                    skeleton_moves = ['GRIMDARK AMBIENCE', 'BARRAGE O’ BONES']
                                    signature_move = random.choice(skeleton_moves)
                                    if signature_move == skeleton_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {skeleton_moves[0]}! ]")
                                        print(f"[ A dark aura suddenly emanated in the area... leaving {player_name} FROZEN! ]")
                                        frozen_check = True
                                        signature_move_trigger = False
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {skeleton_moves[1]}! ]")
                                        print(f"[ Tons of animal bones were thrown in {player_name}'s direction, leaving them bruised! ]")
                                        if kippi_stats[5] < (enemy_stats[2]+25) :
                                            kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        else:
                                            print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                        signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                        if frozen_check == True:
                            for i in range(2):
                                print(f"                         .-.\n                        (●●)\n                         |=|\n                        __|__\n                      //.=|=.〵.\n                     // .=|=. 〵.\n      ^----^        .〵 .=|=. //\n     (U'>.< )        .〵(_=_)//\n     |     ||          (:| |:)\n  _  | |   ||           || ||\n  ||_!_|   |!           () ()\n   ---|  T |            || ||\n      |  | |            || ||\n      !__!_!           ==' '==")
                                print(f"[ {player_name} is still terrified! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                            frozen_check = False
                            print(f"[ {player_name} has gotten over his petrification! ]")
                    #skeleton is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                         .-.\n                        (●●)\n                         |=|\n                        __|__\n                      //.=|=.〵.\n                     // .=|=. 〵.\n      ^----^        .〵 .=|=. //\n     (  {face} )        .〵(_=_)//\n     |     ||          (:| |:)\n  _  | |   ||           || ||\n  ||_!_|   |!           () ()\n   ---|  T |            || ||\n      |  | |            || ||\n      !__!_!           ==' '==")
                        if signature_move_trigger == True:
                            skeleton_moves = ['GRIMDARK AMBIENCE', 'BARRAGE O’ BONES']
                            signature_move = random.choice(skeleton_moves)
                            if signature_move == skeleton_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {skeleton_moves[0]}! ]")
                                print(f"[ A dark aura suddenly emanated in the area... leaving {player_name} FROZEN! ]")
                                frozen_check = True
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {skeleton_moves[1]}! ]")
                                print(f"[ Tons of animal bones were thrown in {player_name}'s direction, leaving them bruised! ]")
                                if kippi_stats[5] < (enemy_stats[2]+25) :
                                    kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                else:
                                    print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        if frozen_check == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                         .-.\n                        (●●)\n                         |=|\n                        __|__\n                      //.=|=.〵.\n                     // .=|=. 〵.\n      ^----^        .〵 .=|=. //\n     (  {face} )        .〵(_=_)//\n     |     ||          (:| |:)\n  _  | |   ||           || ||\n  ||_!_|   |!           () ()\n   ---|  T |            || ||\n      |  | |            || ||\n      !__!_!           ==' '==")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                break
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    random_chance = random.randint(1, 3)
                                    if random_chance == 1:
                                        item_drop_common(25)
                                    elif random_chance == 2:
                                        item_drop_uncommon(50)
                                    else:
                                        item_drop_rare(100)
                                    break
                        if frozen_check == True:
                            for i in range(2):
                                print(f"                         .-.\n                        (●●)\n                         |=|\n                        __|__\n                      //.=|=.〵.\n                     // .=|=. 〵.\n      ^----^        .〵 .=|=. //\n     (U'>.< )        .〵(_=_)//\n     |     ||          (:| |:)\n  _  | |   ||           || ||\n  ||_!_|   |!           () ()\n   ---|  T |            || ||\n      |  | |            || ||\n      !__!_!           ==' '==")
                                print(f"[ {player_name} is still terrified! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                            frozen_check = False
                            print(f"[ {player_name} has gotten over his petrification! ]")
                    break

            #wraith
            def wraith_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                eternal_check = False
                vanish_check = False
                
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(wraith_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than wraith
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                   .'``'.      ...\n                  :●  ● `....'`  ;\n      ^----^      `. o         :'\n     (  {face} )       `':          `.\n     |     ||         `:.          `.\n  _  | |   ||          : `.         `.\n  ||_!_|   |!          `..'`...       `.       `\n   ---|  T |                  `...     `.       '\n      |  | |                      ``...  `.   ,\n      !__!_!                           `````.")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if eternal_check == True:
                                print(f"[ The whispers in {player_name}'s head keep telling him to fall asleep! ]")
                                kippi_stats[3] -= 5
                                print(f"[ {player_name}'s health went down to {kippi_stats[3]}! ]")
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                random_chance = random.randint(1, 3)
                                if random_chance == 1:
                                    item_drop_common(25)
                                elif random_chance == 2:
                                    item_drop_uncommon(50)
                                else:
                                    item_drop_rare(50)
                                if eternal_check == True:
                                    print(f"[ {player_name} doesn't feel the taste of death lingering on their cat tongue anymore. Hooray! ]\n")
                                break
                            if signature_move_trigger == True:
                                wraith_moves = ['ETERNAL REST', 'VANISHING ACT']
                                signature_move = random.choice(wraith_moves)
                                if signature_move == wraith_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {wraith_moves[0]}! ]")
                                    print(f"[ {player_name} could hear voices in their head! Telling them that they should... fall... asleep...... ]")
                                    eternal_check = True
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {wraith_moves[1]}! ]")
                                    print(f"[ {enemy_stats[0]} vanished! ]")
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    break
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                    #wraith is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                   .'``'.      ...\n                  :●  ● `....'`  ;\n      ^----^      `. o         :'\n     (  {face} )       `':          `.\n     |     ||         `:.          `.\n  _  | |   ||          : `.         `.\n  ||_!_|   |!          `..'`...       `.       `\n   ---|  T |                  `...     `.       '\n      |  | |                      ``...  `.   ,\n      !__!_!                           `````.")
                        if signature_move_trigger == True:
                                wraith_moves = ['ETERNAL REST', 'VANISHING ACT']
                                signature_move = random.choice(wraith_moves)
                                if signature_move == wraith_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {wraith_moves[0]}! ]")
                                    print(f"[ {player_name} could hear voices in their head! Telling them that they should... fall... asleep...... ]")
                                    eternal_check = True
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {wraith_moves[1]}! ]")
                                    print(f"[ {enemy_stats[0]} vanished! ]")
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    break
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                   .'``'.      ...\n                  :●  ● `....'`  ;\n      ^----^      `. o         :'\n     (  {face} )       `':          `.\n     |     ||         `:.          `.\n  _  | |   ||          : `.         `.\n  ||_!_|   |!          `..'`...       `.       `\n   ---|  T |                  `...     `.       '\n      |  | |                      ``...  `.   ,\n      !__!_!                           `````.")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                            break
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if eternal_check == True:
                                print(f"[ The whispers in {player_name}'s head keep telling him to fall asleep! ]")
                                kippi_stats[3] -= 5
                                print(f"[ {player_name}'s health went down to {kippi_stats[3]}! ]")
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                random_chance = random.randint(1, 3)
                                if random_chance == 1:
                                    item_drop_common(25)
                                elif random_chance == 2:
                                    item_drop_uncommon(50)
                                else:
                                    item_drop_rare(50)
                                if eternal_check == True:
                                    print(f"[ {player_name} doesn't feel the taste of death lingering on their cat tongue anymore. Hooray! ]\n")
                                break
                    break

            #phoenix
            def phoenix_encounter():
                battle_mode = True
                signature_move_trigger = True
                burned_check = False
                stall_check = 0
                rebirth_counter = 0
                phoenix_stage_one = True

                while battle_mode and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(phoenix_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    # kippi is faster than phoenix
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1, 4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        if phoenix_stage_one == True:
                            print(f'''                    _,="( _  )"=,_\n                 _,'   〵_>〵_/    ',_\n                 .7,     (  )     ,〵.\n      ^----^      '/:,  .m  m.  ,:〵'\n     (  {face} )       ')",(/ 〵),"('\n     |     ||          '{'!!'}'\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!''')
                        else:
                            print(f"                                  ,\n                  _/|       |〵.\n                 /  |       |  〵\n                |   〵     /    |\n                | 〵 /     〵/  |\n                | 〵 |     |  / |\n                | 〵_〵/^〵/_ / |\n                |    --(//--    |\n                〵_ 〵     /  _/\n                  〵__  |  __/\n                     〵 _ /\n                     _/  〵_\n                    / _/|〵.〵 ,\n                     /  |  〵 \n      ^----^          / v 〵\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()

                        if battle_input not in ['fight', 'items', 'run']:
                            print("[ Please choose either to FIGHT, check your ITEMS, or RUN away. Silly kitty! ]")

                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0

                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                            break

                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                rebirth_counter += 1
                                if rebirth_counter == 2:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    break
                                else:
                                    print(f"[ The {enemy_stats[0]} turned into a pile of ash! ]")
                                    print("[ Wait... It's... REVIVING!? ]")
                                    enemy_stats[1] = phoenix_stats['HP']
                                    phoenix_stage_one = False
                                    print(f"[ {enemy_stats[0]} was reborn! ]")
                            if signature_move_trigger == True:
                                phoenix_moves = ['BURST O\' FLAMES', 'REVIVES']
                                signature_move = phoenix_moves[0]
                                print(f"[ {enemy_stats[0]} decided to use {phoenix_moves[0]}! ]")
                                print(f"[ The hottest of flames were blasted from the {enemy_stats[0]}'s beak... leaving {player_name} with painful burns over their body! ]")
                                if kippi_stats[5] < (enemy_stats[2]+25) :
                                    kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                else:
                                    print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break

                    # phoenix is faster than kippi
                    face = random.randint(1, 4)
                    if face == 1:
                        face = '•w•'
                    elif face == 2:
                        face = '•u•'
                    elif face == 3:
                        face = '^W^'
                    else:
                        face = '^u^'
                    if phoenix_stage_one == True:
                        print(f'''                    _,="( _  )"=,_\n                 _,'   〵_>〵_/    ',_\n                 .7,     (  )     ,〵.\n      ^----^      '/:,  .m  m.  ,:〵'\n     (  {face} )       ')",(/ 〵),"('\n     |     ||          '{'!!'}'\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!''')
                    else:
                        print(f"                                  ,\n                  _/|       |〵.\n                 /  |       |  〵\n                |   〵     /    |\n                | 〵 /     〵/  |\n                | 〵 |     |  / |\n                | 〵_〵/^〵/_ / |\n                |    --(//--    |\n                〵_ 〵     /  _/\n                  〵__  |  __/\n                     〵 _ /\n                     _/  〵_\n                    / _/|〵.〵 ,\n                     /  |  〵 \n      ^----^          / v 〵\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!")
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0:
                        if signature_move_trigger == True:
                            phoenix_moves = ['BURST O\' FLAMES', 'REVIVES']
                            signature_move = phoenix_moves[0]
                            print(f"[ {enemy_stats[0]} decided to use {phoenix_moves[0]}! ]")
                            print(f"[ The hottest of flames were blasted from the {enemy_stats[0]}'s beak... leaving {player_name} with painful burns over their body! ]")
                            if kippi_stats[5] < (enemy_stats[2]+25) :
                                kippi_stats[3] -= ((enemy_stats[2]+25) - kippi_stats[5])
                                print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                            else:
                                print(f"[ ...but {player_name} didn't budge at all! ] \n")
                            signature_move_trigger = False			
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break		
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1, 4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        if phoenix_stage_one == True:
                            print(f'''                    _,="( _  )"=,_\n                 _,'   〵_>〵_/    ',_\n                 .7,     (  )     ,〵.\n      ^----^      '/:,  .m  m.  ,:〵'\n     (  {face} )       ')",(/ 〵),"('\n     |     ||          '{'!!'}'\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!''')
                        else:
                            print(f"                                  ,\n                  _/|       |〵.\n                 /  |       |  〵\n                |   〵     /    |\n                | 〵 /     〵/  |\n                | 〵 |     |  / |\n                | 〵_〵/^〵/_ / |\n                |    --(//--    |\n                〵_ 〵     /  _/\n                  〵__  |  __/\n                     〵 _ /\n                     _/  〵_\n                    / _/|〵.〵 ,\n                     /  |  〵 \n      ^----^          / v 〵\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        if battle_input not in ['fight', 'items', 'run']:
                            print("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]")
                        if battle_input == 'items':
                            inventory_check()		
                        if battle_input == 'run':
                            print("You ran away, coward!")
                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                            break			
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                rebirth_counter += 1
                                if rebirth_counter == 2:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    kippi_stats[1] += enemy_stats[5]
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    break
                                else:
                                    print(f"[ The {enemy_stats[0]} turned into a pile of ash! ]")
                                    print("[ Wait... It's... REVIVING!? ]")
                                    enemy_stats[1] = phoenix_stats['HP']
                                    phoenix_stage_one = False
                                    print(f"[ {enemy_stats[0]} was reborn! ]")
                    break

            #hellhound
            def hellhound_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                paralyzed = False
                paralyzed_check = False
				
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(hellhound_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than hellhound
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        if paralyzed == False:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                  〵           /〵/〵___,\n                 _   ,___/〵/〵〵  ò    /\n                    〵     ó  〵)   XXX\n                       XXX     /    /〵/〵___,\n      ^----^             〵o-o/-o-o/   ò    /\n     (  {face} )              ) /     〵    XXX\n     |     ||             _|    /〵 〵_/\n  _  | |   ||          ,-/   _  〵/   〵\n  ||_!_|   |!         / (   /____,__|  )\n   ---|  T |         (  |_ (    ) 〵) _|\n      |  | |        _/ _)  〵   〵__/  (_\n      !__!_!      (,-(,(,(,/       〵,),),")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()

                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0

                            if battle_input == 'run':
                                print("You ran away, coward!")
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                break

                            if battle_input == 'fight':
                                if paralyzed_check == True:
                                    paralyzed_trigger = random.randint(1, 2)
                                    if paralyzed_trigger == 1:
                                        player_attacks(kippi_stats[4],enemy_stats[3])
                                        if enemy_stats[1] <= 0:
                                            print(f"[ {enemy_stats[0]} fainted! ]")
                                            print(f"[ {player_name} wins! ]\n")
                                            kippi_stats[1] += enemy_stats[5]
                                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                            break
                                    else:
                                        print(f"[ {player_name} is PARALYZED! The static in their body makes them unable to move a single inch! ]")
                                else:
                                    player_attacks(kippi_stats[4],enemy_stats[3])
                                    if enemy_stats[1] <= 0:
                                        print(f"[ {enemy_stats[0]} fainted! ]")
                                        print(f"[ {player_name} wins! ]\n")
                                        kippi_stats[1] += enemy_stats[5]
                                        print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                        random_chance = random.randint(1, 3)
                                        if random_chance == 1:
                                            item_drop_common(10)
                                        elif random_chance == 2:
                                            item_drop_uncommon(25)
                                        else:
                                            item_drop_rare(100)
                                        break
                                    stall_check = 0

                                if signature_move_trigger == True:
                                    hellhound_moves = ['HELLFIRE\'S BITE', 'INFERNAL ROAR']
                                    signature_move = random.choice(hellhound_moves)
                                    if signature_move == hellhound_moves[0]:
                                        print(f"[ {enemy_stats[0]} decided to use {hellhound_moves[0]}! ]")
                                        print(f"[ The fangs of {enemy_stats[0]} clamps onto {player_name}'s torso, not only digging through skin and flesh... but also bone! ]")
                                        if kippi_stats[5] < (enemy_stats[2]+100) :
                                            kippi_stats[3] -= ((enemy_stats[2]+100) - kippi_stats[5])
                                            print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                        else:
                                            print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                        signature_move_trigger = False
                                    else:
                                        print(f"[ {enemy_stats[0]} decided to use {hellhound_moves[1]}! ]")
                                        print(f"[ The roar of the {enemy_stats[0]} left them absolutely petrified, they feel like they're PARALYZED! ]")
                                        paralyzed_check = True
                                        signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
										
                    #hellhound is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0:
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                  〵           /〵/〵___,\n                 _   ,___/〵/〵〵  ò    /\n                    〵     ó  〵)   XXX\n                       XXX     /    /〵/〵___,\n      ^----^             〵o-o/-o-o/   ò    /\n     (  {face} )              ) /     〵    XXX\n     |     ||             _|    /〵 〵_/\n  _  | |   ||          ,-/   _  〵/   〵\n  ||_!_|   |!         / (   /____,__|  )\n   ---|  T |         (  |_ (    ) 〵) _|\n      |  | |        _/ _)  〵   〵__/  (_\n      !__!_!      (,-(,(,(,/       〵,),),")
                        if paralyzed == False:
                            if signature_move_trigger == True:
                                hellhound_moves = ['HELLFIRE\'S BITE', 'INFERNAL ROAR']
                                signature_move = random.choice(hellhound_moves)
                                if signature_move == hellhound_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {hellhound_moves[0]}! ]")
                                    print(f"[ The fangs of {enemy_stats[0]} clamps onto {player_name}'s torso, not only digging through skin and flesh... but also bone! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+100) :
                                        kippi_stats[3] -= ((enemy_stats[2]+100) - kippi_stats[5])
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {hellhound_moves[1]}! ]")
                                    print(f"[ The roar of the {enemy_stats[0]} left them absolutely petrified, they feel like they're PARALYZED! ]")
                                    paralyzed_check = True
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                            if paralyzed == False:
                                print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                                face = random.randint(1,4)
                                if face == 1:
                                    face = '•w•'
                                elif face == 2:
                                    face = '•u•'
                                elif face == 3:
                                    face = '^W^'
                                else:
                                    face = '^u^'
                                print(f"                  〵           /〵/〵___,\n                 _   ,___/〵/〵〵  ò    /\n                    〵     ó  〵)   XXX\n                       XXX     /    /〵/〵___,\n      ^----^             〵o-o/-o-o/   ò    /\n     (  {face} )              ) /     〵    XXX\n     |     ||             _|    /〵 〵_/\n  _  | |   ||          ,-/   _  〵/   〵\n  ||_!_|   |!         / (   /____,__|  )\n   ---|  T |         (  |_ (    ) 〵) _|\n      |  | |        _/ _)  〵   〵__/  (_\n      !__!_!      (,-(,(,(,/       〵,),),")
                                battle_input = input(f"[ What will {player_name} do? ]\n")
                                battle_input = battle_input.lower()
                                while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                    battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                    battle_input = battle_input.lower()
                                if battle_input == 'items':
                                    inventory_check()
                                if battle_input == 'run':
                                    print("You ran away, coward!")
                                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                    break
                                if battle_input == 'fight':
                                    if paralyzed_check == True:
                                        paralyzed_trigger = random.randint(1,2)
                                        if paralyzed_trigger == 1 :
                                            player_attacks(kippi_stats[4],enemy_stats[3])
                                            if enemy_stats[1] <= 0:
                                                print(f"[ {enemy_stats[0]} fainted! ]")
                                                print(f"[ {player_name} wins! ]\n")
                                                kippi_stats[1] += enemy_stats[5]
                                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                                random_chance = random.randint(1, 3)
                                                if random_chance == 1:
                                                    item_drop_common(10)
                                                elif random_chance == 2:
                                                    item_drop_uncommon(25)
                                                else:
                                                    item_drop_rare(100)
                                                break
                                        else:
                                            print(f"[ {player_name} is PARALYZED! The static in their body makes them unable to move a single inch! ]")
                                    else:
                                        player_attacks(kippi_stats[4],enemy_stats[3])
                                        if enemy_stats[1] <= 0:
                                            print(f"[ {enemy_stats[0]} fainted! ]")
                                            print(f"[ {player_name} wins! ]\n")
                                            kippi_stats[1] += enemy_stats[5]
                                            print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                            break
                    break

            #zealous...?
            def zealous_encounter():
                battle_mode = True
                signature_move_trigger = True
                stall_check = 0
                burned_check = False
                deflect_check = False
                deflect_counter = 0
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(zealous_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than zealous
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                       .     _///_,\n                     .      / ` ' '>\n                       )   o'  __/_'>\n                      (   /  _/  )_〵'>\n                       ' "__/   /_/〵_>\n                           ____/_/_/_/\n                          /,---, _/ /\n                         ""  /_/_/_/\n      ^----^                /_(_(_(_                〵\n     (  {face} )              (   〵_〵_〵              )〵\n     |     ||              〵'__〵_〵_〵_            ).〵\n  _  | |   ||               //____|___〵_)           )_/\n  ||_!_|   |!               |  _  〵'__'_(           /'\n   ---|  T |                〵_ (-'〵'___'_〵     __,'_'\n      |  | |                 __) 〵 〵〵___(_   __/.__,'\n      !__!_!              ,((,-,__〵  '", __〵_/. __,'\n                                       '"./_._._-''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            if deflect_check == True:
                                print(f"[ {player_name} attacks the {enemy_stats[0]}! ]")
                                print(f"[ ... But {enemy_stats[0]} managed to deflect it! ]\n")
                                deflect_counter += 1
                                if deflect_counter == 2:
                                    print(f"[ {enemy_stats[0]}'s barriers have been destroyed! Now's {player_name}'s chance to attack! ]\n")
                                    deflect_check = False
                            else:
                                player_attacks(kippi_stats[4],enemy_stats[3])
                            if burned_check == True:
                                kippi_burned()                                                       
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                kippi_stats[1] += enemy_stats[5]
                                print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'=,= )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                                if burned_check == True:
                                    print(f"[ {player_name} fluffy body isn't burning anymore. Hooray! ]\n")
                                break
                            if signature_move_trigger == True:
                                zealous_moves = ['BREATH O\' FLAMES', 'SEDIMENTARY SHIELD', 'ASHES TO ASHES, DUST TO DUST']
                                signature_move = random.choice(zealous_moves)
                                if signature_move == zealous_moves[0]:
                                    print(f"[ {enemy_stats[0]} decided to use {zealous_moves[0]}! ]")
                                    print(f"[ {player_name} feels like a roasted chicken on a barbeque! ]\n")
                                    kippi_stats[5] -= 20
                                    print(f"[ {player_name}'s defence went down to {kippi_stats[5]}! ]\n")
                                    burned_check = True
                                    if burned_check == True:
                                        kippi_burned()
                                    signature_move_trigger = False
                                elif signature_move == zealous_moves[1]:
                                    print(f"[ {enemy_stats[0]} decided to use {zealous_moves[1]}! ]")
                                    print(f"[ A sheild of gravel and magma surrounds {enemy_stats[0]}... leaving him impenetrable! ]")
                                    deflect_check = True
                                    signature_move_trigger = False
                                else:
                                    print(f"[ {enemy_stats[0]} decided to use {zealous_moves[2]}! ]")
                                    print(f"[ {enemy_stats[0]} seems to be reciting some... mysterious incantation! Just as {player_name} was trying to deciper what {enemy_stats[0]} was saying... a large METEORITE headed towards {player_name}! ]")
                                    if kippi_stats[5] < (enemy_stats[2]+100) :
                                        kippi_stats[3] -= ((enemy_stats[2]+100) - kippi_stats[5])
                                        print(f"[ {player_name} was heavily wounded! ]")
                                        print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                    else:
                                        print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                    signature_move_trigger = False
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                    #zealous is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 :
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                       .     _///_,\n                     .      / ` ' '>\n                       )   o'  __/_'>\n                      (   /  _/  )_〵'>\n                       ' "__/   /_/〵_>\n                           ____/_/_/_/\n                          /,---, _/ /\n                         ""  /_/_/_/\n      ^----^                /_(_(_(_                〵\n     (  {face} )              (   〵_〵_〵              )〵\n     |     ||              〵'__〵_〵_〵_            ).〵\n  _  | |   ||               //____|___〵_)           )_/\n  ||_!_|   |!               |  _  〵'__'_(           /'\n   ---|  T |                〵_ (-'〵'___'_〵     __,'_'\n      |  | |                 __) 〵 〵〵___(_   __/.__,'\n      !__!_!              ,((,-,__〵  '", __〵_/. __,'\n                                       '"./_._._-''')
                        if signature_move_trigger == True:
                            zealous_moves = ['BREATH O\' FLAMES', 'SEDIMENTARY SHIELD', 'ASHES TO ASHES, DUST TO DUST']
                            signature_move = random.choice(zealous_moves)
                            if signature_move == zealous_moves[0]:
                                print(f"[ {enemy_stats[0]} decided to use {zealous_moves[0]}! ]")
                                print(f"[ {player_name} feels like a roasted chicken on a barbeque! ]\n")
                                kippi_stats[5] -= 20
                                print(f"[ {player_name}'s defence went down to {kippi_stats[5]}! ]\n")
                                burned_check = True
                                if burned_check == True:
                                    kippi_burned()
                                signature_move_trigger = False
                            elif signature_move == zealous_moves[1]:
                                print(f"[ {enemy_stats[0]} decided to use {zealous_moves[1]}! ]")
                                print(f"[ A sheild of gravel and magma surrounds {enemy_stats[0]}... leaving him impenetrable! ]")
                                deflect_check = True
                                signature_move_trigger = False
                            else:
                                print(f"[ {enemy_stats[0]} decided to use {zealous_moves[2]}! ]")
                                print(f"[ {enemy_stats[0]} seems to be reciting some... mysterious incantation! Just as {player_name} was trying to deciper what {enemy_stats[0]} was saying... a large METEORITE headed towards {player_name}! ]")
                                if kippi_stats[5] < (enemy_stats[2]+100) :
                                    kippi_stats[3] -= ((enemy_stats[2]+100) - kippi_stats[5])
                                    print(f"[ {player_name} was heavily wounded! ]")
                                    print(f"[ {player_name}'s health is down to {kippi_stats[3]}! ] \n")
                                else:
                                    print(f"[ ...but {player_name} didn't budge at all! ] \n")
                                signature_move_trigger = False  
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                       .     _///_,\n                     .      / ` ' '>\n                       )   o'  __/_'>\n                      (   /  _/  )_〵'>\n                       ' "__/   /_/〵_>\n                           ____/_/_/_/\n                          /,---, _/ /\n                         ""  /_/_/_/\n      ^----^                /_(_(_(_                〵\n     (  {face} )              (   〵_〵_〵              )〵\n     |     ||              〵'__〵_〵_〵_            ).〵\n  _  | |   ||               //____|___〵_)           )_/\n  ||_!_|   |!               |  _  〵'__'_(           /'\n   ---|  T |                〵_ (-'〵'___'_〵     __,'_'\n      |  | |                 __) 〵 〵〵___(_   __/.__,'\n      !__!_!              ,((,-,__〵  '", __〵_/. __,'\n                                       '"./_._._-''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()                            
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            if deflect_check == True:
                                print(f"[ {player_name} attacks the {enemy_stats[0]}! ]")
                                print(f"[ ... But {enemy_stats[0]} managed to deflect it! ]\n")
                                deflect_counter += 1
                                if deflect_counter == 2:
                                    print(f"[ {enemy_stats[0]}'s barriers have been destroyed! Now's {player_name}'s chance to attack! ]\n")
                                    deflect_check = False
                            else:
                                player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                break
                            stall_check = 0
                    break

            #zealous, the real one
            def zealous_the_real_one_encounter():
                battle_mode = True
                stall_check = 0
                deteriorate_count = 0
                deathdoor = False
                signature_move_trigger = True
                
                while battle_mode == True and kippi_stats[3] > 0:
                    global enemy_stats
                    enemy_stats = list(wizard_stats.values())
                    speed_check(kippi_stats[6],enemy_stats[4])
                    #kippi is faster than wizard
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0 and deteriorate_count == 0 :
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f"                        ___\n                  〵   /o  _〵 __\n                 _    /  o〵  |_ 〵\n      ^----^          ^____^   |〵〵\n     (  {face} )        ( ò-ó =)__*_〵〵\n     |     ||        ||〵/  ____ |'/\n  _  | |   ||        ||    |    / /\n  ||_!_|   |!        !|    |   / /\n   ---|  T |          | T  |  / /\n      |  | |          | |  | /_/\n      !__!_!          !_!__!")
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if deteriorate_count == 0 and enemy_stats[1] <= 75:
                                print(f"[ With {player_name}'s attack, {enemy_stats[0]} stumbles to the ground. His cane laying bare on Volcana's gravelly grounds. Just as {player_name} was about to deal a final blow, though, {enemy_stats[0]} giggles maniacally. ]")
                                print(f'''[ "Oh... Silly {player_name}. Have you forgotten who I am? Who I WAS?" His eyes stares deeply into {player_name}'s. ]''')
                                print(f'''[ "That... that wasn't even an ounce of my full power!" As {enemy_stats[0]} began to stand up... ]''')
                                print(f"[ {enemy_stats[0]} decided to DETERIORATE! ]")
                                deteriorate_count += 1
                            else:
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                if kippi_stats[3] <= 0:
                                    break
                    #wizard is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 and deteriorate_count == 0:
                        if deteriorate_count == 0 and enemy_stats[1] <= 75:
                            print(f"[ With {player_name}'s attack, {enemy_stats[0]} stumbles to the ground. His cane laying bare on Volcana's gravelly grounds. Just as {player_name} was about to deal a final blow, though, {enemy_stats[0]} giggles maniacally. ]")
                            print(f'''[ "Oh... Silly {player_name}. Have you forgotten who I am? Who I WAS?" His eyes stares deeply into {player_name}'s. ]''')
                            print(f'''[ "That... that wasn't even an ounce of my full power!" As {enemy_stats[0]} began to stand up... ]''')
                            print(f"[ {enemy_stats[0]} decided to DETERIORATE! ]")
                            deteriorate_count += 1
                            break
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f"                        ___\n                  〵   /o  _〵 __\n                 _    /  o〵  |_ 〵\n      ^----^          ^____^   |〵〵\n     (  {face} )        ( ò-ó =)__*_〵〵\n     |     ||        ||〵/  ____ |'/\n  _  | |   ||        ||    |    / /\n  ||_!_|   |!        !|    |   / /\n   ---|  T |          | T  |  / /\n      |  | |          | |  | /_/\n      !__!_!          !_!__!")
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    break
                    #kippi is faster than zealousx
                    while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0 and deteriorate_count == 1:
                        print('''[ "BEHOLD! I, ZEALOUS! THE MOST POWERFUL MAGICAL BEING TO EVER EXIST!" ]''')
                        enemy_stats = list(zealousx_stats.values())
                        #kippi is faster than zealousx
                        while kippi_stats[6] >= enemy_stats[4] and kippi_stats[3] > 0:
                            print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                            face = random.randint(1,4)
                            if face == 1:
                                face = '•w•'
                            elif face == 2:
                                face = '•u•'
                            elif face == 3:
                                face = '^W^'
                            else:
                                face = '^u^'
                            print(f'''                                                                 ,....,.\n                                                             ..''   .'\n                                                          .'"       |\n                                                       .''          〵\n                                                    .''              〵.\n                                                  .'                  .".,\n                                                ,:'             ..,'"'   '...,..::/"".....\n                                              /'"          .,'"'  .,',:,'""'         .,''\n                                            ,'.'      .,'"' ..,""" ""         .'   ."'\n                                          ,'  〵, ..,''  .,''. ..,'""        ./   ."\n                                        ."     .,"  .,'".,"'./           ..''   /\n                                       ,'    .'  ./'.,"'  .'  "'     ." '.     /\n                                     .'   ./' ./"."〵,..,''     '" ../,    ,  |\n                                    ,   ./' .'./'|/     ............        ',|\n                                   /   /' ,'.".,'""〵.....'""""""""'  .::/'.., |\n                                  /  ." ,' ':〵 """  |  ,     ''          '""   〵\n                                 /  /'.''. |:::::::""' ,' ' ''. ".,.,  """'    .""\n                                | ." /.,":. ""..,   "〵'.."'..  ;"'  '〵.'""" ."\n                                | 〵.:〵.   '""./〵〵 | ' '" .,"".           /\n                                /〵'   '"..     ", 〵〵,',     "'..  .,     '\n                               /.'",''..,  '〵,  '〵 ". '〵'.,    , "'. "'.,|\n                              .,'        '". ',   〵 '.".. ''../'      "" __〵\n                              '            〵,',   〵  '.'〵..,  ","'  .'"\n                                            |  |    '| ,〵""'〵/.  |  ."\n                               ."          .|  .    / / ./'. '.".' /'\n                               /'        ..|':"""〵././ /   "  '/〵.'\n                              //  ./  .'"    /' ./'.' .'  | ..,  ':|\n                            ./:  ,/   |",   ' ."'  :  '   |    .../:,\n                           .'.'〵/   /.'           ''  .,   ..〵'\n                         〵.〵".'   /"    ,"'〵...,    "〵.〵| ",\n                        /    ./""""'   ..:    ',|  "".,    '〵  ',\n                     .,' "'  〵|     "".'".    '/  .| '〵.    ", '〵\n                    /         〵.    ../,   "./ '〵 |' 〵/"" '".'〵 〵\n                   /   〵〵:. 〵,"〵::'  ./""'    ./|  .'     .'"/| '|\n                   ' ,"〵:"/"""  /'  ."〵' .., |:| .| |'   .'' .〵|  ',\n                   |/  / /'    .'| /  |.〵,    /'"/. | |:〵..," .||  〵\n                   '' /.'      //〵'  '〵/〵:. :,/"'::.  ,   ..::' |  |\n                               ||'/,   '〵〵/"〵'/|   '〵 '"::::"| | .|\n                               || 〵〵     "".   ...,  '.  〵〵..|  |' |\n                               ||  "〵,        .".〵, ". ',| 〵 '|  |  |\n                                '             |〵|'|〵/.''〵||〵  | |  |\n                                              ||〵/"/|'〵, ., / / /  ,\n                                                ' 〵  "   '"  / / .' /\n                                                   '      .'".' .' /\n                                                     ..'"'.." ." ."\n                                                 .,"":.'""..'" ."\n                                            .,:'"'"'  .'"  ..'"\n                                          ." ."'..'""...,"'\n                                       .." "    , ""'\n                                      /  . :/"'\n                                    .'  :/'\n                                   /  /'\n                                  / .'\n                                 / '\n                                /.'\n                                '\n      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!''')
                            battle_input = input(f"[ What will {player_name} do? ]\n")
                            battle_input = battle_input.lower()
                            while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                                battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                                battle_input = battle_input.lower()
                            if battle_input == 'items':
                                inventory_check()
                                stall_check += 1
                            if stall_check == 3:
                                print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                                enemy_attacks(kippi_stats[5],enemy_stats[2])
                                stall_check = 0
                            if battle_input == 'run':
                                print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                            if battle_input == 'fight':
                                player_attacks(kippi_stats[4],enemy_stats[3])
                                if enemy_stats[1] <= 0:
                                    print(f"[ {enemy_stats[0]} fainted! ]")
                                    print(f"[ {player_name} wins! ]\n")
                                    break
                                if deathdoor == True:
                                    print(f"[ {player_name}'s tiny body desperately tries to hold on a little longer... ]")
                                    kippi_stats[3] -= 10
                                    print(f"[ {player_name}'s health went down to {kippi_stats[3]}! ]")
                                if signature_move_trigger == True:
                                    print(f'''[ "Haw-haw-haw!" {enemy_stats[0]} laughs. "How does it feel to be KNOCKING ON DEATH'S DOOR!?" ]''')
                                    print(f"[ As soon as he said that, {player_name} could feel their whole body becoming more tired by the second... ]")
                                    deathdoor = True
                                    signature_move_trigger = False
                                else:
                                    enemy_attacks(kippi_stats[5],enemy_stats[2])
                                    if kippi_stats[3] <= 0:
                                        break
                    #zealousx is faster than kippi
                    while kippi_stats[6] < enemy_stats[4] and kippi_stats[3] > 0 and deteriorate_count == 1:
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                                                                 ,....,.\n                                                             ..''   .'\n                                                          .'"       |\n                                                       .''          〵\n                                                    .''              〵.\n                                                  .'                  .".,\n                                                ,:'             ..,'"'   '...,..::/"".....\n                                              /'"          .,'"'  .,',:,'""'         .,''\n                                            ,'.'      .,'"' ..,""" ""         .'   ."'\n                                          ,'  〵, ..,''  .,''. ..,'""        ./   ."\n                                        ."     .,"  .,'".,"'./           ..''   /\n                                       ,'    .'  ./'.,"'  .'  "'     ." '.     /\n                                     .'   ./' ./"."〵,..,''     '" ../,    ,  |\n                                    ,   ./' .'./'|/     ............        ',|\n                                   /   /' ,'.".,'""〵.....'""""""""'  .::/'.., |\n                                  /  ." ,' ':〵 """  |  ,     ''          '""   〵\n                                 /  /'.''. |:::::::""' ,' ' ''. ".,.,  """'    .""\n                                | ." /.,":. ""..,   "〵'.."'..  ;"'  '〵.'""" ."\n                                | 〵.:〵.   '""./〵〵 | ' '" .,"".           /\n                                /〵'   '"..     ", 〵〵,',     "'..  .,     '\n                               /.'",''..,  '〵,  '〵 ". '〵'.,    , "'. "'.,|\n                              .,'        '". ',   〵 '.".. ''../'      "" __〵\n                              '            〵,',   〵  '.'〵..,  ","'  .'"\n                                            |  |    '| ,〵""'〵/.  |  ."\n                               ."          .|  .    / / ./'. '.".' /'\n                               /'        ..|':"""〵././ /   "  '/〵.'\n                              //  ./  .'"    /' ./'.' .'  | ..,  ':|\n                            ./:  ,/   |",   ' ."'  :  '   |    .../:,\n                           .'.'〵/   /.'           ''  .,   ..〵'\n                         〵.〵".'   /"    ,"'〵...,    "〵.〵| ",\n                        /    ./""""'   ..:    ',|  "".,    '〵  ',\n                     .,' "'  〵|     "".'".    '/  .| '〵.    ", '〵\n                    /         〵.    ../,   "./ '〵 |' 〵/"" '".'〵 〵\n                   /   〵〵:. 〵,"〵::'  ./""'    ./|  .'     .'"/| '|\n                   ' ,"〵:"/"""  /'  ."〵' .., |:| .| |'   .'' .〵|  ',\n                   |/  / /'    .'| /  |.〵,    /'"/. | |:〵..," .||  〵\n                   '' /.'      //〵'  '〵/〵:. :,/"'::.  ,   ..::' |  |\n                               ||'/,   '〵〵/"〵'/|   '〵 '"::::"| | .|\n                               || 〵〵     "".   ...,  '.  〵〵..|  |' |\n                               ||  "〵,        .".〵, ". ',| 〵 '|  |  |\n                                '             |〵|'|〵/.''〵||〵  | |  |\n                                              ||〵/"/|'〵, ., / / /  ,\n                                                ' 〵  "   '"  / / .' /\n                                                   '      .'".' .' /\n                                                     ..'"'.." ." ."\n                                                 .,"":.'""..'" ."\n                                            .,:'"'"'  .'"  ..'"\n                                          ." ."'..'""...,"'\n                                       .." "    , ""'\n                                      /  . :/"'\n                                    .'  :/'\n                                   /  /'\n                                  / .'\n                                 / '\n                                /.'\n                                '\n      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!''')
                        print('''[ "BEHOLD! I, ZEALOUS! THE MOST POWERFUL MAGICAL BEING TO EVER EXIST!" ]''')
                        if deathdoor == True:
                            print(f"[ {player_name}'s tiny body desperately tries to hold on a little longer... ]")
                            kippi_stats[3] -= 10
                            print(f"[ {player_name}'s health went down to {kippi_stats[3]}! ]")
                        if signature_move_trigger == True:
                            print(f'''[ "Haw-haw-haw!" {enemy_stats[0]} laughs. "How does it feel to be KNOCKING ON DEATH'S DOOR!?" ]''')
                            print(f"[ As soon as he said that, {player_name} could feel their whole body becoming more tired by the second... ]")
                            deathdoor = True
                            signature_move_trigger = False
                        else:
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            if kippi_stats[3] <= 0:
                                break
                        print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                        print(f'''                                                                 ,....,.\n                                                             ..''   .'\n                                                          .'"       |\n                                                       .''          〵\n                                                    .''              〵.\n                                                  .'                  .".,\n                                                ,:'             ..,'"'   '...,..::/"".....\n                                              /'"          .,'"'  .,',:,'""'         .,''\n                                            ,'.'      .,'"' ..,""" ""         .'   ."'\n                                          ,'  〵, ..,''  .,''. ..,'""        ./   ."\n                                        ."     .,"  .,'".,"'./           ..''   /\n                                       ,'    .'  ./'.,"'  .'  "'     ." '.     /\n                                     .'   ./' ./"."〵,..,''     '" ../,    ,  |\n                                    ,   ./' .'./'|/     ............        ',|\n                                   /   /' ,'.".,'""〵.....'""""""""'  .::/'.., |\n                                  /  ." ,' ':〵 """  |  ,     ''          '""   〵\n                                 /  /'.''. |:::::::""' ,' ' ''. ".,.,  """'    .""\n                                | ." /.,":. ""..,   "〵'.."'..  ;"'  '〵.'""" ."\n                                | 〵.:〵.   '""./〵〵 | ' '" .,"".           /\n                                /〵'   '"..     ", 〵〵,',     "'..  .,     '\n                               /.'",''..,  '〵,  '〵 ". '〵'.,    , "'. "'.,|\n                              .,'        '". ',   〵 '.".. ''../'      "" __〵\n                              '            〵,',   〵  '.'〵..,  ","'  .'"\n                                            |  |    '| ,〵""'〵/.  |  ."\n                               ."          .|  .    / / ./'. '.".' /'\n                               /'        ..|':"""〵././ /   "  '/〵.'\n                              //  ./  .'"    /' ./'.' .'  | ..,  ':|\n                            ./:  ,/   |",   ' ."'  :  '   |    .../:,\n                           .'.'〵/   /.'           ''  .,   ..〵'\n                         〵.〵".'   /"    ,"'〵...,    "〵.〵| ",\n                        /    ./""""'   ..:    ',|  "".,    '〵  ',\n                     .,' "'  〵|     "".'".    '/  .| '〵.    ", '〵\n                    /         〵.    ../,   "./ '〵 |' 〵/"" '".'〵 〵\n                   /   〵〵:. 〵,"〵::'  ./""'    ./|  .'     .'"/| '|\n                   ' ,"〵:"/"""  /'  ."〵' .., |:| .| |'   .'' .〵|  ',\n                   |/  / /'    .'| /  |.〵,    /'"/. | |:〵..," .||  〵\n                   '' /.'      //〵'  '〵/〵:. :,/"'::.  ,   ..::' |  |\n                               ||'/,   '〵〵/"〵'/|   '〵 '"::::"| | .|\n                               || 〵〵     "".   ...,  '.  〵〵..|  |' |\n                               ||  "〵,        .".〵, ". ',| 〵 '|  |  |\n                                '             |〵|'|〵/.''〵||〵  | |  |\n                                              ||〵/"/|'〵, ., / / /  ,\n                                                ' 〵  "   '"  / / .' /\n                                                   '      .'".' .' /\n                                                     ..'"'.." ." ."\n                                                 .,"":.'""..'" ."\n                                            .,:'"'"'  .'"  ..'"\n                                          ." ."'..'""...,"'\n                                       .." "    , ""'\n                                      /  . :/"'\n                                    .'  :/'\n                                   /  /'\n                                  / .'\n                                 / '\n                                /.'\n                                '\n      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||\n  ||_!_|   |!\n   ---|  T |\n      |  | |\n      !__!_!''')
                        battle_input = input(f"[ What will {player_name} do? ]\n")
                        battle_input = battle_input.lower()
                        while not battle_input == 'fight' and not battle_input == 'items' and not battle_input == 'run':
                            battle_input = input("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]\n")
                            battle_input = battle_input.lower()
                        if battle_input == 'items':
                            inventory_check()
                            stall_check += 1
                        if stall_check == 3:
                            print(f"[ {player_name} took too long staring at their bag... that the {enemy_stats[0]} decided to attack while they're distracted! ]")
                            enemy_attacks(kippi_stats[5],enemy_stats[2])
                            stall_check = 0
                        if battle_input == 'run':
                            print(f"[ {player_name}'s legs keep shaking from being too scared... They can't run away! ]")
                        if battle_input == 'fight':
                            player_attacks(kippi_stats[4],enemy_stats[3])
                            if enemy_stats[1] <= 0:
                                print(f"[ {enemy_stats[0]} fainted! ]")
                                print(f"[ {player_name} wins! ]\n")
                                break
                            stall_check = 0
                    break

            #modes
            battle_mode = False
            enemy_encounter_check = False
            name_check = True

            if continue_game == True: #picheolin
                player_name = checkpoint_data["player_name"]
                kippi_stats = checkpoint_data["kippi_stats"]
                inventory = checkpoint_data["inventory"]                
                head = checkpoint_data["head"]
                body = checkpoint_data["body"]
                feet = checkpoint_data["feet"]
                hand = checkpoint_data["hand"]
                meanie_counter = checkpoint_data["meanie_counter"]

            if inventory == ['']:
                inventory = []
            if head == ['']:
                head = []
            if body == ['']:
                body = []
            if feet == ['']:
                feet = []
            if hand == ['']:
                hand = []
            
            while kippi_stats[0] == 0:
                print("                  [〵\n                  |〵)                               ____\n                  |                               __(_   )__\n                  Y〵         ___               _(          )\n                 T  〵      __)  )--.          (     )-----`\n                J    〵  ,-(         )_         `---'\n               Y/T`-._〵(     (       _)                 __\n               /[|   ]|  `-(__  ___)-`  |〵          ,-(  __)\n               | |    |      (__)       J'         (     )\n   _           | |  ] |    _           /;〵          `-  '\n  (,,)        [| |    |    L'         /;  〵\n             /||.| /〵|   /〵        /.,-._〵       ___ _\n            /_|||| || |  /  〵       | |{  |       (._.'_)\n  /〵       | 〵|| '` |_ _ {|        | | U |   /〵\n /v^〵/〵  `|  Y | [  '-' '--''-''-=-'`'   | ,`^v〵/〵,`〵\n/ ,'./  〵` |[   |       [     __   L    ] |      /^v〵  〵\n,'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_\n--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y\n   Y Y  --;`~T   |      }  〵####U|[〵 _,.-(^) ,-'  _  (^)__  _\n  Y  YY   ;'~~l  |   L    [|〵###U'E'〵 〵〵Y-` _  (^) _Y  _\n Y  Y Y   ;〵~〵 | [      _,'-〵`= = '.〵_ ,`   (^)(^) (^) (^)\n     --   ;〵~~〵|  _,.-'`_  `.〵_..-'=   _ . ,_ Y_ Y_ _Y  _Y__\n    _    _; 〵~( Y``   Y (^) / `,      (^)      _   (^) (^)\n   (^)  (^)`._~ /  L 〵 _.Y'`  _  ` --  Y - - -(^) - Y - Y -\n    Y    Y    `'--..,-'`      (^)   _  -    _   Y ____\n      --           _    _ --   Y   (^)   _ (^)  ===   ----\n          __   -  (^)  (^)      --- Y   (^) Y\n      _            Y    Y                Y")
                print("[ Once, there was a bustling little town that was considered a home for thousands of kitties, called Nyuwuwovilla. The residents go about their day-today life contributing to society. However, there was one that was not like the other kitties... And that one kitty is you, Kippi! ]\n")
                print("[ Dishevelled and ignored by the whole town, you wander aimlessly around the whole area with your head down. You have been trying to find a job that was suited for you, but no matter how hard you tried, you managed to mess it up. You’ve broken more plates than you can count during your time as a waiter for a run-down restaurant, lost too many parcels that the whole town literally banned you from ever handling delivery jobs, and worst of all, you've almost got yourself arrested because you almost fed a baby kitty to an ogre, thinking she was its mom! Because of this, you are left with not a single penny under your name... ]\n")
                print("[ As you were walking, you saw a dark, murky space between two buildings. While it is not an ideal place to sleep in, heck, you even thought that even sleeping on a pile of rocks would be better than this, you did not want to risk getting charged— again— by the kitty police for being a 'public nuisance'. As you sigh, lie down, and tuck your legs into your body to get a good night's rest, a kitty with a long beard, a silly-looking hat and a crooked stick decides to intrude in your personal space. ]\n")
                wizard_emotes('excited')
                print('''[ “Gweetings, o' fewwowo kitfowk! I couwdn't hewp but notice dat you've been sweepim hewe, pitifuwwy, aww awone! Does a kittie wike you not have a home fow youwsewf?" ]\n''')
                dialogue_options = range(1,4)
                for n in dialogue_options:
                    if n == 1:
                        print(f"{n}. [ No. ]")
                    if n == 2:
                        print(f"{n}. [ What awe you tawkim about? Dis is mie home. ]")
                    if n == 3:
                        print(f"{n}. [ Is dawe a cospwayim event somewhewe? Whie awe you dwessed wike dat? ]\n")
                dialogue_choice = input("[ What would you like to say to him? ]\n")
                while dialogue_choice not in map(str, dialogue_options):
                    print('''[ The wizard looks at you, confused. "Uh... Couwd you be a wittwe bit mowe cweawew?" ]''')
                    dialogue_choice = input("[ What would you like to say to him? ]\n")
                if dialogue_choice == '1':
                    wizard_emotes('happier')
                    print("[ The strange-looking kitty in front of Kippi smiles, strangely. ]")
                    print('''[ “Spwendid!” He exclaims. Kippi is confused on why he would say that, but they decided to shrug it off. Perhaps he’s just a little eccentric. ]''')
                elif dialogue_choice == '2':
                    wizard_emotes('happier')
                    print("[ The kitty looks worried for Kippi for a second, but quickly realises their sarcastic tone, and laughs. ]\n")
                    print('''[ “Haw-haw-haw! You'we a jokew, even in dis twoubwim situation, huh? I wike dat!” He gives a thumbs up— or… more like a paw up! ]\n''')
                else:
                    wizard_emotes('angry')
                    print("[The kitty’s left eye twitches when you said that.]")
                    print('''[“Wowo! Howo wude!” He growls— but quickly regains his composure.]''')
                    print('''[“Weww... Whiwe I don't wike what you've just said about mie wooks, pewhaps you'we just misinfowmed!” The kitty continues.]\n''')
                    meanie_counter += 1
                wizard_emotes('happy')
                print('''[“Y'see, you maie not knowo about dis, but I, in fact, am a wowwdwide-knowon wizawd! 'Da Wizawd of Pawz' is what daie caww me. Haven't you heawd of me?”]\n''')
                for n in dialogue_options:
                    if n == 1:
                        print(f"{n}. [ Nod. ]")
                    elif n == 2:
                        print(f"{n}. [ Shake your head. ]")
                    else:
                        print(f"{n}. [ Stare at him, blankly. ]\n")
                dialogue_choice = input("[ What would you like to say to him? ]\n")
                while dialogue_choice not in map(str, dialogue_options):
                    print('''[ The wizard looks at you, confused. "Uh... Couwd you be a wittwe bit mowe cweawew?" ]''')
                    dialogue_choice = input("[ What would you like to say to him? ]\n")    
                if dialogue_choice == '1':
                    wizard_emotes('happy')
                    print("[The wizard smiles. “Gweat! Den, I have a favouw to ask of you…”]")   
                elif dialogue_choice == '2':
                    wizard_emotes('worried')
                    print('''[The wizard clears his throat. “W-weww, awthuff I wouwd wike to intwoduce mysewf pwopewwie to you, unfowtunatewy, I don’t have much time fow dat!”]\n''')
                    print("[He looks… slightly worried? “Because…”]")   
                else:
                    wizard_emotes('deadpan')
                    print('''[The wizard stares back at Kippi, deadpan, waiting for an answer. After a few seconds, he realises that they had no idea what he is talking about.]\n''')
                    print('''[“W-weww, uh… A-anyways!” He clears his throat… and Kippi could swear that he muttered something to himself. “I have a favouw to ask of you!”]\n''')
                    meanie_counter += 1
                wizard_emotes('disappointed')
                print('''[“If a kittie wike you haven’t heawd about da news yet…”  He takes a deep sigh. “The wowwd is tuwnim upside dowon! Da animaws dat wewe once dociwe and fwiendwy… awe tuwnim in on us kitfowk! Deie keep attackim ouw peopwe… weft and wight. And some of dam even got supewnatuwaw powoews!” The wizard exclaims, worryingly. “This… dis is aww da wowk of…” The wizard dramatically pauses. “Zealous!”]\n''')
                for n in dialogue_options:
                    if n == 1:
                        print(f"{n}. [ Zeawous? ]")
                    elif n == 2:
                        print(f"{n}. [ Wowo... Dat sounds coow! ]")
                    elif n == 3:
                        print(f"{n}. [ What's dis got to do with me? ]\n")
                dialogue_choice = input("[ What would you like to say to him? ]\n")
                while dialogue_choice not in map(str, dialogue_options):
                    print('''[ The wizard looks at you, confused. "Uh... Couwd you be a wittwe bit mowe cweawew?" ]''')
                    dialogue_choice = input("[ What would you like to say to him? ]\n")    
                if dialogue_choice == '1':
                    pass
                elif dialogue_choice == '2':
                    wizard_emotes('happier')
                    print("[“Hah! I know ri— Uh… I mean—” He stutters.]\n")
                else:
                    wizard_emotes('deadpan')
                    print('''[Kippi could swear that they could see the Wizard of Pawz glaring at them for a split second. But… maybe it was just their imagination?]\n''')
                    meanie_counter += 1
                wizard_emotes('sassier')
                print('''[“Yes… Zealous! Awmost evewie kitfowk in dis kingdom onwie dought of him as a myth… but I bewieve he exists! In fact, I bewieve he’s da one doim aww of dis!” The wizard exclaims, a hint of disappointment could be inferred from how he’s speaking. "Fwom da dousands of witewatuwe I’ve gadawed about da histowie of Nyuwuwovilla, he was just a weguwaw kitfowk, wike you! Da onwie dim dat diffews him fwom da odaw kitfowk, dough… are his magicaw powoews!” His eyes shine like bright, white stars. “Awthuff us kitfowk awe abwe to weawn magic, his wevew of magic is— is— odawwowwdwy!” He clenched his paws.]\n''')   
                print('''[“He… couwd’ve used dam fow da good of ouw peopwe… but instead…” The wizard turns his head to his side, looking ashamed. “He used his powoew to twie and contwow us… and take ovew ouw kingdom fow nefawious means! Instead of wantim to hewp us, he wanted wiches, and powoew, evewything— and anythim you couwd dim of!” He growls, angrily. Then, he tries to keep calm, not wanting to be angrier than he already is. “Thus, he used his magicaw powoews to twansfowm into a dwagon, twyim to destwoie da whowe kingdom aftew not gettim what he wanted.” He sighed. “Thankfuwwy, howoevew, kitfowk who happen to have awmost da same wevew of magic as him, and dose who awe physicawwie gifted, managed to stop him in time.” His posture started to look more relaxed. “Theie casted him into stone, and dwew him into da seas, whewe he couwd not be found bie anyone, evew… and one of da kitfowk who managed to stop him…” He looks at you, gleefully. “Was ME!”]\n''')
                wizard_emotes('deadpan')
                print('''[His body starts to become tense, once more. “But… I had a pwemonition wast night…” The wizard’s face… turned pale. “I couwd see dat da animaws wewe not being… damsewves. I couwd see dat da kitfowk wewe acting… not as daie usuawwie awe…” He gulped. “...a-and I saw him… Zealous… again… and he was buwnim da whowe kingdom dowon!” He sputtered, almost crazily. “So… I’ve come to ask you fow hewp.”]\n''')
                for n in dialogue_options:
                    if n == 1:
                        print(f"{n}. [ What do you need me fow? ]")
                    elif n == 2:
                        print(f"{n}. [ Dat sounds wike a wotta nonsense! ]")
                    elif n == 3:
                        print(f"{n}. [ No, dank you! ]\n")
                dialogue_choice = input("[ What would you like to say to him? ]\n")
                while dialogue_choice not in map(str, dialogue_options):
                    print('''[ The wizard looks at you, confused. "Uh... Couwd you be a wittwe bit mowe cweawew?" ]''')
                    dialogue_choice = input("[ What would you like to say to him? ]\n")
                if dialogue_choice == '1':
                    wizard_emotes('happier')
                    print("[“Why, I’m glad you agreed!” The wizard smiled.]\n")
                else:
                    wizard_emotes('worried')
                    print('''[The wizard looks worried, almost terrified! “I-I knowo it might not sound twue… b-but you’ve got to bewieve me!”]\n''')
                    meanie_counter += 1
                wizard_emotes('sassy')
                print('''[“I need a kittie who can take dowon da dwagon.” He explains. “But… not just anie kitty! I need a kittie who has had no histowie of havim magicaw capabiwities. Instead… I need a kittie who is gweat at usim daiw physical capabiwities! Dat way, Zealous wouwd have no chance in beim abwe to defend himsewf. Fwom what i wemembew, he was awfuwwie usewess when it came to avoidim physicaw attacks, wike beim swashed bie swowds, ow bonked bie huge swedgehammews! Haw-haw-haw!” The wizard guffawed.]\n''')
                print('''[“So… Wouwd you wike to hewp me, and y’knowo, save da kingdom fwom etewnaw damnation?”]\n''')
                dialogue_options = range(1,3)
                for n in dialogue_options:
                    if n == 1:
                        print(f"{n}. [ Yes! ]")
                    else:
                        print(f"{n}. [ No. ]\n")
                while True:
                    dialogue_choice = input("[ What would you like to say to him? ]\n")
                    while dialogue_choice not in map(str, dialogue_options):
                        print('''[ The wizard looks at you, confused. "Uh... Couwd you be a wittwe bit mowe cweawew?" ]''')
                        dialogue_choice = input("[ What would you like to say to him? ]\n")
                    if dialogue_choice == '1':
                        break
                    else:
                        wizard_emotes('worried')
                        print("[The wizard looks up at Kippi with adoring eyes. “…Pwease?”]")
                wizard_emotes('happier')
                print('''[“Gweat! I appweciate youw sacw— I mean… contwibution!” The wizard beams. “Nowo… Dis maie seem wike an awbitwawie wuwe, but you shouwd change youw name to somethim ewse!” He advises. “I’m not sayim dat da name dat youw pawents decided to give you was a bad decision… It just doesn’t sound much wike a hewo’s name, no? Like, I wouwdn’t dink of a headstwong wawwiow whenevew I heaw da name ‘Kippi’. Instead, I wouwd dink of a punie wittwe mouse, eatim a smaww swice of cheese.” He laughs. “Haw-haw-haw!”]\n''')                
                if name_check == True:
                        player_name = input('''[ "Please give a name!" The wizard exclaims. ]\n''')
                        player_name = player_name.upper()
                        while len(player_name) > 20 or player_name.isalpha() == False:
                            player_name = input('''[ "Could you please... uh... give a shorter and coherent name?" The wizard orders. ]\n''')
                            player_name = player_name.upper()
                        name_check = False
                wizard_emotes('happy')
                print(f'''[“Spwendid!” The wizard clasps his paws. “Nowo, howd mie hands, {player_name}, because we’we about to…” {player_name} marvels at the sparkles that flow around him, and he could see himself… glowing!?s]\n''') 
                print("[“VADE AD ALIUM LOCUM!”]\n")
                print(f'''[ Suddenly, a flash of light casts onto {player_name}’s eyes, and his body slumps into a patch of grass. {player_name} looks around. This… This is Floresta! But… where is the wizard?]\n''')
                print(f'''[ {player_name} flinches, as they hear a voice in their head. “Nowo, nowo, {player_name}! No need to be so impwessed with mie magicaw capabiwities! Head on ovew to Tundwa nowo.” The Wizard of Pawz orders. The wizard can communicate telepathically? “Ah, but be cawefuw! Dewe awe some hostiwe beasts awound. Don’t pewish! Bye-bye!”]\n''')
                print(f'''[ Even though {player_name} would like to ask the wizard more questions, by talking to themselves, the wizard did not answer. Letting out a sigh of annoyance… Their journey begins here!]\n''')
                kippi_stats_perm[0] += 1
                kippi_stats[0] = kippi_stats_perm[0]
                        
            #the actual game
            #floresta
            while kippi_stats[0] > 0 and kippi_stats[0] < 10 :
                if enemy_encounter_check == True:
                    floresta_location = random.randint(1,6)
                else:
                    floresta_location = random.randint(1,3)
                    enemy_encounter_check = True
                if floresta_location == 1:
                    print("                               * *    \n             * *            *    *  *\n          *   *    *     *  *    *     *  *\n    *  *      *        *     *    *  *    *\n  *       *    *   * *   *    *    *    *   *\n  * *      *  *  * *     *  *    * * .#  *   *\n *    *  #  *   *  *   *     * #.  .# *   *\n* *     :# * .*     *      #.  #: #  * *    *\n*   * *  ## #     *   * *  #. ##        *\n *     * ###    *            ###\n   *  * ##   *                ##\n      .##                      ##.\n     :##.                      .##:\n    :###                       :###\n     ;###                     ;###\n    ,####.                   ,####.\n   .######.                 .######.\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`\n")
                    print(f"[ As the wind blows stronger, the viridescent leaves of the trees around {player_name} keep falling to the ground, gracefully. ]\n[ {player_name} wishes they could simply make a pile of leaves, jump into them, and make an adsolute mess, but alas, to finish their quest was their ultimate priority. No playing around! ]")
                elif floresta_location == 2:
                    print("     @%      @%         \n     `@%.  `;@%.      @@%;         \n      `@%%. `@%%    ;@@%;        \n       ;@%. :@%%  %@@%;       \n         %@bd%%%bd%%:;     \n          #@%%%%%:;;\n            %@@%::;\n            %@@(o);  . '         \n          %@@@;:(.,'         \n        `.. %@@@::;         \n           `)@o%::;         \n            %(o)::;        \n           .%@@%::;         \n           ;%@@%::;.          \n          ;%@@%%:;;;. \n     ...;%@@@%%:;;;;,. \n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                    print(f"[ {player_name} could see a couple of dead trees around... ]\n[ {player_name} feel a bit unsettled, but they try their best to pay no mind to it. ]")
                elif floresta_location == 3:
                    print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                    random_chance_input = input(f"[ {player_name} could see some berry bushes around them! They feel tempted to see what's behind them. ]\n[ Would you like to take a peek? ]\n")
                    random_chance_input = random_chance_input.lower()
                    while random_chance_input not in yes_or_no:
                        random_chance_input = input("[ Uh... Is that a no...? ]\n")
                        random_chance_input = random_chance_input.lower()
                    if random_chance_input == 'yes' :
                        random_chance = random.randint(1,4)
                        if random_chance == 1:
                            print("[ A SKUNK suddenly appeared out of the bush! ]")
                            skunk_encounter()
                        elif random_chance == 2:
                            print("[ A MONKEY suddenly appeared out of the bush! ]")
                            monkey_encounter()
                        elif random_chance == 3:
                            print("[ A RAVEN suddenly appeared out of the bush! ]")
                            raven_encounter()
                        else:
                            item = random.choice(common_items)
                            print(f"[ {player_name} found a {item} inside of the bush! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                            inventory.append(item)
                    if random_chance_input == 'no' :
                        continue
                elif floresta_location == 4:
                    print(f"[ While {player_name} was walking... a SKUNK appeared out of nowhere! ]")
                    skunk_encounter()
                elif floresta_location == 5:
                    print(f"[ While {player_name} was walking... a MONKEY appeared out of nowhere! ]")
                    monkey_encounter()
                else:
                    print(f"[ While {player_name} was walking... a RAVEN appeared out of nowhere! ]")
                    raven_encounter()
                if kippi_stats[3] <= 0:
                    game_over_mechanic()
                    break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
            
            while kippi_stats[0] == 10 :
                print("     @%      @%               (#%#%#%#%# \n     `@%.  `;@%.      @@%;      (#%#%#%#\n      `@%%. `@%%    ;@@%;        (%#%#%#\n       ;@%. :@%%  %@@%;          /   #%#\n         %@bd%%%bd%%:;          /    _/\n          #@%%%%%:;;           /    /__\n            %@@%::;           /___    /\n            %@@(o);  . '         /   /\n          %@@@;:(.,'            /   /\n        `.. %@@@::;            /   /\n           `)@o%::;           /   /\n            %(o)::;          /__ /_\n           .%@@%::;            / _/\n           ;%@@%::;.     〵 . /_/\n          ;%@@%%:;;;.    .     //\n     ...;%@@@%%:;;;;,.         /\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  'o' )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                print(f"[ {player_name} LEFT ear perked up as they hear a sudden thunder in the distance! ...even though it's daytime? ]")
                print(f'[ {player_name} hears a familiar voice inside their head, saying... "Be cawefuw, {player_name}, dawe seems to be a dangewous entitie nearby!" ]')
                direction_choice = input("[ What shall you do? ]\n[ WALK RIGHT ] [ WALK LEFT ] [ WALK FORWARD ] [ CHECK INVENTORY ]\n")
                direction_choice = direction_choice.lower()
                while 'inventory' not in direction_choice and 'right' not in direction_choice and 'left' not in direction_choice and 'forward' not in direction_choice:
                    direction_choice = input("[ Uh... Your command seems to not be clear enough. Perhaps you could try again? ]\n")
                    direction_choice = direction_choice.lower()
                if 'inventory' in direction_choice:
                    inventory_check()
                elif 'left' in direction_choice:
                    print(f"[ As most kitfolk would be in this situation, {player_name}'s curiosity got the better of them. {player_name} decides walk in the direction of where the thunder was! ]")
                    print(f"[ At first, they did not see anything out of the usual. Just wide plains of grass from all directions, and maybe some scary-looking dead trees. Just as {player_name} was about to head in the other direction, however, a sudden, loud squeal could be heard from afar— ]")
                    print(f"[ {player_name}'s whole body flinched as they saw a giant, luminescent RHINO charging towards them! ]")
                    print(f"[ Using their kitty reflexes, though, {player_name} manages to swerve just in time before the RHINO manages to flung him into the air like a cannonball! ]")
                    print(f'''[ "I guess it's time t-to fight?!?!" {player_name} thought in their head. ]\n''')
                elif 'right' or 'forward' in direction_choice:
                    print(f"[ Adhering to PAWZ's word, {player_name} decides to walk away from where the thunder appeared. ]")
                    print(f"[ As {player_name} took a few steps, however, rapid footsteps could be heard from... behind!? And they're getting closer— ]")
                    print(f"[ Before {player_name} could swerve out of the it's way, a large, luminescent RHINO caused {player_name} to be flung into the air! When {player_name}'s body finally kisses Mother Earth's dirt, a large, painful crunch could be heard! ]")
                    kippi_stats[3] -= 5
                    print(f"[ Writhing from the pain... {player_name}'s health is down to {kippi_stats[3]}! ]")
                    print(f"[ ...Not wanting to stand down, however— {player_name} decides to FIGHT the RHINO! ]\n")
                rhino_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                #cutscene 1
                print(f'''[ "Wowozews! Congwatuwations on defeatim dat whino, {player_name}! Awthuff I wouwd saie dat you desewve a nice, wong west, dawe's stiww a wong ways to go!" The voice in {player_name}'s head tells them. ]''')
                print(f"[ As {player_name} waddles out of Floresta, pretty snowflakes could be seen dropping from the sky, how pretty! ]")
                print(f'''[ "This must be... Tundra!" {player_name} wonders. ]\n''')

            #tundra
            enemy_encounter_check = False
            
            while kippi_stats[0] > 10 and kippi_stats[0] < 25 :
                if enemy_encounter_check == True:
                    tundra_location = random.randint(1,7)
                else:
                    tundra_location = random.randint(1,3)
                    enemy_encounter_check = True
                if tundra_location == 1:
                    print("          A         `      *     *\n    *    d$b\n`      .d〵$$b.    *   `       `\n     .d$i$$〵$$b.            *    *\n   `    d$$@b         *\n*      d〵$$$ib   `           `\n     .d$$$〵$$$b        *\n ` .d$$@$$$$〵$$ib.         *   `   *\n       d$$i$$b\n   *  d〵$$$$@$b    `    *   `   *\n ` .d$@$$〵$$$$$@b.             `    *\n .d$$$$i$$$〵$$$$$$b.     *\n         ###\n         ###          *   `    *\n``````````````````````      ```````````\n      ^----^         /     /\n     (  'w' )       /     /\n     |     ||      /     /      _\n  _  | |   ||     /     /      /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                    print(f'[ As the never-ending snow falls from the sky, {player_name} feels like wanting to open their mouth, let their kitty tongue out and taste the snowflakes. "What would it taste like?" they wonder. ]')
                elif tundra_location == 2:
                    print("    ...        *                        *       *\n      ...   *         * ..   ...                        *\n *      ...        *           *            *\n          ...               ...                          *\n            ..                            *\n    *        ..        *                       *\n           __##____              *                      *\n  *    *  /  ##  ****                   *\n         /        ****               *         *  X   *\n   *    /        ******     *                    XXX      *\n       /___________*****          *             XXXXX\n        |            ***               *       XXXXXXX   X\n    *   | ___        |                    *   XXXXXXXX  XXX\n  *     | | |   ___  | *       *             XXXXXXXXXXXXXXX\n        | |_|   | |  ****             *           X   XXXXXXX\n    *********** | | *******      *                X      X\n`````````````````````````````      ``````````````````````````\n      ^----^                /     /\n     (  ^u^ )              /     /\n     |     ||             /     /      _\n  _  | |   ||            /     /      /_〵\n  ||_!_|   |!           /     /\n  `---|  T |````````````       ``````````````````````````````\n      |  | |\n      !__!_!\n\n````````````````       ``````````````````````````````````````\n                〵     〵")
                    print(f"[ As {player_name}'s eyes glance around, they spotted a little house in the distance! They silently prayed in their heart that the residents of that home are doing fine... and have all of their limbs intact... considering the fact that there are a lot of dangerous beasts around! ]")
                elif tundra_location == 3:
                    print(" * `       *   `   *   `   *   * __  *\n         `                  `  _|==|_ ` \n  `   *       *     *           ('')___/\n `     `        `      `    >--(`^^')\n   *     *          *      `  (`^'^'`)\n``````````````````````      ```````````\n      ^----^         /     /\n     (  0o0 )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                    random_chance_input = input(f'[ {player_name} gasps. "A snowman!" They shout, excitedly. ]\n[ Would you like to check out the snowman? ]\n')
                    random_chance_input = random_chance_input.lower()
                    while random_chance_input not in yes_or_no:
                        random_chance_input = input("[ Uh... Is that a no...? ]\n")
                        random_chance_input = random_chance_input.lower()
                    if random_chance_input == 'yes' :
                        random_chance = random.randint(1,10)
                        if random_chance == 1:
                            print("[ The snowman... IS ALIVE!? ]")
                            snowman_encounter()
                        else:
                            item = random.choice(common_items)
                            print(f"[ {player_name} found a {item} inside of the snowman! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                            inventory.append(item)
                    if random_chance_input == 'no' :
                        continue
                elif tundra_location == 4:
                    print(f"[ While {player_name} was walking... a PENGUIN appeared out of nowhere! ]")
                    penguin_encounter()
                elif tundra_location == 5:
                    print(f"[ While {player_name} was walking... a SEAL appeared out of nowhere! ]")
                    seal_encounter()
                elif tundra_location == 6:
                    print(f"[ While {player_name} was walking... an ARCTIC WOLF appeared out of nowhere! ]")
                    wolf_encounter()
                else:
                    print(f"[ While {player_name} was walking... a POLAR BEAR appeared out of nowhere! ]")
                    bear_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break

            while kippi_stats[0] == 25 :
                print(" * `       *   `   *   `   *   * __  *\n         `                  `  _|==|_ ` \n  `   *       *     *           ('')___/\n `     `        `      `    >--(`^^')\n   *     *          *      `  (`^'^'`)\n``````````````````````      ```````````\n      ^----^         /     /\n     (  0o0 )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                random_chance_input = input(f'[ {player_name} gasps. "A snowman!" They shout, excitedly. ]\n[ Would you like to check out the snowman? ]\n')
                random_chance_input = random_chance_input.lower()
                while random_chance_input not in yes_or_no:
                    random_chance_input = input("[ Uh... Is that a no...? ]\n")
                    random_chance_input = random_chance_input.lower()
                if random_chance_input == 'yes' :
                    print(" * `       *   `   *   `   *   _ _ _  *\n         `                  ` | | |_|  ` \n  `   *       *     *     `   |_|_|_ 〵   \n `     `        `      `      (   (  /\n   *     *          *      `   |    |  *\n``````````````````````      ```````````\n      ^----^         /     /\n     (U'0o0 )       /     /\n     |     ||      /     /   _\n  _  | |   ||     /     /   /_〵\n  ||_!_|   |!    /     /\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n                〵     〵")
                    print(f"[ As {player_name} was about to head over to the silly snowman... a giant fist punctured through its snowy body!? ]")
                    bigfoot_encounter()
                if random_chance_input == 'no' :
                    print("[ As {player_name} started to walk away from the silly snowman... a feminine figure was bestowed upon {player_name}'s eyes! ]\n")
                    print('''                       |\n                    .*`|'*,\n       .-""-.      --- * ---      .-""-.\n     .'_.-.  |      '*,|.*`      |  .-._'.\n    /    _/ /          |         〵 〵_    〵\n   /.--.' | |                     | | '.--.〵\n  /   .-`-| |       _.---._       | |-`-.   〵\n ;.--':   | |     .'     / '.     | |   :'--.;\n|   _〵.'-| |    /      _/   〵   | |-'./_    |\n;_.-'/:   | |   /   .-'`  '.  〵  | |  :〵'-._;\n|   | _:-'〵〵.'   | ^ _ ^ |   './  /'-:_ |   |\n;  .:` '._〵.'     |   _   |     〵/ _.' `:.  ;\n|-` '-.;_ ./        '.___.'       '.` _;.-' `-|\n; / .'〵| |        _.'   '._        〵'| /'.〵;\n| .' / `'.|      .' `"---"` '.       |'` 〵'. |\n;/  /〵_/-〵     |           |       /-〵_/〵;|\n |.' .| `; 〵    | |       | |      /;` |. '.|\n |  / 〵.'〵/〵  | :--"""--: |    /`_/'./ 〵 |\n 〵| ; | ; |/)   | |       | |   (〵| : | ;|/\n  〵 | ; | //   〵.'-.....-'./    〵〵| ;| /\n   `〵 | |`/    .' / ;|: | 〵'.    |`| | /`\n     .-:_/〵_.-' .' / ' . : '. '. /`〵_:'\n     | 〵```      .'  ;    〵    `:\n     〵 〵                   '     `'.\n   .--'〵 |  '         '       .      `-._\n  /`;--' /_.'          .                  `-.\n  |  `--`        /              〵          〵\n  〵       .'   '                 '-.        |\n   〵   '               '          __〵      |\n     '.      .                 _.-'  `)     /\n       '-._                _.-' `| .-`   _.'\n           `'--....____.--'|     (`  _.-'\n                    /  | | 〵     `"`\n                   〵__/ 〵_/\n''')
                    print('''[ "Greetings, child. I am a spirit that belongs to these snowstorms of Tundra." She smiles, almost menacingly. ]''')
                    print('''[ She continues, saying, "My child... I normally avoid exposing my physical body towards the likes of mortals, such as thyself, but I've been seeing thou killing the innocent animals of my land. Does thou not feel an ounce of pity?" ]\n''')
                    dialogue_options = range(1,4)
                    for n in dialogue_options:
                        if n == 1:
                            print(f"{n}. [ But... I'm doim dis fow da gweatew good! ]")
                        if n == 2:
                            print(f"{n}. [ Dose animaws desewved it! Dey'we goim cwazy! ]")
                        if n == 3:
                            print(f"{n}. [ I'm twyim to defend mysewf! Haven't you've seen howo daie wewe acting? ]\n")
                    dialogue_choice = input("[ What would you like to say to her? ]\n")
                    while dialogue_choice not in map(str, dialogue_options):
                        print("[ The spirit tilts her head to the side, not understanding what you were trying to articulate. ]")
                        dialogue_choice = input("[ What would you like to say to her? ]\n")
                    print('''                       |\n                    .*`|'*,\n       .-""-.      --- * ---      .-""-.\n     .'_.-.  |      '*,|.*`      |  .-._'.\n    /    _/ /          |         〵 〵_    〵\n   /.--.' | |                     | | '.--.〵\n  /   .-`-| |       _.---._       | |-`-.   〵\n ;.--':   | |     .'     / '.     | |   :'--.;\n|   _〵.'-| |    /      _/   〵   | |-'./_    |\n;_.-'/:   | |   /   .-'`  '.  〵  | |  :〵'-._;\n|   | _:-'〵〵.'   | ò _ ó |   './  /'-:_ |   |\n;  .:` '._〵.'     |   .   |     〵/ _.' `:.  ;\n|-` '-.;_ ./        '.___.'       '.` _;.-' `-|\n; / .'〵| |        _.'   '._        〵'| /'.〵;\n| .' / `'.|      .' `"---"` '.       |'` 〵'. |\n;/  /〵_/-〵     |           |       /-〵_/〵;|\n |.' .| `; 〵    | |       | |      /;` |. '.|\n |  / 〵.'〵/〵  | :--"""--: |    /`_/'./ 〵 |\n 〵| ; | ; |/)   | |       | |   (〵| : | ;|/\n  〵 | ; | //   〵.'-.....-'./    〵〵| ;| /\n   `〵 | |`/    .' / ;|: | 〵'.    |`| | /`\n     .-:_/〵_.-' .' / ' . : '. '. /`〵_:'\n     | 〵```      .'  ;    〵    `:\n     〵 〵                   '     `'.\n   .--'〵 |  '         '       .      `-._\n  /`;--' /_.'          .                  `-.\n  |  `--`        /              〵          〵\n  〵       .'   '                 '-.        |\n   〵   '               '          __〵      |\n     '.      .                 _.-'  `)     /\n       '-._                _.-' `| .-`   _.'\n           `'--....____.--'|     (`  _.-'\n                    /  | | 〵     `"`\n                   〵__/ 〵_/''')
                    print('''[ She furrowed her eyebrows. "Regardless of what thy disgusting cat tongue might decide to spit out, I shall not take these horrible actions no longer!" ]''')
                    print('''[ {player_name} could feel large gusts of cold wind and piles of snow spiralling around them. It looks like some kind of performance! But... "Ergo, I shall take thy life... just like how thou have taken the lives of the other animals of my land!" The spirit sputtered out." ]''')
                    spirit_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                #cutscene 2
                if random_chance_input == 'yes':
                    print("[ As Bigfoot slumps over in defeat, you hear him once again... ]")
                    print(f'''[ "Gweat job, {player_name}! To be honest, I was pwettie scawed dat you wewe goim to tuwn into a fewine pancake! I mean, it was twice as big as you!" The wizard says, telepathically. Where even is he? ]''')
                    print(f"[ {player_name} shrugs, not knowing what to answer. ]\n")
                    print('''[ "Weww dan, next up, Sahawa!" He orders, casually. ]''')
                if random_chance_input == 'no':
                    print("[ The light eminating from the spirit's body started to dim, and the look on her face started to look more and more worn out. ]")
                    print('''[ "T-Thou...!" She sputters. She puts up her wings, signalling that she'll take off. "I'll get you next time, you scoundrel!" ]\n''')
                    print(f'''[ {player_name} hears... clapping? "Haw-haw-haw! Weww done, weww done!" The wizard exclaims. ]''')
                    print(f"[ {player_name} blushes a little. But this isn't a time where {player_name} should just be standing around and be praised by someone! {player_name} has a quest to fulfill! ]")
                    print(f'''[ The Wizard of Paws barges inside {player_name}'s mental chamber. "Nowo, nowo, head ovew to Sahawa, wiww ya?" ]\n''')
                print(f"[ {player_name}'s nose scrunches as soon as they heard that place's name. ]")
                print('''[ "Sahara... THE DESERT!?" They anguished, mentally. ]''')

            #sahara
            enemy_encounter_check = False

            while kippi_stats[0] > 25 and kippi_stats[0] < 50 :
                if enemy_encounter_check == True:
                    sahara_location = random.randint(1,8)
                else:
                    sahara_location = random.randint(1,3)
                    enemy_encounter_check = True
                if sahara_location == 1:
                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n\n     .*.       .*.\n   , | | ,     | |\n  ||_| |_||  , | | ,\n  `--, ,--` ||_| |_||\n     | |    `--, ,--`\n     | |       | |\n     | |       | |                 _\n```````````````| |````      ``````/_〵``\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                    print(f"[ As {player_name} walks further, it seems like it's just neverending stretches of sands and cactuses around them... ]")
                elif sahara_location == 2:
                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                    print(f'''[ "Dis pwace seems... awfuwwie quiet." {player_name} thought to themselves. They keep looking behind themselves because they're afraid of being jumped on by a scary beast! ]''')
                elif sahara_location == 3:
                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                %%%,%%%%%%%\n                             ,'%% 〵〵-*%%%%%%%\n                       ;%%%%%*%   _%%%%'\n                        ,%%%       〵(_.*%%%%.\n                        % *%%, ,%%%%*(    '\n                      %^     ,*%%% )〵|,%%*%,_\n                           *%    〵/ #).-'*%%*\n                               _.) ,/ *%,\n                                /)#(\n``````````````````````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                    random_chance_input = input(f'''[ "Oh, wook! A twee!" {player_name} exclaims. The heat is getting unbearably hot! ]\n[ Would you like to try sitting under the shady tree? ]\n''')
                    random_chance_input = random_chance_input.lower()
                    while random_chance_input not in yes_or_no:
                        random_chance_input = input("[ Uh... Is that a no...? ]\n")
                        random_chance_input = random_chance_input.lower()
                    if random_chance_input == 'yes' :
                        random_chance = random.randint(1,6)
                        if random_chance == 1:
                            print(f"[ While {player_name} was about to take a little rest, a LIZARD appeared out of nowhere! ]")
                            lizard_encounter()
                        elif random_chance == 2:
                            print(f"[ While {player_name} was about to take a little rest, a SNAKE appeared out of nowhere! ]")
                            snake_encounter()
                        elif random_chance == 3:
                            print(f"[ While {player_name} was about to take a little rest, an OSTRITCH appeared out of nowhere! ]")
                            ostritch_encounter()
                        elif random_chance == 4:
                            print(f"[ While {player_name} was about to take a little rest, a COYOTE appeared out of nowhere! ]")
                            coyote_encounter()
                        elif random_chance == 5:
                            print(f"[ While {player_name} was about to take a little rest, a TORTOISE appeared out of nowhere! ]")
                            tortoise_encounter()
                        else:
                            item = random.choice(uncommon_items)
                            print(f"[ {player_name} found a {item} under the tree! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                            inventory.append(item)
                    if random_chance_input == 'no' :
                        continue
                elif sahara_location == 4:
                    print(f"[ While {player_name} was walking... a LIZARD appeared out of nowhere! ]")
                    lizard_encounter()
                elif sahara_location == 5:
                    print(f"[ While {player_name} was walking... a SNAKE appeared out of nowhere! ]")
                    snake_encounter()
                elif sahara_location == 6:
                    print(f"[ While {player_name} was walking... an OSTRITCH appeared out of nowhere! ]")
                    ostritch_encounter()
                elif sahara_location == 7:
                    print(f"[ While {player_name} was walking... a COYOTE appeared out of nowhere! ]")
                    coyote_encounter()
                else:
                    print(f"[ While {player_name} was walking... a TORTOISE appeared out of nowhere! ]")
                    tortoise_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break

            while kippi_stats[0] == 50 :
                print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '                      _*_\n                              (|||)\n                              |||||\n                          __  |||||\n                         (||) |||||\n                         |||| |||||  __\n                         |||| ||||| (||)\n                         |||| ||||| ||||\n                         〵|`-'|||| ||||\n                          〵__ |||| ||||\n                              ||||`-'|||\n                              |||| ___/\n                              |||||\n                              |||||\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                print(f'''[ "Dis pwace seems... awfuwwie quiet." {player_name} thought to themselves. They keep looking behind themselves because they're afraid of being jumped on by a scary beast! ]''')
                direction_choice = input("[ What shall you do? ]\n[ WALK RIGHT ] [ WALK LEFT ] [ WALK FORWARD ] [ CHECK INVENTORY ]\n")
                direction_choice = direction_choice.lower()
                while 'inventory' not in direction_choice and 'right' not in direction_choice and 'left' not in direction_choice and 'forward' not in direction_choice:
                        direction_choice = input("[ Uh... Your command seems to not be clear enough. Perhaps you could try again? ]\n")
                        direction_choice = direction_choice.lower()
                if 'inventory' in direction_choice:
                    inventory_check()
                elif 'left' in direction_choice:
                    print(f"[ As {player_name} started to walk in the direction of the... unusually large cactus, they suddenly felt the ground rumbling. As they tried to run away to save themselves from being a victim of a natural disaster, large pillars of sand surrounded them! Turning their head back, they saw that the unassuming cactus... has become a COLOSSAL CACTUS! ]")
                    print('''[ "Well, well, well, lil' feller!" The cactus boomed. "Been seein' ya attackin' mah people left and right. Don't really appreciate that much! Guess I gotta kill ya now." He shrugs. ]''')
                    cactus_encounter()
                elif 'right' or 'forward' in direction_choice:
                    print(f"[ As {player_name} was walking, they suddenly bumped into a... another kitfolk!? In this area!? ]")
                    traveller_emotes('happy')
                    print(f'''[ "Oh, heie dawe! Suwpwised to see anodaw kitfowk awound dase pawts." The hat-wearing kitfolk says to {player_name}. ]''')
                    if head[0] == 'SUNGLASSES' :
                        print(f'''[ He looks up and down at {player_name} for a moment. "And dose awe some coow shades you've got!... Y'knowo what, I kinda wike you! Hewe—" ]''')
                        print(f"[ The strange kitfolk hands you a... RUMBLESTRIKE HAMMER!? ]")
                        inventory.append('RUMBLESTRIKE HAMMER')
                        traveller_emotes('happier')
                        print(f'''[ He waves his paw at you, grinning. "Somethim dat'ww pwobabwie make youw twavewwim easiew. Have a nice day!" It looked like he was about to leave for a second, but he stopped in his tracks. He looks at {player_name}, one last time, and says "Oh, and just an advice fow a kitfowk fwom a kitfowk, don't bewieve da wowds of peopwe whom you just met, m'kay?" ]''')
                        print(f"[ As {player_name} was about to thank him for his kindness... he suddenly vanished! Like the wind... ]")
                    else:
                        print(f'''[ "Hey, you don't mind if I tawk about awmadiwwos to you, wight? I wove awmadiwwos!" He says, rather enthusiastically. ]\n''')
                        dialogue_options = range(1,3)
                        for n in dialogue_options:
                            if n == 1:
                                print(f"{n}. [ Uh... Suwe! ]")
                            if n == 2:
                                print(f"{n}. [ No. I'm busie. ]\n")
                        dialogue_choice = input("[ What would you like to say to him? ]\n")
                        while dialogue_choice not in map(str, dialogue_options):
                            print('''[ "Uh... Guess we'we fwom diffewent pawts of nyuwuwoviwwa, huh? 'Cause I can't seem to undewstand you..." ]''')
                            dialogue_choice = input("[ What would you like to say to him? ]\n")
                        if dialogue_choice == '1' :
                            traveller_emotes('happier')
                            print(f'''[ "Fantastic!" He clears his throat before unleashing an ungodly amount of armadillo facts to {player_name}— ]''')
                            armadillo_facts_moment(1)
                        else:
                            pass
                        traveller_emotes('angry')
                        print('[ The overly-talkative traveller suddenly goes quiet... ]')
                        traveller_emotes('angrier')
                        print('''[ "Y'knowo, I awweadie knew you wewen't actuawwie wistenim to what I was sayim... but just outwight ignowim me is extwemewie wude!" He sputters. ]''')
                        print('''[ Although you tried your best to calm him down and tried to clarify that you were— mostly— listening to whatever he was saying, he screeches "IF YOU HATED LISTENIM TO WHAT I WAS SAYIM SO MUCH, YOU SHOULD'VE JUST WALKED AWAY!" ]''')
                        traveller_emotes('angriest')
                        print('''[ The traveller clapped both of his paws together, and shouted "JEREMY～!" Thinking this was one of his silly antics again, {player_name} giggled a little. Suddenly, the ground started to shake, and a big hole started to form in front of you! Running away before you could be consumed by it, you turned your back towards the strange phenomenon ocurring before your eyes, and there— comes out a BROBDINGNAGIAN ARMADILLO!? ]\n''')
                        armadillo_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break

            #still sahara
            enemy_encounter_check = False

            while kippi_stats[0] >= 51 and kippi_stats[0] < 75 :
                if enemy_encounter_check == True:
                    sahara_location = random.randint(1,8)
                else:
                    sahara_location = random.randint(1,3)
                    enemy_encounter_check = True
                if sahara_location == 1:
                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n\n     .*.       .*.\n   , | | ,     | |\n  ||_| |_||  , | | ,\n  `--, ,--` ||_| |_||\n     | |    `--, ,--`\n     | |       | |\n     | |       | |                 _\n```````````````| |````      ``````/_〵``\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                    print(f"[ As {player_name} walks further, it seems like it's just neverending stretches of sands and cactuses around them... ]")
                elif sahara_location == 2:
                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                ,*-.\n                                |  |\n                            ,.  |  |\n                            | |_|  | ,.\n                            `---.  |_| |\n                                |  .--`\n                                |  |\n             _                  |  |\n````````````/_〵```````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                    print(f'''[ "Dis pwace seems... awfuwwie quiet." {player_name} thought to themselves. They keep looking behind themselves because they're afraid of being jumped on by a scary beast! ]''')
                elif sahara_location == 3:
                    print("        .\n     〵 | /\n    '-.;;;.-'\n   -==;;;;;==-\n    .-';;;'-.\n      / | 〵\n        '\n                                %%%,%%%%%%%\n                             ,'%% 〵〵-*%%%%%%%\n                       ;%%%%%*%   _%%%%'\n                        ,%%%       〵(_.*%%%%.\n                        % *%%, ,%%%%*(    '\n                      %^     ,*%%% )〵|,%%*%,_\n                           *%    〵/ #).-'*%%*\n                               _.) ,/ *%,\n                                /)#(\n``````````````````````      ```````````\n``````^----^`````````/     /```````````\n`````(U'ówò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````       ````````````````\n      |  | |\n      !__!_!\n\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                    random_chance_input = input(f'''[ "Oh, wook! A twee!" {player_name} exclaims. The heat is getting unbearably hot! ]\n[ Would you like to try sitting under the shady tree? ]\n''')
                    random_chance_input = random_chance_input.lower()
                    while random_chance_input not in yes_or_no:
                        random_chance_input = input("[ Uh... Is that a no...? ]\n")
                        random_chance_input = random_chance_input.lower()
                    if random_chance_input == 'yes' :
                        random_chance = random.randint(1,6)
                        if random_chance == 1:
                            print(f"[ While {player_name} was about to take a little rest, a LIZARD appeared out of nowhere! ]")
                            lizard_encounter()
                        elif random_chance == 2:
                            print(f"[ While {player_name} was about to take a little rest, a SNAKE appeared out of nowhere! ]")
                            snake_encounter()
                        elif random_chance == 3:
                            print(f"[ While {player_name} was about to take a little rest, an OSTRICH appeared out of nowhere! ]")
                            ostrich_encounter()
                        elif random_chance == 4:
                            print(f"[ While {player_name} was about to take a little rest, a COYOTE appeared out of nowhere! ]")
                            coyote_encounter()
                        elif random_chance == 5:
                            print(f"[ While {player_name} was about to take a little rest, a TORTOISE appeared out of nowhere! ]")
                            tortoise_encounter()
                        else:
                            item = random.choice(uncommon_items)
                            print(f"[ {player_name} found a {item} under the tree! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                            inventory.append(item)
                    if random_chance_input == 'no' :
                        continue
                elif sahara_location == 4:
                    print(f"[ While {player_name} was walking... a LIZARD appeared out of nowhere! ]")
                    lizard_encounter()
                elif sahara_location == 5:
                    print(f"[ While {player_name} was walking... a SNAKE appeared out of nowhere! ]")
                    snake_encounter()
                elif sahara_location == 6:
                    print(f"[ While {player_name} was walking... an OSTRICH appeared out of nowhere! ]")
                    ostrich_encounter()
                elif sahara_location == 7:
                    print(f"[ While {player_name} was walking... a COYOTE appeared out of nowhere! ]")
                    coyote_encounter()
                else:
                    print(f"[ While {player_name} was walking... a TORTOISE appeared out of nowhere! ]")
                    tortoise_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break

            while kippi_stats[0] == 75 :
                print(f'''[ "Gosh, I'm so diwsty!" {player_name} thought to themselves. ]''')
                print(f"[ While {player_name} was fantisizing about how amazing it could be if {player_name} could drink from, or even bathe in a cold, refreshing oasis... The grounds of Sahara started to crack, pulling {player_name} away from their thoughts! ]")
                print("     .*.       .*.\n   , | | ,     | |\n  ||_| |_||  , | | ,\n  `--, ,--` ||_| |_||\n     | |    `--, ,--`\n     | |       | |\n     | |       | |                 _\n```````````````| |````      ``````/_〵``\n``````^----^`````````/     /```````````\n`````(U'ó.ò )```````/     /````````````\n`````|     ||``````/     /```_`````````\n``_``| |   ||`````/     /```/_〵```````\n``||_!_|   |!````/     /```````````````\n  `---|  T |````    |  ````````````````\n      |  | |     〵___〵_`__._`___`__/_\n      !__!_!        __`__/〵`__  〵\n                   /           〵\n````````````````       ````````````````\n````````````````〵     〵``````````````")
                print(f'''[ "W-What is goim on!?" {player_name} shouted. Almost answering their question, a gigantic dinosaur erupted from the cracks; leaving debris of sand everywhere, even on {player_name}'s fur! ]''')
                print(f'''[ "Didn't dinosauws went extinct 5000 yeaws ago!? Gwah! Nowo I have to fight one!" {player_name} screamed at themselves, mentally. ]''')
                behemoth_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                          os.remove("kippi_save.txt")
                        else:
                          pass
                        break
                #cutscene 3
                print(f'''[ "Woah!" The wizard's voice in {player_name} brain echoes. "Not to be wude, but wowo! I didn't expect dat you'd defeat dat monstew! I mean, it was ten feet tawwew dan you!" Although {player_name} couldn't see the wizard, they could tell that he was scoffing. ]''')
                print(f'''[ "I knew it wasn't a mistake choosim you as mie mentee!" He praises. {player_name} could feel their self-esteem rising hearing those words from a world-renowned wizard! ]\n''')
                print('''[ "Nowo, da next and finaw chawwenge might be a wittwe too tuff fow you..." The wizard warns. "Because we'we about to head ovew to..." ]''')
                print('''                        (   (( . : (    .)   ) :  )\n                          (   ( :  .  :    :  )  ))\n                           ( ( ( (  .  :  . . ) )\n                            ( ( : :  :  )   )  )\n                             ( :(   .   .  ) .'\n                              '. :(   :    )\n                                (   :  . )  )\n                                 ')   :   #@##\n                                #',### " #@  #@\n                               #/ @'#~@#~/〵  #\n                             ##  @@# @##@  `..@,\n                           @#/  #@#   _##     `〵\n                         @##;  `#~._.' ##@      〵.\n                       .-#/           @#@#@--,_,--〵\n                      / `@#@..,     .~###'         `~.\n                    _/         `-.-' #@####@          〵\n                 __/     &^^       ^#^##~##&&&   %     〵.\n                /       && ^^      @#^##@#%%#@&&&&  ^    〵\n              ~/         &&&    ^^^   ^^   &&&  %%% ^^^   `~._\n           .-'   ^^    %%%. &&   ___^     &&   && &&   ^^     〵\n          /akg ^^^ ___&&& X & && |n|   ^ ___ %____&& . ^^^^^   `~.\n                   |M|       ---- .  ___.|n| /〵___〵  X\n                             |mm| X  |n|X    ||____|''')
                print('''[ "VOLCANA, DA PLACE WHERE ZEALOUS IS RESIDING!" The wizard says, perhaps a litte too entusiastically. ]\n''')
                print(f'''[ "...Wait, I'm gonna fight Zeawous!?" A thought just crossed {player_name}'s mind. ]''')
                print(f"[ Just as {player_name} was about to ask for clarification whether they will or will not be defeating a huge dragon— twenty times the size as a regular kitfolk, like themselves, the wizard, of course, doesn't respond to their inquiries. ]")
                print(f'''[ "That wizawd bettew tweat me to a nice, fishie dinnew aftew dis!" {player_name} internally cursed to themselves. ]''')

            #volcana
            enemy_encounter_check = False
            while kippi_stats[0] >= 76 and kippi_stats[0] < 100 :
                if enemy_encounter_check == True:
                    volcana_location = random.randint(1,7)
                else:
                    volcana_location = random.randint(1,3)
                    enemy_encounter_check = True
                if volcana_location == 1:
                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n                    _ --        -_ =-_\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'ó-ò )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                    print(f'''[ "This pwace is... swewtewimwie hot!" {player_name} mutters to themselves. They feel like they could melt into a puddle at any moment! ]''')
                elif volcana_location == 2:
                    print("  `:--._      _.---.\n    :--:〵   .:`--.' _ _   --__     -_\n     :/ (〵^.` `./\n--__  ``〵/-==:'`     - -__     -_\n         |.--    --___     _ __--__  _\n_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n                    _ --        -_ =-_\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'O.O )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                    print(f"[ {player_name} ears perk up suddenly as they hear something... or someone— roaring in the distance! ]")
                elif volcana_location == 3:
                    print("_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n --                 _ --        -_ =-_\n     --  --               __   ___   .-\n       --___     _ __--__     (0.0)\n --                            |m|〵\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'ó,ò )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                    random_chance_input = input(f"[ Oh, look! It's a... skull... ]\n[ Would you like to check out what's inside of it... for some reason? ]\n")
                    random_chance_input = random_chance_input.lower()
                    while random_chance_input not in yes_or_no:
                        random_chance_input = input("[ Uh... Is that a no...? ]\n")
                        random_chance_input = random_chance_input.lower()
                    if random_chance_input == 'yes' :
                        random_chance = random.randint(1,5)
                        if random_chance == 1:
                            print(f"[ Uh, oh! Turns out the skull... was actually a SKELETON THAT'S ALIVE!? ]")
                            skeleton_encounter()
                        else:
                            item = random.choice(uncommon_items)
                            print(f"[ {player_name} found a {item} in the... skull! {player_name} decided to stuff it into their handy-dandy backpack. Just in case! ]\n")
                            inventory.append(item)
                    if random_chance_input == 'no' :
                        continue
                elif volcana_location == 4:
                    print(f"[ While {player_name} was walking... an UNASSUMING BLOB OF LAVA appeared out of nowhere! ]")
                    lavablob_encounter()
                elif volcana_location == 5:
                    print(f"[ While {player_name} was walking... a SMOKEY WRAITH appeared out of nowhere! ]")
                    wraith_encounter()
                elif volcana_location == 6:
                    print(f"[ While {player_name} was walking... a PHOENIX appeared out of nowhere! ]")
                    phoenix_encounter()
                else:
                    print(f"[ While {player_name} was walking... a HELLHOUND appeared out of nowhere! ]")
                    hellhound_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        break
                level_up_mechanic()
                deciding_direction = True
                direction_mechanic()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        break

            while kippi_stats[0] == 100 :
                print("  `:--._      _.---.\n    :--:〵   .:`--.' _ _   --__     -_\n     :/ (〵^.` `./\n--__  ``〵/-==:'`     - -__     -_\n         |.--    --___     _ __--__  _\n_ _   --           - -__     -_\n       --  --___     _ __--__ -= _\n                    _ --        -_ =-_\n#.#.#.#.#.#.#.##.#.#.#/`````/#.#.#.#.#.\n#.#.#.^----^#.#.#.#.#/`````/#.#.#.#.#.#\n#.#.#(U'O.O )#.#.#.#/`````/#.#.#.#.#.#.\n#.#.#|     ||#.#.#./`````/#.#.#.#.#.#.#\n#._#.| |   ||#.#.#/`````/#.#.#.#.#.#.#.\n#.||_!_|   |!#.#./`````/#.#.#.#.#.#.#.#\n```---|  T |````  ```` ````````````````\n``````|  | |```````````````````````````\n````` !__!_!```````````````````````````\n```````````````````````````````````````\n#.#.#.#.#.#.#.#.〵`````〵#.#.#.#.#.#.#.\n#.#.#.#.#.#.#.#.#〵`````〵#.#.#.#.##.#.")
                print(f"[ {player_name} ears perk up suddenly as they hear something... or someone— roaring in the distance! ]")
                direction_choice = input("[ What shall you do? ]\n[ WALK RIGHT ] [ WALK LEFT ] [ WALK FORWARD ] [ CHECK INVENTORY ]\n")
                direction_choice = direction_choice.lower()
                while 'inventory' not in direction_choice and 'right' not in direction_choice and 'left' not in direction_choice and 'forward' not in direction_choice:
                        direction_choice = input("[ Uh... Your command seems to not be clear enough. Perhaps you could try again? ]\n")
                        direction_choice = direction_choice.lower()
                if 'inventory' in direction_choice:
                    inventory_check()
                elif 'left' in direction_choice:
                    print(f"[ As {player_name} was about to walk into the direction of where the neverending roars were coming from... a giant, red dragon slithered towards you! ]")
                elif 'right' or 'forward' in direction_choice:
                    print(f"[ As {player_name} was about to walk away from the direction of where the neverending roars were coming from... a giant, red dragon slithered towards you! ]")
                print(f'''[ {player_name} gasps. "Z-ZEAWOUS!?" They stuttered. ]\n''')
                print(f"[ Although he looks a little too... small from what {player_name} has imagined, the Wizard of Pawz mentioned that he could take in any form, ferocious beast or not, so better to attack him while he's in this form! ]")
                zealous_encounter()
                if kippi_stats[3] <= 0:
                    print(f"[ {player_name} fainted! ]")
                    print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                    print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        break
                print("[ After dealing the very final blow towards Zealous, he falls over, and disintegrate into a pile of ashes. ...The pile of ashes, though, proceeds to transform into a... another kitfolk!? ]")
                print("[ Not just any regular kitfolk, however... It's the King of Nyuwuwovilla! ]\n")
                king_emotes('rescued')
                print(''''[ "Oh, goodness gwacious... Dank you!" The king says, crying from joy. ]\n''')
                king_emotes('happy')
                print(''''[ "Y'see,  deaw, I was cuwsed bie a wizawd to tuwn into a wowowie dwagon! Awthuff I twied mie hawdest to contwow mysewf whiwe i was in dis dwaconic fowm... Da animawistic instincts ovewpowoewed mie empadatic natuwe." The king bows his head... to you! ''') 
                print('''[ "I deepwie apowogize fow da actions I have done towoawds you whiwe I was not wight in mie mind..." ]''')
                dialogue_options = range(1,3)
                for n in dialogue_options:
                    if n == 1:
                        print(f"{n}. [ Yes, I accept youw apowogy! ]")
                    if n == 2:
                        print(f"{n}. [ No, I don't accept youw apowogie. ]")
                dialogue_choice = input("[ What would you like to say to him? ]\n")
                while dialogue_choice not in map(str, dialogue_options):
                    print("[ The king forces a smile, pretending to understand what you've just said. ]")
                    dialogue_choice = input("[ What would you like to say to him? ]\n")
                king_emotes('possessed')
                print("[ Just as you were about to respond to his worries, his eyes glossed over, and his body fell backwards. Behind him... was the Wizard of Pawz!? ]")
                wizard_emotes('happier')
                print('''[ "Haw-haw-haw!" The wizard laughs. "You've been caught in my trap! Y'see, I was the dragon whom I was talking about during the first time we met. I was the one who was thrown into the seas. And I was the one who wanted anything, and everything!" ]''')
                print(f'''[ {player_name} gulps down their spit, not liking where this is heading... "Yes... I am... Indeed... ZEALOUS!" The wizar— actually— ZEALOUS reveals! ]''')
                if meanie_counter > 0:
                    wizard_emotes('sassier')
                    print('''[ "And y'know what? I didn't really appreciate the things you've said to me during our first meeting." Zealous scoffs. ]''')
                    print(f'''[ "And although I have the power to simply obliterate you from the face of the Earth— I'm quite a kind-hearted person, so I wouldn't do that! Haw-haw-haw!" Zealous laughs, but {player_name} isn't. ]''')
                    wizard_emotes('happier')
                    print('''[ "So, instead, I shall turn you into a frog so that you could feel how it feels to be slimy! Not only on the inside, but the outside, as well!" ]''')
                    print(f'''[ {player_name} pleaded with Zealous to change his mind, but alas, with a twirl of Zealous' paws, {player_name} turned into a frog! ]''')
                    print("     /     〵\n     _(I)(I)_\n    ( _ .. _ )\n     `.`--'.'\n      )    (\n  ,-.!      !,-.\n ( _( ||  || )_ )\n__)  )||--||(  (__ \n`-._))||)(||((_.-'\n     `--'`--'\n")
                    game_over = input("[ Would you like to try again? ]\n")
                    game_over = game_over.lower()
                    while game_over not in yes_or_no:
                        game_over = input("[ Input not recognised. Please try again! ]")
                        game_over = game_over.lower()
                    if game_over == 'yes':
                        intro_screen = False
                        game_start = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        continue_game = False
                        break
                    if game_over == 'no':
                        game_start = False
                        intro_screen = True
                        if os.path.exists("kippi_save.txt"):
                            os.remove("kippi_save.txt")
                        else:
                            pass
                        break
                else:
                    wizard_emotes('happy')
                    print('''[ "But... Y'know..." Zealous has an understanding look in his eyes. "I've seen you improve not only your physical capibilities, but also your mental capilities all this while. So..." ]''')
                    print('''[ "Why don't we both team up together? Join our forces, and we shall be UNSTOPPABLE! No one shall take us both down." Zealous proposes. ]''')
                    dialogue_options = range(1,3)
                    for n in dialogue_options:
                        if n == 1:
                            print(f"{n}. [ Yes! ]")
                        else:
                            print(f"{n}. [ No. ]")
                    dialogue_choice = input("[ Do you agree with him? ]\n")
                    while dialogue_choice not in map(str, dialogue_options):
                        print('''[ The wizard looks at you, confused. "Could you please be a bit more clearer?" ]''')
                        dialogue_choice = input("[ Do you agree with him? ]\n")
                    if dialogue_choice == '1':
                        print('''[ Zealous smirks. "Haw-haw-haw! Wonderful!" ]''')
                        print(f"[ Ever since {player_name} has agreed to Zealous' proposal, he has gone more powerful than he ever was before! Just the sight of seeing {player_name} in the streets of Nyuwuwovilla causes any kitfolk walking by to run for their lives! ]")
                        print(f"[ ...However, one who has a non-rational mind could not predict that Zealous would ever frame {player_name} for being the sole cause of all the destruction of the world... And it worked! The Queen of Nyuwuwovilla ordered her strongest guards to capture {player_name}, keeping them locked in a jail cell for the rest of their lifespan! ]")
                        print(f"[ {player_name} died in that very jail cell... Loved by no one, hated by everyone. ]")
                        print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        game_over = input("[ Would you like to try again? ]\n")
                        game_over = game_over.lower()
                        while game_over not in yes_or_no:
                            game_over = input("[ Input not recognised. Please try again! ]")
                            game_over = game_over.lower()
                        if game_over == 'yes':
                            intro_screen = False
                            game_start = True
                            if os.path.exists("kippi_save.txt"):
                                os.remove("kippi_save.txt")
                            else:
                                pass
                            continue_game = False
                            break
                        if game_over == 'no':
                            game_start = False
                            intro_screen = True
                            if os.path.exists("kippi_save.txt"):
                                os.remove("kippi_save.txt")
                            else:
                                pass
                            break
                    else:
                        print("[ Zealous frowns. ]")
                        print('''[ "Hah! Fine, then. Act that way. Let's see how you'll match with my unbridled fury!" Zealous booms. ]''')
                        zealous_the_real_one_encounter()
                        if kippi_stats[3] <= 0:
                            print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")
                            print("        _.---,._,'\n       /' _.--.<\n         /'     `'                                 ____\n       /' _.---._____                           __(_   )__\n       〵.'   ___, .-'`                       _(          )\n           /'    〵.                         (     )-----`\n         /'       `-.  ,-                     `---'\n        |\n        |                   .-------.\n        |                 .'         `.\n        |                 |  H E R E  |\n        |                 |           |\n        |                 |  L I E S  |\n        |                 |           |\n        |                 | K I P P I |\n        |                 |           | **\n        !                 |           |//\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            game_over = input("[ Would you like to try again? ]\n")
                            game_over = game_over.lower()
                            while game_over not in yes_or_no:
                                game_over = input("[ Input not recognised. Please try again! ]")
                                game_over = game_over.lower()
                            if game_over == 'yes':
                                intro_screen = False
                                game_start = True
                                if os.path.exists("kippi_save.txt"):
                                    os.remove("kippi_save.txt")
                                else:
                                    pass
                                continue_game = False
                                break
                            if game_over == 'no':
                                game_start = False
                                intro_screen = True
                                if os.path.exists("kippi_save.txt"):
                                    os.remove("kippi_save.txt")
                                else:
                                    pass
                                break
                        print("             .#############. \n          .###################. \n       .####%####################.,::;;;;;;;;;;, \n      .####%###############%######:::;;;;;;;;;;;;;, \n      ####%%################%######:::;;;;;;;;@;;;;;;, \n      ####%%################%%#####:::;;;;;;;;;@;;;;;;, \n      ####%%################%%#####:::;;;;;;;;;@@;;;;;; \n      `####%################%#####:::;;;;;;;;;;@@;;;;;; \n        `###%##############%####:::;;;;;;;;;;;;@@;;;;;; \n           `#################'::%%%%%%%%%%%%;;;@;;;;;;' \n             `#############'.%%%%%%%%%%%%%%%%%%;;;;;' \n               `#########'%%%%#%%%%%%%%%%%%%%%%%%%, \n                 `#####'.%%%%#%%%%%%%%%%%%%%#%%%%%%, \n                   `##' %%%%##%%%%%%%%%%%%%%%##%%%%% \n                   ###  %%%%##%%%%%%%%%%%%%%%##%%%%% \n                    '   %%%%##%%%%%%%%%%%%%%%##%%%%% \n                   '    `%%%%#%%%%%%%%%%%%%%%#%%%%%' \n                  '       `%%%#%%%%%%%%%%%%%#%%%%' \n                  `         `%%%%%%%%%%%%%%%%%%' \n                   `          `%%%%%%%%%%%%%%' \n                    `           `%%%%%%%%%%'  ' \n                     '            `%%%%%%'   ' \n                    '              `%%%'    ' \n                   '               .%%      ` \n                  `                %%%       ' \n                   `                '       ' \n                    `              '      ' \n                    '            '      ' \n                   '           '       ` \n                  '           '        ' \n                              `       ' \n                               ' \n                              ' \n                             ' \n\n\na@@@@@@@@a  a@@@@@@a  a@@@@@@@a a@@@@@@@@a a@@a.  .a@@a  a@@a \n@@@@  @@@@ @@@@  @@@@ @@@@  @@@ @@@@@@@@@@ @@@@a  a@@@@  @@@@ \n@@@@  @@@@ @@@@  @@@@ @@@@  @@@    @@@@    `@@@@  @@@@'  @@@@ \n@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@'    @@@@      `@@@@@@'    @@@@ \n@@@@@@@@@' @@@@@@@@@@ @@@@@@@@a    @@@@        @@@@      `@@' \n@@@@       @@@@  @@@@ @@@@ @@@@    @@@@        @@@@ \n@@@@       @@@@  @@@@ @@@@ @@@@    @@@@        @@@@       @@\n")
                        print("[ Congratulations! You've just saved the kingdom of Nyuwuwoville from being caught up in flames! ]")
                        print("[ Every kitfolk in the kingdom appreciates you now, and they won't throw stones at you whenever they see you! ]")
                        print("[ Is this what they call a... happy ending? ]\n")
                        game_over = input("[ Would you like to try again? ]\n")
                        game_over = game_over.lower()
                        while game_over not in yes_or_no:
                            game_over = input("[ Input not recognised. Please try again! ]")
                            game_over = game_over.lower()
                        if game_over == 'yes':
                            intro_screen = False
                            game_start = True
                            if os.path.exists("kippi_save.txt"):
                                os.remove("kippi_save.txt")
                            else:
                                pass
                            continue_game = False
                            break
                        if game_over == 'no':
                            game_start = False
                            intro_screen = True
                            if os.path.exists("kippi_save.txt"):
                                os.remove("kippi_save.txt")
                            else:
                                pass
                            break
