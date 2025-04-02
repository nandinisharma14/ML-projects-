from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a given file.
    """
    requirements = []
    with open(file_path, "r", encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Removes newline properly

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',  # Corrected version format
    author='Nandini',
    author_email='sharmanandini0914@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)