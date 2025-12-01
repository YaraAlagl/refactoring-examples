"""Simple tree generator (clean + easy to understand)

This version keeps the idea but removes:
- argparse
- type hints
- randomness
- extra structure

Just one function to generate and one to draw.
Run normally:
    python simple_tree.py
Saves: tree.png
"""

from math import sin, cos
from matplotlib import pyplot as plt


def generate_tree(iterations, length, angle, shrink):
    """Generate a list of line segments for a simple branching tree."""
    branches = [(0.0, 0.0, 0.0, length)]  # x, y, direction, length
    segments = []

    for _ in range(iterations):
        new_branches = []
        for x, y, direction, L in branches:
            # endpoint of the branch
            x2 = x + L * sin(direction)
            y2 = y + L * cos(direction)
            segments.append(((x, y), (x2, y2)))

            # sub-branches
            new_L = L * shrink
            new_branches.append((x2, y2, direction - angle, new_L))
            new_branches.append((x2, y2, direction + angle, new_L))

        branches = new_branches

    return segments


def plot_tree(segments, save_path="tree.png"):
    plt.figure(figsize=(10, 8))
    for (x0, y0), (x1, y1) in segments:
        plt.plot([x0, x1], [y0, y1])

    
    plt.title("Group 4's Tree Plot")
    plt.axis("on")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.xlim(-0.5, 0.5)   
    plt.ylim(0, 2.5)    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


def main():
    iterations=5
    length=1.0
    angle=0.1
    shrink=0.6

    segments = generate_tree(iterations, length, angle, shrink)
    plot_tree(segments)
    print("Saved tree.png")


if __name__ == "__main__":
    main()
