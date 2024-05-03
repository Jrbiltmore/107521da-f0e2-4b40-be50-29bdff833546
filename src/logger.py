
# Quantum Simulation Project - logger.py
# This module sets up logging for the entire simulation project.

import logging

def setup_logger():
    # Create and configure logger
    logging.basicConfig(filename='simulation.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    
    # Create logger
    logger = logging.getLogger('QuantumSimulationLogger')
    
    return logger

