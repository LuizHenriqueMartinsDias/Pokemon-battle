
class Pokemon:
    def __init__(self,stats,name,moves,poke_types,lvl):
        self.stats = stats
        self.name = name
        self.moves = moves
        if "/" in poke_types:
            self.poke_types = poke_types.split("/")
        else:
            self.poke_types = poke_types
        self.lvl = lvl
        self.hp = self.stats.calc_hp(self.lvl)
        self.max_hp = self.hp
        self.atk = self.stats.calc_atk(self.lvl)
        self.def_ = self.stats.calc_def(self.lvl)
        self.sp_atk = self.stats.calc_sp_atk(self.lvl)
        self.sp_def = self.stats.calc_sp_def(self.lvl)
        self.speed = self.stats.calc_speed(self.lvl)

        self.atk_stage = 0
        self.def_stage = 0
        self.sp_atk_stage = 0
        self.sp_def_stage = 0
        self.speed_stage = 0

    def __str__(self):
        return self.name

class Move:
    def __init__(self,name,move_type,category,power,accuracy,effect=None):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.effect = effect


    def __str__(self):
        return self.name

    def apply_effect(self, user, target):
        if self.effect:
            return self.effect(user, target)
        return None