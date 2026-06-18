import numpy as np

import dynamics


def test_linear_motion_model_returns_state_derivative():
    """状態微分が [速度, 加速度] になることを確認する。"""

    state_vector = np.array([0.0, 1.0])  # position [m], velocity [m/s]
    control_input_vector = np.array([0.0])  # acceleration [m/s^2]

    state_derivative = dynamics.linear_motion_model(
        state_vector,
        control_input_vector,
    )

    expected_state_derivative = np.array([1.0, 0.0])

    np.testing.assert_allclose(
        state_derivative,
        expected_state_derivative,
        rtol=1.0e-12,
        atol=1.0e-12,
    )