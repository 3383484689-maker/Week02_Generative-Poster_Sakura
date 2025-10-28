# Generative Sakura Poster
# Concepts: randomness, lists, loops, functions, matplotlib

import random
import math
import numpy as np
import matplotlib.pyplot as plt

def sakura_palette(k=6):
    """
    Return k shades of pink/sakura colors
    """
    base_colors = [
        (1.0, 0.9, 0.95),
        (1.0, 0.8, 0.9),
        (1.0, 0.7, 0.85),
        (1.0, 0.6, 0.8),
        (0.95, 0.75, 0.85),
        (0.98, 0.85, 0.9)
    ]
    if k < len(base_colors):
        return random.sample(base_colors, k)
    else:
        return base_colors

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.30):
    """
    Generate a wobbly closed shape
    """
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

def generate_sakura_poster(seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    else:
        random.seed()
        np.random.seed()

    plt.figure(figsize=(7,10))
    plt.axis('off')
    plt.gca().set_facecolor((0.98,0.97,0.96))

    palette = sakura_palette(6)
    n_layers = 12
    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.20)
        x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05,0.25))
        color = random.choice(palette)
        alpha = random.uniform(0.4, 0.9)
        plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

    plt.text(0.05, 0.95, "Generative Sakura Poster", fontsize=18, weight='bold', transform=plt.gca().transAxes)
    plt.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=plt.gca().transAxes)

    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.show()
