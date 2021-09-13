from setuptools import setup, find_packages
import re


with open("README.md", "r") as f:
    long_description = f.read()


with open("firi/__init__.py") as f:
    version = re.search(
        r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE
    ).group(1)


setup(
    name="firi",
    version=version,
    author="offish",
    author_email="overutilization@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/offish/firi",
    download_url="https://github.com/offish/firi/tarball/v" + version,
    packages=["firi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
)