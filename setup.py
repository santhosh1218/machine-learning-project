from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filepath)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
       requirements=file_obj.readlines()
       requirements=[req.replace('\n','') for req in requirements] 
       if HYPEN_E_DOT in requirements:
          requirements.remove(HYPEN_E_DOT)
    return requirements

setup(

    name='machinelearning project',
    version='0.0.1',
    author='santhosh',
    author_email='santhoshkommula98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)