import os
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():

    init_py = os.path.join(
        os.path.dirname(__file__),
        '{{name}}',
        '__init__.py',
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp',
    'aiohttp_jinja2',
    'trafaret_config',
    'markdown2',
    {% if not without_postgres %}
    'aiopg[sa]',
    'psycopg2-binary',
    'alembic',
    {% endif %}
    {% if redis %}
    'aioredis',
    {% endif %}
    # todo: remove test requirements
    'pytest',
    'pytest-cov',
    'pytest-aiohttp',
]


setup(
    name='{{name}}',
    version=read_version(),
    description='{{name}}',
    platforms=['POSIX'],
    packages=find_packages(),
    package_data={
        '': ['config/*.*']
    },
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
