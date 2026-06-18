import numpy as np


def linear_motion_model(state_vector, control_input):
    """
    Compute the time derivative of a 1D acceleration-input model.

    State:
        state_vector[0]: position [m]
        state_vector[1]: velocity [m/s]

    Control input:
        control_input_vector[0]: acceleration [m/s^2]

    Returns:
        numpy.ndarray: time derivative [position_dot, velocity_dot]
    """
    velocity = state_vector[1]
    acceleration = control_input

    position_derivative = velocity
    velocity_derivative = acceleration

    return np.array([position_derivative, velocity_derivative])
