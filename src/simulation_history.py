from dataclasses import dataclass, field

import numpy as np


@dataclass
class ErrorHistory:
    """
    偏差履歴のデータクラス.
    """

    value: list[float] = field(default_factory=list)
    derivative: list[float] = field(default_factory=list)
    integral: list[float] = field(default_factory=list)


@dataclass
class ControlInputHistory:
    """
    制御入力履歴のデータクラス.
    """

    p: list[float] = field(default_factory=list)
    i: list[float] = field(default_factory=list)
    d: list[float] = field(default_factory=list)
    pid: list[float] = field(default_factory=list)


@dataclass
class SimulationHistory:
    """
    一次元制御システムのシミュレーション履歴を保持するデータクラス.
    """

    time: list[float] = field(default_factory=list)  # 時間[s]
    state: list[np.ndarray] = field(
        default_factory=list
    )  # 状態ベクトル [値, 一次微分値]
    error: ErrorHistory = field(
        default_factory=ErrorHistory
    )  # 偏差履歴 [値, 一次微分値, 積分値]
    control_input: ControlInputHistory = field(
        default_factory=ControlInputHistory
    )  # 制御入力履歴 [P制御入力, I制御入力, D制御入力, PID制御入力]

    def append(
        self,
        current_time,
        current_state,
        error,
        derivative_error,
        integral_error,
        p_control_input,
        i_control_input,
        d_control_input,
        pid_control_input,
    ):
        """
        シミュレーション履歴に現在の状態、偏差、制御入力を追加する.
        """

        # 状態履歴に現在の状態を追加する
        self.time.append(current_time)
        self.state.append(current_state.copy())

        # 偏差履歴に現在の偏差を追加する
        self.error.value.append(error)
        self.error.derivative.append(derivative_error)
        self.error.integral.append(integral_error)

        # 制御入力履歴に現在の制御入力を追加する
        self.control_input.p.append(p_control_input)
        self.control_input.i.append(i_control_input)
        self.control_input.d.append(d_control_input)
        self.control_input.pid.append(pid_control_input)
