from setuptools import find_packages, setup

install_requires = [
    "python-unsplash==1.1.0",
    "django>=3",
    "wagtail>=2",
]

test_require = [
    "black",
    "flake8",
    "isort",
    "pytest",
    "pytest-django",
]

docs_require = []

setup(
    name="wagtail-stock-images",
    version="0.1.0",
    description="",
    author="R.Moorman <rob@vicktor.nl>",
    install_requires=install_requires,
    extras_require={"test": test_require},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
    ],
)
