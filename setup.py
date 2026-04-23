"""패키지 설치 설정"""
from setuptools import setup, find_packages

setup(
    name='auto-readme-gen',
    version='0.1.0',
    description='자동으로 README.md를 생성해주는 도구',
    author='hayoung-929',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'click>=8.0.0',
        'GitPython>=3.1.0',
        'PyGithub>=2.0.0',
        'jinja2>=3.1.0',
    ],
    entry_points={
        'console_scripts': [
            'readme-gen=readme_gen.cli:cli',
        ],
    },
    python_requires='>=3.7',
)