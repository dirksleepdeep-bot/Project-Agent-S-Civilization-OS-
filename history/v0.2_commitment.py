import random

class CivilizationOS_v02:
    def __init__(self):
        self.state = {"ENERGY": 0.6, "KNOWLEDGE": 0.5, "INDUSTRY": 0.5}
        # 新增：轨迹与承诺 (惯性)
        self.trajectory = None 
        self.commitment = 0.0 
        self.history = []

    def step(self):
        # 1. 选择路径 (惯性越大，越难改)
        paths = ["ENERGY", "KNOWLEDGE", "INDUSTRY"]
        if self.trajectory is None:
            self.trajectory = random.choice(paths)
        else:
            # 只有极小概率能改弦更张
            if random.random() < (0.1 * (1 - self.commitment)):
                self.trajectory = random.choice(paths)

        # 2. 增加惯性 (路走得越久，越不可逆)
        self.commitment = min(1.0, self.commitment + 0.05)

        # 3. 执行 (强化当前路径，削弱其他)
        target = self.trajectory
        self.state[target] += 0.05
        for p in paths:
            if p != target: self.state[p] -= 0.01 # 偏科代价

        # 4. 熵增
        for p in paths: self.state[p] = max(0, self.state[p] - 0.01)

        self.history.append((self.trajectory, round(self.commitment, 2)))

if __name__ == "__main__":
    os = CivilizationOS_v02()
    for _ in range(50): os.step()
    print("v0.2 Simulation Complete.")
