#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <vector>

int main(int argc, char** argv) {
    // Initialize the ROS node
    ros::init(argc, argv, "goal_publisher");
    ros::NodeHandle nh;

    // Create a publisher object
    ros::Publisher goal_pub = nh.advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal", 10);

    // Define a vector of goals
    std::vector<geometry_msgs::PoseStamped> goals;

    // Create and populate goals
    for (int i = 0; i < 5; ++i) {
        geometry_msgs::PoseStamped goal;
        goal.header.frame_id = "map"; // Change this as per your reference frame
        goal.pose.position.x = i; // Replace with desired x coordinate
        goal.pose.position.y = i * 2; // Replace with desired y coordinate
        goal.pose.position.z = 0.0; // z is usually 0 for 2D navigation
        goal.pose.orientation.x = 0.0;
        goal.pose.orientation.y = 0.0;
        goal.pose.orientation.z = 0.0;
        goal.pose.orientation.w = 1.0; // w=1 represents no rotation
        goals.push_back(goal);
    }

    // Set the loop rate (1 Hz)
    ros::Rate loop_rate(1);

    // Publish each goal in the list
    for (size_t i = 0; i < goals.size() && ros::ok(); ++i) {
        // Update the header timestamp
        goals[i].header.stamp = ros::Time::now();

        // Publish the goal
        goal_pub.publish(goals[i]);

        // Log the published message
        ROS_INFO("Published goal %lu: x=%f, y=%f", i + 1, goals[i].pose.position.x, goals[i].pose.position.y);

        // Spin and sleep to maintain the loop rate
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
