from __future__ import print_function
from setuptools import setup, find_packages
import pytorch_quant_tool

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="pytorch_quant_tool",
    version=pytorch_quant_tool.__version__,
    author="Jiazhen Lin",
    author_email="neolunsu@gmail.com",
    description="An experimental neural network quantization environment in Pytorch.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/neolinsu/pytorch_quant_tool",
    packages=find_packages(),
    install_requires=[
        "pytorch == 1.3.1",
        ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
