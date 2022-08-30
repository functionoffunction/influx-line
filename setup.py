from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

version = os.environ.get('VERSION')
DESCRIPTION = 'Influx line protocol builder'

# Setting up
setup(
    name="influx-line",
    version=version,
    author="Oluwatimilehin Akogun",
    author_email="hello@timiakogun.com",
    description=DESCRIPTION,
    py_modules=["influx_line"],
    package_dir={'': 'src'},
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[],
    keywords=['python', 'influx', 'influxdb',
              'line protocol', 'flux', 'influx line protocol'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    }

)
