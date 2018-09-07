**mybot_gazebo**: * provides launch files and worlds for easy starting of simulation *

**mybot_description**: * provides the 3D model of the robot and the description of joints and sensors *

**mybot_control** :*configures the ROS interface to our robot’s joints *
---
├── CMakeLists.txt -> /opt/ros/melodic/share/catkin/cmake/toplevel.cmake  
├── darwin_control  
│   ├── CMakeLists.txt  
│   ├── config  
│   │   └── darwin_control.yaml  
│   ├── launch
│   │   └── darwin_control.launch
│   └── package.xml
├── darwin_description
│   ├── CMakeLists.txt
│   ├── meshes
│   │   ├── ankle1_l_coll.stl
│   │   ├── ankle1_l.STL
│   │   ├── ankle1_r_coll.stl
│   │   ├── ankle1_r.STL
│   │   ├── ankle2_l_coll.stl
│   │   ├── ankle2_l.STL
│   │   ├── ankle2_r_coll.stl
│   │   ├── ankle2_r.STL
│   │   ├── arm_high_l_coll.stl
│   │   ├── arm_high_l.STL
│   │   ├── arm_high_r_coll.stl
│   │   ├── arm_high_r.STL
│   │   ├── body_coll.stl
│   │   ├── body.STL
│   │   ├── head_coll.stl
│   │   ├── head.STL
│   │   ├── neck_coll.stl
│   │   ├── neck.STL
│   │   ├── pelvis_l_coll.stl
│   │   ├── pelvis_l.STL
│   │   ├── pelvis_r_coll.stl
│   │   ├── pelvis_r.STL
│   │   ├── shoulder_l_coll.stl
│   │   ├── shoulder_l.STL
│   │   ├── shoulder_r_coll.stl
│   │   ├── shoulder_r.STL
│   │   ├── thigh1_l_coll.stl
│   │   ├── thigh1_l.STL
│   │   ├── thigh1_r_coll.stl
│   │   ├── thigh1_r.STL
│   │   ├── thigh2_l_coll.stl
│   │   ├── thigh2_l.STL
│   │   ├── thigh2_r_coll.stl
│   │   ├── thigh2_r.STL
│   │   ├── tibia_l_coll.stl
│   │   ├── tibia_l.STL
│   │   ├── tibia_r_coll.stl
│   │   └── tibia_r.STL
│   ├── package.xml
│   └── urdf
│       ├── darwin.urdf
│       └── mydarwin.urdf
└── darwin_gazebo
    ├── CMakeLists.txt
    ├── launch
    │   └── darwin_gazebo.launch
    ├── package.xml
    ├── scripts
    │   ├── walker_demo.py
    │   └── walker.py
    ├── setup.py
    └── src
        └── darwin_gazebo
            ├── darwin.py
            ├── darwin.pyc
            └── __init__.py
            
