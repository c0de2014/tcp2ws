#!/usr/bin/env python
import roslib; #roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)


def listener():
    rospy.init_node('roslistennonrospublisher', anonymous=True)
    rospy.Subscriber("nonroschatter", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
