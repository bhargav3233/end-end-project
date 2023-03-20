from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file:
        for line in file:
            if line.startswith("-e"):
                continue
            requirements.append(line.strip())

    return requirements


setup(
    name='end-end project',
    version='0.0.1',
    author='Bhargav',
    author_email='bhargavnagireddy@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
