from setuptools import setup, find_namespace_packages

setup(
    name="render-log-ui",
    description="""A log viewer for render logs by Qt.""",
    url="https://github.com/bigly87/render_log_viewer",
    author="Omid Taherdin",
    author_email="m.taherdin@gmail.com",
    license="",
    packages=find_namespace_packages(),
    install_requires=["setuptools>=40.2.0", "PySide2"],
    extras_require={"dev": ["black"]},
    include_package_data=True,
)