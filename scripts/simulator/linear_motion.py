import dynamics
import numpy as np
import visualizer.linear_motion as visualize


def simulate():
    """
    Simulates the linear motion of a system using the linear motion dynamics model.
    """

    # 初期値
    simulate_time = 1000.0  # シミュレーション実行時間[sec]
    resolution_sec = 0.01  # シミュレーション時間解像度[sec]
    current_state = np.array([0.0, 0.0])  # 初期位置[m],初期速度[m/s]
    target_state = np.array([50.0, 0.0])  # 目標位置[m],目標速度[m/s]
    p_gain = 0.005  # P制御器のゲイン
    d_gain = 0.015  # D制御器のゲイン
    current_time = 0.0
    mass = 1.0  # 質量[kg]

    # 初期偏差
    position_error = target_state[0] - current_state[0]
    derivative_position_error = 0.0

    # 初期制御入力を計算する
    p_control_input = position_error * p_gain
    p_d_control_input = p_control_input

    # 初期値を履歴に設定
    time_vector = [current_time]  # 時刻の履歴
    state_history = [current_state.copy()]  # 状態ベクトルの履歴
    position_error_history = [position_error]  # 位置誤差[m]
    derivative_position_error_history = [
        derivative_position_error
    ]  # 位置誤差の一時微分[m/s ]
    p_control_input_history = [p_control_input]  # P制御入力[m/s^2]
    d_control_input_history = [0.0]  # D制御入力[m/s^2]
    p_d_control_input_history = [p_d_control_input]  # P+D制御入力[m/s^2]

    # 伝搬ループ
    while current_time < simulate_time:
        # ダイナミクス計算
        # ------------------------------------------------
        # ダイナミクスモデルから状態ベクトルの一次微分を取得する
        state_derivative = dynamics.linear_motion_model(
            current_state, p_d_control_input, mass
        )  # 初期加速度[m/s^2]
        # ------------------------------------------------

        # 状態更新
        # ------------------------------------------------
        # 時刻の更新
        current_time += resolution_sec

        # 状態ベクトルを更新する
        current_state = current_state + state_derivative * resolution_sec
        # ------------------------------------------------

        # 偏差更新
        # ------------------------------------------------
        # 位置誤差(偏差[m])を計算
        position_error = target_state[0] - current_state[0]

        # 偏差の一時微分を計算
        derivative_position_error = (
            position_error - position_error_history[-1]
        ) / resolution_sec
        # ------------------------------------------------

        # 制御入力更新
        # ------------------------------------------------
        # P 制御入力を計算する
        p_control_input = position_error * p_gain

        # D 制御入力を計算する
        d_control_input = derivative_position_error * d_gain

        # P+D 制御入力を計算する
        p_d_control_input = p_control_input + d_control_input
        # ------------------------------------------------

        # 結果保存
        # ------------------------------------------------
        # 時刻を保存する
        time_vector.append(current_time)

        # 偏差の保存
        position_error_history.append(position_error)

        # 偏差の一時微分の保存
        derivative_position_error_history.append(derivative_position_error)

        # P 制御入力を保存する
        p_control_input_history.append(p_control_input)

        # D 制御入力を保存する
        d_control_input_history.append(d_control_input)

        # P+D 制御入力を保存する
        p_d_control_input_history.append(p_d_control_input)

        # 状態ベクトルを保存する
        state_history.append(current_state.copy())
        # ------------------------------------------------

    # visualize
    visualize.plot_linear_motion(
        state_history,
        time_vector,
        position_error_history,
        derivative_position_error_history,
        p_control_input_history,
        d_control_input_history,
        p_d_control_input_history,
        output_path="docs/linear_motion_result.png",
    )


if __name__ == "__main__":
    simulate()
