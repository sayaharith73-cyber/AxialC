"""
Axial compressor CFD setup tool.

This script:
1. Loads user configuration.
2. Reads blade surface coordinates.
3. Checks basic geometry validity.
4. Plots the blade and neighbouring periodic copies.

It does NOT solve the Navier-Stokes equations.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from config import CompressorConfig, validate_config


def load_blade_geometry(filename):
    """Read blade surface coordinates from a CSV file."""

    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(
            f"Cannot find {filename}. "
            "Place it in the project folder."
        )

    points = np.genfromtxt(
        path,
        delimiter=",",
        names=True,
        dtype=float
    )

    if points.dtype.names is None:
        raise ValueError("CSV must have column headers x,y.")

    if not {"x", "y"}.issubset(points.dtype.names):
        raise ValueError("CSV columns must be named x and y.")

    x = np.atleast_1d(points["x"])
    y = np.atleast_1d(points["y"])

    coordinates = np.column_stack((x, y))

    if len(coordinates) < 5:
        raise ValueError(
            "Enter at least five blade boundary points."
        )

    if not np.all(np.isfinite(coordinates)):
        raise ValueError("Geometry contains invalid numbers.")

    # Remove consecutive duplicate points
    differences = np.diff(coordinates, axis=0)
    keep = np.r_[
        True,
        np.linalg.norm(differences, axis=1) > 1e-12
    ]
    coordinates = coordinates[keep]

    if len(coordinates) < 5:
        raise ValueError("Too few distinct geometry points.")

    # Check whether the profile is closed
    closure_error = np.linalg.norm(
        coordinates[0] - coordinates[-1]
    )

    if closure_error > 1e-6:
        raise ValueError(
            "Blade profile is not closed. "
            "Make the last point match the first point."
        )

    return coordinates


def check_geometry(coordinates, cfg):
    """Perform basic geometry checks."""

    x = coordinates[:, 0]
    y = coordinates[:, 1]

    chord_x = np.max(x) - np.min(x)
    thickness_y = np.max(y) - np.min(y)

    if chord_x <= 0 or thickness_y <= 0:
        raise ValueError("Blade geometry has zero dimensions.")

    if not np.isclose(
        chord_x, cfg.chord, rtol=0.05, atol=1e-9
    ):
        print(
            "WARNING: Profile axial-coordinate extent "
            f"is {chord_x:.5f} m, while configured chord "
            f"is {cfg.chord:.5f} m."
        )

    # This checks bounding-box thickness only.
    # It does not establish that the profile is valid.
    if thickness_y >= cfg.pitch:
        print(
            "WARNING: Blade bounding-box thickness is "
            "greater than or equal to the pitch. "
            "Check the geometry and stagger."
        )

    print(f"Number of blade points: {len(coordinates)}")
    print(f"Coordinate x extent: {chord_x:.5f} m")
    print(f"Coordinate y extent: {thickness_y:.5f} m")


def plot_blade_passage(coordinates, cfg):
    """Plot one blade and two periodic copies."""

    fig, ax = plt.subplots(figsize=(11, 5))

    # Periodic copies translated by the pitch.
    # This is a visual check, not a mesh.
    for offset in (-cfg.pitch, 0.0, cfg.pitch):
        ax.plot(
            coordinates[:, 0],
            coordinates[:, 1] + offset,
            linewidth=2,
            label=f"Offset {offset:.3f} m"
        )

    ax.set_title("Axial compressor: blade geometry check")
    ax.set_xlabel("Axial coordinate x [m]")
    ax.set_ylabel("Pitchwise coordinate y [m]")

    ax.set_aspect("equal", adjustable="datalim")
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "blade_geometry.png"
    fig.savefig(output_file, dpi=200)
    print(f"Geometry plot saved to: {output_file}")

    plt.show()


def main():
    # Step 1: Load configuration
    cfg = CompressorConfig()
    validate_config(cfg)

    # Step 2: Load the geometry
    coordinates = load_blade_geometry(cfg.blade_file)

    # Step 3: Check geometry dimensions
    check_geometry(coordinates, cfg)

    # Step 4: Visualise the blade passage
    plot_blade_passage(coordinates, cfg)

    print("\nSetup completed.")
    print(
        "Next step: generate a suitable mesh and configure "
        "a validated compressible-flow solver."
    )


if __name__ == "__main__":
    main()
