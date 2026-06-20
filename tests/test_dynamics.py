import numpy as np

from dynamics import linear_motion_model


def euler_step(model, state_vector, control_input, mass, dt):
    derivative = model(
        state_vector=state_vector,
        control_input=control_input,
        mass=mass,
    )

    return state_vector + derivative * dt


def test_linear_motion_reaches_expected_position_after_10_seconds_by_euler():
    """
    質量1kgの物体に1Nの力を10秒間加えたときの到達位置を確認する.

    Model:
        x_dot = v
        v_dot = F / m

    Condition:
        mass = 1.0 kg
        force = 1.0 N
        acceleration = 1.0 m/s^2
        initial position = 0.0 m
        initial velocity = 0.0 m/s
        simulation time = 10.0 s
        dt = 0.01 s

    Explicit Euler:
        x_{k+1} = x_k + v_k dt
        v_{k+1} = v_k + a dt

    Expected:
        velocity = 10.0 m/s
        position = 49.95 m
    """

    mass = 1.0
    force = 1.0

    dt = 0.01
    simulation_time = 10.0
    number_of_steps = int(simulation_time / dt)

    state_vector = np.array([0.0, 0.0])

    for _ in range(number_of_steps):
        state_vector = euler_step(
            model=linear_motion_model,
            state_vector=state_vector,
            control_input=force,
            mass=mass,
            dt=dt,
        )

    expected_position = 49.95
    expected_velocity = 10.0

    np.testing.assert_allclose(
        state_vector[0],
        expected_position,
        rtol=1.0e-12,
        atol=1.0e-12,
    )

    np.testing.assert_allclose(
        state_vector[1],
        expected_velocity,
        rtol=1.0e-12,
        atol=1.0e-12,
    )
