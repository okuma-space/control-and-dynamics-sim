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

    position_line = ax_position.plot(
        time_array,
        position_history,
        color="tab:blue",
        label="position [m]",
    )
    ax_position.set_xlabel("time [s]")
    ax_position.set_ylabel("position [m]")
    ax_position.grid(True)

    ax_velocity = ax_position.twinx()
    velocity_line = ax_velocity.plot(
        time_array,
        velocity_history,
        color="tab:orange",
        label="velocity [m/s]",
    )
    ax_velocity.set_ylabel("velocity [m/s]")

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
        P control input [N]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_error = plt.subplots(figsize=(10, 6))

    error_line = ax_error.plot(
        time_array,
        position_error_array,
        color="tab:blue",
        label="position error [m]",
    )
    ax_error.set_xlabel("time [s]")
    ax_error.set_ylabel("position error [m]")
    ax_error.grid(True)

    ax_control = ax_error.twinx()
    control_line = ax_control.plot(
        time_array,
        p_control_input_array,
        color="tab:orange",
        label="P control input [N]",
    )
    ax_control.set_ylabel("P control input [N]")

    ax_error.axhline(0.0, linestyle="--", linewidth=1.0)

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
        D control input [N]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_derivative_error = plt.subplots(figsize=(10, 6))

    derivative_error_line = ax_derivative_error.plot(
        time_array,
        derivative_position_error_array,
        color="tab:blue",
        label="derivative position error [m/s]",
    )
    ax_derivative_error.set_xlabel("time [s]")
    ax_derivative_error.set_ylabel("derivative position error [m/s]")
    ax_derivative_error.grid(True)

    ax_d_control = ax_derivative_error.twinx()
    d_control_line = ax_d_control.plot(
        time_array,
        d_control_input_array,
        color="tab:orange",
        label="D control input [N]",
    )
    ax_d_control.set_ylabel("D control input [N]")

    ax_derivative_error.axhline(0.0, linestyle="--", linewidth=1.0)

    lines = derivative_error_line + d_control_line
    labels = [line.get_label() for line in lines]
    ax_derivative_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Derivative Position Error and D Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_integral_position_error_i_control(
    time_array,
    integral_position_error_array,
    i_control_input_array,
    output_path,
):
    """
    Figure 4:
        integral position error [m s]
        I control input [N]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_integral_error = plt.subplots(figsize=(10, 6))

    integral_error_line = ax_integral_error.plot(
        time_array,
        integral_position_error_array,
        color="tab:blue",
        label="integral position error [m s]",
    )
    ax_integral_error.set_xlabel("time [s]")
    ax_integral_error.set_ylabel("integral position error [m s]")
    ax_integral_error.grid(True)

    ax_i_control = ax_integral_error.twinx()
    i_control_line = ax_i_control.plot(
        time_array,
        i_control_input_array,
        color="tab:orange",
        label="I control input [N]",
    )
    ax_i_control.set_ylabel("I control input [N]")

    ax_integral_error.axhline(0.0, linestyle="--", linewidth=1.0)

    lines = integral_error_line + i_control_line
    labels = [line.get_label() for line in lines]
    ax_integral_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Integral Position Error and I Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_pid_control_input(
    time_array,
    p_control_input_array,
    i_control_input_array,
    d_control_input_array,
    pid_control_input_array,
    output_path,
):
    """
    Figure 5:
        P control input [N]
        I control input [N]
        D control input [N]
        PID control input [N]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_pid_control = plt.subplots(figsize=(10, 6))

    p_line = ax_pid_control.plot(
        time_array,
        p_control_input_array,
        color="tab:blue",
        label="P control input [N]",
    )
    i_line = ax_pid_control.plot(
        time_array,
        i_control_input_array,
        color="tab:purple",
        label="I control input [N]",
    )
    d_line = ax_pid_control.plot(
        time_array,
        d_control_input_array,
        color="tab:orange",
        label="D control input [N]",
    )
    pid_line = ax_pid_control.plot(
        time_array,
        pid_control_input_array,
        color="tab:green",
        label="PID control input [N]",
    )

    ax_pid_control.set_xlabel("time [s]")
    ax_pid_control.set_ylabel("control input [N]")
    ax_pid_control.grid(True)

    ax_pid_control.axhline(0.0, linestyle="--", linewidth=1.0)

    lines = p_line + i_line + d_line + pid_line
    labels = [line.get_label() for line in lines]
    ax_pid_control.legend(lines, labels, loc="upper right")

    fig.suptitle("P / I / D / PID Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_linear_motion(simulation_history, output_dir_path):
    """
    Plot histories of 1D linear motion simulation.
    """
    output_dir_path = Path(output_dir_path)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    time_array = np.array(simulation_history.time)
    state_history_array = np.array(simulation_history.state)

    position_error_array = np.array(simulation_history.error.value)
    derivative_position_error_array = np.array(simulation_history.error.derivative)
    integral_position_error_array = np.array(simulation_history.error.integral)

    p_control_input_array = np.array(simulation_history.control_input.p)
    i_control_input_array = np.array(simulation_history.control_input.i)
    d_control_input_array = np.array(simulation_history.control_input.d)
    pid_control_input_array = np.array(simulation_history.control_input.pid)

    position_history = state_history_array[:, 0]
    velocity_history = state_history_array[:, 1]

    plot_position_velocity(
        time_array=time_array,
        position_history=position_history,
        velocity_history=velocity_history,
        output_path=output_dir_path / "linear_motion_result.png",
    )

    plot_position_error_p_control(
        time_array=time_array,
        position_error_array=position_error_array,
        p_control_input_array=p_control_input_array,
        output_path=output_dir_path / "linear_motion_p_control_result.png",
    )

    plot_derivative_position_error_d_control(
        time_array=time_array,
        derivative_position_error_array=derivative_position_error_array,
        d_control_input_array=d_control_input_array,
        output_path=output_dir_path / "linear_motion_d_control_result.png",
    )

    plot_integral_position_error_i_control(
        time_array=time_array,
        integral_position_error_array=integral_position_error_array,
        i_control_input_array=i_control_input_array,
        output_path=output_dir_path / "linear_motion_i_control_result.png",
    )

    plot_pid_control_input(
        time_array=time_array,
        p_control_input_array=p_control_input_array,
        i_control_input_array=i_control_input_array,
        d_control_input_array=d_control_input_array,
        pid_control_input_array=pid_control_input_array,
        output_path=output_dir_path / "linear_motion_pid_control_result.png",
    )
