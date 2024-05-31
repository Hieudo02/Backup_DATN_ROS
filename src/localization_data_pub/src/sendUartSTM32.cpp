#include "ros/ros.h"
#include <iostream>
#include <string>
#include <chrono>
#include <thread>
#include <serial/serial.h>

int main() {
    serial::Serial ser("/dev/ttyUSB0", 115200, serial::Timeout::simpleTimeout(100));
    if (!ser.isOpen()) {
        std::cerr << "Không thể kết nối với cổng serial." << std::endl;
        return 1;
    }

    std::cout << "Chay chuong trinh" << std::endl;

    float testVelR = 1.23;
    float testVelL = 2.54;

    try {
        while (true) {
            // Receive
            if (ser.available()) { // Kiểm tra xem có dữ liệu đến không
                std::string c = ser.read(ser.available());

                // ROS_INFO("Character read: %s", c.c_str());
                size_t r_pos = c.find('r');
                size_t l_pos = c.find('l');

                // Extract the substrings before and after 'r'
                std::string first_number = c.substr(0, r_pos);
                std::string second_number = c.substr(r_pos + 1, l_pos - r_pos - 1);

                std::string s = first_number + " " + second_number;
                ROS_INFO("%s", s.c_str());
            }

            // Transmit
            std::string message = std::to_string(testVelR) + "r" + std::to_string(testVelL) + "l";
            ser.write(message);
            ser.flush(); // Xóa bộ nhớ đệm
            std::this_thread::sleep_for(std::chrono::milliseconds(1000)); // Add a delay of 1000 milliseconds
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    } catch (...) {
        std::cerr << "Undefined Error" << std::endl;
    }

    return 0;
}
