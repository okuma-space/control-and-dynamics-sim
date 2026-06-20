
# シミュレーション自習結果サマリ_v2.0
[previous version](https://github.com/okuma-space/balloon-simulation/blob/main/docs/reports/report_v1.0.md)

## 1.気球飛翔ダイナミクスシミュレーション

## 2 運動ダイナミクスモデル
### 2.1 平面直線運動モデル
### 2.2 平面回転運動モデル
### 2.3 平面直線運動モデル(粘性摩擦込み)
### 2.4 垂直駆動アームモデル
### 2.5 RL回路モデル
### 2.6 RC回路モデル
### 2.7 RLC回路モデル
### 2.8 増幅回路モデル
### 2.9 液体の電熱機モデル
### 2.10 機械式振動計モデル
### 2.11 タンクモデル
### 2.12 結合2タンクモデル


## 3 制御モデル
### 3.1 P制御モデル
### 3.2 D制御モデルモデル
### 3.3 I制御モデルモデル
### 3.4 PD, PID制御モデル



## 5 Environment models(環境モデル)

## Appendix. 過去versionの検証ログ(保存/振り返り用)

### version0.6
[Repository](https://github.com/okuma-space/control-and-dynamics-sim/tree/v0.6)

[PR](https://github.com/okuma-space/control-and-dynamics-sim/pull/8)

I制御を実装し, PID制御にしてみた.

ゲインに敏感で発散しやすく,また制御効果もあまり大きくはない.

どうも今回のような制御モデルだと安定収束できるから,あまり効果はないらしい.収束地点にバイアスなどがあると偏差の積分が効いてきて,I制御による補正が効いてくるらしい.

PID全部のグラフも出力できるようにした.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.6_a.png)
![p_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_p_control_result_0.6_a.png)
![i_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_d_control_result_0.6_a.png)
![d_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_d_control_result_0.6_a.png)
![pid_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_pid_control_result_0.6_a.png)

ゲインを調整して振動をせずに収束できるようにした.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.6_b.png)
![p_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_p_control_result_0.6_b.png)
![i_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_d_control_result_0.6_b.png)
![d_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_d_control_result_0.6_b.png)
![pid_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_pid_control_result_0.6_b.png)

簡単にgif動画化した.
![pid_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_animation_0.6_a.gif)
![pid_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_animation_0.6_b.gif)


### version0.5
[Repository](https://github.com/okuma-space/control-and-dynamics-sim/tree/v0.5)

[PR](https://github.com/okuma-space/control-and-dynamics-sim/pull/6)

D制御を実装し, PD制御にしてみた.

正しく制御されて目標位置で停止している事が確認できる.

質量も追加してみたが、さほど大きな影響はなさそう.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.5_.png)
![p_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_p_control_result_0.5_.png)
![d_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_d_control_result_0.5_.png)
![pd_control](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_pd_control_result_0.5_.png)

### version0.4
[Repository](https://github.com/okuma-space/control-and-dynamics-sim/tree/v0.4)

P制御を実装し, 50[m]を停止目標にしてみた.

P制御だけでは止まらない事が確認できた.

目標点を中心として,加速度が完全に対象になるから収束しないが想定通りではある.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.4_.png)


### version0.3
[Repository](https://github.com/okuma-space/control-and-dynamics-sim/tree/v0.3)

[PR](https://github.com/okuma-space/control-and-dynamics-sim/pull/5)

加速度を一定として加える事で、等加速度直線運動が実装できている事が確認できた.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.3_.png)

### version0.2
[Repository](https://github.com/okuma-space/control-and-dynamics-sim/tree/v0.2)

[PR](https://github.com/okuma-space/control-and-dynamics-sim/pull/2)

初期速度を設定することで右肩上がりの等速直線運動が実装できている事が確認できた.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.2_.png)


### version0.1
version0.1として一次元の直線運動のダイナミクスを実装.

[Repository](https://github.com/okuma-space/control-and-dynamics-sim/tree/v0.1)

[PR](https://github.com/okuma-space/control-and-dynamics-sim/pull/1)

初期値0でとりあえず横一直線グラフの作成ができていることが確認できた.

###### Figures 
![trajectry](https://okuma-space.github.io/control-and-dynamics-sim/images/generated/v0/linear_motion_result_0.1_.png)


___
___

