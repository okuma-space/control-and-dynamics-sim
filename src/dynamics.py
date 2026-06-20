import numpy as np


def linear_motion_model(state_vector, control_input, mass, damping_coefficient = 0.0):
    """
    摩擦をともなう物体の直線運動モデルのダイナミクス.
        (はじめての制御工学P.18, P.20)

    Args:
        State 状態ベクトル:
            state_vector[0]: 位置 [m]
            state_vector[1]: 速度 [m/s]

        Control input 制御入力: 力 [N]

        mass: 質量 [kg]
        damping_coefficient: 摩擦係数 [Ns/m]
    Returns:
        numpy.ndarray: 一次微分 [position_dot 速度[m/s], velocity_dot 加速度[m/s^2]]
    """
    velocity = state_vector[1]
    damping_force = damping_coefficient * velocity  # 摩擦力[N] = 摩擦係数[Ns/m] * 速度[m/s]
    acceleration = (control_input - damping_force) / mass  # 加速度[m/s^2] = (力[N] - 摩擦力[N]) / 質量[kg]

    position_derivative = velocity
    velocity_derivative = acceleration

    return np.array([position_derivative, velocity_derivative])

def rigid_body_rotation_model(state_vector, control_input, moment_of_inertia):
    """
    剛体回転モデルのダイナミクス.
        (はじめての制御工学P.18)

    Args:
        State 状態ベクトル:
            state_vector[0]: 角度 [rad]
            state_vector[1]: 角速度 [rad/s]

        Control input 制御入力: トルク [Nm]

        moment_of_inertia: 慣性モーメント [kg*m^2]

    Returns:
        numpy.ndarray: 一次微分 [angle_dot 角速度[rad/s], angular_velocity_dot 角加速度[rad/s^2]]
    """
    angular_velocity = state_vector[1]
    angular_acceleration = (
        control_input / moment_of_inertia
    )  # 角加速度[rad/s^2] = トルク[Nm] / 慣性モーメント[kg*m^2]

    angle_derivative = angular_velocity
    angular_velocity_derivative = angular_acceleration

    return np.array([angle_derivative, angular_velocity_derivative])

