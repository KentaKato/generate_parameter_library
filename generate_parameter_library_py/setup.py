# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

package_name = "generate_parameter_library_py"

setup(
    name=package_name,
    version="0.3.3",
    packages=find_packages(),
    data_files=[
        ("share/" + package_name, ["package.xml"]),
        (
            "share/" + package_name + "/test",
            ["generate_parameter_library_py/test/wrong_default_type.yaml"],
        ),
        (
            "share/" + package_name + "/test",
            ["generate_parameter_library_py/test/missing_type.yaml"],
        ),
        (
            "share/" + package_name + "/test",
            ["generate_parameter_library_py/test/invalid_syntax.yaml"],
        ),
        (
            "share/" + package_name + "/test",
            ["generate_parameter_library_py/test/invalid_parameter_type.yaml"],
        ),
        (
            "share/" + package_name + "/test",
            ["generate_parameter_library_py/test/valid_parameters.yaml"],
        ),
        (
            "share/" + package_name + "/test",
            ["generate_parameter_library_py/test/valid_parameters_with_none_type.yaml"],
        ),
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
    ],
    install_requires=["setuptools", "typeguard", "jinja2"],
    package_data={
        "": [
            "jinja_templates/cpp/declare_parameter",
            "jinja_templates/cpp/set_parameter",
            "jinja_templates/cpp/declare_struct",
            "jinja_templates/cpp/parameter_library_header",
            "jinja_templates/cpp/parameter_validation",
            "jinja_templates/cpp/update_parameter",
            "jinja_templates/cpp/update_runtime_parameter",
            "jinja_templates/cpp/declare_runtime_parameter",
            "jinja_templates/cpp/remove_runtime_parameter",
            "jinja_templates/cpp/set_runtime_parameter",
            "jinja_templates/cpp/set_stack_params",
        ]
    },
    zip_safe=False,
    author="Paul Gesel",
    author_email="paul.gesel@picknik.ai",
    url="https://github.com/PickNikRobotics/generate_parameter_library",
    download_url="https://github.com/PickNikRobotics/generate_parameter_library/releases",
    keywords=["ROS"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD-3-Clause",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    description="Generate the ROS parameter struct in C++ with callbacks for updating.",
    license="BSD-3-Clause",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "generate_parameter_library_cpp = generate_parameter_library_py.generate_cpp_header:main",
            "generate_parameter_library_rst = generate_parameter_library_py.generate_rst:main",
        ],
    },
)
