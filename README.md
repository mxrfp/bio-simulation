# Ecosystem Simulation

A basic 2D terminal-based simulation written in Python that models simple predator-prey behaviors. 

Entities on the grid calculate Euclidean distances to nearest threats and food sources to determine their movement. The update loop is buffered, meaning all entity intentions are calculated before any state changes are applied. This prevents movement-order bias during a single tick.

## Requirements
* Python 3.10+ (Uses the `|` operator for union type hinting)
* No external dependencies

## Usage

Clone the repository and run the main script:

```bash
python main.py
