from setuptools import setup, find_packages

setup(
    name="llm-context-cli",  
    version="0.0.4",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "rich>=10.0.0"
    ],
    entry_points={
        'console_scripts': [
            'llm-context-cli=ai_context.cli:main',
        ],
    },
    author="AtomGradient",
    author_email="alex@atomgradient.com",
    description="A tool to combine multiple files into a single file for AI context",
    long_description="A command-line tool to combine multiple files into a single file formatted for AI context",
    long_description_content_type="text/markdown",
    url="https://github.com/atomgradient/llm-context",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)