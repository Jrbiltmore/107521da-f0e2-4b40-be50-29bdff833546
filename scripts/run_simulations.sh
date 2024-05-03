#!/bin/bash

# Define simulation parameters
NUM_SIMULATIONS=10
SIMULATION_DURATION=100
OUTPUT_DIR="sim_results"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through simulations
for ((i=1; i<=$NUM_SIMULATIONS; i++)); do
    # Generate unique simulation ID
    SIM_ID="sim_$i"

    # Run simulation with specified duration
    echo "Running simulation $SIM_ID..."
    python simulate.py --id "$SIM_ID" --duration "$SIMULATION_DURATION" --output "$OUTPUT_DIR"

    # Check if simulation was successful
    if [ $? -eq 0 ]; then
        echo "Simulation $SIM_ID completed successfully."
    else
        echo "Error: Simulation $SIM_ID encountered an error."
    fi
done

echo "All simulations completed."
