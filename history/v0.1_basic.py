import random

class CivilizationOS_v01:
    def __init__(self):
        self.year = 2026
        # 初始状态
        self.energy_security = 0.5
        self.knowledge_level = 0.2
        self.infrastructure = 0.6
        self.history = []

    def decide(self):
        # 硬编码的生存逻辑 (恒温器)
        if self.energy_security < 0.6:
            return "INVEST_ENERGY"
        elif self.knowledge_level < 0.7:
            return "RESEARCH"
        else:
            return "BUILD"

    def step(self):
        self.year += 1
        decision = self.decide()

        # 执行结果
        if decision == "INVEST_ENERGY":
            self.energy_security += 0.05
        elif decision == "RESEARCH":
            # 学习有失败概率
            if random.random() < 0.6: self.knowledge_level += 0.05
        elif decision == "BUILD":
            self.infrastructure += 0.04

        # 熵增 (自然损耗)
        self.energy_security -= 0.01
        self.infrastructure -= 0.01

        self.history.append((self.year, decision, round(self.energy_security, 2)))

if __name__ == "__main__":
    os = CivilizationOS_v01()
    for _ in range(50): os.step()
    print("v0.1 Simulation Complete.")
