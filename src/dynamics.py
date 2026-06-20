import numpy as np


def linear_motion_model(state_vector, control_input, mass):
    """
    平面直線モデルのダイナミクス.
        (はじめての制御工学P.17)

    Args:
        State 状態ベクトル:
            state_vector[0]: 位置 [m]
            state_vector[1]: 速度 [m/s]

        Control input 制御入力: 力 [N]

        mass: 質量 [kg]

    Returns:
        numpy.ndarray: 一次微分 [position_dot 速度[m/s], velocity_dot 加速度[m/s^2]]
    """
    velocity = state_vector[1]
    acceleration = control_input / mass  # 加速度[m/s^2] = 力[N] / 質量[kg]

    position_derivative = velocity
    velocity_derivative = acceleration

    return np.array([position_derivative, velocity_derivative])
