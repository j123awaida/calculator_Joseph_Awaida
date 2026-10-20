"""PyBuilder configuration for Lab 6."""
from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "calculator_Joseph_Awaida"
version = "1.0.0"
default_task = "publish"
summary = "Lab 6 calculator with automated tests and packaging"
author = "Joseph Awaida"
license = "Proprietary"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Joseph_Awaida",
    )
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("dir_target", "target")
    project.set_property("distutils_readme_description", True)
    project.set_property("distutils_readme_file", "README.md")
