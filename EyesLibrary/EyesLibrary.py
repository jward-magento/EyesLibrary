#!/usr/bin/env python


#  Copyright 2013-2014 NaviNet Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

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

#from applitools.images import Eyes as ImageEyes
#from applitools.utils import image_utils
#from applitools.core import EyesScreenshot


class EyesLibrary:
    """
    EyesLibrary is a visual verfication library for Robot Framework that leverages
    the Eyes-Selenium and Selenium/Appium libraries.



    *Before running tests*

    Prior to running tests, EyesLibrary must first be imported into your Robot test suite.

    Example:
        | Library | EyesLibrary |



    In order to run EyesLibrary and return results, you have to create a free account https://applitools.com/sign-up/ with Applitools.
    You can retrieve your API key from the applitools website and that will need to be passed in your Open Eyes Session keyword.



    *Using Selectors*

    Using the keyword Check Eyes Region By Selector. *All* the following strategies are supported:

    | *Strategy*        | *Example*                                                                                                      | *Description*                                   |
    | CSS SELECTOR      | Check Eyes Region By Selector `|` .first.expanded.dropdown `|`  CssElement      `       |` CSS SELECTOR        | Matches by CSS Selector                         |
    | XPATH             | Check Eyes Region By Selector `|` //div[@id='my_element']  `|`  XpathElement   `        |` XPATH               | Matches with arbitrary XPath expression         |
    | ID                | Check Eyes Region By Selector `|` my_element               `|`  IdElement    `          |` ID                  | Matches by @id attribute                        |
    | CLASS NAME        | Check Eyes Region By Selector `|` element-search           `|`  ClassElement   `        |` CLASS NAME          | Matches by @class attribute                     |
    | LINK TEXT         | Check Eyes Region By Selector `|` My Link                  `|`  LinkTextElement      `  |` LINK TEXT           | Matches anchor elements by their link text      |
    | PARTIAL LINK TEXT | Check Eyes Region By Selector `|` My Li                    `|`  PartialLinkTextElement` |` PARTIAL LINK TEXT   | Matches anchor elements by partial link text    |
    | NAME              | Check Eyes Region By Selector `|` my_element               `|`  NameElement    `        |` NAME                | Matches by @name attribute                      |
    | TAG NAME          | Check Eyes Region By Selector `|` div                      `|`  TagNameElement       `  |` TAG NAME            | Matches by HTML tag name                        |
    """

    def open_eyes_session(self,
                          appname,
                          testname,
                          apikey,
                          library='SeleniumLibrary',
                          # package='selenium',
                          width=None,
                          height=None,
                          osname=None,
                          matchlevel=None,
                          includeEyesLog=False,
                          httpDebugLog=False,
                          baselineName=None,
                          batchName=None,
                          branchname=None,
                          parentbranch=None):
        """
        Starts a session with the Applitools Eyes Website.
        Arguments:
                |  Application Name (string)            | The name of the application under test.                                                                     |
                |  Test Name (string)                   | The test name.                                                                                              |
                |  API Key (string)                     | User's Applitools Eyes key.                                                                                 |
                |  Library (default=SeleniumLibrary)    | Library to test (Either SeleniumLibrary or AppiumLibrary)                                                   |
                |  (Optional) Width (int)               | The width of the browser window e.g. 1280                                                                   |
                |  (Optional) Height (int)              | The height of the browser window e.g. 1000                                                                  |
                |  (Optional) Operating System (string) | The operating system of the test, can be used to override the OS name to allow cross OS verfication         |
                |  (Optional) Browser Name (string)     | The browser name for the test, can be used to override the browser name to allow cross browser verfication  |
                |  (Optional) Match Level (string)      | The match level for the comparison - can be STRICT, LAYOUT or CONTENT                                       |
                |  Include Eyes Log (default=False)     | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                    |
                |  HTTP Debug Log (default=False)       | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.              |
                |  Branch Name (default=False)          | The branch to use to check test                                                                             |
                |  Parent Branch (default=False)        | Parent Branch to base the new Branch on                                                                     |
        Creates an instance of the AppiumLibrary or SeleniumLibrary webdriver, given the library argument.
        Defines a global driver and sets the webdriver to the global driver.
        Checks if there has been a width or height value passed in.
        If there no are values passed in, eyes calls the method open without the width and height values.
        Otherwise eyes calls open with the width and height values defined.
        The Height resolution should not be greater than 1000, this is currently Applitools maximum setting.
        Starts a session with the Applitools Eyes Website. See https://eyes.applitools.com/app/sessions/
        Example:
        | *Keywords*         |  *Parameters*                                                                                                                                                                                                                    |
        | Open Browser       |  http://google.com/ | gc                |                       
        | Open Eyes Session  |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey  |  1024  |  768  |  OSOverrideName  |  BrowserOverrideName  |  matchlevel=LAYOUT   |  includeEyesLog=True  |  httpDebugLog=True  |
        | Check Eyes Window  |  Google Homepage            |                              
        | Close Eyes Session |  False                   |                              
        """
        global driver
        global eyes

        # if package is 'selenium':
        #     eyes = Eyes()
        # else:
        #     eyes = ImageEyes()

        eyes = Eyes()
        eyes.api_key = apikey

        try:
            libraryInstance = BuiltIn().get_library_instance(library)

            if library == 'AppiumLibrary':
                driver = libraryInstance._current_application()
            else:
                driver = libraryInstance._current_browser()
        except RuntimeError:
            raise Exception('%s instance not found' % library)

        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1
        if osname is not None:
            eyes.host_os = osname  # (str)
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
            # driver = eyes.open(appname, testname)
            driver = eyes.open(driver, appname, testname)
        else:
            intwidth = int(width)
            intheight = int(height)
            # driver = eyes.open(appname, testname, {
            #     'width': intwidth, 'height': intheight})

            driver = eyes.open(driver, appname, testname, {
                'width': intwidth, 'height': intheight})

    def check_eyes_window(self, name, force_full_page_screenshot=False,
                          includeEyesLog=False, httpDebugLog=False):
        """
        Takes a snapshot from the browser using the web driver and matches it with
        the expected output.
        Arguments:
                |  Name (string)                                | Name that will be given to region in Eyes.                                                      |
                |  Force Full Page Screenshot (default=False)   | Will force the browser to take a screenshot of whole page.                                      |
                |  Include Eyes Log (default=False)             | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.        |
                |  HTTP Debug Log (default=False)               | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.  |
        Example:
        | *Keywords*         |  *Parameters*                                                                                                    |
        | Open Browser       |  http://google.com/ | gc                |     
        | Open Eyes Session  |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey  |  1024  |  768  |
        | Check Eyes Window  |  Google Homepage            | True              |  
        | Close Eyes Session |  False                   |     
        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        eyes.force_full_page_screenshot = force_full_page_screenshot
        eyes.check_window(name)

    def check_eyes_region(self, left, top, width, height, name, includeEyesLog=False, httpDebugLog=False):
        """
        Takes a snapshot of the given region from the browser using a Region object (identified by left, top, width, height)
        and matches it with the expected output.
        The width and the height cannot be greater than the width and the height specified in the open_eyes_session keyword.
        Arguments:
                |  Left (float)                      | The left coordinate of the region that is tested e.g. 100                                                |
                |  Top (float)                     | The top coordinate of the region that is tested e.g. 150                                               |
                |  Width (float)                      | The width of the region that is tested e.g. 500                                                |
                |  Height (float)                     | The height of the region that is tested e.g. 120                                               |
                |  Name (string)                    | Name that will be given to region in Eyes.                                                     |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.       |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable. |
        Example:
        | *Keywords*         |  *Parameters*                                                                                                        |
        | Open Browser       |  http://google.com/     | gc                 | 
        | Open Eyes Session  |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey    |  1024  |  768  |
        | Check Eyes Region  |  100   | 150   | 500                   |  120                        |  Google Logo    |  
        | Close Eyes Session |  False                       | 
        """

        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        region = Region(float(left), float(top), float(width), float(height))
        eyes.check_region(region, name)

    def check_eyes_region_by_element(self, element, name, includeEyesLog=False, httpDebugLog=False):
        """
        Takes a snapshot of the region of the given element from the browser using the web driver. Not available to mobile native apps.
        Arguments:
                |  Element (WebElement)                | The Web Element to be checked. See `Get Element`   |
                |  Name (string)                    | Name that will be given to region in Eyes.                                                                           |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                             |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                       |
        Example:
        | *Keywords*                    |  *Parameters*                                                                                                    |
        | Open Browser                  |  http://www.google.com/  |  gc                |                        
        | Open Eyes Session             |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey |  1024 |  768 |
        | ${element}=    Get Element   |    //*[@id="hplogo"]  |
        | Check Eyes Region By Element  |  ${element}     |  ElementName      |               
        | Close Eyes Session            |  False                    |        
        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        if not isinstance(element, EyesWebElement):
            element = EyesWebElement(element, driver)

        eyes.check_region_by_element(element, name)

    def check_eyes_region_by_selector(self, value, name, selector="id", includeEyesLog=False, httpDebugLog=False):
        """
        Takes a snapshot of the region of the element found by calling find_element(by, value) from the browser using the web driver
        and matches it with the expected output. With a choice from eight selectors, listed below to check by.
        Not available to mobile native apps.
        Arguments:
                |  Value (string)                   | The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                                                |
                |  Name (string)                    | Name that will be given to region in Eyes.                                                                                                                            |
                |  Selector (default=id)            | This will decide what element will be located. The supported selectors include: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME.    |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                                                                              |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                                                                        |
        Example:
        | *Keywords*                    |  *Parameters*                                                                                                            |
        | Open Browser                  |  http://www.google.com/  |  gc                       |     
        | Open Eyes Session             |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey |  1024  |  768  |
        | Check Eyes Region By Selector |    .first.expanded.dropdown |  CssElement         |     CSS SELECTOR             |
        | Close Eyes Session            |  False                    |                                   
        """
        if includeEyesLog is True:
            logger.set_logger(StdoutLogger())
            logger.open_()
        if httpDebugLog is True:
            httplib.HTTPConnection.debuglevel = 1

        searchElement = None

        if selector.upper() == 'CSS SELECTOR':
            searchElement = By.CSS_SELECTOR
        elif selector.upper() == 'XPATH':
            searchElement = By.XPATH
        elif selector.upper() == 'ID':
            searchElement = By.ID
        elif selector.upper() == 'LINK TEXT':
            searchElement = By.LINK_TEXT
        elif selector.upper() == 'PARTIAL LINK TEXT':
            searchElement = By.PARTIAL_LINK_TEXT
        elif selector.upper() == 'NAME':
            searchElement = By.NAME
        elif selector.upper() == 'TAG NAME':
            searchElement = By.TAG_NAME
        elif selector.upper() == 'CLASS NAME':
            searchElement = By.CLASS_NAME
        else:
            raise InvalidElementStateException(
                'Please select a valid selector: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME')

        eyes.check_region_by_selector(searchElement, value, name)

    def compare_image(self, path, imagename=None, ignore_mismatch=False):
        """
        Select an image and send it to Eyes for comparison. A name can be used in place of the image's file name.
        Arguments:
                |  Path                             | Path of the image to send to eyes for visual comparison.                                                                   |
                |  imagename (default=None)         | Can manually set the name desired for the image passed in. If no name is passed in it will default file name of the image. |
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                                   |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                             |
        Example:
        | *Keywords*         |  *Parameters*                                                                                                         |
        | Open Eyes Session  |  EyesLibrary_AppName    |  EyesLibrary_TestName |  YourApplitoolsKey |  1024  |  768  |
        | Compare Image      |  screenshot-1.png |  Image Name Example   |      package=images                      |                    |        |       |
        | Close Eyes Session |                            |                       |                            |                    |        |       |
        """
        if imagename is None:
            tag = os.path.basename(path)
        else:
            tag = imagename

        #eyes = Eyes()
        #eyes.api_key = apikey
        #outdriver = eyes.open(app_name, test_name)

        eyes.check_image(path, tag)

        # with open(path, 'rb') as image_file:
        #     screenshot64 = image_file.read().encode('base64')
        #     screenshot = image_utils.image_from_base64(screenshot64)
        # screenshotBytes = EyesScreenshot.create_from_image(
        #     screenshot, eyes._driver)
        # title = eyes.get_title()
        # app_output = {'title': title, 'screenshot64': None}
        # user_inputs = []
        # prepare_match_data = eyes.match_window_task._create_match_data_bytes(
        #     app_output, user_inputs, tag, ignore_mismatch, screenshotBytes)

        # eyes_base._match_window_task.match_window(retry_timeout=match_timeout,
        #                                           tag=tag,
        #                                           user_inputs=self._user_inputs,
        #                                           default_match_settings=self.default_match_settings,
        #                                           target=target,
        #                                           run_once_after_wait=self._should_match_once_on_timeout)

        # # eyes._match_window_task._agent_connector.match_window(
        # #     eyes._match_window_task._running_session, prepare_match_data)

        # eyes.close()
        # eyes.abort_if_not_closed()

    def close_eyes_session(self, includeEyesLog=False, httpDebugLog=False):
        """
        Closes a session and returns the results of the session.
        If a test is running, aborts it. Otherwise, does nothing.
        Arguments:
                |  Include Eyes Log (default=False) | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.        |
                |  HTTP Debug Log (default=False)   | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.  |
        Example:
        | *Keywords*                    |  *Parameters*                                                                                                         |
        | Open Browser                  |  http://google.com/  |  gc                    |        
        | Open Eyes Session             |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey  |  1024  |  768  |
        | Check Eyes Region By Selector |  LINK TEXT                |  RESOURCES             |  LinkTextElement    |    
        | Close Eyes Session            |                           |                                 
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
        | *Keywords*        |  *Parameters*                                                                                                       |
        | Open Browser      |  http://google.com/  |  gc                  | 
        | Open Eyes Session |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey  |  1024  |  768  |
        | ${isOpen}=        |  Eyes Session Is Open     |          
        | Run Keyword If    |  ${isOpen}==True          | Close Eyes Session   |              
        """
        return eyes.is_open
