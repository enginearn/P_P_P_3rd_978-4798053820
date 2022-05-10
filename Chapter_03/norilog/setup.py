# import os
from setuptools import setup, find_packages

#####サンプルとして追記######
# def read_file(filename):
#     basepath = os.path.dirname(os.path.dirname(__file__))
#     filepath = os.path.join(basepath, filename)
#     if os.path.exists(filepath):
#         return open(filepath).read()
#     else:
#         return ""
############################
setup(
    name="norilog",
    version="1.0.0",
    # description="The Norilog Appkication",
    # long_description=read_file("README.rst"),
    # author="your name",
    # author_email="your email address",
    # url="https://github.com/your_account/norilog/",
    # classifiers=[
    #     "Development Status :: 4 - Beta",
    #     "Framework :: Flask",
    #     "License :: OSI Approved :: BSD License",
    #     "Programming Language :: Python",
    #     "Programming Language :: Python :: 3.10",
    # ], 
    packages=find_packages(),
    include_package_data=True,
    # keywords=["web", "norilog"],
    # license="BSD License",
    install_requires=[
        "flask",
        ],
    # bottleを使うなら以下のように書き換える
    # install_requires=[
    #     "bottle",
    #     ],
        entry_points="""
        [console_scripts]
        norilog = norilog:main
        """,
    )
