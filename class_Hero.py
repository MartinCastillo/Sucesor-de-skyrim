from random import randint
class Hero:
    def __init__(self, hp,ap,endurance,attack_hability):
        """HP,AP,Endurance,attack_hability"""
        self.hp = hp
        self.ap = ap
        self.alive = True
        self.attack_hability = attack_hability
        self.endurance = endurance
        self.attack_chance = randint(self.attack_hability,100)
        self.curation_range = (-10,20)
    def display_turn_info(self,max_space = 15):
        print('''
                    Your Turn
    ##################################################
    INFO::              | Controls:
    HP: {}              | a : Attack with a {}%
    Attack points: {}   | chance of hit.
    Endurance: {}       | b: Block whith {}% chance
                        | of revive critical dagmage.
                        | c: Cure yourself ({} to {})
                        | points
    ##################################################
        '''.format(self.hp,self.attack_chance,self.ap,self.endurance,self.hp/(self.ap/10),
        self.curation_range[0],self.curation_range[1]))

    def _attack_object(self,obj,range_probability):
        #Takes as param the object (Monster to attak) and the range of probability
        rand = randint(5,105)
        theorical_hp = int((self.ap*rand)/range_probability)
        if(rand < range_probability):
            print('-You attack, {} lose {} health points'.format(\
                obj.prefix,theorical_hp))
            return(theorical_hp)
        else:
            print('-You try to attack the {}, you fail'.format(obj.prefix))
            return(0)

    def _block(self):
        if(randint(0,100)>self.hp/(self.ap/10)):
            dag = int(100/self.endurance)
            print('-You block sucefully, you just lose {} of health points'.format(dag))
            return(dag)
        else:
            dag = int(obj.attack(self.endurance))
            print('-Your block fail, you lose {} of health points'.format(dag))
            return(dag)

    def _set_hp(self,new_hp):
        self.hp = new_hp
        print('-Now you have {} of health points'.format(self.hp))

    def cure_yourself(self):
        _hp = (randint(0,40))
        if(_hp>0):
            print('You cure yourself sucefully (+{})'.format(_hp))
        else:
            print('You hurt yourself trying to cure yourself ({})'.format(_hp))
        self._set_hp(self.hp+_hp)

    def combat_to(self,obj):
        print('YOU START A COMBAT WITH a {}'.format(obj.prefix.upper()))
        self.attack_chance = randint(self.attack_hability,100)
        #This function have all the bucle for combat events
        #with the obj object
        while(True):
            if(self.hp<0):
                print('You are dead')
                self.alive = False
                break
            if(obj.hp<0):
                print('{} is dead'.format(obj.prefix))
                break
            self.display_turn_info()
            action_satisfaced = False
            block = False
            while(not action_satisfaced):
                act = input('-Action: ')
                if(act == 'a'):
                    obj._set_hp(obj.hp -self._attack_object(obj,self.attack_chance))
                    action_satisfaced = True
                elif(act == 'b'):
                    block = True ; action_satisfaced = True
                elif(act == 'c'):
                    self.cure_yourself()
                    action_satisfaced = True
                else:
                    print('Please enter a valid action')
            if(block):
                self._set_hp(self.hp -self._block())
            else:
                self._set_hp(self.hp - obj.attack(self.endurance))
        print('##################################')
        return(self.alive)
