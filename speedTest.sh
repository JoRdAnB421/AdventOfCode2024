#!/bin/bash

# Name of the Python script to execute
day="$1"
chat="$2"
SCRIPT=$day$2".py"

echo "Runing speed test for $SCRIPT"

# Number of times to run the script
RUNS=10

# Initialize total time
total_time=0

# Loop to run the script multiple times
for i in $(seq 1 $RUNS)
do
    # Run the script and capture the real time in seconds
    real_time=$( (time python $SCRIPT) 2>&1 | grep real | awk '{print $2}' )
    
    # Convert time format (e.g., 0m1.234s to seconds as a float)
    minutes=$(echo $real_time | awk -Fm '{print $1}')
    seconds=$(echo $real_time | awk -Fm '{print $2}' | sed 's/s//')
    real_seconds=$(awk "BEGIN {print ($minutes * 60) + $seconds}")
    
    # Add to total time
    total_time=$(awk "BEGIN {print $total_time + $real_seconds}")
done

# Calculate average time
average_time=$(awk "BEGIN {print $total_time / $RUNS}")

# Output the average time
echo "Average wall-clock time over $RUNS runs: $average_time seconds"