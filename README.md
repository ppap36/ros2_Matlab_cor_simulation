# ros2 + Matlab simulation
 ### 3.1 设计思路

直接基于 `sl_drivepoint` 模型，订阅机器人的 `/neor_foxy_mini/pose`坐标信息 `xy`，将其作为反馈信息求出前轮偏转角 `gamma`和速度 `v`（两个公式），发布一个自己的topic节点 `sim_akm_topic`  ( `AckermannDrive`类型的信息)，自己在wsl写一个订阅节点，订阅 `sim_akm_topic`并将信息转化为 `AckermannDriveStamp`类型发布给 `/neor_foxy_mini/cmd_ackermann`话题

<aside>
💡 这里应该可以在Simulink中直接发送AckermannDrive

</aside>

### 3.2 simulink模型
![Untitled (1)](https://github.com/ppap36/ros2_Matlab_cor_simulation/assets/108739132/2e9325d2-141e-41e7-9e9f-64ccc9ee7db0)



### 3.3 仿真流程以及仿真结果

**S1** 在matlab界面用ros2genmsg()加入ackermann_msgs_master中的AckermannDrive.msg

使用教程：

[Generate custom messages from ROS 2 definitions - MATLAB ros2genmsg
- MathWorks 中国](https://ww2.mathworks.cn/help/ros/ref/ros2genmsg.html)

**S2** 在wsl中
（1）终端1中打开empty_world

```bash
cd neor_mini/sim_20_ws
source install/setup.bash
ros2 launch neor_mini_foxy neor_mini_gazebo.launch.py world:=empty
```

（2）终端2打开中介节点

```matlab
cd akm/akm_ws
source install/setup.bash
ros2 run ackermann_interface akm_topic
```

**S3** 在simulink中，打开drpoint.slxc，配置好ros2之后运行

仿真结果：

![Untitled (2)](https://github.com/ppap36/ros2_Matlab_cor_simulation/assets/108739132/0a1d743b-0cd1-468b-98da-24eb9d9b4c84)


小车到达了(5,5)的位置并停止
