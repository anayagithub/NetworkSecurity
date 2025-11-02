from setuptools import find_packages,setup
from typing import List


def get_requirememts()->List[str]:
    '''
    This function will return list of requirements
    This function will read requirements.txt
    '''
    
    requirememt_lst:List[str]=[]
    
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirememt=line.strip()
                # ignore empty lines and -e .
                if requirememt and requirememt!='-e .':
                    requirememt_lst.append(requirememt)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
                     
    return requirememt_lst

setup(
    name="NetworSecurity",
    version='0.0.1',
    author="Anaya Jain",
    author_email="anayajain1009@gmail.com",
    packages=find_packages(),
    install_requires=get_requirememts()
)