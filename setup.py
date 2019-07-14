import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='own-blockchain-sdk',
    version='1.0',
    author="Marian Gheorghe",
    author_email="marian.gheorghe@weown.com",
    description="Own Blockchain SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OwnMarket/OwnBlockchainSdkPython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
