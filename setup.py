from setuptools import find_packages, setup


setup(
    name="me-results-viz",
    version="0.1.0",
    license="",
    description="Code to display a visualisation of ME results with significance.",
    packages=find_packages('src'),
    package_dir={"": "src"},
    author="Matt Crooks",
)
