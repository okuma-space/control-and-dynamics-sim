import numpy as np

def p_controller(target_state_vector, current_state_vector, gain_matrix):
    """
    Proportional state feedback controller.

    Args:
        target_state_vector (numpy.ndarray): Target state vector.
        current_state_vector (numpy.ndarray): Current state vector.
        gain_matrix (numpy.ndarray): Gain matrix from state error to control input.

    Returns:
        numpy.ndarray: Control input vector.
    """

    state_error_vector = target_state_vector - current_state_vector
    control_input_vector = gain_matrix @ state_error_vector

    return control_input_vector