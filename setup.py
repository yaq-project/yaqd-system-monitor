#!/usr/bin/env python3

"""The setup script."""

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent

with open(here / "yaqd_system_monitor" / "VERSION") as version_file:
    version = version_file.read().strip()


with open("README.md") as readme_file:
    readme = readme_file.read()


requirements = ["yaqd-core", "psutil", "uptime"]

extra_requirements = {"dev": ["black", "pre-commit"]}
extra_files = {"system_monitor": ["VERSION"]}

setup(
    author="yaq developers",
    author_email="blaise@untzag.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    description="Yaq daemon for monitoring system usage.",
    entry_points={
        "console_scripts": [
            "yaqd-system-monitor=yaqd_system_monitor._system_monitor:SystemMonitor.main",
        ],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    license="GNU Lesser General Public License v3 (LGPL)",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data=extra_files,
    keywords="system-monitor",
    name="system-monitor",
    packages=find_packages(include=["yaqd-system-monitor", "yaqd-system-monitor.*"]),
    url="https://gitlab.com/yaq/system-monitor",
    version=version,
    zip_safe=False,
)