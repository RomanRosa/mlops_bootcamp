from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

    


setup(

    name='divorce_predictor',
    version='0.0.1',
    author='Francisco Roman Peña de la Rosa',
    author_email='mldevops2@gmail.com',
    url='https://github.com/RomanRosa/mlops_bootcamp',
    description='Divorce Predictor',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)