#!/usr/bin/env python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wallex-python",
    version="0.0.6",
    author="Pourya Moghadam",
    author_email="p.moghadam@msn.com",
    description="Wallex Exchange Unofficial API Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wallexchange/wallex-python",
    license="MIT",
    keywords='wallex crypto exchange api bitcoin ethereum btc eth python',
    install_requires=[
        'requests==2.28.1',
        'pydantic==1.9.2'
    ],
    project_urls={
        "Bug Tracker": "https://github.com/wallexchange/wallex-python/issues",
        "Documentation": "https://api-docs.wallex.ir/",
        "repository": "https://github.com/wallexchange/wallex-python"
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
