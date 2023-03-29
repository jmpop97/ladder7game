import random

class BaseCharacter:
    def __init__(self, name, hp, mp, _str, arm, _int, spd):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self._str = _str
        self.arm = arm
        self._int = _int
        self.spd = spd

    def status(self):
        print(f"{self.name}: Hp {self.hp}/{self.max_hp} MP {self.max_mp}/{self.max_mp}")

    def show_detail(self):
        print(f'{self.name} 직업:{type(self).__name__}  Hp {self.hp}/{self.max_hp} MP {self.max_mp}/{self.max_mp}')
        print(f'힘 {self._str} 방어력 {self.arm} 지능 {self._int} 속도 {self.spd}')

    def attack(self, other):
        damage = random.randint(self._str, self._str)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

class Warrior(BaseCharacter):
    def __init__(self, name, hp, mp, _str, arm, _int, spd):
        super().__init__(name, hp, mp, _str, arm, _int, spd)
        self.max_hp = hp + 20
        self.hp = hp + 20
        self._str = _str + 15
        self.arm = arm + 5 
        self.spd = spd - 2

    def power_attack(self, other):
        damage = random.randint(self._str*0.8, self._str*1.2)
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)  
        print(f"{self.name}의 파워 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
    
    def gaurd(self):
        self.gaurdstack += 1 
        self.arm += self.gaurdstack*4 
        print(f"{self.name}이 공격을 방어합니다! {self.name}의 방어력이 {self.arm}상승")
        
        #방어력이 계속 올라감 가드스택을 초기화 해줘야 함
class Mage(BaseCharacter):
    def __init__(self, name, hp, mp, _str, arm, _int, spd):
        super().__init__(name, hp, mp, _str, arm, _int, spd)
        self.max_hp = hp - 10
        self.hp = hp - 10
        self._str = _str - 15
        self.arm = arm - 1
        self.spd = spd + 2
        self.max_mp = mp + 40
        self.mp = mp + 40
        self._int = _int + 25

    def fire_magic(self, other):
        damage = random.randint(self._int*0.8, self._int*1.2)
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)  
        print(f"{self.name}의 화염 마법! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def wind_magic(self, other):
        damage1 = random.randint((self._int - other.arm)*0.3, (self._int - other.arm)*0.7)
        damage2 = random.randint((self._int - other.arm)*0.3, (self._int - other.arm)*0.7)
        damage3 = random.randint((self._int - other.arm)*0.3, (self._int - other.arm)*0.7)

        damage = damage1 + damage2 + damage3
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - 5, 0)  
        print(f"{self.name}의 바람 마법! {other.name}에게 {damage1}, {damage2}, {damage3}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Thief(BaseCharacter):
    def __init__(self, name, hp, mp, _str, arm, _int, spd):
        super().__init__(name, hp, mp, _str, arm, _int, spd)
        self._str = _str + 5
        self.arm = arm + 2
        self.spd = spd + 12
        self.hide = False
    

    def hide(self):
        self.hide = True
        self.spd += 5
        print(f"{self.name}은 은신했습니다. spd가 {5}만큼 상승")

    def hide_attack(self, other):
        damage = random.randint((self._str + self.spd)*1.6 , (self._str + self.spd)*2.4)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 은신공격! {other.name}에게 {damage}의 치명적인 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        
        self.hide = False
        self.spd -= 5
        
        
class Archer(BaseCharacter):
    def __init__(self, name, hp, mp, _str, arm, _int, spd):
        super().__init__(name, hp, mp, _str, arm, _int, spd)
        self.max_hp = hp + 7
        self.hp = hp + 7
        self._str = _str + 7
        self.arm = arm + 2
        self.spd = spd + 7
    
    def silver_arrow_shot(self, other):
        if other.type == '언데드':
            damage = random.randint(int(self._str+self.spd)*1.8, int(self._str+self.spd)*2.2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 은화살공격! {other.name}은 언데드라 {damage}의 치명적인 데미지를 입었습니다.")
        else:
            damage = random.randint(int(self._str+self.spd)*0.8, int(self._str+self.spd)*1.2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 은화살공격! {other.name}은 {damage}의 데미지를 입었습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

# 실험용 
class Monster(BaseCharacter):
    def __init__(self, name, hp, mp, _str, arm, _int, spd):
        super().__init__(name, hp, mp, _str, arm, _int, spd)
        self.max_hp = hp + 7
        self.hp = hp + 7
        self._str = _str + 7
        self.arm = arm + 2
        self.spd = spd + 7
        self.type = '언데드'
# 몬스터 


jobs = ['Archer', 'Archer', 'Mage', 'Thief']
players = ['player1','player2','player3','player4']


for i in [0, 1, 2, 3]:
    if jobs[i] == 'Archer':
        players[i] = Archer('archerkim',100,100,20,5,10,5)
    elif jobs[i] == 'Warrior':
        players[i] = Warrior('WarriorChoi',100,100,20,5,10,5)
    elif jobs[i] == 'Mage':
        players[i] = Mage('MageLee',100,100,20,5,10,5)
    elif jobs[i] == 'Thief':
        players[i] = Thief('ThiefHwang',100,100,20,5,10,5)

print(players[3])

mon1 = Monster('언데드 아처',1,1,1,1,1,1)
players[1].silver_arrow_shot(mon1)



# 메인에서 jobs = 'Archer' 보네면 , 

