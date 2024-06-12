#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def main():
    rospy.init_node('goal_publisher')
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)

    goal = PoseStamped()
    goal.header.frame_id = "map"  
    goal.header.stamp = rospy.Time.now()
    goal.header.seq = 1
    goal.pose.position.x = 1 
    goal.pose.position.y = 2  
    goal.pose.position.z = 0.0  
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0  # w = 1 represents no rotation

    goal_pub.publish(goal)

    rospy.loginfo("Published goal: x = %f, y = %f", goal.pose.position.x, goal.pose.position.y)

    rospy.sleep(1)
    rospy.spin()

if __name__ == '__main__':
    main()

'''
#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

goals = []

def main():
    rospy.init_node('goal_publisher')
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(1)
    for i in range(5):
        goal = PoseStamped()
        goal.header.frame_id = "map"  
        goal.pose.position.x = i 
        goal.pose.position.y = i * 2  
        goal.pose.position.z = 0.0  
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0  # w = 1 represents no rotation
        goals.append(goal)

    seq_num = 0
    for i in range(len(goals)):
        if rospy.is_shutdown():
            break

        goals[i].header.stamp = rospy.Time.now()
        goals[i].header.seq = seq_num
        seq_num += 1
        goal_pub.publish(goals[i])

        rospy.loginfo("Published goal %d: x = %f, y = %f", i, goals[i].pose.position.x, goals[i].pose.position.y)

        rospy.sleep(1)

if __name__ == '__main__':
    main()

'''