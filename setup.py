import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithms-shritwik",
    version="0.0.2",
    author="shritwik bhaduri",
    author_email="sritwikbhaduri@outlook.com",
    description="contain code for algorithms specified in CLRS text book",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shritwikbhaduri/algorithms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
