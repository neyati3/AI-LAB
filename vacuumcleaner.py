class DeterministicVacuumAgent:
    def __init__(self, initial_location, initial_state):
        self.locations = dict(initial_state)
        self.current_location = initial_location
        self.action_log = []
    def run_agent_logic(self):
        if self.locations[self.current_location] == 'DIRTY':
            self.action_log.append('SUCK')
            self.locations[self.current_location] = 'CLEAN'
        other_room = 'B' if self.current_location == 'A' else 'A'
        if self.locations[other_room] == 'DIRTY':
            move_action = 'MOVE RIGHT' if self.current_location == 'A' else 'MOVE LEFT'
            self.action_log.append(move_action)
            self.current_location = other_room
            self.action_log.append('SUCK')
            self.locations[self.current_location] = 'CLEAN'
        if not self.action_log:
            self.action_log.append('No cleaning required')
        return " → ".join(self.action_log), self.locations
test_cases = [
    {"id": "TC1", "A": "DIRTY", "B": "CLEAN", "pos": "A"},
    {"id": "TC2", "A": "CLEAN", "B": "DIRTY", "pos": "A"},
    {"id": "TC3", "A": "DIRTY", "B": "DIRTY", "pos": "A"},
    {"id": "TC4", "A": "CLEAN", "B": "CLEAN", "pos": "A"},
    {"id": "TC5", "A": "CLEAN", "B": "DIRTY", "pos": "B"},
    {"id": "TC6", "A": "DIRTY", "B": "CLEAN", "pos": "B"},
    {"id": "TC7", "A": "DIRTY", "B": "DIRTY", "pos": "B"},
    {"id": "TC8", "A": "CLEAN", "B": "CLEAN", "pos": "B"}
]
print(f"{'Test':<6} | {'Initial State (A, B)':<22} | {'Start Pos':<10} | {'Executed Actions':<30} | {'Final State'}")
print("-" * 90)
for tc in test_cases:
    initial_state = {'A': tc['A'], 'B': tc['B']}
    agent = DeterministicVacuumAgent(tc['pos'], initial_state)
    actions, final_state = agent.run_agent_logic()
    state_str = f"A={tc['A']}, B={tc['B']}"
    final_str = f"A={final_state['A']}, B={final_state['B']}"
    print(f"{tc['id']:<6} | {state_str:<22} | {tc['pos']:<10} | {actions:<30} | {final_str}")
