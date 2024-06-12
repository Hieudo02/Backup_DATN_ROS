#!/bin/bash

# Function to check if roscore is running
check() {
    rostopic list > /dev/null 2>&1
    return $?
}

# Clean log
yes | rosclean purge

# ------------ Open FIRST TERMINAL ------------
# gnome-terminal -- bash -c
# --geometry=COLUMNSxROWS+X+Y

#gnome-terminal --geometry=80x24+800+580 -- bash -c "export ROS_MASTER_URI=http://$(hostname -I | awk '{print $1}'):11311; \
                           #export ROS_IP=$(hostname -I | awk '{print $1}'); \
                           #cd ~/datn_navbot; \
                           #source devel/setup.bash; \
                           #rosrun navstack_pub custom_teleop_twist_keyboard.py; \
                           #exec bash"
# Wait for teleop to start
#echo "Waiting for teleop to fully start..."
#until check; do
    #sleep 1
#done
#echo "teleop is active."

# ------------ Open SECOND TERMINAL ------------
#gnome-terminal --geometry=80x24+50+580 -- bash -c "cd ~/datn_navbot/ && \
                           #source devel/setup.bash && \
                           #roslaunch navstack_pub load_map.launch map_name:="$1"; \
                           #exec bash" 
# Wait for load map
#echo "Waiting for loading map..."
#until check; do
    #sleep 1
#done
#echo "map loaded."
               
# ------------ Current TERMINAL ------------
gnome-terminal -- bash -c "cd ~/datn_navbot/ && \
                           source devel/setup.bash && \
                           roslaunch navstack_pub navbot.launch map_name:="$1"; \
                           exec bash"                 
#cd ~/datn_navbot/
#source devel/setup.bash
#roslaunch navstack_pub navbot.launch
#roslaunch navstack_pub map_generate.launch


