from setuptools import setup, find_packages
from typing import List


HYPEN_E = "-e ."

# def long_description(filename= "README.md"):
#     with open("filename", 'r' , encoding='utf-8') as f:
#         return f.read()

# long_desc = long_description()

def requriements(file_path:str)->list[str]:
    '''
    this function will return a list of lines present in requriements.txt
    '''

    requirement=[]
    with open(file_path) as read_obj:
        requirement = read_obj.readlines()
        requirement= [req.replace("\n", "") for req in requirement]

        if HYPEN_E in requirement:
            requirement.remove(HYPEN_E)

        return requirement
    
          
setup(
    name='mlproject',
    version='0.0.0',
    # long_description=long_desc,
    author="PRASHANT SUNDGE",
    author_email="prashantsundge@gmail.com",
    packages=find_packages(),
    install_requires = requriements('requirements.txt')
)