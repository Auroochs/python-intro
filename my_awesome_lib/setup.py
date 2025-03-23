from setuptools import setup, find_packages

setup(
    name="my_awesome_lib",
    version="0.1.0",
    packages=find_packages(),
    description="Biblioteka z funkcjami do obsługi danych, obliczeń matematycznych oraz przetwarzania tekstu.",
    author="Michał Tur",
    url="https://github.com/Auroochs/my-awesome-lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
