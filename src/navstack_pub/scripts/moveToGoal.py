#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def move_to_goal(x, y, z, w, point_number):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    client.send_goal(goal)
    rospy.loginfo("Send point {} successfully".format(point_number))
    client.wait_for_result()
    rospy.loginfo("Done point {}".format(point_number))

if __name__ == '__main__':
    rospy.init_node('auto_nav')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    # waypoints = [(0, 2, 0, 1), (3, 4, 0, 1), (5, 6, 0, 1)]  # Danh sách các điểm (x, y, z, w)
    waypoints = [(0.5, 0.5, 0, 1)]  # Danh sách các điểm (x, y, z, w)

    for idx, point in enumerate(waypoints, start=1):
        move_to_goal(point[0], point[1], point[2], point[3], idx)
    
    rospy.loginfo("All points reached")
    rospy.spin()
