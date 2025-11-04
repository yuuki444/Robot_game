import random


class Robot:
    def __init__(self, clas, hp, damage=100, defense=20, stamina=50):
        self.clas = clas
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.stamina = stamina
        self.wins = 0

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        if not self.is_alive():
            print(f"{self.clas} не может атаковать, он повержен!")
            return
        print(f"{self.clas} атакует {other.clas}!")
        other.take_damage(self.damage)

    def take_damage(self, dmg):
        real_damage = max(0, dmg - self.defense)
        self.hp = max(0, self.hp - real_damage)
        print(f"{self.clas} получает {real_damage} урона (ХП: {self.hp})")

    def heal(self, amount):
        if not self.is_alive():
            print(f"{self.clas} повержен, не может лечиться")
            return
        self.hp = min(100, self.hp + amount)
        print(f"{self.clas} восстановил {amount} ХП (ХП: {self.hp})")

    def __str__(self):
        return f"{self.clas}: ХП={self.hp}, Дамаг={self.damage}, Защита={self.defense}"



















# ------------------ Танк ------------------
class Tank(Robot):
    def __init__(self):
        super().__init__("Танк", hp=200, damage=30, defense=100, stamina=20)
        self.has_resistance = False

    def activate_resistance(self):
        if not self.is_alive():
            print(f"{self.clas} не может активировать резист — повержен")
            return
        self.has_resistance = True
        print(f"{self.clas} активирует резист! Следующий удар уменьшен на 40%")

    def take_damage(self, dmg):
        if self.has_resistance:
            dmg = int(dmg * 0.6)
            print(f"{self.clas} СНИЗИЛ УРОН 40% !!!!!({dmg} осталось)")
            self.has_resistance = False
        super().take_damage(dmg)


















# ------------------ Снайпер ------------------
class Sniper(Robot):
    def __init__(self):
        super().__init__("Снайпер", hp=100, damage=170, defense=5, stamina=20)

    def headshot(self, other):
        if not self.is_alive():
            print(f"{self.clas} не может атаковать — повержен")
            return
        critical = random.random() < 0.3
        dmg = self.damage * 2 if critical else self.damage
        print(f"{self.clas} стреляет {'(ДАЕДАЛУС СРАБОТАЛ!!!!!!!!)' if critical else ''} по {other.clas}")
        other.take_damage(dmg)















# ------------------ Медик ------------------
class Medic(Robot):
    def __init__(self, clas="Медик"):
        super().__init__(clas, hp=100, damage=50, defense=20, stamina=60)

    def heal_ally(self, ally):
        if not self.is_alive():
            print(f"{self.clas} не может лечить — уничтожен!")
            return
        amount = random.randint(20, 40)
        print(f"{self.clas} ПЛЮС ХП(ЛЕЧИТ) {ally.clas} на {amount} ХП!")
        ally.hp = min(ally.hp + amount, 100)
        print(f"{ally.clas} теперь имеет {ally.hp} ХП.")







# ------------------ Ассасин ------------------
class Assassin(Robot):
    def __init__(self, clas="Ассасин"):
        super().__init__(clas, hp=90, damage=100, defense=10)
        self.miss_chance = 0.3 

    def attack(self, other):
        if not self.is_alive():
            return
        if random.random() < self.miss_chance:
            print(f"{self.clas} ПРОМАХИВАЕТСЯ!!!!!!!!!!!! по {other.clas}!")
        else:
            print(f"{self.clas} атакует {other.clas}!")
            other.take_damage(self.damage)












# ------------------ Варлок ------------------
class Warlock(Robot):
    def __init__(self, clas="Варлок"):
        super().__init__(clas, hp=120, damage=50, defense=15, stamina=40)
        self.poison_turns = 0
        self.poison_damage = 10

    def poison_attack(self, other):
        if not self.is_alive():
            print(f"{self.clas} не может атаковать, он повержен")
            return
        print(f"{self.clas} использует ЯДОВИТУЮ АТАКУ!!!! на {other.clas}!")
        other.take_damage(self.damage)
        if getattr(other, "poison_turns", 0) <= 0:
            other.poison_turns = 3
            print(f"{other.clas} отравлен на 3 хода!!!")

    def apply_poison(self):
        if self.poison_turns > 0 and self.is_alive():
            self.hp = max(0, self.hp - self.poison_damage)
            self.poison_turns -= 1
            print(f"{self.clas} получает {self.poison_damage} УРОН от ЯДА! Осталось ХП: {self.hp}")















# ================== БОЙ ==================
def battle(robot1, robot2, max_turns=50):
    print("\n=== НАЧАЛО БОЯ ===")
    print(robot1)
    print(robot2)
    print("==================\n")

    turn = 1
    while robot1.is_alive() and robot2.is_alive() and turn <= max_turns:
        print(f"\n--- ХОД {turn} ---")
        attacker, defender = (robot1, robot2) if turn % 2 else (robot2, robot1)

#======================ETO YAD================
        for r in [attacker, defender]:
            if isinstance(r, Warlock) and r.poison_turns > 0:
                r.apply_poison()

        if isinstance(attacker, Warlock) and random.random() < 0.5:
            attacker.poison_attack(defender)
        elif isinstance(attacker, Tank) and random.random() < 0.3:
            attacker.activate_resistance()
        elif isinstance(attacker, Sniper) and random.random() < 0.4:
            attacker.headshot(defender)
        elif isinstance(attacker, Medic) and random.random() < 0.4:
            attacker.heal_ally(attacker)
        else:
            attacker.attack(defender)

        if not defender.is_alive():
            print(f"\n💀 {defender.clas} уничтожен!\n")
            break

        turn += 1

    if turn > max_turns:
        print("\n⚠️ Бой закончился по лимиту ходов! Победитель определяется по ХП")
        winner = robot1 if robot1.hp > robot2.hp else robot2
    else:
        winner = robot1 if robot1.is_alive() else robot2
        winner.wins += 1  # Увеличиваем счетчик побед
        print(f"🏆 Победитель: {winner.clas}! (Побед всего: {winner.wins})\n")

    return winner


# ================== ТУРНИР ==================
def tournament():
    robots = [Tank(), Sniper(), Medic(), Assassin(), Warlock(),
              Tank(), Sniper(), Assassin()]
    random.shuffle(robots)

    print("=== ТУРНИР ===")

    semi1 = battle(robots[0], robots[1])
    semi2 = battle(robots[2], robots[3])
    semi3 = battle(robots[4], robots[5])
    semi4 = battle(robots[6], robots[7])

    final1 = battle(semi1, semi2)
    final2 = battle(semi3, semi4)

    champion = battle(final1, final2)
    print(f"🎉 ЧЕМПИОН ТУРНИРА: {champion.clas}!")



if __name__ == "__main__":
    tournament()
