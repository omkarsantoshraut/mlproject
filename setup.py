from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This method will return the list of requiremets.
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = [ req.replace('\n', '') for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='omkar',
    author_email='omkar.raut2355@gmail.com',
    packages=find_packages(),
    install_requies=get_requirements('requirements.txt')
)