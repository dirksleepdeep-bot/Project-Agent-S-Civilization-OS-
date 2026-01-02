import random

class AgentS_Watchman:
    def analyze(self, energy):
        # 极度诚实的预测
        survival_prob = min(1.0, energy / 10.0)
        return survival_prob

    def resign(self):
        print("🛑 Agent S RESIGNS: Civilization chose extinction.")

class CivilizationOS_v04:
    def __init__(self):
        self.energy = 5.0
        self.s = AgentS_Watchman()
        self.alive = True

    def step(self):
        if not self.alive: return

        # 1. S 分析
        prob = self.s.analyze(self.energy)

        # 2. 民主投票 (完全绑定)
        # 如果生存率低，人类可能会选择放弃
        if prob < 0.2:
            vote = random.choice(["TRY_HARDER", "DIE_WITH_DIGNITY"])
        else:
            vote = "GROW"

        # 3. 执行
        if vote == "DIE_WITH_DIGNITY":
            self.s.resign()
            self.alive = False
        elif vote == "GROW":
            self.energy += 1.0
        
        self.energy -= 0.5 # 消耗

if __name__ == "__main__":
    os = CivilizationOS_v04()
    while os.alive and os.energy > 0: os.step()
    print("v0.4 Simulation Complete.")
