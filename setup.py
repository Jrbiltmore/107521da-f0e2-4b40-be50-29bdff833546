from setuptools import setup, find_packages

setup(
    name="e-ic2",
    version="0.1.0",
    author="Jacob Thomas Redmond",
    author_email="vespersinc@icloud.com",
    description="A package for simulating quantum phonon interactions in lattice systems",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jrbiltmore/e-ic2n",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "matplotlib",  # if you use plotting functions
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
