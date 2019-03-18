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
from EyesLibrary.resources import utils, variables


class SessionKeywords:
    def open_eyes_session(
        self,
        appname,
        testname,
        apikey,
        library="SeleniumLibrary",
        width=None,
        height=None,
        osname=None,
        browsername=None,
        matchlevel=None,
        enableEyesLog=False,
        enableHttpDebugLog=False,
        baselineName=None,
        batchName=None,
        branchname=None,
        parentbranch=None,
    ):
        """
        Starts a session with the Applitools Eyes Website. See https://eyes.applitools.com/app/sessions/

                | *Arguments*                           | *Description*                                                                                               |
                |  Application Name (string)            | The name of the application under test.                                                                     |
                |  Test Name (string)                   | The test name.                                                                                              |
                |  API Key (string)                     | User's Applitools Eyes key.                                                                                 |
                |  Library (default=SeleniumLibrary)    | Library to test (Either SeleniumLibrary or AppiumLibrary)                                                   |
                |  (Optional) Width (int)               | The width of the browser window e.g. 1280                                                                   |
                |  (Optional) Height (int)              | The height of the browser window e.g. 1000                                                                  |
                |  (Optional) Operating System (string) | The operating system of the test, can be used to override the OS name to allow cross OS verfication         |
                |  (Optional) Browser Name (string)     | The browser name for the test, can be used to override the browser name to allow cross browser verification  |
                |  (Optional) Match Level (string)      | The match level for the comparison - can be STRICT, LAYOUT, CONTENT or EXACT                                    |
                |  Enable Eyes Log (default=False)     | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                    |
                |  Enable HTTP Debug Log (default=False)       | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.              |
                |  Baseline Branch Name (default=None)  | The branch to use to check test                                                                             |
                |  Parent Branch (default=None)        | Parent Branch to base the new Branch on                                                                     |
        Creates an instance of the AppiumLibrary or SeleniumLibrary webdriver, given the library argument.

        Defines a global driver and sets the webdriver to the global driver.

        Checks if there has been a width or height value passed in.
        If there no are values passed in, eyes calls the method open without the width and height values.
        Otherwise, Eyes calls open with the width and height values defined.

        *Note:* When opening the session on a mobile browser or hybrid app, the context must be set to WEBVIEW in order to retrieve the correct viewport size. Geolocation of the device may have to be set after switching context.

        *Example:*                                                                                                                                                                                                                               
                | Open Eyes Session  |  Eyes_AppName |  Eyes_TestName |  YourApplitoolsKey  | SeleniumLibrary |  1024  |  768  |  OSOverrideName  |  BrowserOverrideName  |  LAYOUT   |  True  |  True  |  BranchName   |  ParentBranch   |
        """

        variables.eyes = Eyes()
        variables.eyes.api_key = apikey

        try:
            libraryInstance = BuiltIn().get_library_instance(library)

            if library == "AppiumLibrary":
                driver = libraryInstance._current_application()
            else:
                driver = libraryInstance._current_browser()
        except RuntimeError:
            raise Exception("%s instance not found" % library)

        utils.manage_logging(enableEyesLog, enableHttpDebugLog)

        if osname is not None:
            variables.eyes.host_os = osname  # (str)
        if browsername is not None:
            variables.eyes.host_app = browsername  # (str)
        if baselineName is not None:
            variables.eyes.baseline_branch_name = baselineName  # (str)
        if batchName is not None:
            batch = BatchInfo(batchName)
            variables.eyes.batch = batch
        if matchlevel is not None:
            variables.eyes.match_level = utils.get_match_level(matchlevel)
        if parentbranch is not None:
            variables.eyes.parent_branch_name = parentbranch  # (str)
        if branchname is not None:
            variables.eyes.branch_name = branchname  # (str)

        if width is None and height is None:
            driver = variables.eyes.open(driver, appname, testname)
        else:
            intwidth = int(width)
            intheight = int(height)

            driver = variables.eyes.open(
                driver, appname, testname, {"width": intwidth, "height": intheight}
            )

    def close_eyes_session(self, enableEyesLog=False, enableHttpDebugLog=False):
        """
        Closes a session and returns the results of the session.
        If a test is running, aborts it. Otherwise, does nothing.

                |  *Arguments*                      | *Description*                                                                                   |
                |  Enable Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.        |
                |  Enable HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.  |

        *Example:*
            | Close Eyes Session    |    True   |   True    |                                 
        """
        utils.manage_logging(enableEyesLog, enableHttpDebugLog)

        variables.eyes.close()
        variables.eyes.abort_if_not_closed()

    def eyes_session_is_open(self):
        """
        Returns True if an Applitools Eyes session is currently running, otherwise it will return False.

        *Example:*
            | ${isOpen}=        |  Eyes Session Is Open     |                    
        """
        return variables.eyes.is_open
