from game import person 

magic = [{"name": "fire", "cost": 10, "dmg": 100},
         {"name": "thunder", "cost": 12, "dmg": 124},
         {"name": "blizzard", "cost": 10, "dmg": 100}]


player = person(460, 65, 60, 34, magic)
enemy = person(1200, 65, 45, 25, magic)

running = True
i = 0

print("AN ENEMY ATTACKS!")

while running:
    print("================")
    player.choose_action()
    choice = input("Choose action")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print("\n lol you broke\n")
            continue
     
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print("\n" + spell + " deals", str(magic_dmg), "points of damage")
        
        
        
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy atacks for", enemy_dmg)

    print("------------------------------")
    print("Enemy HP:", + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + "\n")

    print("your HP:", + str(player.get_hp()) + "/" + str(player.get_max_hp()))
    print("your MP:", + str(player.get_mp()) + "/" + str(player.get_max_mp()) + "\n")
    

    if enemy.get_hp() == 0:
        print("you win!!")
        running = False
    elif player.get_hp() == 0:
        print("your enemy has defeated you! :(")
        running = False
