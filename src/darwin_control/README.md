**darwin_control**: *configures the ROS interface to our robot’s joints controller*

```

darwin_control  
  ├── CMakeLists.txt              //  No use at all. But don't delete it, because it is created when using catkin_create_pkg.
  ├── config  
  │   └── darwin_control.yaml     //  Defines what controllers we are using, and which joints they are controlling.
  ├── launch  
  │   └── darwin_control.launch   //  Load joint controller configurations from darwin_control.yaml to parameter server (rosparam for yaml)
  │                                   Load the controllers from parameter server using controller_manager spawner
  |                                   convert joint states to TF transforms for rviz, etc
  |                                   This file will be included by darwin_gazebo/launch/darwin_gazebo.launch
  |
  └── package.xml                 //  Contains some metadata describing the package, which will not be utilized by ros,
                                      neither at build time or run time. It is there mainly for the spirit of keeping 
                                      documentation in sync with actual functionality.

```
