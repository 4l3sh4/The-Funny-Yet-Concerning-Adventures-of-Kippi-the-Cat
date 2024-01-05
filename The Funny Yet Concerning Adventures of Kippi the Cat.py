#we use this to do all the random chances that is involved in our game. makes it more fun, hehe!
import random

start_options = ['play', 'continue', 'credit']
game_start = False

print("		  _______ __   __ _______   _______ __   __ __    _ __    _ __   __\n		 |       |  | |  |       | |       |  | |  |  |  | |  |  | |  | |  |\n		 |_     _|  |_|  |    ___| |    ___|  | |  |   |_| |   |_| |  |_|  |\n 		   |   | |       |   |___  |   |___|  |_|  |       |       |       |\n 		   |   | |       |    ___| |    ___|       |  _    |  _    |_     _|\n 		   |   | |   _   |   |___  |   |   |       | | |   | | |   | |   |\n 	 	   |___| |__| |__|_______| |___|   |_______|_|  |__|_|  |__| |___|\n __   __ _______ _______   _______ _______ __    _ _______ _______ ______   __    _ ___ __    _ _______ \n|  | |  |       |       | |       |       |  |  | |       |       |    _ | |  |  | |   |  |  | |       |\n|  |_|  |    ___|_     _| |       |   _   |   |_| |       |    ___|   | || |   |_| |   |   |_| |    ___|\n|       |   |___  |   |   |       |  | |  |       |       |   |___|   |_||_|       |   |       |   | __\n|_     _|    ___| |   |   |      _|  |_|  |  _    |      _|    ___|    __  |  _    |   |  _    |   ||  |\n  |   | |   |___  |   |   |     |_|       | | |   |     |_|   |___|   |  | | | |   |   | | |   |   |_| |\n  |___| |_______| |___|   |_______|_______|_|  |__|_______|_______|___|  |_|_|  |__|___|_|  |__|_______|\n   _______ ______  __   __ _______ __    _ _______ __   __ ______   _______ _______   _______ _______     \n  |   _   |      ||  | |  |       |  |  | |       |  | |  |    _ | |       |       | |       |       |\n  |  |_|  |  _    |  |_|  |    ___|   |_| |_     _|  | |  |   | || |    ___|  _____| |   _   |    ___|\n  |       | | |   |       |   |___|       | |   | |  |_|  |   |_||_|   |___| |_____  |  | |  |   |___\n  |       | |_|   |       |    ___|  _    | |   | |       |    __  |    ___|_____  | |  |_|  |    ___|\n  |   _   |       ||     ||   |___| | |   | |   | |       |   |  | |   |___ _____| | |       |   |\n  |__| |__|______|  |___| |_______|_|  |__| |___| |_______|___|  |_|_______|_______| |_______|___|\n	 ___   _ ___ _______ _______ ___   _______ __   __ _______   _______ _______ _______ \n	|   | | |   |       |       |   | |       |  | |  |       | |       |   _   |       |\n	|   |_| |   |    _  |    _  |   | |_     _|  |_|  |    ___| |       |  |_|  |_     _|\n	|      _|   |   |_| |   |_| |   |   |   | |       |   |___  |       |       | |   |\n	|     |_|   |    ___|    ___|   |   |   | |       |    ___| |      _|       | |   |\n	|    _  |   |   |   |   |   |   |   |   | |   _   |   |___  |     |_|   _   | |   |\n	|___| |_|___|___|   |___|   |___|   |___| |__| |__|_______| |_______|__| |__| |___|\n\n\n                                                   ^✦\n                                                  |||\n                                        ^----^    |||\n                                       (  •u• )   |||\n                                       |     |〵_|〵/|\n                                    _  | |   |〵__|_|\n                                    ||_!_|   〵 \n                                     ---|  T_ 〵\n                                        |  |_|_|\n                                        !_/     〵    ^\n                                   /〵  /         〵 / 〵\n                                  /  〵/           〵   〵\n\n                                          [ PLAY ]\n\n                                        [ CONTINUE ]\n\n                                         [ CREDIT ]\n")
start_input = input("[ Insert any command! ]\n")
start_input = start_input.lower()
while start_input not in start_options:
        start_input = input("[ Input not recognised. Please try again! ]")
