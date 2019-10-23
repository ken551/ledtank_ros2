package_name = 'ledtank_ros2_examples'
from setuptools import setup
setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'teleop_keyboard',
        'teleop_joystick'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='user',
    author_email="user@todo.todo",
    maintainer='user',
    maintainer_email="user@todo.todo",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_keyboard = teleop_keyboard:main',
            'teleop_joystick = teleop_joystick:main'
        ],
    },
)
