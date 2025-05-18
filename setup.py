from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='student performance predictor',
    version='0.1.0',
    author='Ashutosh Kumar Yadav',
    author_email='ashutoshkumaryadav040903@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)