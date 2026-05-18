# SVEA_16S
Bioinformatic pipeline and R-scripts for the analysis of 16S rRNA gene sequences from Baltic Sea bacterioplankton (2021-2022). Developed as part of a Master's Thesis in Molecular Biology.


# Baltic Sea 16S Bacterioplankton Analysis (2021-2022)

This repository contains the bioinformatic workflow and statistical analysis code for my Master's Thesis.

## Project Overview
The study investigates microbial community shifts in the Baltic Sea across spatial and temporal scales using 16S rRNA gene sequencing (V3-V4 region).

## Pipeline Configuration
The primary sequence processing was performed using the **nf-core/ampliseq (v2.15.0)** pipeline on the Dardel HPC cluster (PDC, KTH).

### Core Parameters
| Parameter | Value | Description |
| :--- | :--- | :--- |
| `trunc_qmin` | 25 | Quality threshold for truncation |
| `max_ee` | 2 | Maximum expected errors |
| `min_len` | 50 | Minimum read length |
| `taxonomy` | SILVA 138.2 | Reference database |

## Repository Structure
- `/scripts`: R-scripts for diversity analysis and visualization. Also python script from geographical map with sampling stations. 
- `params.json`: Complete record of Nextflow/nf-core parameters.
- `dardel_job.sh`: SLURM batch script for cluster execution.
