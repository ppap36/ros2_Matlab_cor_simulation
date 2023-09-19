import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import String

class simulink_subscribe(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info('simulink监听节点已启动！')
        self.sim_sub = self.create_subscription(AckermannDrive,'sim_akm_topic',self.sim_sub_callback,10)
        self.get_logger().info('robot发布节点已启动！')
        self.robot_pub = self.create_publisher(AckermannDriveStamped,'/neor_mini_foxy/cmd_ackermann',10)
        self.timer = self.create_timer(0.5,self.timer_callback)
        self.akm_msg = AckermannDrive()
    def sim_sub_callback(self,msg):
        self.akm_msg = msg
        self.get_logger().info(f'收到角度信息{msg.steering_angle}')
        self.get_logger().info(f'收到速度信息{msg.speed}')
    def timer_callback(self):
        akm_msg_stm = AckermannDriveStamped()
        akm_msg_stm.drive.steering_angle = self.akm_msg.steering_angle
        akm_msg_stm.drive.speed = self.akm_msg.speed
        self.robot_pub.publish(akm_msg_stm)
        self.get_logger().info(f'发布了指令，角度为{akm_msg_stm.drive.steering_angle}，速度为{akm_msg_stm.drive.speed}')
def main(args=None):
    rclpy.init(args=args)
    node = simulink_subscribe('simulink_subscribe')
    rclpy.spin(node)
    rclpy.shutdown()