#! /usr/bin/env python3

import roslib
roslib.load_manifest('yolact_ros')
import sys
import os
from pympler.asizeof import asizeof

import rospy

from yolact_ros_msgs.msg import Detections
from yolact_ros_msgs.msg import Detection
from yolact_ros_msgs.msg import Box
from yolact_ros_msgs.msg import Mask

# 640 X 510
class MSG:

  def __init__(self):

    self.detections_sub = rospy.Subscriber('/yolact_ros/detections', 
                                      Detections, self.callback)
    
  def callback(self, msg):

    self.Detections = msg

    # self.header = self.Detections.Header

    number = len(self.Detections.detections)

    for idx in range(0, number):
      
      print(idx+1)

      print(self.Detections.detections[idx].box)

    # self.pa = self.Detections.detections[1]
    
    # parent_n = asizeof(self.pa)

    # self.ch = self.Detections.detections[0]

    # child_n = asizeof(self.ch)

    # print(parent_n / child_n)

    # print('Size: ' + str(asizeof(self.d)))
    
    # print(self.d[1].box)

    # print(self.d)

rospy.init_node('YOLACT MSG')

follower = MSG()

rospy.spin()