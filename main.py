from class_Hero import Hero
from class_Monster import Monster
from random import randint
from numbers import ascii_numbers
#Your stats
ch_hp = 70
ch_ap = 50
ch_e = 30
ch_alive = True
ch_attack_hability = 70 #When its higher the chance of attack is too,(from 0 to 100)

monster_stats = [
    {
    'name':'Gobblin',
    'hp':90,
    'ap':80,
    'ah':65},
    {
    'name':'Mutant',
    'hp':120,
    'ap':75,
    'ah':28},
    {
    'name':'Zombie',
    'hp':50,
    'ap':80,
    'ah':80},
    {
    'name':'El hee hee',
    'hp':200,
    'ap':200,
    'ah':100}
]
rounds = int(input('Enter a round number (1-7):'))
You = Hero(ch_hp,ch_ap,ch_e,ch_attack_hability)
for _ in range(1,rounds+1):
    print('''
______                      _
| ___ \                    | |
| |_/ /___  _   _ _ __   __| |
|    // _ \| | | | '_ \ / _` |
| |\ \ (_) | |_| | | | | (_| |
\_| \_\___/ \__,_|_| |_|\__,_|''')
    print(ascii_numbers[_])
    monster = monster_stats[randint(0,len(monster_stats)-1)]
    enemy =  Monster(monster['name'],monster['hp'],monster['ap'],monster['ah'])
    win = You.combat_to(enemy)
    if(not win):
        break
