from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str):
    """Read requirements.txt and return a list of dependencies."""
    with open(file_path) as f:
        requirements = [line.strip() for line in f.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mrs",
    version="0.0.1",
    author="Your Name",
    author_email="you@example.com",
    description="A content-based Movie Recommender System",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)
