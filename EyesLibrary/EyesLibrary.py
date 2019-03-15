#!/usr/bin/env python

import os
import httplib
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from robot.libraries.BuiltIn import BuiltIn
from applitools import logger
from applitools.logger import StdoutLogger
from applitools.logger import FileLogger
from applitools.geometry import Region
from applitools.eyes import Eyes, BatchInfo
from applitools.selenium.webelement import EyesWebElement


class EyesLibrary:
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
        includeEyesLog=False,
        httpDebugLog=False,
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
                |  (Optional) Match Level (string)      | The match level for the comparison - can be STRICT, LAYOUT or CONTENT                                       |
                |  Include Eyes Log (default=False)     | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                    |
                |  HTTP Debug Log (default=False)       | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.              |
                |  Branch Name (default=None)          | The branch to use to check test                                                                             |
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
        global driver
        global eyes

        eyes = Eyes()
        eyes.api_key = apikey

        try:
            libraryInstance = BuiltIn().get_library_instance(library)

            if library == "AppiumLibrary":
                driver = libraryInstance._current_application()
            else:
                driver = libraryInstance._current_browser()
        except RuntimeError:
            raise Exception("%s instance not found" % library)

        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1
        if osname is not None:
            eyes.host_os = osname  # (str)
        if browsername is not None:
            eyes.host_app = browsername  # (str)
        if baselineName is not None:
            eyes.baseline_branch_name = baselineName  # (str)
        if batchName is not None:
            batch = BatchInfo(batchName)
            eyes.batch = batch
        if matchlevel is not None:
            eyes.match_level = matchlevel
        if parentbranch is not None:
            eyes.parent_branch_name = parentbranch  # (str)
        if branchname is not None:
            eyes.branch_name = branchname  # (str)

        if width is None and height is None:
            driver = eyes.open(driver, appname, testname)
        else:
            intwidth = int(width)
            intheight = int(height)

            driver = eyes.open(
                driver, appname, testname, {"width": intwidth, "height": intheight}
            )

    def check_eyes_window(
        self,
        name,
        force_full_page_screenshot=False,
        includeEyesLog=False,
        httpDebugLog=False,
    ):
        """
        Takes a snapshot from the browser using the web driver and matches it with
        the expected output.

                |  *Arguments*                                  | *Description*                                                                                   |
                |  Name (string)                                | Name that will be given to region in Eyes.                                                      |
                |  Force Full Page Screenshot (default=False)   | Will force the browser to take a screenshot of whole page.                                      |
                |  Include Eyes Log (default=False)             | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.        |
                |  HTTP Debug Log (default=False)               | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.  |

        *Example:*
            | Check Eyes Window  |  Google Homepage   |  True   |  True  |   True   |

        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        eyes.force_full_page_screenshot = force_full_page_screenshot
        eyes.check_window(name)

    def check_eyes_region(
        self, left, top, width, height, name, includeEyesLog=False, httpDebugLog=False
    ):
        """
        Takes a snapshot of the given region from the browser using a Region object (identified by left, top, width, height)
        and matches it with the expected output.

        The width and the height cannot be greater than the width and the height specified in the open_eyes_session keyword.

                |  *Arguments*                       | *Description*                                         |
                |  Left (float)                      | The left coordinate of the region that is tested e.g. 100                                      |
                |  Top (float)                       | The top coordinate of the region that is tested e.g. 150                                       |
                |  Width (float)                     | The width of the region that is tested e.g. 500                                                |
                |  Height (float)                    | The height of the region that is tested e.g. 120                                               |
                |  Name (string)                     | Name that will be given to region in Eyes.                                                     |
                |  Include Eyes Log (default=False)  | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.       |
                |  HTTP Debug Log (default=False)    | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable. |

        *Example:*            
            | Check Eyes Region  |  100   | 150   | 500   |  120  |  Google Logo   |  True  | True  |

        """

        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        region = Region(float(left), float(top), float(width), float(height))
        eyes.check_region(region, name)

    def check_eyes_region_by_element(
        self, element, name, includeEyesLog=False, httpDebugLog=False
    ):
        """
        Takes a snapshot of the region of the given element from the browser using the web driver. Not available to mobile native apps.

                |  *Arguments*                      | *Description*                                      |
                |  Element (WebElement)             | The Web Element to be checked. See `Get Element`   |
                |  Name (string)                    | Name that will be given to region in Eyes.                                                                           |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                             |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                       |

        *Example:*
            | ${element}=    Get Element   |    //*[@id="hplogo"]  |
            | Check Eyes Region By Element  |  ${element}     |  ElementName    |   True  | True  |    

        *Note (Safari on mobile):* 
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.
        
        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        if not isinstance(element, EyesWebElement):
            element = EyesWebElement(element, driver)

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if eyes.host_app == "Safari" and eyes.host_os == "iOS":
            location = element.location
            size = element.size

            eyes.check_region(
                Region(
                    location.__getitem__("x"),
                    location.__getitem__("y") + 71,
                    size.__getitem__("width"),
                    size.__getitem__("height"),
                )
            )
        else:
            eyes.check_region_by_element(element, name)

    def check_eyes_region_by_selector(
        self, value, name, selector="id", includeEyesLog=False, httpDebugLog=False
    ):
        """
        Takes a snapshot of the region of the element found by calling find_element(by, value) from the browser using the web driver
        and matches it with the expected output. With a choice from eight selectors, listed below to check by.

        Not available to mobile native apps.

                |  *Arguments*                      | *Description*                                                                              |
                |  Value (string)                   | The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                                                |
                |  Name (string)                    | Name that will be given to region in Eyes.                                                                                                                            |
                |  Selector (default=id)            | This will decide what element will be located. The supported selectors include: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME.    |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                                                                              |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                                                                        |

        *Example:*
            | Check Eyes Region By Selector |    .first.expanded.dropdown |  CssElement         |     CSS SELECTOR             |

        *Note (Safari on mobile):* 
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.

        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        searchElement = None

        if selector.upper() == "CSS SELECTOR":
            searchElement = By.CSS_SELECTOR
        elif selector.upper() == "XPATH":
            searchElement = By.XPATH
        elif selector.upper() == "ID":
            searchElement = By.ID
        elif selector.upper() == "LINK TEXT":
            searchElement = By.LINK_TEXT
        elif selector.upper() == "PARTIAL LINK TEXT":
            searchElement = By.PARTIAL_LINK_TEXT
        elif selector.upper() == "NAME":
            searchElement = By.NAME
        elif selector.upper() == "TAG NAME":
            searchElement = By.TAG_NAME
        elif selector.upper() == "CLASS NAME":
            searchElement = By.CLASS_NAME
        else:
            raise InvalidElementStateException(
                "Please select a valid selector: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME"
            )

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if eyes.host_app == "Safari" and eyes.host_os == "iOS":
            element = driver.find_element(searchElement, value)
            location = element.location
            size = element.size

            eyes.check_region(
                Region(
                    location.__getitem__("x"),
                    location.__getitem__("y") + 71,
                    size.__getitem__("width"),
                    size.__getitem__("height"),
                )
            )
        else:
            eyes.check_region_by_selector(searchElement, value, name)

    def close_eyes_session(self, includeEyesLog=False, httpDebugLog=False):
        """
        Closes a session and returns the results of the session.
        If a test is running, aborts it. Otherwise, does nothing.

                |  *Arguments*                      | *Description*                                                                                   |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.        |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.  |

        *Example:*
            | Close Eyes Session    |    True   |   True    |                                 
        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        eyes.close()
        eyes.abort_if_not_closed()

    def eyes_session_is_open(self):
        """
        Returns True if an Applitools Eyes session is currently running, otherwise it will return False.

        *Example:*
            | ${isOpen}=        |  Eyes Session Is Open     |                    
        """
        return eyes.is_open
