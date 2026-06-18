from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_linear_motion(
    state_history,
    time_vector,
    output_path="docs/linear_motion_result.png",
):
    """
    Plot position and velocity histories of 1D linear motion simulation.

    Left y-axis:
        position [m]

    Right y-axis:
        velocity [m/s]
    """

    time_array = np.array(time_vector)
    state_history_array = np.array(state_history)

    position_history = state_history_array[:, 0]
    velocity_history = state_history_array[:, 1]

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

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
    ax_position.legend(lines, labels, loc="upper left")

    fig.suptitle("1D Linear Motion Simulation")
    fig.tight_layout()

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return output_path
