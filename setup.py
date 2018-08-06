from setuptools import setup, find_packages

install_requires = ['torch>=0.4.0', 'Pillow']

setup(
    name='CVdevKit',
    version='1.0.0.dev1',
    description='A development kit for Computer Vision',
    url='https://github.com/JiaminRen/CVdevKit.git',
    author='Jiamin Ren',
    author_email='jarman.ren@gmail.com',
    license='Apache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Computer Vision',
    packages=find_packages(),
    install_requires=install_requires,
)