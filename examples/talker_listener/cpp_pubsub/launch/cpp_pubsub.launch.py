from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription ([

        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='cpp_pubsub', node_executable='talker', output='screen', emulate_tty=True),

        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='cpp_pubsub', node_executable='listener', output='screen', emulate_tty=True),
    ])
