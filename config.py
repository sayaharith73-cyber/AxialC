"""
Axial compressor CFD: user configuration.

All geometry inputs are in metres.
Angles are in degrees.
Pressure is in pascals.
Temperature is in kelvin.
Rotational speed is in rpm.
"""

from dataclasses import dataclass


@dataclass
class CompressorConfig:
    # ------------------------------------------
    # 1. Blade geometry
    # ------------------------------------------
    blade_file: str = "blade_geometry.csv"

    chord: float = 0.050       # Blade chord [m]
    pitch: float = 0.030       # Circumferential pitch [m]
    span: float = 0.100        # Blade span [m]
    tip_clearance: float = 0.0005  # Tip gap [m]

    stagger_angle_deg: float = 30.0

    # ------------------------------------------
    # 2. Operating conditions
    # ------------------------------------------
    rotational_speed_rpm: float = 10000.0

    inlet_total_pressure: float = 101325.0  # [Pa]
    inlet_total_temperature: float = 288.0  # [K]

    inlet_absolute_velocity: float = 150.0  # [m/s]
    inlet_flow_angle_deg: float = 0.0

    # ------------------------------------------
    # 3. Working fluid
    # Air approximated as an ideal gas
    # ------------------------------------------
    gas_constant: float = 287.05       # [J/(kg K)]
    specific_heat_cp: float = 1005.0   # [J/(kg K)]
    gamma: float = 1.4
    dynamic_viscosity: float = 1.81e-5  # [Pa s]

    # ------------------------------------------
    # 4. Computational domain
    # ------------------------------------------
    axial_length: float = 0.150  # [m]
    upstream_length: float = 0.050  # [m]
    downstream_length: float = 0.050  # [m]

    # Preliminary mesh resolution
    cells_axial: int = 200
    cells_pitchwise: int = 100

    # ------------------------------------------
    # 5. Numerical controls
    # These are targets, not a guarantee of
    # numerical stability or convergence.
    # ------------------------------------------
    max_iterations: int = 5000
    residual_tolerance: float = 1e-6


def validate_config(cfg: CompressorConfig) -> None:
    """Check that the main user inputs are physically sensible."""

    positive_values = {
        "chord": cfg.chord,
        "pitch": cfg.pitch,
        "span": cfg.span,
        "tip_clearance": cfg.tip_clearance,
        "rotational speed": cfg.rotational_speed_rpm,
        "inlet total pressure": cfg.inlet_total_pressure,
        "inlet total temperature": cfg.inlet_total_temperature,
        "inlet velocity": cfg.inlet_absolute_velocity,
        "gas constant": cfg.gas_constant,
        "specific heat": cfg.specific_heat_cp,
        "dynamic viscosity": cfg.dynamic_viscosity,
        "axial length": cfg.axial_length,
        "upstream length": cfg.upstream_length,
        "downstream length": cfg.downstream_length,
        "axial cell count": cfg.cells_axial,
        "pitchwise cell count": cfg.cells_pitchwise,
        "maximum iterations": cfg.max_iterations,
        "residual tolerance": cfg.residual_tolerance,
    }

    for name, value in positive_values.items():
        if value <= 0:
            raise ValueError(
                f"{name} must be greater than zero; got {value}"
            )

    if not 1.0 < cfg.gamma < 2.0:
        raise ValueError("gamma must be between 1 and 2.")

    if cfg.tip_clearance >= cfg.span:
        raise ValueError(
            "Tip clearance must be smaller than blade span."
        )

    if cfg.pitch <= 0:
        raise ValueError("Blade pitch must be positive.")

    print("Configuration checks passed.")
