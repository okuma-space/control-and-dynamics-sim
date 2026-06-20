from simulator import linear_motion, rigid_body_rotation
from visualizer import rigid_body_rotation as rigid_body_rotation_visualize
from visualizer import linear_motion as linear_motion_visualize
from visualizer import linear_motion_animation as linear_motion_animation
from visualizer import rigid_body_rotation_animation as rigid_body_rotation_animation
import numpy as np
import argparse


def linear_motion_simulation():

    # シミュレーションパラメータ
    # --------------------------------------------------------------
    simulate_time = 1000.0  # シミュレーション実行時間 [sec]
    resolution_sec = 0.01  # シミュレーション時間解像度 [sec]

    current_time = 0.0
    current_state = np.array([0.0, 0.0])  # 初期位置 [m], 初期速度 [m/s]
    target_state = np.array([50.0, 0.0])  # 目標位置 [m], 目標速度 [m/s]
    
    p_gain = 1.0e-2  # P制御器のゲイン
    i_gain = 1.0e-6  # I制御器のゲイン
    d_gain = 1.0e-2  # D制御器のゲイン

    mass = 1.0  # 質量 [kg]
    damping_coefficient = 1.0e-2  # 摩擦係数 [Ns/m]
    # --------------------------------------------------------------

    # シミュレーション実行
    history = linear_motion.simulate(
        simulate_time,
        resolution_sec,
        current_time,
        current_state,
        target_state,
        p_gain,
        i_gain,
        d_gain,
        mass,
        damping_coefficient
    )

    # 可視化
    linear_motion_visualize.plot_linear_motion(
        history,
        output_dir_path="docs/images/generated/",
    )

    # 動画出力
    linear_motion_animation.create_linear_motion_animation(
        simulation_history=history,
        target_position=target_state[0],
        output_path="docs/images/generated/linear_motion_animation.gif",
        fps=30,
        max_frames=800,
    )


def rigid_body_rotation_simulation():

    # シミュレーションパラメータ
    # --------------------------------------------------------------
    simulate_time = 1000.0  # シミュレーション実行時間 [sec]
    resolution_sec = 0.01  # シミュレーション時間解像度 [sec]

    current_time = 0.0
    current_state = np.array([0.0, 0.0])  # 初期位置 [rad], 初期角速度 [rad/s]
    target_state = np.array([2.0, 0.0])  # 目標位置 [rad], 目標角速度 [rad/s]
    p_gain = 1.0e-2  # P制御器のゲイン
    i_gain = 1.0e-6  # I制御器のゲイン
    d_gain = 5.0e-1  # D制御器のゲイン

    moment_of_inertia = 1.0  # 慣性モーメント [kg*m^2]
    # --------------------------------------------------------------

    # シミュレーション実行
    history = rigid_body_rotation.simulate(
        simulate_time,
        resolution_sec,
        current_time,
        current_state,
        target_state,
        p_gain,
        i_gain,
        d_gain,
        moment_of_inertia,
    )

    # 可視化
    rigid_body_rotation_visualize.plot_rigid_body_rotation(
        history,
        output_dir_path="docs/images/generated/",
    )

    # 動画出力
    rigid_body_rotation_animation.create_rigid_body_rotation_animation(
        simulation_history=history,
        target_angle=target_state[0],
        output_path="docs/images/generated/rigid_body_rotation_animation.gif",
        fps=30,
        max_frames=800,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "simulation_name",
        choices=[
            "linear_motion",
            "rigid_body_rotation",
        ],
    )

    args = parser.parse_args()

    if args.simulation_name == "linear_motion":
        linear_motion_simulation()
    elif args.simulation_name == "rigid_body_rotation":
        rigid_body_rotation_simulation()


if __name__ == "__main__":
    main()
