from setuptools import find_packages, setup

install_requires = [
    "python-unsplash==1.1.0",
    "wagtail>=2",
]

tests_requires = [
    "black",
    "coverage",
    "flake8",
    "isort",
    "pytest",
    "pytest-cov",
    "pytest-django",
]

setup(
    name="wagtail-stock-images",
    version="0.1.0",
    description="",
    author="R. Moorman <rob@vicktor.nl>",
    install_requires=install_requires,
    tests_requires=tests_requires,
    extras_require={"test": tests_requires},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
