from setuptools import setup, find_packages

setup(
    name='doxy-helm',
    version='1.0.10',
    description='Doxy-Helm is a command-line utility designed to streamline the process of creating comprehensive documentation for Helm charts. Helm charts provide a convenient way to package and deploy Kubernetes applications, but documenting their configurations can be time-consuming. Doxy-Helm automates this task by extracting information from Helm charts values files and templates and generating Markdown documentation.',
    author='Yousef Alwaer',
    author_email='elwaeryousef@gmail.com',
    url='https://github.com/tactful-ai/doxy-helm',
    packages=find_packages(),
    install_requires=[
        'argparse',
        'typing',
        'markdown',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'doxy-helm = pkg.runner:full_run'
        ]
    },
)
