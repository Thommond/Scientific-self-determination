import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Scientific-Self-Determination"
    version="0.0.1",
    author="Thom Mondeaux, Joe Pekarek",
    author_email="Thommond@protonmail.com",
    url="https://github.com/Thommond/Scientific-Self-Determination",
    description="A website/wiki for SSD and how it could be implemented on political levels.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'psycopg2', 'gunicorn'],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
