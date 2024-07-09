from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open("requirements.txt") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    name="MLProject1",
    version="0.0.1",
    author="parth",
    author_email="parthraheja1205@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)
