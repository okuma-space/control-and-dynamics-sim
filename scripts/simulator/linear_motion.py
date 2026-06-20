import dynamics
import simulation_history
import numpy as np
import visualizer.linear_motion as visualize
import visualizer.linear_motion_animation as animation_visualize


def propagate(
    current_state,
    target_state,
    p_gain,
    i_gain,
    d_gain,
    mass,
    simulate_time,
    resolution_sec,
    simulation_history,
):
    """
    Propagate 1D linear motion with PID control.
    """

    current_time = simulation_history.time[-1]
    integral_error = simulation_history.error.integral[-1]
    pid_control_input = simulation_history.control_input.pid[-1]

    # 伝搬ループ
    while current_time < simulate_time:
        # ダイナミクス計算
        state_derivative = dynamics.linear_motion_model(
            current_state,
            pid_control_input,
            mass,
        )

        # 状態更新
        current_time += resolution_sec
        current_state = current_state + state_derivative * resolution_sec

        # 偏差更新
        # --------------------------------------------------------------
        # 偏差計算
        error = target_state[0] - current_state[0]

        # 偏差の積分
        integral_error += error * resolution_sec

        # 偏差の一階微分
        derivative_error = (error - simulation_history.error.value[-1]) / resolution_sec
        # --------------------------------------------------------------

        # PID制御入力更新
        # --------------------------------------------------------------
        p_control_input = error * p_gain
        i_control_input = integral_error * i_gain
        d_control_input = derivative_error * d_gain
        pid_control_input = p_control_input + i_control_input + d_control_input
        # --------------------------------------------------------------

        # 履歴保存
        simulation_history.append(
            current_time=current_time,
            current_state=current_state,
            error=error,
            derivative_error=derivative_error,
            integral_error=integral_error,
            p_control_input=p_control_input,
            i_control_input=i_control_input,
            d_control_input=d_control_input,
            pid_control_input=pid_control_input,
        )

    return simulation_history


def simulate():
    """
    Simulates the linear motion of a system using the linear motion dynamics model.
    """

    # シミュレーションパラメータ
    # --------------------------------------------------------------
    simulate_time = 1000.0  # シミュレーション実行時間 [sec]
    resolution_sec = 0.01  # シミュレーション時間解像度 [sec]

    current_time = 0.0
    current_state = np.array([0.0, 0.0])  # 初期位置 [m], 初期速度 [m/s]
    target_state = np.array([50.0, 0.0])  # 目標位置 [m], 目標速度 [m/s]

    p_gain = 1.0e-2  # P制御器のゲイン
    i_gain = 1.0e-6  # I制御器のゲイン
    d_gain = 5.0e-1  # D制御器のゲイン

    mass = 1.0  # 質量 [kg]
    # --------------------------------------------------------------

    # 初期化
    # --------------------------------------------------------------
    initial_error = target_state[0] - current_state[0]
    initial_derivative_error = 0.0
    initial_integral_error = 0.0

    initial_p_control_input = initial_error * p_gain
    initial_i_control_input = initial_integral_error * i_gain
    initial_d_control_input = initial_derivative_error * d_gain
    initial_pid_control_input = (
        initial_p_control_input + initial_i_control_input + initial_d_control_input
    )

    # 偏差履歴の初期化
    error_history = simulation_history.ErrorHistory(
        value=[initial_error],
        derivative=[initial_derivative_error],
        integral=[initial_integral_error],
    )

    # 制御入力履歴の初期化
    control_input_history = simulation_history.ControlInputHistory(
        p=[initial_p_control_input],
        i=[initial_i_control_input],
        d=[initial_d_control_input],
        pid=[initial_pid_control_input],
    )

    # シミュレーション履歴の初期化
    history = simulation_history.SimulationHistory(
        time=[current_time],
        state=[current_state.copy()],
        error=error_history,
        control_input=control_input_history,
    )
    # --------------------------------------------------------------

    # 伝搬シミュレーション
    history = propagate(
        current_state=current_state,
        target_state=target_state,
        p_gain=p_gain,
        i_gain=i_gain,
        d_gain=d_gain,
        mass=mass,
        simulate_time=simulate_time,
        resolution_sec=resolution_sec,
        simulation_history=history,
    )

    # 可視化
    visualize.plot_linear_motion(
        history,
        output_dir_path="docs/images/generated/",
    )

    # 動画出力
    animation_visualize.create_linear_motion_animation(
        simulation_history=history,
        target_position=target_state[0],
        output_path="docs/images/generated/linear_motion_animation.gif",
        fps=30,
        max_frames=800,
    )


if __name__ == "__main__":
    simulate()
