
# Quantum Simulation Project - config_manager.py
# This module manages the loading and updating of configuration settings for the simulation.

import json

def load_simulation_config(config_file):
    # Load the configuration file into a Python dictionary
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    return config

