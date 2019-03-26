#!/usr/bin/env python

import os
import httplib
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from robot.libraries.BuiltIn import BuiltIn
from applitools.core import logger
from applitools.geometry import Region
from applitools.eyes import Eyes, BatchInfo
from applitools.selenium.webelement import EyesWebElement
from .session import SessionKeywords
from applitools.selenium.positioning import StitchMode
from robot.api import logger as loggerRobot
from EyesLibrary.resources import variables, utils


class CheckKeywords:
    def check_eyes_window(
        self,
        name,
        force_full_page_screenshot=None,
        enable_eyes_log=False,
        enable_http_debug_log=False,
        target=None,
        match_timeout=None,
    ):
        """
        Takes a snapshot from the browser using the web driver and matches
        it with the expected output.

            | =Arguments=                                | =Description=                                                                                                                |
            | Name (string)                              | Name that will be given to region in Eyes.                                                                                   |
            | Force Full Page Screenshot (default=False) | Will force the browser to take a screenshot of whole page. Define "Stitch Mode" argument on `Open Eyes Session` if necessary |
            | Enable Eyes Log (default=False)            | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                                     |
            | Enable HTTP Debug Log (default=False)      | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                               |

        *Example:*
            | Check Eyes Window | Google Homepage | True | True | True |
        """
        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        if force_full_page_screenshot is not None:
            variables.eyes.force_full_page_screenshot = force_full_page_screenshot

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":
            size = variables.driver.get_window_size("current")

            variables.eyes.check_region(
                Region(0, 71, size.__getitem__("width"), size.__getitem__("height")),
                name,
                target=target,
            )
        else:
            variables.eyes.check_window(name, target=target)

    def check_eyes_region(
        self,
        left,
        top,
        width,
        height,
        name,
        enable_eyes_log=False,
        enable_http_debug_log=False,
        target=None,
        match_timeout=None,
    ):
        """
        Takes a snapshot of the given region from the browser using a Region
        object (identified by left, top, width, height) and matches it with the
        expected output.

        The width and the height cannot be greater than the width and the height specified in the `Open Eyes Session` keyword.

            | =Arguments=                           | =Description=                                                                                  |
            | Left (float)                          | The left coordinate of the region that is tested e.g. 100                                      |
            | Top (float)                           | The top coordinate of the region that is tested e.g. 150                                       |
            | Width (float)                         | The width of the region that is tested e.g. 500                                                |
            | Height (float)                        | The height of the region that is tested e.g. 120                                               |
            | Name (string)                         | Name that will be given to region in Eyes.                                                     |
            | Enable Eyes Log (default=False)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.       |
            | Enable HTTP Debug Log (default=False) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable. |


        *Example:*
            | Check Eyes Region | 100 | 150 | 500 | 120 | Google Logo | True | True |
        """

        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        region = Region(float(left), float(top), float(width), float(height))
        variables.eyes.check_region(region, name, target=target)

    def check_eyes_region_by_element(
        self,
        element,
        name,
        enable_eyes_log=False,
        enable_http_debug_log=False,
        target=None,
        match_timeout=None,
    ):
        """
        Takes a snapshot of the region of the given element from the browser
        using the web driver. Not available to mobile native apps.

            | =Arguments=                           | =Description=                                                                                  |
            | Element (WebElement)                  | The Web Element to be checked.                                                                 |
            | Name (string)                         | Name that will be given to region in Eyes.                                                     |
            | Enable Eyes Log (default=False)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.       |
            | Enable HTTP Debug Log (default=False) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable. |
            
        *Example:*
            | ${element}=                  | Get Element | //*[@id="hplogo"] |
            | Check Eyes Region By Element | ${element}  | ElementName       | True | True |

        *Note (Safari on mobile):*
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.
        """

        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":
            location = element.location
            size = element.size

            variables.eyes.check_region(
                Region(
                    location.__getitem__("x"),
                    location.__getitem__("y") + 71,
                    size.__getitem__("width"),
                    size.__getitem__("height"),
                ),
                target=target,
            )
        else:
            variables.eyes.check_region_by_element(element, name, target=target)

    def check_eyes_region_by_selector(
        self,
        value,
        name,
        selector="id",
        enable_eyes_log=False,
        enable_http_debug_log=False,
        target=None,
        match_timeout=None,
    ):
        """
        Takes a snapshot of the region of the element found by calling
        find_element(by, value) from the browser using the web driver and
        matches it with the expected output. With a choice from eight
        selectors, to check by on `Using Selectors` section.

        Not available to mobile native apps.

            | =Arguments=                           | =Description=                                                                                                                                                      |
            | Value (string)                        | The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                                             |
            | Name (string)                         | Name that will be given to region in Eyes.                                                                                                                         |
            | Selector (default=id)                 | This will decide what element will be located. The supported selectors include: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME. |
            | Enable Eyes Log (default=False)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable.                                                                           |
            | Enable HTTP Debug Log (default=False) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable.                                                                     |
        
        *Example:*
            | Check Eyes Region By Selector | .first.expanded.dropdown | CssElement | CSS SELECTOR | True | True |

        *Note (Safari on mobile):*
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.
        """
        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        selector_strategy = utils.get_selector_strategy(selector)

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":
            element = variables.driver.find_element(selector_strategy, value)
            location = element.location
            size = element.size

            variables.eyes.check_region(
                Region(
                    location.__getitem__("x"),
                    location.__getitem__("y") + 71,
                    size.__getitem__("width"),
                    size.__getitem__("height"),
                ),
                target=target,
            )
        else:
            variables.eyes.check_region_by_selector(
                selector_strategy, value, name, target=target
            )

