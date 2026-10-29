
# Axial Compressor CFD Study

### Python-Based Computational Fluid Dynamics for Axial Compressor Aerodynamics

![Status](https://img.shields.io/badge/Project-In%20Development-orange)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Field](https://img.shields.io/badge/Field-Turbomachinery-00599C)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This project aims to develop a Python-based computational fluid
dynamics (CFD) framework for studying the aerodynamics of axial
compressors.

The long-term objective is to investigate flow behaviour through
compressor blade passages, understand aerodynamic loss mechanisms,
and establish a foundation for future research into compressor
performance and flow instability.

The project will progress from fundamental CFD validation cases
towards blade-resolved axial compressor simulations.

**Current scope:** Numerical-method development, flow visualisation,
geometry preparation, and verification of simplified CFD models.

**Important:** A validated, blade-resolved compressor solver is a
future development goal, not a current project capability.

---

## Research Objectives

- Develop a structured and reproducible Python CFD workflow.
- Understand the governing equations of fluid flow.
- Investigate velocity and pressure distributions in internal flows.
- Prepare and analyse axial compressor blade geometries.
- Develop numerical methods suitable for turbomachinery applications.
- Validate numerical results against analytical solutions and
  published experimental benchmarks.
- Establish a foundation for investigating compressor losses,
  tip-leakage flows, and stall inception.

---

## Planned Development

| Stage | Development | Status |
|---|---|---|
| 1 | Python environment and project structure | In progress |
| 2 | Analytical channel-flow benchmark | In progress |
| 3 | Numerical verification and grid refinement | Planned |
| 4 | Compressor blade geometry preparation | Planned |
| 5 | Blade-passage mesh generation | Planned |
| 6 | Compressible-flow solver | Planned |
| 7 | Rotating-frame modelling | Planned |
| 8 | Compressor performance validation | Planned |
| 9 | Stall and loss-mechanism investigation | Future work |

---

## Physical Models

The project is intended to progress towards solving the
compressible Navier–Stokes equations.

### Conservation of Mass

For compressible flow:

\[
\frac{\partial \rho}{\partial t}
+\nabla\cdot(\rho\mathbf{u})=0
\]

### Conservation of Momentum

\[
\frac{\partial(\rho\mathbf{u})}{\partial t}
+\nabla\cdot(\rho\mathbf{u}\otimes\mathbf{u})
=-\nabla p+\nabla\cdot\boldsymbol{\tau}
\]

### Conservation of Energy

The energy equation will be incorporated in the compressible-flow
stage to account for temperature changes, energy transport,
and viscous effects.

The exact numerical formulation, boundary conditions, and turbulence
model will be documented as the solver develops.

---

## Technology Stack

- **Python** — primary programming language
- **NumPy** — numerical calculations and array operations
- **Matplotlib** — scientific plotting and flow visualisation
- **SciPy** — planned numerical solvers and post-processing
- **Git and GitHub** — version control and reproducible development

---

## Repository Structure

```text
axial-compressor-cfd/
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── geometry/
│   └── README.md
├── results/
│   └── .gitkeep
├── tests/
│   └── README.md
└── docs/
    └── methodology.md
```

The repository structure will evolve as the numerical solver,
geometry tools, and validation procedures are implemented.

---

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd axial-compressor-cfd
```

Replace `<YOUR_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the current example

```bash
python main.py
```

Run only the scripts that have been implemented and tested in the
current repository version.

---

## Validation Strategy

Numerical results will be assessed through:

1. Comparison with analytical solutions.
2. Grid-refinement and mesh-independence studies.
3. Monitoring of residuals and conservation errors.
4. Comparison against published compressor or cascade benchmarks.
5. Documentation of modelling assumptions and numerical uncertainty.

A visually plausible flow field will not, by itself, be considered
evidence that a simulation is accurate.

---

## Future Research Directions

Potential research extensions include:

- Aerodynamic loss mechanisms in axial compressor blade passages.
- Effects of blade geometry and operating conditions on flow turning.
- Tip-leakage vortices and secondary-flow structures.
- Compressor stability and stall inception.
- Physics-informed machine learning for flow analysis.
- Automated aerodynamic design and optimisation.

These are research directions under consideration rather than
capabilities already implemented in the repository.

---

## References and Learning Resources

- [NASA Technical Reports Server](https://ntrs.nasa.gov/)
- [CFD Python: The 12 Steps to Navier–Stokes](https://doi.org/10.21105/jose.00021)
- [OpenFOAM Documentation](https://doc.openfoam.com/)
- [SU2 Documentation](https://su2code.github.io/)

---

## Contributing

Suggestions, bug reports, numerical verification cases, and
improvements to the documentation are welcome.

When contributing numerical methods, please document the governing
equations, boundary conditions, assumptions, and validation tests.

---

## Author

**Research Area:** Turbomachinery and Computational Fluid Dynamics

**Project:** Axial Compressor CFD Study

---

*This repository is an evolving educational and research project.
Numerical models and their capabilities will be documented as they
are implemented and validated.*
