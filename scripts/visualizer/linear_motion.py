from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def _prepare_output_path(output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def plot_position_velocity(
    time_array,
    position_history,
    velocity_history,
    output_path,
):
    """
    Figure 1:
        position [m]
        velocity [m/s]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_position = plt.subplots(figsize=(10, 6))

    # 左軸: 位置
    position_line = ax_position.plot(
        time_array,
        position_history,
        color="tab:blue",
        label="position [m]",
    )
    ax_position.set_xlabel("time [s]")
    ax_position.set_ylabel("position [m]")
    ax_position.grid(True)

    # 右軸: 速度
    ax_velocity = ax_position.twinx()
    velocity_line = ax_velocity.plot(
        time_array,
        velocity_history,
        color="tab:orange",
        label="velocity [m/s]",
    )
    ax_velocity.set_ylabel("velocity [m/s]")

    # 凡例をまとめる
    lines = position_line + velocity_line
    labels = [line.get_label() for line in lines]
    ax_position.legend(lines, labels, loc="upper right")

    fig.suptitle("1D Linear Motion Simulation")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_position_error_p_control(
    time_array,
    position_error_array,
    p_control_input_array,
    output_path,
):
    """
    Figure 2:
        position error [m]
        P control input [m/s^2]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_error = plt.subplots(figsize=(10, 6))

    # 左軸: 位置偏差
    error_line = ax_error.plot(
        time_array,
        position_error_array,
        color="tab:blue",
        label="position error [m]",
    )
    ax_error.set_xlabel("time [s]")
    ax_error.set_ylabel("position error [m]")
    ax_error.grid(True)

    # 右軸: P制御入力
    ax_control = ax_error.twinx()
    control_line = ax_control.plot(
        time_array,
        p_control_input_array,
        color="tab:orange",
        label="P control input [m/s^2]",
    )
    ax_control.set_ylabel("P control input [m/s^2]")

    # 0ライン
    ax_error.axhline(0.0, linestyle="--", linewidth=1.0)

    # 凡例をまとめる
    lines = error_line + control_line
    labels = [line.get_label() for line in lines]
    ax_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Position Error and P Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_derivative_position_error_d_control(
    time_array,
    derivative_position_error_array,
    d_control_input_array,
    output_path,
):
    """
    Figure 3:
        derivative position error [m/s]
        D control input [m/s^2]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_derivative_error = plt.subplots(figsize=(10, 6))

    # 左軸: 位置偏差の一階微分
    derivative_error_line = ax_derivative_error.plot(
        time_array,
        derivative_position_error_array,
        color="tab:blue",
        label="derivative position error [m/s]",
    )
    ax_derivative_error.set_xlabel("time [s]")
    ax_derivative_error.set_ylabel("derivative position error [m/s]")
    ax_derivative_error.grid(True)

    # 右軸: D制御入力
    ax_d_control = ax_derivative_error.twinx()
    d_control_line = ax_d_control.plot(
        time_array,
        d_control_input_array,
        color="tab:orange",
        label="D control input [m/s^2]",
    )
    ax_d_control.set_ylabel("D control input [m/s^2]")

    # 0ライン
    ax_derivative_error.axhline(0.0, linestyle="--", linewidth=1.0)

    # 凡例をまとめる
    lines = derivative_error_line + d_control_line
    labels = [line.get_label() for line in lines]
    ax_derivative_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Derivative Position Error and D Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_pd_control_input(
    time_array,
    p_control_input_array,
    d_control_input_array,
    p_d_control_input_array,
    output_path,
):
    """
    Figure 4:
        P control input [m/s^2]
        D control input [m/s^2]
        P + D control input [m/s^2]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_pd_control = plt.subplots(figsize=(10, 6))

    p_line = ax_pd_control.plot(
        time_array,
        p_control_input_array,
        color="tab:blue",
        label="P control input [m/s^2]",
    )
    d_line = ax_pd_control.plot(
        time_array,
        d_control_input_array,
        color="tab:orange",
        label="D control input [m/s^2]",
    )
    pd_line = ax_pd_control.plot(
        time_array,
        p_d_control_input_array,
        color="tab:green",
        label="P + D control input [m/s^2]",
    )

    ax_pd_control.set_xlabel("time [s]")
    ax_pd_control.set_ylabel("control input [m/s^2]")
    ax_pd_control.grid(True)

    # 0ライン
    ax_pd_control.axhline(0.0, linestyle="--", linewidth=1.0)

    # 凡例をまとめる
    lines = p_line + d_line + pd_line
    labels = [line.get_label() for line in lines]
    ax_pd_control.legend(lines, labels, loc="upper right")

    fig.suptitle("P / D / P+D Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_linear_motion(
    state_history,
    time_vector,
    position_error_history,
    derivative_position_error_history,
    p_control_input_history,
    d_control_input_history,
    p_d_control_input_history,
    output_path="docs/linear_motion_result.png",
    control_output_path="docs/linear_motion_p_control_result.png",
    derivative_control_output_path="docs/linear_motion_d_control_result.png",
    pd_control_output_path="docs/linear_motion_pd_control_result.png",
):
    """
    Plot histories of 1D linear motion simulation.
    """

    time_array = np.array(time_vector)
    state_history_array = np.array(state_history)

    position_error_array = np.array(position_error_history)
    derivative_position_error_array = np.array(derivative_position_error_history)

    p_control_input_array = np.array(p_control_input_history)
    d_control_input_array = np.array(d_control_input_history)
    p_d_control_input_array = np.array(p_d_control_input_history)

    position_history = state_history_array[:, 0]
    velocity_history = state_history_array[:, 1]

    position_velocity_output_path = plot_position_velocity(
        time_array=time_array,
        position_history=position_history,
        velocity_history=velocity_history,
        output_path=output_path,
    )

    position_error_p_control_output_path = plot_position_error_p_control(
        time_array=time_array,
        position_error_array=position_error_array,
        p_control_input_array=p_control_input_array,
        output_path=control_output_path,
    )

    derivative_error_d_control_output_path = plot_derivative_position_error_d_control(
        time_array=time_array,
        derivative_position_error_array=derivative_position_error_array,
        d_control_input_array=d_control_input_array,
        output_path=derivative_control_output_path,
    )

    pd_control_input_output_path = plot_pd_control_input(
        time_array=time_array,
        p_control_input_array=p_control_input_array,
        d_control_input_array=d_control_input_array,
        p_d_control_input_array=p_d_control_input_array,
        output_path=pd_control_output_path,
    )

    return (
        position_velocity_output_path,
        position_error_p_control_output_path,
        derivative_error_d_control_output_path,
        pd_control_input_output_path,
    )
