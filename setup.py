import os
from setuptools import setup, Extension

extra_compile_args = ['-O0', '-g']
extra_compile_args.append('-Wno-write-strings')  # fix "warning: deprecated conversion from string constant to 'char*'"
extra_link_args = []

# To use the ARCH flag simply:
#   ARCH=x86_64 python setup.py build
if 'ARCH' in os.environ:
    extra_compile_args += ['-arch', os.environ['ARCH']]
    extra_link_args += ['-arch', os.environ['ARCH']]

if os.name == 'nt':
    # Windows
    libraries = ['pinproc', 'ftd2xx']
else:
    # Linux
    libraries = ['usb', 'ftdi1', 'pinproc']

module1 = Extension("pinproc",
                    include_dirs=['../libpinproc/include'],
                    libraries=libraries,
                    library_dirs=['/usr/local/lib', '../libpinproc/bin'],
                    extra_compile_args=extra_compile_args,
                    extra_link_args=extra_link_args,
                    sources=['pypinproc.cpp', 'dmdutil.cpp', 'dmd.c'])

setup(
        name="pypinproc",
        version="2.2",

        description='Python wrapper for libpinproc',
        long_description='''pypinproc is a native Python extension exposing the
        libpinproc API to Python programs. pypinproc provides a low-level
        interface for controlling a Multimorphic P-ROC or P3-ROC (http://www.pinballcontrollers.com/)
        Pinball Remote Operations Controller from Python.

        Note that Python wheels include libpinproc as well. Building manually
        requires that you build and install libpinproc first.''',

        url='http://www.pinballcontrollers.com/forum/index.php?board=10.0',
        author='Adam Preble, Gerry Stellenberg, & the home brew pinball '
               'community',
        author_email='brian@missionpinball.com',
        license='MIT',

        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Topic :: Games/Entertainment :: Arcade',
            'Topic :: System :: Hardware :: Hardware Drivers'
        ],

        ext_modules=[module1])
