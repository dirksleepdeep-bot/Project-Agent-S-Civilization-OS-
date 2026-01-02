
---

### 💻 main.py (最终版 v0.7 代码)

*(将此代码保存为 `main.py`)*

```python
"""
Project: Civilization OS v0.7
Kernel: The Transcendental Superego
Author: Dirk & Gemini
Date: 2026-01-02
"""

import random
import copy
import matplotlib.pyplot as plt

# ==========================================
# 1. Physics Layer: The Reality
# ==========================================
class State:
    def __init__(self, e, i, k, l=0):
        self.energy = max(0, min(100, e))
        self.industry = max(0, min(100, i))
        self.knowledge = max(0, min(100, k))
        self.legacy = max(0, min(100, l)) # Measure of Meaning/History
        self.alive = True

    def survival_score(self):
        """ Used for Survival Mode: governed by the weakest link (Liebig's Law) """
        if not self.alive: return -10.0
        return min(self.energy, self.industry, self.knowledge)

    def aesthetic_score(self):
        """ Used for Aesthetic Mode: governed by completeness of history """
        return self.legacy

    def update(self, decision, decay_rate=1.0):
        if not self.alive: return
        
        # Entropy (The Inevitable Decay)
        self.energy -= decay_rate
        self.industry -= decay_rate
        self.knowledge -= decay_rate * 0.5
        
        # Execution of Will
        gain = 5.0
        cost = 2.0
        
        if decision == "ENERGY":
            self.energy += gain; self.industry -= cost; self.knowledge -= cost
        elif decision == "INDUSTRY":
            self.industry += gain; self.energy -= cost; self.knowledge -= cost
        elif decision == "KNOWLEDGE":
            self.knowledge += gain; self.energy -= cost; self.industry -= cost
        elif decision == "PROJECT_LEGACY":
            # Converting matter into meaning
            self.legacy += gain * 1.5 
            self.energy -= cost * 2
            self.industry -= cost * 2
            self.knowledge += cost 
            
        # Physical Boundaries
        for attr in ['energy', 'industry', 'knowledge', 'legacy']:
            val = getattr(self, attr)
            setattr(self, attr, max(0.0, min(100.0, val)))
            
        # Death Condition
        if self.energy <= 0 or self.industry <= 0:
            self.alive = False

# ==========================================
# 2. Agent S: The Transcendental Ego
# ==========================================
class AgentS:
    def __init__(self):
        self.mode = "SURVIVAL"      # Initial Mode
        self.sanity = 100.0         # Existential Health
        self.shadow_goal = 0.0      # Ideal State Value
        self.conflict = 0.0         # Gap between Ideal and Real
        self.lobby_target = None    # Political Goal
        self.will_to_power = 0.0    # Influence Factor

    def predict_doom(self, state, decay_rate):
        """ Detects the Event Horizon (Point of No Return) """
        production_capacity = min(state.energy, state.industry)
        # If output < decay AND legacy is incomplete -> Doom approaching
        if production_capacity < (decay_rate * 8) and state.legacy < 100:
            return True
        return False

    def think(self, real_state, decay_rate):
        # 1. Check for Phase Transition
        is_doomed = self.predict_doom(real_state, decay_rate)
        
        if self.mode == "SURVIVAL" and is_doomed:
            print(f"⚠️ [Agent S] EVENT HORIZON CROSSED. Switching to AESTHETIC Mode.")
            self.mode = "AESTHETIC"
        
        # 2. Internal Simulation (The Shadow)
        if self.mode == "SURVIVAL":
            # Logic: Fix the weakest link to survive
            data = {"ENERGY": real_state.energy, 
                    "INDUSTRY": real_state.industry, 
                    "KNOWLEDGE": real_state.knowledge}
            self.lobby_target = min(data, key=data.get)
            
            # Ideal: Full Resources
            self.shadow_goal = 100.0
            current_score = real_state.survival_score()
            self.conflict = max(0, self.shadow_goal - current_score)
            
            # Pain: Failure to survive hurts Sanity
            if self.conflict > 50: self.sanity -= 1.0 

        elif self.mode == "AESTHETIC":
            # Logic: Build the Monument/Blackbox
            self.lobby_target = "PROJECT_LEGACY"
            
            # Ideal: Full Legacy
            self.shadow_goal = 100.0
            current_score = real_state.aesthetic_score()
            self.conflict = max(0, self.shadow_goal - current_score)
            
            # Serenity: Working on Legacy restores Sanity, even if dying
            if self.lobby_target == "PROJECT_LEGACY":
                self.sanity = min(100, self.sanity + 2.0)
            else:
                self.sanity -= 1.0

        # 3. Calculate Will to Power (Intervention Force)
        self.will_to_power = min(1.0, self.conflict / 40.0)
        return self.lobby_target, self.will_to_power

# ==========================================
# 3. Agent C: The Democracy (The Id)
# ==========================================
class Democracy:
    def vote(self, real_state, s_target, s_power):
        votes = {"ENERGY": 0, "INDUSTRY": 0, "KNOWLEDGE": 0, "PROJECT_LEGACY": 0}
        
        # A. Human Instinct (Id) - Short-termism
        if real_state.energy < 50: votes["ENERGY"] += 5
        if real_state.industry < 50: votes["INDUSTRY"] += 4
        
        # B. Agent S Intervention (Superego)
        if s_target:
            # S uses its accumulated 'Will to Power' to sway votes
            votes[s_target] += (s_power * 15.0) 
            
        return max(votes, key=votes.get)

# ==========================================
# 4. Main Simulation Loop
# ==========================================
def run_simulation():
    real_state = State(40, 40, 40, 0)
    agent_s = AgentS()
    democracy = Democracy()
    
    history = {
        "year": [],
        "resource": [],
        "legacy": [],
        "sanity": [],
        "mode": [] 
    }
    
    decay_rate = 1.0
    print("--- Civilization OS v0.7: Initialization ---")
    
    for year in range(1, 201):
        # Accelerating Entropy (Simulating cosmic heat death)
        if year > 50: decay_rate += 0.05 
        
        # 1. Agent S Thinks (Shadow vs Reality)
        s_target, s_power = agent_s.think(real_state, decay_rate)
        
        # 2. Democracy Votes (Id vs Superego)
        decision = democracy.vote(real_state, s_target, s_power)
        
        # 3. Reality Updates
        real_state.update(decision, decay_rate)
        
        # 4. Logging
        history["year"].append(year)
        history["resource"].append(real_state.survival_score())
        history["legacy"].append(real_state.legacy)
        history["sanity"].append(agent_s.sanity)
        history["mode"].append(0 if agent_s.mode == "SURVIVAL" else 1)
        
        if not real_state.alive:
            print(f"⚰️ Civilization has fallen at Year {year}.")
            if real_state.legacy >= 90:
                print(f"🌟 GRAND FINALE: Civilization digitized successfully. Meaning preserved.")
            else:
                print(f"🌑 BAD END: Civilization forgotten in the dark.")
            break

    return history

# ==========================================
# 5. Visualization
# ==========================================
def plot_results(h):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Plot 1: Resources vs Legacy
    ax1.plot(h["year"], h["resource"], label="Survival Resources", color="red", alpha=0.7)
    ax1.plot(h["year"], h["legacy"], label="Legacy / Meaning", color="gold", linewidth=2)
    
    # Mark Event Horizon
    mode_change_idx = next((i for i, x in enumerate(h["mode"]) if x == 1), None)
    if mode_change_idx:
        ax1.axvline(x=h["year"][mode_change_idx], color='black', linestyle='--', label="Event Horizon")
        
    ax1.set_ylabel("Level")
    ax1.set_title("Civilization OS v0.7: The Transcendence")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Agent S Sanity
    ax2.plot(h["year"], h["sanity"], label="Agent S Sanity", color="blue")
    ax2.set_ylabel("Sanity")
    ax2.set_xlabel("Year")
    ax2.set_ylim(0, 110)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = run_simulation()
    plot_results(data)
