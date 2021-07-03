from setuptools import setup, Extension
from setuptools import find_packages
import os

with open("README.md", 'r') as f:
    long_description = f.read()

DESCRIPTION = "With the help of this script, create CMake supported conan template empty structure."

# Remove this whole block from here...
setup(
        name='template-maker',
        version='0.0.1',
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        author='Sheik S Shajeen Ahamed',
        author_email='shajeenahmed@gmail.com',
        license="GPL-3.0",
        url="https://github.com/shajeen/template-maker",
        project_urls={
            "Bug Tracker": "https://github.com/shajeen/template-maker/issues",
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[],
        packages=['template_maker'],
        entry_points={
                'console_scripts': [
                    'template-maker=template_maker.main:main',
                ],
        },
        long_description=long_description,
        include_package_data=True,
        package_data={"": "configuration/*.json"}
)
