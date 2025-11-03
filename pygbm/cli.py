import argparse
from .gbm_simulation import GBMSimulator

def main():
    parser = argparse.ArgumentParser(description="Simulate Geometric Brownian Motion")
    parser.add_argument("--y0", type=float, required=True, help="Initial value Y(0)")
    parser.add_argument("--mu", type=float, required=True, help="Drift coefficient")
    parser.add_argument("--sigma", type=float, required=True, help="Diffusion coefficient")
    parser.add_argument("--T", type=float, required=True, help="Total time for simulation")
    parser.add_argument("--N", type=int, required=True, help="Number of time steps")
    parser.add_argument("--method", choices=["exact", "euler", "milstein"], default="exact",
                        help="Integration scheme (default: exact)")
    parser.add_argument("--output", type=str, default="gbm_plot.png",
                        help="Output file for the plot (PNG).")

    args = parser.parse_args()

    simulator = GBMSimulator(args.y0, args.mu, args.sigma)

    if args.method == "exact":
        t_values, y_values = simulator.simulate_path(args.T, args.N)
    elif args.method == "euler":
        t_values, y_values = simulator.simulate_euler(args.T, args.N)
    else:  # milstein
        t_values, y_values = simulator.simulate_milstein(args.T, args.N)

    simulator.plot_path(t_values, y_values, output=args.output)

