from random import randint
class Monster:
    def __init__(self,prefix,max_hp,attack_point,attack_hability):
        """Prefix , max_hp , attack_point , attack_hability"""
        self.prefix = prefix
        self.hp = max_hp
        self.attack_point = attack_point
        self.alive = True
        self.attack_hability = attack_hability
    def attack(self,range_probability):
        #A bigger range probability closer to 100 (from 0 to 100) is more
        #probaby to block the attack
        print('-The {} '.format(self.prefix),end='')
        rand = randint(self.attack_hability,105)
        #Calculate the dagmage recibed
        theorical_hp = int((self.attack_point*rand)/(range_probability*10))
        if(rand > range_probability):
            print('attack you, you lose {} health points'.format(\
                theorical_hp))
            return(theorical_hp)
        else:
            print('try to attack you, he fails')
            return(0)
    def is_alive(self):
        if(self.hp>0):
            return True
        else:
            return False
    def _set_hp(self,new_hp):
        self.hp = new_hp
        print('-Now {} have {} of health points'.format(self.prefix,self.hp))