if start_input == 'play':
        game_start = True


while game_start == True:
        #list of stats
        #kippi
        #dictionary ver.
        kippi_stats_dictionary = {'LVL': 1, 'EXP' : 0, 'EXP TO LVL UP' : 1, 'HP': 10, 'ATK': 3, 'DEF': 1, 'SPD' : 4}

        #list ver.
        kippi_stats_perm = list(kippi_stats_dictionary.values())
        kippi_stats = list(kippi_stats_dictionary.values())


        #enemies
        #we use dictionaries for this! i was originally gonna use lists, but bruh, it's so hard to memorise which stat is which... so yeah!
        skunk_stats = {'NAME' : 'SKUNK', 'HP': 3, 'ATK': 2, 'DEF': 2, 'SPD' : 3, 'EXP GAIN' : 1}

        #list of defines
        #we use 'define' whenever we want to re-use similar code, saves time! it also makes the code neater, which is god's gift to my eyes and my awful comprehension skills.

        def death_mechanic():
            if kippi_stats <= 0:
                print("[ KIPPI fainted! ]")
                print("[ As your life flashes before your tiny eyes... You wondered whether your fate would've stayed the same if you did anything different...? ]")

        def level_up_mechanic():
            if kippi_stats[1] >= kippi_stats[2]:
                print("You feel somehow stronger!")
                kippi_stats_perm[0] += 1 #level up
                kippi_stats_perm[1] = 0 #restart experience points to 0
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

        def direction_mechanic():
            while deciding_direction == True :
                direction_choice = input("[ What shall you do? ]\n[ WALK RIGHT ] [ WALK LEFT ] [ WALK FORWARD ]\n")
                direction_choice = direction_choice.lower()
                while direction_choice not in directions :
                        direction_choice = input("[ Uh... Your command seems to not be clear enough. Perhaps you could try again? ]\n")
                if 'right' in direction_choice:
                    break
                elif 'left' in direction_choice:
                    break
                elif 'forward' in direction_choice:
                    break

        def skunk_encounter():
            battle_mode = True
            while battle_mode == True:
                enemy_stats = list(skunk_stats.values())
                print(enemy_stats)
                random_chance = random.randint(1, 3)
                print(f" [ A {enemy_stats[0]} suddenly appeared out of the bush! ]")
                if kippi_stats[6] >= enemy_stats[4] :
                    if random_chance == 1:
                        print("[ Kippi manages to react first! ]")
                    elif random_chance == 2:
                        print("[ Kippi gets the upper hand! ]")
                    else:
                        print("[ The swift lil' kitty legs of Kippi acted on their own! ]")
                if kippi_stats[6] < enemy_stats[4] :
                    if random_chance == 1:
                        print("[ Kippi dissociated themselves from the situation for a second, and now they're being attacked! ]")
                    elif random_chance == 2:
                        print("[ Kippi was blindsided by the enemy's swiftness! ]")
                    else:
                        print("[ Kippi could not keep up with the enemy's actions in time! ]")
                while kippi_stats[6] >= enemy_stats[4] :
                    print("[FIGHT] [ITEMS] [RUN]\n".center(32))
                    face = '•w•'
                    print(f"      ^----^\n     (  {face} )\n     |     ||\n  _  | |   ||    〵         __/|\n  ||_!_|   |!   _  _c,     / __/\n   ---|  T |      |ó 〵___/ /\n      |  | |        〵      |\n      !__!_!         L/``〵_J")
                    battle_input = input("[ What will Kippi do? ]\n")
                    battle_input = battle_input.lower()
                    if not battle_input == 'fight' and not f_o_f == 'items' and not f_o_f == 'run':
                        print("[ Please choose either FIGHT, ITEMS, or RUN. Silly kitty! ]")
                    if battle_input == 'fight':
                        enemy_stats[1] -= (kippi_stats[4] - enemy_stats[3])
                        if enemy_stats[1] <= 0:
                            print(f"[ {enemy_stats[0]} fainted! ]")
                            print("[ Kippi wins! ]")
                            kippi_stats[1] += enemy_stats[5]
                            print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                            break
                        print(f"[ {enemy_stats[0]} health is down to {enemy_stats[1]}! ]")
                        kippi_stats[3] -= (enemy_stats[2] - kippi_stats[5])
                        print(f"[ {enemy_stats[0]} fights back! Kippi's health is down to {kippi_stats[3]}! ] \n")
                        if kippi_stats[3] <= 0:
                            print("[ KIPPI fainted! ]")
                            break
                        face = random.randint(1,4)
                        if face == 1:
                            face = '•w•'
                        elif face == 2:
                            face = '•u•'
                        elif face == 3:
                            face = '^W^'
                        else:
                            face = '^u^'
                break

        #list of lists (lol)
        directions = ['right','left','forward']
        inventory = []

        #modes
        battle_mode = False

        #the actual game
        while kippi_stats[0] < 10:
                floresta_location = random.randint(1, 3)
                if floresta_location == 1:
                    print("                               * *    \n             * *            *    *  *\n          *   *    *     *  *    *     *  *\n    *  *      *        *     *    *  *    *\n  *       *    *   * *   *    *    *    *   *\n  * *      *  *  * *     *  *    * * .#  *   *\n *    *  #  *   *  *   *     * #.  .# *   *\n* *     :# * .*     *      #.  #: #  * *    *\n*   * *  ## #     *   * *  #. ##        *\n *     * ###    *            ###\n   *  * ##   *                ##\n      .##                      ##.\n     :##.                      .##:\n    :###                       :###\n     ;###                     ;###\n    ,####.                   ,####.\n   .######.                 .######.\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`\n")
                    print("[ As the wind blows stronger, the viridescent leaves of the trees around you keep falling to the ground, gracefully. ]\n[ You wish you could simply make a pile of leaves, jump into them, and make an adsolute mess, but alas, to finish your quest is your ultimate priority. No playing around! ]")
                if floresta_location == 2:
                    print("     @%      @%         \n     `@%.  `;@%.      @@%;         \n      `@%%. `@%%    ;@@%;        \n       ;@%. :@%%  %@@%;       \n         %@bd%%%bd%%:;     \n          #@%%%%%:;;\n            %@@%::;\n            %@@(o);  . '         \n          %@@@;:(.,'         \n        `.. %@@@::;         \n           `)@o%::;         \n            %(o)::;        \n           .%@@%::;         \n           ;%@@%::;.          \n          ;%@@%%:;;;. \n     ...;%@@@%%:;;;;,. \n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                    print("[ You could see a couple of dead trees around... ]\n[ You feel a bit unsettled, but you try your best to pay no mind to it. ]")
                if floresta_location == 3:
                    print("       _____                     ___\n      (#.#.#)__                _(#.#\n     (#.#.#.#)#)              (#.#.#\n`.`.`.^----^`.`.`.`.`/     /`.`.`.`.\n`.`.`(  •w• )`.`.`.`/     /`.`.`.`.`\n`.`.`|     ||`.`.`./     /`.`.`.`.`.\n`._.`| |   ||`.`.`/     /`.`.`.`.`.`\n` ||_!_|   |!`.`./     /`.`.`.`.`.`.\n`.`---|  T |`.`./     /`.`.`.`.`.``.\n      |  | |\n      !__!_!\n________________       ________________\n`.`.`.`.`.`.`.`.〵     〵`.`.`.`.`.`.`.`")
                    random_chance_input = input("[ You could see some berry bushes around you! You feel tempted to see what's behind them. ]\n[ Would you like to take a peek? ]\n")
                    if random_chance_input == 'yes' :
                        random_chance = random.randint(1, 4)
                        if random_chance == 1 or random_chance == 2 or random_chance == 3 or random_chance == 4 :
                            skunk_encounter()
                ##          elif random_chance == 2:
                ##              monkey_encounter()
                ##          elif random_chance == 3:
                ##              crow_encounter()
                ##          else:
                ##              item_find()
                    if random_chance_input == 'no' :
                        continue
                level_up_mechanic()
                print(kippi_stats)
                deciding_direction = True
                direction_mechanic()

