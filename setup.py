from setuptools import find_packages,setup
from typing import List
HYPHEN_DOT = '-e .'
def get_req(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements
    
setup(
    name="mlproject",
    version="0.0.1",
    author="Muhammad Zuhair",
    author_email="zuhair.zaidi407@gmail.com",
    packages=find_packages(),
    install_requires=get_req("requirements.txt")
)