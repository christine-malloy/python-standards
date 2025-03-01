from setuptools import setup, find_packages

setup(
    name="python_standards",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here, for example:
        # 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'hello_world = hello_world.main:main',
            'webserver = webserver.main:run',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
