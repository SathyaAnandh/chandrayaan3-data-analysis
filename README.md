# Chandrayaan-3 ILSA Data Analysis

This project analyzes Chandrayaan-3 ILSA (Instrument for Lunar Seismic Activity) datasets obtained from the ISSDC/ISDA portal.

## Project Objectives
- Analyze lunar seismic activity data
- Visualize multi-axis seismic sensor readings
- Study thermal variations in ILSA sensors
- Explore raw Chandrayaan-3 telemetry datasets

## Dataset Information
The dataset contains:
- Time-series seismic sensor readings
- X, Y, and Z axis coarse/fine data
- Temperature measurements
- Raw observational telemetry

## Tools & Libraries Used
- Python
- Pandas
- Matplotlib
- NumPy
- VS Code

## Analysis Performed
- Data loading and inspection
- Metadata interpretation
- Missing value analysis
- Multi-axis seismic visualization
- Signal centering and smoothing
- Temperature variation analysis

## Key Observations
- Coarse seismic channels showed measurable fluctuations.
- Fine sensor channels remained mostly constant.
- Multi-axis seismic activity varied continuously over time.
- Temperature values remained relatively stable during the observation interval.

## Project Structure
```text
data/
scripts/
outputs/
notebooks/