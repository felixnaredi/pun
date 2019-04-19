import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pun-felixnaredi",
    version="0.0.1",
    author="Felix Naredi",
    author_email="felixnaredi@gmail.com",
    description="A game where you play as a snake",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felixnaredi/pun",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Simplified BSD License",
        "Operating System :: MacOS"
    ]
)