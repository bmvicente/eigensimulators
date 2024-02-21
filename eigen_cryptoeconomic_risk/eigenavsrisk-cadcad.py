
# Monte Carlo runs

from cadCAD.configuration import Configuration
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
import pandas as pd
import numpy as np

# System State
initial_state = {
    'total_restaked': 10000  # Initial total amount restaked
}

# Policy Function
def slashing_policy(params, substep, state_history, previous_state):
    risk_score = np.random.randint(0, 101)  # Random risk score between 0 and 100
    risk_factor = risk_score + 10
    slashing_amount = (previous_state['total_restaked'] / 3) * (risk_factor / 100)
    return {'slashing_amount': slashing_amount}

# Update Function
def update_total_restaked(params, substep, state_history, previous_state, policy_input):
    new_total_restaked = previous_state['total_restaked'] - policy_input['slashing_amount']
    return 'total_restaked', max(new_total_restaked, 0)  # Ensure total doesn't go negative

# Partial State Update Block
partial_state_update_block = [
    {
        'policies': {
            'slashing_policy': slashing_policy
        },
        'variables': {
            'total_restaked': update_total_restaked
        }
    }
]


# System Configuration
sim_config = {
    'N': 1,  # Number of Monte Carlo runs
    'T': range(10),  # Number of time steps
    'M': {},  # System parameters (none in this simple example)
    'user_id': 'user_a',  # Default user_id
    'subset_id': 0,  # Default subset_id
    'subset_window': None  # Default subset_window
}

# Create Configuration
config = Configuration(initial_state=initial_state,
                       partial_state_update_blocks=partial_state_update_block,
                       sim_config=sim_config)

# Execute Simulation
exec_mode = ExecutionMode()
exec_context = ExecutionContext(exec_mode.single_proc)
executor = Executor(exec_context, [config])  # Pass the configuration object inside a list
results = executor.execute()  # Execute the simulation

# Process Results
df = pd.DataFrame(results[0])
print(df[['total_restaked']])
