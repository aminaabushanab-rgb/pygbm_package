# pygbm — Geometric Brownian Motion Simulator

A Python package for simulating Geometric Brownian Motion (GBM), a stochastic process that evolves multiplicatively and is commonly used to model stock prices and diffusion-driven systems.

Developed as part of the Research Computing / Data-Intensive Science coursework at the University of Cambridge.

## Overview

The Geometric Brownian Motion follows the stochastic differential equation (SDE):

dY(t) = μY(t)dt + σY(t)dB(t)

where:
- B(t) is a Brownian motion (Wiener process)
- μ is the drift (expected rate of return)
- σ is the diffusion coefficient (volatility)

The analytical solution is given by:

Y(t) = Y₀ * exp[(μ - σ²/2)t + σB(t)]

## Features

- Simulate GBM trajectories using:
  - Analytical solution
  - Euler–Maruyama numerical method
  - Milstein numerical method
- Visualize and export simulated paths
- Command-line interface (CLI) for easy control of parameters and methods
- Reproducible simulations using a random seed
- Modular, object-oriented design

## Installation

Clone the repository and install it in editable mode:

git clone https://github.com/aminaabushanab-rgb/pygbm_package.git
cd pygbm_package
python -m venv .venv
source .venv/bin/activate
pip install -e .

This will install pygbm along with its dependencies (numpy, matplotlib, etc).

## Usage

### From the Command Line

Once installed, the package can be run directly using:

pygbm --y0 1.0 --mu 0.05 --sigma 0.2 --T 1.0 --N 100 --method exact --output gbm_plot.png

### Available Methods

- `exact` — closed-form analytical solution
- `euler` — Euler–Maruyama numerical approximation
- `milstein` — Milstein numerical approximation

Example:

pygbm --y0 1.0 --mu 0.05 --sigma 0.2 --T 1.0 --N 100 --method euler --output gbm_euler.png

To ensure reproducibility, a seed can be specified:

pygbm --y0 1.0 --mu 0.05 --sigma 0.2 --T 1.0 --N 100 --method milstein --seed 42 --output gbm_milstein.png

This will simulate a GBM trajectory using the Milstein method and save the plot as gbm_milstein.png.

### From Python

from pygbm.gbm_simulation import GBMSimulator

# Parameters
y0 = 1.0
mu = 0.05
sigma = 0.2
T = 1.0
N = 100

simulator = GBMSimulator(y0, mu, sigma)
t, y = simulator.simulate_path(T, N, method="milstein", seed=42)
simulator.plot_path(t, y, output="gbm_plot.png")

## Numerical Methods Overview

1. Euler–Maruyama Method

Y_{t+Δt} = Y_t + μY_tΔt + σY_tΔB_t

Simple first-order approximation. The discretization error scales with sqrt(Δt).

2. Milstein Method

Y_{t+Δt} = Y_t + μY_tΔt + σY_tΔB_t + 0.5σ²Y_t[(ΔB_t)² - Δt]

Higher-order approximation that improves accuracy by adding a correction term.

Both methods can be compared with the analytical solution by running multiple simulations with the same random seed.

## Project Structure

pygbm_package/
│
├── pygbm/
│   ├── __init__.py
│   ├── base_pygbm.py
│   ├── gbm_simulation.py
│   ├── cli.py
│   └── version.py
│
├── tests/
│
├── pyproject.toml
├── README.md
└── .gitignore

## Notes

- The CLI defaults to the analytical method if none is specified
- Numerical solvers can be further extended for custom SDEs
- Tested with Python 3.9 and higher

## Author

Amina Abu Shanab  
MPhil in Data-Intensive Science — University of Cambridge  
GitHub: https://github.com/aminaabushanab-rgb

## License

This project is licensed under the MIT License. See the LICENSE file for details.
