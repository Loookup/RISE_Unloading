#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge
import os

class Camera:

  def __init__(self):

    self.bridge = cv_bridge.CvBridge()

    self.image_sub = rospy.Subscriber('/yolact_ros/visualization', 
                                      Image, self.image_callback)
    
  def image_callback(self, msg):

    image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')

    # print(image.shape[:2])

    cv2.namedWindow("window", 1)

    cv2.imshow("window", image)

    key= cv2.waitKey(0)

    if key == 27:

      cv2.destroyAllWindows()

      print("---end---")

      os._exit(1)

rospy.init_node('Spaceshuttle_camera')

follower = Camera()

rospy.spin()