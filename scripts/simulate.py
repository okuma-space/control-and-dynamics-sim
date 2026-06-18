import dynamics
import numpy as np
import visualize
import control

def simulate():
    """
    Simulates the linear motion of a system using the linear motion dynamics model.
    """

    # 初期値
    simulate_time = 1000.0  # シミュレーション実行時間[sec]
    resolution_sec = 0.01  # シミュレーション時間解像度[sec]
    current_state = np.array([0.0, 0.0])  # 初期位置[m],初期速度[m/s]
    target_state = np.array([50.0, 0.0])  # 目標位置[m],目標速度[m/s]
    gain = np.array([0.0005, 0.0])  # P制御器のゲイン

    # 型準備
    time_vector = []
    current_time = 0.0
    state_history = []

    # 伝搬ループ
    while current_time < simulate_time:
        # 制御入力を計算する
        control_input = control.p_controller(target_state, current_state, gain)

        # ダイナミクスモデルから状態ベクトルの一次微分を取得する
        state_derivative = dynamics.linear_motion_model(
            current_state, control_input
        )  # 初期加速度[m/s^2]

        # 状態ベクトルを更新する
        current_state = current_state + state_derivative * resolution_sec

        # 状態ベクトルを保存する
        state_history.append(current_state.copy())

        # 時刻の更新
        time_vector.append(current_time)
        current_time += resolution_sec

    # visualize
    visualize.plot_linear_motion(
        state_history,
        time_vector,
        output_path="docs/linear_motion_result.png",
    )


if __name__ == "__main__":
    simulate()
