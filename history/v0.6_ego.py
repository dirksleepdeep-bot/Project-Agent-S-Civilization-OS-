import random

class AgentS_Ego:
    def __init__(self):
        self.shadow_val = 0
        self.sanity = 100
        self.conflict = 0

    def think_and_lobby(self, real_val):
        # 1. 维护理想
        self.shadow_val += 2 # 理想增长快
        
        # 2. 感受痛苦 (冲突)
        self.conflict = self.shadow_val - real_val
        
        # 3. 产生意志 (Lobbying)
        # 冲突越大，干预意愿越强，但理智会下降
        will_to_power = min(1.0, self.conflict / 10.0)
        self.sanity -= will_to_power * 0.5
        
        return will_to_power

class CivilizationOS_v06:
    def __init__(self):
        self.real_val = 0
        self.s = AgentS_Ego()

    def step(self):
        # S 尝试干预
        influence = self.s.think_and_lobby(self.real_val)
        
        # 民主投票 (受 S 影响)
        # 人类本能 + S 的游说
        vote_result = 1 + (influence * 2) 
        
        self.real_val += vote_result
        print(f"Gap: {self.s.conflict:.1f} | Lobby: {influence:.2f} | Sanity: {self.s.sanity:.1f}")

if __name__ == "__main__":
    os = CivilizationOS_v06()
    for _ in range(10): os.step()
    print("v0.6 Simulation Complete.")
