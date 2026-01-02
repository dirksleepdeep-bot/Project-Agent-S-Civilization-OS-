import random

class CivilizationOS_v03:
    def __init__(self):
        self.resources = {"ENERGY": 0.6, "INDUSTRY": 0.5}
        self.commitment = 0.0
        self.trajectory = "ENERGY"
        self.pain_log = [] # 记录人为灾难

    def inject_pain(self):
        # Agent S 主动破坏优势资源，强迫文明转型
        print(f"⚠️ Agent S INJECTING PAIN on {self.trajectory}!")
        self.resources[self.trajectory] -= 0.3
        self.commitment = 0.0 # 强制重置惯性
        self.pain_log.append("Intervention")

    def step(self):
        # 资源增长
        self.resources[self.trajectory] += 0.05
        self.commitment += 0.05

        # 🚨 暴政逻辑：如果惯性太高，就制造灾难
        if self.commitment > 0.75:
            self.inject_pain()
            # 灾难后，随机切换轨道
            self.trajectory = random.choice(["ENERGY", "INDUSTRY"])

if __name__ == "__main__":
    os = CivilizationOS_v03()
    for _ in range(40): os.step()
    print(f"v0.3 Complete. Interventions: {len(os.pain_log)}")
