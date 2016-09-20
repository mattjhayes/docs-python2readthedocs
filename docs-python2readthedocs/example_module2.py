#!/usr/bin/python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is a second example Python module for the Python to Read the Docs
documentation repository.

It is used to show how Read the Docs can be configured to install
dependant modules so that Sphinx autodoc can run

Written by Matthew John Hayes
"""

#*** Logging imports (don't need install):
import logging
import logging.handlers

#*** Lets import coloredlogs. It's cool, and it will cause build on
#*** Read the Docs to fail unless we've set it up properly (to prove
#*** the point):
import coloredlogs

class ExampleModule2(object):
    """
    This is the main class of example_module2
    """
    def __init__(self):
        """
        Initialise the ExampleModule2 class
        """
        #*** Set up logging:
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        #*** Go coloredlogs:
        coloredlogs.install(level="DEBUG",
                logger=self.logger,
                fmt="%(asctime)s.%(msecs)03d %(name)s[%(process)d] " \
                "%(funcName)s %(levelname)s %(message)s", datefmt='%H:%M:%S')
        #*** Initialise our class variable:
        self.class_variable = 1

    def run(self):
        """
        Run the ExampleModule2 instance
        """
        self.logger.info("ExampleModule2 is running!")
        self.logger.debug("Class Variable is %s", self.class_variable)
        self.increment(5)
        self.logger.debug("Class Variable is %s", self.class_variable)

    def increment(self, value):
        """
        Increment the value of self.class_variable by value passed
        to this method
        """
        self.class_variable += value

    def _private_method(self):
        """
        Example private method that won't be documented by autodoc
        unless you add :private-members: to the automodule directive
        """
        self.class_variable += 1

if __name__ == '__main__':
    #*** Instantiate the ExampleModule2 class:
    example_module2 = ExampleModule2()
    #*** Start ExampleModule:
    example_module2.run()
