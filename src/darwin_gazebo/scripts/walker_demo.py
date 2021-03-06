#!/usr/bin/env python
import rospy
from darwin_def_pkg.darwin_def import Darwin

if __name__=="__main__":
    rospy.init_node("walker_demo")

    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)

    rospy.loginfo("Darwin Walker Demo Starting")

    darwin.set_walk_velocity(0.2,0,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(1,0,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(0,1,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(0,-1,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(-1,0,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(1,1,0)
    rospy.sleep(5)
    darwin.set_walk_velocity(0,0,0)

    rospy.loginfo("Darwin Walker Demo Finished")
