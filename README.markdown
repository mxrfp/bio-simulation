# Ecosystem Simulation

## Table of Contents
1. Introduction
2. Key Features
3. System Requirements
4. Installation Instructions
5. Usage and Configuration
6. Architecture and File Overview
7. Core Mechanics and Algorithms
   - 7.1 Grid and Environment
   - 7.2 Entities and Behaviors
   - 7.3 Main Simulation Loop
8. Known Limitations and Future Work

---

## 1. Introduction
The Ecosystem Simulation is a terminal-based, discrete-time artificial life simulation written in Python. It models a basic predator-prey relationship within a bounded two-dimensional grid. The simulation features autonomous entities (Creatures and Predators) that exhibit goal-oriented behaviors such as food foraging and threat evasion. The environment is rendered dynamically in the console using ANSI escape sequences to provide a clear, color-coded visualization of the ecosystem state.

## 2. Key Features
* **Dynamic Ecosystem:** Models the interactions between distinct entities: Predators, Creatures (Prey), and Food sources.
* **Algorithmic Pathfinding:** Entities compute optimal movement vectors based on the proximity of threats, targets, and boundaries using Euclidean distance calculations.
* **Console-Based Visualization:** Utilizes the `colorama` library to render a high-contrast, real-time representation of the grid directly in standard terminal environments.
* **Parameterized Initialization:** Users can interactively define grid dimensions, entity populations, and frame rates prior to runtime with built-in validation and correction options.
* **Extensible Object-Oriented Design:** Built on a modular architecture that efficiently accommodates the introduction of new entity classes and environmental variables.

## 3. System Requirements
* **Python Version:** Python 3.10 or higher (required for structural pattern matching `match/case` utilized in the initial setup sequence).
* **Standard Python Libraries:** `math`, `time`, `os`, `random`.
* **Third-Party Dependencies:** `colorama` (for terminal color formatting).

## 4. Installation Instructions
1. Clone the repository or download the source code files to a local directory.
2. Ensure Python 3.10+ is installed on your system.
3. Install the required external dependency via pip by running the following command in your terminal:
   ```bash
   pip install colorama
   ```
4. Verify that all primary Python modules (the files corresponding to `grid.py`, `main.py`, `creature.py`, and `food.py`) reside within the same root directory.

## 5. Usage and Configuration
To initiate the simulation, execute the main execution script from the terminal:
```bash
python main.py
```

Upon execution, the program will prompt the user to configure the initial state of the simulation. The following parameters must be entered sequentially:
* `b`: The horizontal width of the grid (number of columns).
* `h`: The vertical height of the grid (number of rows).
* `preds`: The initial population count of Predators.
* `creat`: The initial population count of Creatures.
* `food`: The initial quantity of Food items.
* `fr`: The frame rate or delay between simulation steps.

**Input Correction:** During configuration, typing `back` allows the user to revert to the previous parameter to correct any input errors. Invalid inputs (e.g., entering text instead of numerical digits) are handled safely and will prompt the user to retry.

## 6. Architecture and File Overview

### grid.py (Grid Environment)
Defines the `Grid` class, which serves as the foundational spatial structure. It maintains a 2D matrix representing spatial coordinates, handles object insertion, oversees movement constraints, and computes spatial queries such as identifying empty spaces and determining the nearest entities via distance calculations.

### main.py (Simulation Controller)
Contains the main execution loop and setup logic. It interacts with the `Grid` class to instantiate the environment, spawns entities at random free coordinates via the `random_add` function, and orchestrates the discrete time steps by calling the `update` function. The console screen is cleared and redrawn iteratively.

### creature.py (Entity Definitions)
Contains the `Creature` base class and the `Pred` (Predator) subclass. 
* `Creature`: Implements core attributes like health and hunger metrics. Contains spatial reasoning methods (`get_delta_pos` and `final_coord`) to determine the movement vector based on the coordinates of neighboring entities.
* `Pred`: Overrides specific behaviors and introduces the `eat` method, which scans adjacent orthogonal and diagonal cells to consume neighboring Creatures and replenish health.

### food.py (Static Objects)
Defines the `Food` class. Food objects possess a defined position and a nutritional value. They act as stationary attractants meant to influence the movement logic of the basic Creatures.

## 7. Core Mechanics and Algorithms

### 7.1 Grid and Environment
The simulation area is a discrete Cartesian grid where the top-left coordinate is designated as (0,0). Each cell is strictly limited to holding a maximum of one entity (Predator, Creature, or Food) or remaining empty.
* **Rendering Logic:** The environment is parsed iteratively row by row. Background colors are applied dynamically: empty cells display as cyan, food as light yellow, predators as red, and creatures as white.

### 7.2 Entities and Behaviors
* **Creatures (Prey):** 
  At each time step, Creatures evaluate their surroundings. If both food and predators are absent, they perform a random walk. If a predator is detected, evasion takes precedence; they calculate a vector directly away from the nearest predator. If food is detected without immediate predator threats, they navigate toward the nearest food source.
* **Predators:**
  Predators actively seek out standard Creatures. They compute the distance to all mapped Creatures and set a course for the nearest target. If positioned adjacent to a Creature (within a 1-cell radius covering all 8 directions), the Predator consumes the Creature, permanently removing it from the grid and restoring 10 health points.
* **Movement Constraints:**
  All calculated movement vectors are clamped to unit directions (-1, 0, 1) on both axes. Mathematical boundary checks guarantee that entities cannot maneuver outside the defined spatial limits of the grid.

### 7.3 Main Simulation Loop
The simulation operates on a turn-based architecture synchronized by the main continuous loop:
1. **State Evaluation:** The `update` function parses all grid cells to identify active entities.
2. **Decision Phase:** Every active entity computes its intended next coordinate based on its current proximity to targets and threats.
3. **Execution Phase:** Actions are buffered in a secondary list to prevent sequential update bias (ensuring simultaneous movement logic). Once all decisions are computed, Predators execute their eating mechanics, and surviving entities transition to their new coordinates if the space is viable.
4. **Visualization:** The terminal is cleared (`cls` or `clear`), and the updated state of the grid is printed to standard output.

## 8. Known Limitations and Future Work
* **Energy Mechanics:** The `hunger` attribute for Creatures is initialized but does not currently decrement over time or trigger starvation events. Similarly, the mechanical consumption of food by standard Creatures requires full implementation.
* **Spatial Conflict Resolution:** During the simultaneous movement execution phase, edge cases may arise where multiple entities attempt to transition into the identical final coordinate. Advanced collision handling is slated for a future update.


