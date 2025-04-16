from setuptools import setup, find_packages

setup(
    name='autoprivrecon',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'rich',
        'paramiko'
    ],
    entry_points={
        'console_scripts': [
            'autoprivrecon=autoprivrecon:main',
        ],
    },
    author='@DarwinTusarma & @R4c0d3',
    description='Automated Privilege Escalation & Bypass Recon Tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Security :: Information Analysis',
    ],
)
