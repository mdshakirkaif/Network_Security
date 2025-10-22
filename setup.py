from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    '''This function returns list of requirements'''
    
    try:
        requirements_list:List[str]=[]
        with open('requirements.txt','rb') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement in requirement!='-e .':
                    requirements_list.append(requirement)
                
        
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirements_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="mohd shakir kaif",
    author_email='mdshakirkaif07@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements()
)