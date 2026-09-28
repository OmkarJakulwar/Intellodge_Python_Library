from setuptools import setup, find_packages

setup(
    name="intellodge_core",
    version="1.0.0",
    author="IntellLodge Omi",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "python-jose",
        "pytz",
        "django"
    ],
    description="Reusable core utilities for IntellLodge platform",
)
