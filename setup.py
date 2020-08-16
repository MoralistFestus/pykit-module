import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pykit",
    version="0.1",
    author="Moralist Festus",
    author_email="moralistfestus@gmail.com",
    tests_require=["pytest"],
    py_modules=["pykit"],
    description="Easy programming Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MoralistFestus/pykit",
    keywords=['list, turple, dictionary, tools, module, pk, pykit']
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        # Indicates who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

    ],
    python_requires='>=3.6, <4',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/MoralistFestus/pykit/issues',
        'Source': 'https://github.com/MoralistFestus/pykit/',
    },
)
