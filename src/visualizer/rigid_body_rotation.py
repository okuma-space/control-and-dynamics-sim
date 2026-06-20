from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def _prepare_output_path(output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def plot_angle_angular_velocity(
    time_array,
    angle_history,
    angular_velocity_history,
    output_path,
):
    """
    Figure 1:
        angle [rad]
        angular velocity [rad/s]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_angle = plt.subplots(figsize=(10, 6))

    angle_line = ax_angle.plot(
        time_array,
        angle_history,
        color="tab:blue",
        label="angle [rad]",
    )
    ax_angle.set_xlabel("time [s]")
    ax_angle.set_ylabel("angle [rad]")
    ax_angle.grid(True)

    ax_angular_velocity = ax_angle.twinx()
    angular_velocity_line = ax_angular_velocity.plot(
        time_array,
        angular_velocity_history,
        color="tab:orange",
        label="angular velocity [rad/s]",
    )
    ax_angular_velocity.set_ylabel("angular velocity [rad/s]")

    lines = angle_line + angular_velocity_line
    labels = [line.get_label() for line in lines]
    ax_angle.legend(lines, labels, loc="upper right")

    fig.suptitle("Rigid Body Rotation Simulation")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_angle_error_p_control(
    time_array,
    angle_error_array,
    p_control_input_array,
    output_path,
):
    """
    Figure 2:
        angle error [rad]
        P control input [N m]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_error = plt.subplots(figsize=(10, 6))

    error_line = ax_error.plot(
        time_array,
        angle_error_array,
        color="tab:blue",
        label="angle error [rad]",
    )
    ax_error.set_xlabel("time [s]")
    ax_error.set_ylabel("angle error [rad]")
    ax_error.grid(True)

    ax_control = ax_error.twinx()
    control_line = ax_control.plot(
        time_array,
        p_control_input_array,
        color="tab:orange",
        label="P control input [N m]",
    )
    ax_control.set_ylabel("P control input [N m]")

    ax_error.axhline(0.0, linestyle="--", linewidth=1.0)

    lines = error_line + control_line
    labels = [line.get_label() for line in lines]
    ax_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Angle Error and P Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_derivative_angle_error_d_control(
    time_array,
    derivative_angle_error_array,
    d_control_input_array,
    output_path,
):
    """
    Figure 3:
        derivative angle error [rad/s]
        D control input [N m]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_derivative_error = plt.subplots(figsize=(10, 6))

    derivative_error_line = ax_derivative_error.plot(
        time_array,
        derivative_angle_error_array,
        color="tab:blue",
        label="derivative angle error [rad/s]",
    )
    ax_derivative_error.set_xlabel("time [s]")
    ax_derivative_error.set_ylabel("derivative angle error [rad/s]")
    ax_derivative_error.grid(True)

    ax_d_control = ax_derivative_error.twinx()
    d_control_line = ax_d_control.plot(
        time_array,
        d_control_input_array,
        color="tab:orange",
        label="D control input [N m]",
    )
    ax_d_control.set_ylabel("D control input [N m]")

    ax_derivative_error.axhline(0.0, linestyle="--", linewidth=1.0)

    lines = derivative_error_line + d_control_line
    labels = [line.get_label() for line in lines]
    ax_derivative_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Derivative Angle Error and D Control Input")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path


def plot_integral_angle_error_i_control(
    time_array,
    integral_angle_error_array,
    i_control_input_array,
    output_path,
):
    """
    Figure 4:
        integral angle error [rad s]
        I control input [N m]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_integral_error = plt.subplots(figsize=(10, 6))

    integral_error_line = ax_integral_error.plot(
        time_array,
        integral_angle_error_array,
        color="tab:blue",
        label="integral angle error [rad s]",
    )
    ax_integral_error.set_xlabel("time [s]")
    ax_integral_error.set_ylabel("integral angle error [rad s]")
    ax_integral_error.grid(True)

    ax_i_control = ax_integral_error.twinx()
    i_control_line = ax_i_control.plot(
        time_array,
        i_control_input_array,
        color="tab:orange",
        label="I control input [N m]",
    )
    ax_i_control.set_ylabel("I control input [N m]")

    ax_integral_error.axhline(0.0, linestyle="--", linewidth=1.0)

    lines = integral_error_line + i_control_line
    labels = [line.get_label() for line in lines]
    ax_integral_error.legend(lines, labels, loc="upper right")

    fig.suptitle("Integral Angle Error and I Control Input")
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
        P control input [N m]
        I control input [N m]
        D control input [N m]
        PID control input [N m]
    """

    output_path = _prepare_output_path(output_path)

    fig, ax_pid_control = plt.subplots(figsize=(10, 6))

    p_line = ax_pid_control.plot(
        time_array,
        p_control_input_array,
        color="tab:blue",
        label="P control input [N m]",
    )
    i_line = ax_pid_control.plot(
        time_array,
        i_control_input_array,
        color="tab:purple",
        label="I control input [N m]",
    )
    d_line = ax_pid_control.plot(
        time_array,
        d_control_input_array,
        color="tab:orange",
        label="D control input [N m]",
    )
    pid_line = ax_pid_control.plot(
        time_array,
        pid_control_input_array,
        color="tab:green",
        label="PID control input [N m]",
    )

    ax_pid_control.set_xlabel("time [s]")
    ax_pid_control.set_ylabel("control input [N m]")
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


def plot_rigid_body_rotation(simulation_history, output_dir_path):
    """
    Plot histories of 1-axis rigid body rotation simulation.
    """

    output_dir_path = Path(output_dir_path)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    time_array = np.array(simulation_history.time)
    state_history_array = np.array(simulation_history.state)

    angle_error_array = np.array(simulation_history.error.value)
    derivative_angle_error_array = np.array(simulation_history.error.derivative)
    integral_angle_error_array = np.array(simulation_history.error.integral)

    p_control_input_array = np.array(simulation_history.control_input.p)
    i_control_input_array = np.array(simulation_history.control_input.i)
    d_control_input_array = np.array(simulation_history.control_input.d)
    pid_control_input_array = np.array(simulation_history.control_input.pid)

    angle_history = state_history_array[:, 0]
    angular_velocity_history = state_history_array[:, 1]

    plot_angle_angular_velocity(
        time_array=time_array,
        angle_history=angle_history,
        angular_velocity_history=angular_velocity_history,
        output_path=output_dir_path / "rigid_body_rotation_result.png",
    )

    plot_angle_error_p_control(
        time_array=time_array,
        angle_error_array=angle_error_array,
        p_control_input_array=p_control_input_array,
        output_path=output_dir_path / "rigid_body_rotation_p_control_result.png",
    )

    plot_derivative_angle_error_d_control(
        time_array=time_array,
        derivative_angle_error_array=derivative_angle_error_array,
        d_control_input_array=d_control_input_array,
        output_path=output_dir_path / "rigid_body_rotation_d_control_result.png",
    )

    plot_integral_angle_error_i_control(
        time_array=time_array,
        integral_angle_error_array=integral_angle_error_array,
        i_control_input_array=i_control_input_array,
        output_path=output_dir_path / "rigid_body_rotation_i_control_result.png",
    )

    plot_pid_control_input(
        time_array=time_array,
        p_control_input_array=p_control_input_array,
        i_control_input_array=i_control_input_array,
        d_control_input_array=d_control_input_array,
        pid_control_input_array=pid_control_input_array,
        output_path=output_dir_path / "rigid_body_rotation_pid_control_result.png",
    )