#!/bin/bash
#SBATCH -A naiss2025-22-1066     
#SBATCH -p shared                
#SBATCH -t 72:00:00              
#SBATCH -n 1                     
#SBATCH --cpus-per-task=16       
#SBATCH --mem=64G                
#SBATCH --job-name=ampliseq_CB   

# Navigate to the correct directory for context
cd /cfs/klemming/projects/supr/naiss2025-22-1652/master_thesis_16S/

# Load environment within the job
module load PDC           
module load java/17.0.4   
module load singularity   

# Run the nf-core/ampliseq pipeline
# OBS! Vi använder -profile singularity, INTE pdc_kth,
# för att undvika inbyggda konflikter.
/cfs/klemming/projects/supr/naiss2025-22-1652/master_thesis_16S/nextflow run nf-core/ampliseq \
    -c custom_dardel.config \
    -profile singularity \
    --input SamplesheetDardel.csv \
    --FW_primer "CCTAYGGGRBGCASCAG" \
    --RV_primer "GGACTACNNGGGTATCTAAT" \
    --outdir results/ \
    -r 2.15.0 \
    -resume
