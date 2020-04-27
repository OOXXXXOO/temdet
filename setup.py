import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="temdet", # Replace with your own username
    version="0.0.5",
    author="Winshare",
    author_email="tanwenxuan@live.com",
    description="template & nms to do detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OOXXXXOO/temdet.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)