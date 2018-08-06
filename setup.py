from setuptools import setup
import os
from subprocess import call

call(["pip3", "install", "git+https://github.com/dpallot/simple-websocket-server.git"])
call(["pip3", "install", "git+https://github.com/giampaolo/psutil.git"])

user = os.listdir("/home")
pth = '/home/' + user[0]

call(["wget", "-P", pth, "https://raw.githubusercontent.com/garatronic/s2-nadhat/master/s2_nadhat/s2_nadhat.js"])

setup(
    name='s2-nadhat',
    version='0.10',
    packages=['s2_nadhat'],

    entry_points={
            'console_scripts': ['s2nadhat = s2_nadhat.s2_nadhat:run_server',
                                'sbx_to_sb2 = s2_nadhat.sbx_to_sb2:sbx_to_sb2'],
        },
    url='https://github.com/garatronic/s2-nadhat',
    license='GNU General Public License v3 (GPLv3)',
    author='Melany Cordova',
    author_email='mcordova@nadhat.com',
    description='Scratch 2 Extension For The Nadhat GSM/GPRS board',
    keywords=['Raspberry Pi', 'Scratch 2', 'Extensions', 'Nadhat', 'SMS'],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Other Environment',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4',
            'Topic :: Education',
            'Topic :: Software Development',
        ],
)
