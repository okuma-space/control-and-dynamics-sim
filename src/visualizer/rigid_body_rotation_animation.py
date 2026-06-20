from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter


def create_rigid_body_rotation_animation(
    simulation_history,
    target_angle=None,
    output_path="docs/images/generated/rigid_body_rotation_animation.gif",
    fps=30,
    max_frames=800,
):
    """
    1軸剛体回転運動のシミュレーション履歴からアニメーションを作成する.

    Figure:
        1. 剛体の回転運動
        2. 角度履歴
        3. P/I/D/PID制御入力履歴

    Args:
        simulation_history:
            SimulationHistory.
            simulation_history.time: 時刻履歴
            simulation_history.state: 状態履歴 [angle, angular_velocity]
            simulation_history.control_input.p: P制御入力履歴
            simulation_history.control_input.i: I制御入力履歴
            simulation_history.control_input.d: D制御入力履歴
            simulation_history.control_input.pid: PID制御入力履歴

        target_angle:
            目標角度 [rad]. None の場合は目標線を表示しない.

        output_path:
            出力先. ".gif" または ".mp4" を指定する.

        fps:
            動画のフレームレート.

        max_frames:
            使用する最大フレーム数.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    time_array = np.array(simulation_history.time)
    state_array = np.array(simulation_history.state)

    angle_array = state_array[:, 0]
    angular_velocity_array = state_array[:, 1]

    p_control_input_array = np.array(simulation_history.control_input.p)
    i_control_input_array = np.array(simulation_history.control_input.i)
    d_control_input_array = np.array(simulation_history.control_input.d)
    pid_control_input_array = np.array(simulation_history.control_input.pid)

    number_of_samples = len(time_array)
    number_of_frames = min(max_frames, number_of_samples)

    frame_indices = np.linspace(
        0,
        number_of_samples - 1,
        number_of_frames,
        dtype=int,
    )

    # ============================================================
    # angle axis range
    # ============================================================
    angle_min = np.min(angle_array)
    angle_max = np.max(angle_array)

    if target_angle is not None:
        angle_min = min(angle_min, target_angle)
        angle_max = max(angle_max, target_angle)

    angle_margin = max((angle_max - angle_min) * 0.1, 0.1)

    # ============================================================
    # control input axis range
    # ============================================================
    control_input_min = min(
        np.min(p_control_input_array),
        np.min(i_control_input_array),
        np.min(d_control_input_array),
        np.min(pid_control_input_array),
    )
    control_input_max = max(
        np.max(p_control_input_array),
        np.max(i_control_input_array),
        np.max(d_control_input_array),
        np.max(pid_control_input_array),
    )

    control_input_margin = max(
        (control_input_max - control_input_min) * 0.1,
        1.0,
    )

    fig, (ax_rotation, ax_angle, ax_control) = plt.subplots(
        3,
        1,
        figsize=(12, 11),
        gridspec_kw={"height_ratios": [3.5, 2, 2]},
    )

    # 凡例を右外に出すため、右側に余白を確保する
    fig.subplots_adjust(
        right=0.78,
        hspace=0.45,
    )

    # ============================================================
    # 上段: 剛体回転
    # ============================================================
    rod_length = 1.0

    ax_rotation.set_xlim(-1.2, 1.2)
    ax_rotation.set_ylim(-1.2, 1.2)
    ax_rotation.set_aspect("equal", adjustable="box")
    ax_rotation.set_xlabel("x")
    ax_rotation.set_ylabel("y")
    ax_rotation.grid(True)

    circle = plt.Circle(
        (0.0, 0.0),
        rod_length,
        fill=False,
        linestyle="--",
        linewidth=1.0,
    )
    ax_rotation.add_patch(circle)

    (rigid_body_line,) = ax_rotation.plot(
        [],
        [],
        linewidth=3.0,
        label="rigid body",
    )
    (rigid_body_tip,) = ax_rotation.plot(
        [],
        [],
        "o",
        markersize=8,
    )

    if target_angle is not None:
        target_x = rod_length * np.cos(target_angle)
        target_y = rod_length * np.sin(target_angle)

        ax_rotation.plot(
            [0.0, target_x],
            [0.0, target_y],
            linestyle="--",
            linewidth=1.5,
            label="target angle",
        )

    ax_rotation.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    # ============================================================
    # 中段: angle履歴
    # ============================================================
    ax_angle.set_xlim(time_array[0], time_array[-1])
    ax_angle.set_ylim(angle_min - angle_margin, angle_max + angle_margin)
    ax_angle.set_xlabel("time [s]")
    ax_angle.set_ylabel("angle [rad]")
    ax_angle.grid(True)

    (angle_line,) = ax_angle.plot(
        [],
        [],
        label="angle [rad]",
    )
    (current_angle_marker,) = ax_angle.plot(
        [],
        [],
        "o",
        markersize=6,
    )

    if target_angle is not None:
        ax_angle.axhline(
            target_angle,
            linestyle="--",
            linewidth=1.0,
            label="target angle",
        )

    ax_angle.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    # ============================================================
    # 下段: PID制御入力履歴
    # ============================================================
    ax_control.set_xlim(time_array[0], time_array[-1])
    ax_control.set_ylim(
        control_input_min - control_input_margin,
        control_input_max + control_input_margin,
    )
    ax_control.set_xlabel("time [s]")
    ax_control.set_ylabel("control input [N m]")
    ax_control.grid(True)

    (p_control_line,) = ax_control.plot(
        [],
        [],
        label="P control input [N m]",
    )
    (i_control_line,) = ax_control.plot(
        [],
        [],
        label="I control input [N m]",
    )
    (d_control_line,) = ax_control.plot(
        [],
        [],
        label="D control input [N m]",
    )
    (pid_control_line,) = ax_control.plot(
        [],
        [],
        label="PID control input [N m]",
    )

    (current_pid_marker,) = ax_control.plot(
        [],
        [],
        "o",
        markersize=6,
    )

    ax_control.axhline(0.0, linestyle="--", linewidth=1.0)

    ax_control.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    title = fig.suptitle("")

    def init():
        rigid_body_line.set_data([], [])
        rigid_body_tip.set_data([], [])

        angle_line.set_data([], [])
        current_angle_marker.set_data([], [])

        p_control_line.set_data([], [])
        i_control_line.set_data([], [])
        d_control_line.set_data([], [])
        pid_control_line.set_data([], [])
        current_pid_marker.set_data([], [])

        title.set_text("")

        return (
            rigid_body_line,
            rigid_body_tip,
            angle_line,
            current_angle_marker,
            p_control_line,
            i_control_line,
            d_control_line,
            pid_control_line,
            current_pid_marker,
            title,
        )

    def update(frame_number):
        sample_index = frame_indices[frame_number]

        current_time = time_array[sample_index]
        current_angle = angle_array[sample_index]
        current_angular_velocity = angular_velocity_array[sample_index]
        current_pid_control_input = pid_control_input_array[sample_index]

        current_x = rod_length * np.cos(current_angle)
        current_y = rod_length * np.sin(current_angle)

        # 剛体回転
        rigid_body_line.set_data(
            [0.0, current_x],
            [0.0, current_y],
        )
        rigid_body_tip.set_data(
            [current_x],
            [current_y],
        )

        # angle履歴
        angle_line.set_data(
            time_array[: sample_index + 1],
            angle_array[: sample_index + 1],
        )

        current_angle_marker.set_data(
            [current_time],
            [current_angle],
        )

        # PID制御入力履歴
        p_control_line.set_data(
            time_array[: sample_index + 1],
            p_control_input_array[: sample_index + 1],
        )

        i_control_line.set_data(
            time_array[: sample_index + 1],
            i_control_input_array[: sample_index + 1],
        )

        d_control_line.set_data(
            time_array[: sample_index + 1],
            d_control_input_array[: sample_index + 1],
        )

        pid_control_line.set_data(
            time_array[: sample_index + 1],
            pid_control_input_array[: sample_index + 1],
        )

        current_pid_marker.set_data(
            [current_time],
            [current_pid_control_input],
        )

        title.set_text(
            f"Rigid Body Rotation  "
            f"t = {current_time:.2f} s, "
            f"theta = {current_angle:.3f} rad, "
            f"omega = {current_angular_velocity:.3f} rad/s, "
            f"tau = {current_pid_control_input:.3f} N m"
        )

        return (
            rigid_body_line,
            rigid_body_tip,
            angle_line,
            current_angle_marker,
            p_control_line,
            i_control_line,
            d_control_line,
            pid_control_line,
            current_pid_marker,
            title,
        )

    animation = FuncAnimation(
        fig,
        update,
        frames=number_of_frames,
        init_func=init,
        interval=1000 / fps,
        blit=True,
    )

    suffix = output_path.suffix.lower()

    if suffix == ".mp4":
        writer = FFMpegWriter(fps=fps, bitrate=1800)
    elif suffix == ".gif":
        writer = PillowWriter(fps=fps)
    else:
        raise ValueError(
            f"output_path must end with '.gif' or '.mp4'. Got: {output_path}"
        )

    animation.save(output_path, writer=writer, dpi=150)
    plt.close(fig)

    return output_path