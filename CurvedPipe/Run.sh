#!/bin/sh
#BSUB -J test		# job name
#BSUB -q hpc          	# cluster
#BSUB -B                # send notification at start 
#BSUB -N                # send notification at completion
#BSUB -u s204389@student.dtu.dk         # mail address
#BSUB -W 01:00       	# maximum simulation time    
#BSUB -n 20           	# total number of workers
#BSUB -R "span[ptile=20]"	# reserve N cores on each machine
#BSUB -R "rusage[mem=1GB]"   	# memory per core
#BSUB -o Output_%J.out          #
#BSUB -e Error_%J.err           #

# Set license key
export LM_PROJECT=xNBF+vG3YRiHlJypo92dnQ

# Define executable 
export EXE=/appl/star-ccm/18.06.007-R8/STAR-CCM+18.06.007-R8/star/bin/starccm+

# Define input file 
export FILE=Aircraft.sim

# Run ! 
$EXE -np ${LSB_DJOB_NUMPROC} -bs lsf -mpi intel -rsh blaunch -batchsystem lsf -power -podkey $LM_PROJECT -batch $FILE 2>&1 > log.run