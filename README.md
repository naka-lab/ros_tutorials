# ros_tutorials
ROSのメッセージ，サービス，アクション，パラメータのサンプル．

## 事前準備
- 自身のPCへソースコードをクローン（ダウンロード）．
```
cd ~/catkin_ws/src
git clone https://github.com/naka-lab/ros_tutorials.git
```

- ROSCOREの起動
```
roscore
```

## メッセージの利用
2つのプログラム間でデータの送受信を行います．（`rosrun`でも実行できますが，わかりやすさを考え`Python`で実行する例になってます．）

- ファイルをデスクトップへコピー
```
cd ~/デスクトップ
cp ~/catkin_ws/src/ros_tutorials/scripts/msg_listener.py ./
cp ~/catkin_ws/src/ros_tutorials/scripts/msg_talker.py ./
```

- 送信側の実行
```
python msg_talker.py 
```

- 受信側の実行
```
python msg_listener.py
```


## サービスの利用

異なるプログラム上に書かれている関数を実行します．

- 関数の定義の確認
```
gedit ~/catkin_ws/src/ros_tutorials/srv/SrvTutrial.srv
```

`a`と`b`が引数で，`result`が戻り値の関数であることを意味しています．

- 関数を外部から実行できるようにするためmake
```
cd ~/catkin_ws/
catkin_make
```

- 関数提供側と実行側のプログラムをデスクトップにコピー
```
cd ~/デスクトップ
cp ~/catkin_ws/src/ros_tutorials/scripts/servise_server.py ./
cp ~/catkin_ws/src/ros_tutorials/scripts/servise_server.py ./
```

- 関数提供側を実行
```
python servise_server.py
```

- 関数実行側を実行
```
python servise_client.py  1 5
```
この例では，関するの引数`a`と`b`にそれぞれ，1と5が渡され，`servise_server.py`上の関するが実行されます．



## アクション

サービスと同様に外部のプログラムの関数を実行するための機能です．ただし，アクションでは，実行の途中経過も送受信することができます．
例えば，ロボットに時間のかかる動作を実行させた場合に，その途中経過を監視するのに利用します．
アクションでは，関数の引数をGoal，戻り値をResult，途中経過をFeedbackと呼び，それぞれの値を代入する型（メッセージ）が定義されています．

- アクションの定義の確認
```
 gedit ~/catkin_ws/src/ros_tutorials/action/ActTutorial.action 
```
`order`が関するの引数（Goal），中断の`sequence`が戻り値（Result），下段の`sequence`が計算途中（Feedback）が入る変数になります．

- 関数提供側と実行側のプログラムをデスクトップにコピー
```
cd ~/デスクトップ
cp ~/catkin_ws/src/ros_tutorials/scripts/act_server.py ./
cp ~/catkin_ws/src/ros_tutorials/scripts/act_client.py ./
```

- 関数の提供側を実行
```
python act_server.py
```

- 関数の実行側を実行
```
python act_client.py 
```
サービスとは異なり，計算の途中経過（Feedback）が送られてきています．

