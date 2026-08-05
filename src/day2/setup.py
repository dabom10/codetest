from setuptools import find_packages, setup

package_name = 'day2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mu-08',
    maintainer_email='dabom425@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'image_publisher = day2.2_0_a_image_publisher:main',
            'image_subscriber = day2.2_0_b_image_subscriber:main',
            'data_publisher = day2.2_0_c_data_publisher:main',
            'data_subscriber = day2.2_0_d_data_subscriber:main',

            'capture_wc_image = day2.2_1_a_capture_wc_image:main',
            'cont_capture_wc_image = day2.2_1_b_cont_capture_wc_image:main',
            'capture_wc_thread = day2.2_1_c_capture_wc_thread:main',
            'capture_image = day2.2_1_d_capture_image:main',
            'capture_comp_image = day2.2_1_e_capture_comp_image:main',
            'cont_capture_image = day2.2_1_f_cont_capture_image:main',

            'yolov8_obj_det_wc = day2.2_4_d_yolov8_obj_det_wc:main',
            'yolo_publisher_wc = day2.2_4_e_yolo_publisher_wc:main',
            'yolo_subscriber_wc = day2.2_4_f_yolo_subscriber_wc:main',

            'yolov8_obj_det = day2.2_4_g_yolov8_obj_det:main',
            'yolov8_obj_det_thread = day2.2_4_h_yolov8_obj_det_thread:main',
            'yolov8_obj_det_track = day2.2_4_i_yolov8_obj_det_track:main',
        ],
    },
)
