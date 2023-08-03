#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np
import timeit

from cv_bridge import CvBridge

rospy.init_node('image_publishing', anonymous=True)

image_pub = rospy.Publisher("/camera/color/image_raw", Image, queue_size=10)

cv_image = cv2.imread("input_image.png")

bridge = CvBridge()

while not rospy.is_shutdown():

    # cv2.imshow("im", cv_image)

    # key = cv2.waitKey(0)

    # if key == 27:

    #     cv2.destroyAllWindows()

    image_pub.publish(bridge.cv2_to_imgmsg(cv_image, "bgr8"))

