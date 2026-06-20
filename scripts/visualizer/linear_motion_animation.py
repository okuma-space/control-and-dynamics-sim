from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation, PillowWriter


def create_linear_motion_animation(
    simulation_history,
    target_position=None,
    output_path="docs/images/generated/linear_motion_animation.gif",
    fps=30,
    max_frames=800,
):
    """
    1次元直線運動のシミュレーション履歴からアニメーションを作成する.

    Figure:
        1. 質点の1次元運動
        2. 位置履歴
        3. P/I/D/PID制御入力履歴

    Args:
        simulation_history:
            SimulationHistory.
            simulation_history.time: 時刻履歴
            simulation_history.state: 状態履歴 [position, velocity]
            simulation_history.control_input.p: P制御入力履歴
            simulation_history.control_input.i: I制御入力履歴
            simulation_history.control_input.d: D制御入力履歴
            simulation_history.control_input.pid: PID制御入力履歴

        target_position:
            目標位置 [m]. None の場合は目標線を表示しない.

        output_path:
            出力先. ".gif" または ".mp4" を指定する.

        fps:
            動画のフレームレート.

        max_frames:
            使用する最大フレーム数.
            dt=0.01, 800秒などを全フレーム動画化すると重すぎるため間引く.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    time_array = np.array(simulation_history.time)
    state_array = np.array(simulation_history.state)

    position_array = state_array[:, 0]
    velocity_array = state_array[:, 1]

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
    # position axis range
    # ============================================================
    x_min = np.min(position_array)
    x_max = np.max(position_array)

    if target_position is not None:
        x_min = min(x_min, target_position)
        x_max = max(x_max, target_position)

    x_margin = max((x_max - x_min) * 0.1, 1.0)

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

    fig, (ax_motion, ax_position, ax_control) = plt.subplots(
        3,
        1,
        figsize=(10, 9),
        gridspec_kw={"height_ratios": [1, 2, 2]},
    )

    # ============================================================
    # 上段: 1次元上の質点運動
    # ============================================================
    ax_motion.set_xlim(x_min - x_margin, x_max + x_margin)
    ax_motion.set_ylim(-1.0, 1.0)
    ax_motion.set_xlabel("position [m]")
    ax_motion.set_yticks([])
    ax_motion.grid(True)

    (mass_point,) = ax_motion.plot([], [], "o", markersize=12)

    if target_position is not None:
        ax_motion.axvline(
            target_position,
            linestyle="--",
            linewidth=1.0,
            label="target position",
        )
        ax_motion.legend(loc="upper right")

    # ============================================================
    # 中段: position履歴
    # ============================================================
    ax_position.set_xlim(time_array[0], time_array[-1])
    ax_position.set_ylim(x_min - x_margin, x_max + x_margin)
    ax_position.set_xlabel("time [s]")
    ax_position.set_ylabel("position [m]")
    ax_position.grid(True)

    (position_line,) = ax_position.plot([], [], label="position [m]")
    (current_position_marker,) = ax_position.plot([], [], "o", markersize=6)

    if target_position is not None:
        ax_position.axhline(
            target_position,
            linestyle="--",
            linewidth=1.0,
            label="target position",
        )

    ax_position.legend(loc="upper right")

    # ============================================================
    # 下段: PID制御入力履歴
    # ============================================================
    ax_control.set_xlim(time_array[0], time_array[-1])
    ax_control.set_ylim(
        control_input_min - control_input_margin,
        control_input_max + control_input_margin,
    )
    ax_control.set_xlabel("time [s]")
    ax_control.set_ylabel("control input [N]")
    ax_control.grid(True)

    (p_control_line,) = ax_control.plot([], [], label="P control input [N]")
    (i_control_line,) = ax_control.plot([], [], label="I control input [N]")
    (d_control_line,) = ax_control.plot([], [], label="D control input [N]")
    (pid_control_line,) = ax_control.plot([], [], label="PID control input [N]")

    (current_pid_marker,) = ax_control.plot([], [], "o", markersize=6)

    ax_control.axhline(0.0, linestyle="--", linewidth=1.0)
    ax_control.legend(loc="upper right")

    title = fig.suptitle("")

    def init():
        mass_point.set_data([], [])

        position_line.set_data([], [])
        current_position_marker.set_data([], [])

        p_control_line.set_data([], [])
        i_control_line.set_data([], [])
        d_control_line.set_data([], [])
        pid_control_line.set_data([], [])
        current_pid_marker.set_data([], [])

        title.set_text("")

        return (
            mass_point,
            position_line,
            current_position_marker,
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
        current_position = position_array[sample_index]
        current_velocity = velocity_array[sample_index]
        current_pid_control_input = pid_control_input_array[sample_index]

        # 質点位置
        mass_point.set_data([current_position], [0.0])

        # position履歴
        position_line.set_data(
            time_array[: sample_index + 1],
            position_array[: sample_index + 1],
        )

        current_position_marker.set_data(
            [current_time],
            [current_position],
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
            f"1D Linear Motion  "
            f"t = {current_time:.2f} s, "
            f"x = {current_position:.3f} m, "
            f"v = {current_velocity:.3f} m/s, "
            f"u = {current_pid_control_input:.3f} N"
        )

        return (
            mass_point,
            position_line,
            current_position_marker,
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
