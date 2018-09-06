#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/qkx515/ros_darwin/src/darwin_gazebo"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/qkx515/ros_darwin/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/qkx515/ros_darwin/install/lib/python2.7/dist-packages:/home/qkx515/ros_darwin/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/qkx515/ros_darwin/build" \
    "/usr/bin/python2" \
    "/home/qkx515/ros_darwin/src/darwin_gazebo/setup.py" \
    build --build-base "/home/qkx515/ros_darwin/build/darwin_gazebo" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/qkx515/ros_darwin/install" --install-scripts="/home/qkx515/ros_darwin/install/bin"
