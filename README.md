# Schelling Model Simulation

This Python script implements the Schelling segregation model, a classic agent-based model that simulates residential segregation based on agent preferences. The model features agents of two types (red and blue) moving to empty cells if dissatisfied with their neighbors, with options for different movement strategies and update orders.

## Overview

The `SchellingModel` class simulates:
- **Agents**: Red ('R') and blue ('B') agents, with a specified happiness threshold (`H`).
- **Movement**: Agents move to empty cells based on 'random' or 'horizontal' strategies.
- **Update Order**: Sequential or random updates of agents.
- **Convergence**: The simulation stops when no agent needs to move or reaches a maximum iteration limit.
- **Visualization**: Plots the final grid state with color-coded agents and empty cells.

The script runs multiple combinations of movement types and update orders, with optional exploration of varying happiness thresholds.

## Requirements

- Python 3.x
- Libraries:
  - `numpy` (for array operations)
  - `random` (for shuffling and choices)
  - `matplotlib` (for plotting)
  - `matplotlib.colors` (for custom colormaps)

Install the required libraries using pip:
```bash
pip install numpy matplotlib
```

## Usage

1. Save the script as `schelling_model.py`.
2. Adjust global parameters (e.g., `H`, `num_runs`, `move_types`, `update_orders`) or class initialization parameters as needed.
3. Run the script:
   ```bash
   python schelling_model.py
   ```
4. The script will execute multiple simulation runs and save plots for each case.



## Simulation Cases

### Case 1
- Runs `num_runs` (3) simulations for each combination of:
  - `move_type`: 'random', 'horizontal'.
  - `update_order`: 'sequential', 'random'.
  - Fixed `H = 4`.
- Total of 12 plots (3 runs × 2 move types × 2 update orders).

### CAse 2 (Commented)
- Varies `H` from 0 to 7 (commented code).
- Uses `move_type = 'random'` and `update_order = 'random'`.
- Runs 3 simulations per `H` value (commented out).
