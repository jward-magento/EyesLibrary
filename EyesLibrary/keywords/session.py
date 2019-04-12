#!/usr/bin/env python

import os
import httplib
import base64
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from applitools import logger
from applitools.logger import StdoutLogger
from applitools.logger import FileLogger
from applitools.geometry import Region
from applitools.eyes import Eyes, BatchInfo
from applitools.selenium.webelement import EyesWebElement
from applitools.selenium.positioning import StitchMode
from robot.api import logger as loggerRobot

from EyesLibrary.resources import utils, variables


class SessionKeywords(object):

    library_arguments = {}

    def open_eyes_session(
        self,
        apikey=None,
        appname=None,
        testname=None,
        library=None,
        width=None,
        height=None,
        osname=None,
        browsername=None,
        matchlevel=None,
        enable_eyes_log=None,
        enable_http_debug_log=None,
        baselinename=None,
        batchname=None,
        branchname=None,
        parentbranch=None,
        serverurl=None,
        force_full_page_screenshot=None,
        stitchmode=None,
        matchtimeout=None,
        hidescrollbars=None,
        save_new_tests=None,
        wait_before_screenshots=None,
        send_dom=None,
        stitchcontent=False,
    ):
        """
        Starts a session with Applitools.

        Some of the following arguments may also be defined on library import.
        See `Before running tests` or `Importing`.

            | =Arguments=                       | =Description=                                                                                                                            |
            | API Key (str)                     | *Mandatory* - User's Applitools Eyes key                                                                                                 |
            | Application Name (str)            | *Mandatory* - The name of the application under test                                                                                     |
            | Test Name (str)                   | *Mandatory* - The test name                                                                                                              |  
            | Library (str)                     | Library to test (Either SeleniumLibrary or AppiumLibrary)                                                                                |
            | Width (int)                       | The width of the browser window e.g. 1280                                                                                                |
            | Height (int)                      | The height of the browser window e.g. 1000                                                                                               |
            | Operating System (str)            | The operating system of the test, can be used to override the OS name to allow cross OS verification                                     |
            | Browser Name (str)                | The browser name for the test, can be used to override the browser name to allow cross browser verification                              |
            | Match Level (str)                 | The match level for the comparison of this session's tests - can be STRICT, LAYOUT, CONTENT or EXACT                                     |
            | Enable Eyes Log (bool)            | Determines if the trace logs of Applitools Eyes SDK are activated for this session                                                       |
            | Enable HTTP Debug Log (bool)      | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                            |
            | Baseline Name (str)               | Name of the branch where the baseline reference will be taken from and where new and accepted steps will be saved to                     |
            | Batch Name (str)                  | The name of the batch                                                                                                                    |
            | Branch Name (str)                 | The branch to use to check test                                                                                                          |
            | Parent Branch (str)               | Parent Branch to base the new Branch on                                                                                                  |
            | Server URL (str)                  | The URL of the Eyes server. If not provided then your test will run on the public cloud                                                  |
            | Force Full Page Screenshot (bool) | Will force the browser to take a screenshot of whole page                                                                                |
            | Stitch Mode (str)                 | Type of stitching used for full page screenshots - can be CSS or SCROLL                                                                  |
            | Match Timeout (int)               | Determines how much time in milliseconds Eyes continues to retry the matching before declaring a mismatch on this session's tests        |
            | Hide Scrollbars (bool)            | Sets if the scrollbars are hidden this session's tests, by passing 'True' or 'False' in the variable                                     |
            | Save New Tests (bool)             | Sets if the new tests on this session are automatically accepted, by passing 'True' or 'False' in the variable                           |
            | Wait Before Screenshots (int)     | Determines the number of milliseconds that Eyes will wait before capturing a screenshot on this sessions's tests                         |
            | Send DOM (bool)                   | Sets if DOM information should be sent for this session's checkpoints                                                                    |    
            | Stitch Content (bool)             | If this session test's elements/region are scrollable, determines if Eyes will scroll this them to take a full region/element screenshot |    

        *Mandatory Arguments:* They may be defined through this keyword, or when importing the library.
        In order to run a test, provide at least the API Key, Application Name and Test Name.

        Creates an instance of the AppiumLibrary or SeleniumLibrary webdriver, given the library argument.

        Defines a global driver and sets it to the webdriver found.

        Checks if there has been a width or height value passed in.
        If there no are values passed in, eyes calls the method open without the width and height values.
        Otherwise, Eyes calls open with the width and height values defined.
 
        *Note:* When opening the session on a mobile browser or hybrid app, the context must be set to WEBVIEW in order to retrieve the correct viewport size. Geolocation of the device may have to be set after switching context.

        *Example:*                                                                                                                                                                                                                               
            | Open Eyes Session | YourApplitoolsKey | AppName | TestName | SeleniumLibrary | 1024 | 768 | OSOverrideName | BrowserOverrideName | layout | ${true} | batchname=BatchName | serverurl=https://myserver.com |
        """

        if appname is None:
            appname = self.library_arguments["appname"]
        if testname is None:
            testname = self.library_arguments["testname"]
        if apikey is None:
            apikey = self.library_arguments["apikey"]
        if library is None:
            library = self.library_arguments["library"]
        if osname is None:
            osname = self.library_arguments["osname"]
        if browsername is None:
            browsername = self.library_arguments["browsername"]
        if matchlevel is None:
            matchlevel = self.library_arguments["matchlevel"]
        if enable_eyes_log is None:
            enable_eyes_log = self.library_arguments["enable_eyes_log"]
        if serverurl is None:
            serverurl = self.library_arguments["serverurl"]
        if save_new_tests is None:
            save_new_tests = self.library_arguments["save_new_tests"]
        if matchtimeout is None:
            matchtimeout = self.library_arguments["matchtimeout"]

        if serverurl is None:
            variables.eyes = Eyes()
        else:
            variables.eyes = Eyes(serverurl)

        variables.eyes.api_key = apikey

        try:
            libraryInstance = BuiltIn().get_library_instance(library)

            if library == "AppiumLibrary":
                driver = libraryInstance._current_application()
            else:
                driver = libraryInstance._current_browser()
        except RuntimeError:
            raise Exception("%s instance not found" % library)

        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        if osname is not None:
            variables.eyes.host_os = osname
        if browsername is not None:
            variables.eyes.host_app = browsername
        if baselinename is not None:
            variables.eyes.baseline_branch_name = baselinename
        if batchname is not None:
            if variables.batch is None or variables.batch.name != batchname:
                variables.batch = BatchInfo(batchname)
            variables.eyes.batch = variables.batch
        if matchlevel is not None:
            variables.eyes.match_level = utils.get_match_level(matchlevel)
        if parentbranch is not None:
            variables.eyes.parent_branch_name = parentbranch
        if branchname is not None:
            variables.eyes.branch_name = branchname
        if osname is not None:
            variables.eyes.host_os = osname
        if stitchmode is not None:
            variables.eyes.stitch_mode = utils.get_stitch_mode(stitchmode)
        if matchtimeout is not None:
            variables.eyes.match_timeout = int(matchtimeout)
        if force_full_page_screenshot is not None:
            variables.eyes.force_full_page_screenshot = force_full_page_screenshot
        if save_new_tests is not None:
            variables.eyes.save_new_tests = save_new_tests
        if wait_before_screenshots is not None:
            variables.eyes.wait_before_screenshots = int(wait_before_screenshots)
        if send_dom is not None:
            variables.eyes.send_dom = send_dom
        if stitchcontent is not False:
            variables.stitchcontent = stitchcontent

        if width is None and height is None:
            variables.driver = variables.eyes.open(driver, appname, testname)
        else:
            intwidth = int(width)
            intheight = int(height)

            variables.driver = variables.eyes.open(
                driver, appname, testname, {"width": intwidth, "height": intheight}
            )

        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

    def close_eyes_session(self, enable_eyes_log=False, enable_http_debug_log=False):
        """
        Closes a session and returns the results of the session.
        If a test is running, aborts it. Otherwise, does nothing.

            | =Arguments=                  | =Description=                                                                                  |
            | Enable Eyes Log (bool)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.       |
            | Enable HTTP Debug Log (bool) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable. |

        *Example:*
            | Close Eyes Session | ${true} | ${true} |                                 
        """
        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        variables.eyes.close()
        variables.eyes.abort_if_not_closed()

    def eyes_session_is_open(self):
        """
        Returns True if an Applitools Eyes session is currently running, otherwise it will return False.

        *Example:*
            | ${isOpen}= | Eyes Session Is Open |                    
        """
        return variables.eyes.is_open

    def add_eyes_property(self, name, value):
        """
        Adds a custom key name/value property that will be associated with the session.
        You can view these properties and filter and group by these properties in the [https://eyes.applitools.com/app/test-results/|Test Manager]
        Make sure to use this keyword right after `Open Eyes Session`.

            | =Arguments= | =Description=                      |
            | Name (str)  | The name of the property           |
            | Value (str) | The value associated with the name |

        *Example:*
            | Add Eyes Property | Language | PT |                         
        """
        variables.eyes.add_property(name, value)
