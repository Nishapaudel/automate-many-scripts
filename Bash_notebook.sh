
#continues the loop as long as the value in the variable COUNTER is less than 10 (incremented by 1 on each iteration of the loop).

while, do, and done are keywords

COUNTER=0
while [ ${COUNTER} -lt 10 ]; do
    command 1
    command 2
    COUNTER=`expr ${COUNTER} + 1` 
done

#for loop
#.................................................................................................
#!/bin/bash

# enter directory with raw FASTQs
cd ~/unix_lesson/raw_fastq

# count bad reads for each FASTQ file in our directory
for filename in *.fq
do

  # create a prefix for all output files
  samplename=`basename $filename .subset.fq`

  # tell us what file we're working on
  echo $filename

  # grab all the bad read records
  grep -B1 -A2 NNNNNNNNNN $filename > ~/unix_lesson/badreads/${samplename}_badreads.fq

  # grab the number of bad reads and write it to a summary file
  grep -cH NNNNNNNNNN $filename >> ~/unix_lesson/badreads/badreads.count.summary
done



#............................................................................

