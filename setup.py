from setuptools import setup, find_packages

setup(
    name="lib-ml",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=[
        "nltk~=3.9.1",
        "numpy~=2.2.5",      
        "pandas~=2.2.3",     
        "scikit-learn~=1.6.1",  
        "joblib~=1.4.2", 
    ],
    python_requires='>=3.10',
)
