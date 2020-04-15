# 【sss】
# https://packaging.python.org/discussions/install-requires-vs-requirements/
# https://stackoverflow.com/questions/46877667/how-to-push-a-new-initial-project-to-github-using-vs-code
# https://github.com/avinassh/rockstar/blob/master/setup.py#L11,#L19

version = '2.0'

setup(
    name='stockspython',
    version=version,
    install_requires=[
        'selenium',
        'lxml'
    ],
    author='Nicholas Langford',
)
