from setuptools import setup, find_packages

setup(
    name="morse_midi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "midiutil",
    ],
    author="Moudather Chelbi",
    author_email="moudather.chelbi@gmail.com",
    description="A package to convert text to Morse code and then to MIDI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vinerya/morse_midi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)