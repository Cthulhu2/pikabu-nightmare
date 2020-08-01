import os

from setuptools import setup, Command

__VERSION__ = '0.1'
BASE_PATH = os.path.dirname(os.path.realpath('__file__'))


class ApiCodeGen(Command):
    """generate API server stubs by swagger specs"""
    description = __doc__
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def run():
        import swagger_py_codegen
        swagger_doc = os.path.abspath(BASE_PATH
                                      + '/../../../specs/user-pn-specs-v1.json')
        swagger_py_codegen.generate([
            BASE_PATH,
            '--swagger-doc', swagger_doc,
            '--package', 'users',
            '--templates', 'tornado',
            '--specification',
            '--ui',
            '--validate',
        ])


setup(
    name='users',
    version='0.1',
    description='A useful module',
    packages=['users'],
    setup_requires=['swagger-py-codegen'],
    cmdclass={
        'apiCodeGen': ApiCodeGen,
    },
)
