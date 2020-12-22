import os
import subprocess
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
    libraries = ['pinproc', 'libftd2xx']
else:
    # Linux
    libraries = ['libusb', 'libftdi1', 'pinproc']

def pkgconfig(package, kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = subprocess.getoutput(
        'pkg-config --cflags --libs {}'.format(package))
    for token in output.strip().split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

kw = {}
for library in libraries:
    kw = pkgconfig(library, kw)


module1 = Extension("pinproc",
                    extra_compile_args=extra_compile_args,
                    extra_link_args=extra_link_args,
                    sources=['pypinproc.cpp', 'dmdutil.cpp', 'dmd.c'],
                    **kw
                    )

setup(
        name="pypinproc",
        version="3.0",

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
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Topic :: Games/Entertainment :: Arcade',
            'Topic :: System :: Hardware :: Hardware Drivers'
        ],

        ext_modules=[module1])
