#!/usr/bin/env python

from applitools.geometry import Region
from applitools.selenium.target import (
    Target,
    IgnoreRegionByElement,
    IgnoreRegionBySelector,
    FloatingRegion,
    FloatingRegionByElement,
    FloatingRegionBySelector,
    FloatingBounds,
)
from EyesLibrary.resources import utils


class TargetKeywords:
    def ignore_region_by_coordinates(self, left, top, width, height, target=None):
        """
        Returns a Target object that ignores the region specified in the arguments.
        See `Defining Ignore and Floating Regions`.

                |  *Arguments*            | *Description*                                                                                     |
                |  Left (float)           | The left coordinate of the region to ignore e.g. 100                                              |
                |  Top (float)            | The top coordinate of the region to ignore e.g. 150                                               |
                |  Width (float)          | The width of the region to ignore e.g. 500                                                        |
                |  Height (float)         | The height of the region to ignore e.g. 120                                                       |
                |  Target (default=None)  | The previously existent Target, to be used if a ignore region or floating region was already set  |
                
        *Example:*
            | ${target}=    Ignore Region By Coordinates    |  10           |    20          |    100  |  100  |
            | Check Eyes Window  |  Google Homepage   |  True   |  True  |   True   | ${target} |

        """

        if target is None:
            target = Target()

        ignore_region = Region(float(left), float(top), float(width), float(height))
        target.ignore(ignore_region)

        return target

    def ignore_region_by_element(self, element, target=None):
        """
        Returns a Target object that ignores the region of the element specified in the arguments.
        See `Defining Ignore and Floating Regions`.

                |  *Arguments*            | *Description*                                                                                     |
                |  Element (WebElement)   | The WebElement to ignore                                                                          |
                |  Target (default=None)  | The previously existent Target, to be used if a ignore region or floating region was already set  |
                
        *Example:*
            | ${element}=    Get Element              |  //*[@id="hplogo"]  |
            | ${target}=    Ignore Region By Element  |  ${element}         | 
            | Check Eyes Window                       |  Google Homepage    |  True   |  True  |   True   | ${target} |
        """

        if target is None:
            target = Target()

        ignore_region = IgnoreRegionByElement(element)
        target.ignore(ignore_region)

        return target

    def ignore_region_by_selector(self, value, selector="id", target=None):
        """
        Returns a Target object that ignores the region of the element specified in the arguments by selector and value.
        See `Defining Ignore and Floating Regions` and `Using Selectors`

                |  *Arguments*           | *Description*                                                                                                                                                       |
                |  Value (string)        | The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                                              |
                |  Selector (default=id) | This will decide what element will be located. The supported selectors include: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME.  |
                |  Target (default=None) | The previously existent Target, to be used if a ignore region or floating region was already set                                                                    |
                
        *Example:*
            | ${target}=    Ignore Region By Selector |  .first.expanded.dropdown |  CSS SELECTOR  |
            | Check Eyes Window                       |  Google Homepage          |  True          |  True  |   True | ${target} |
        """

        if target is None:
            target = Target()

        selector_strategy = utils.get_selector_strategy(selector)
        ignore_region = IgnoreRegionBySelector(selector_strategy, value)
        target.ignore(ignore_region)

        return target

    def floating_region_by_coordinates(
        self,
        left,
        top,
        width,
        height,
        max_left_offset=0,
        max_top_offset=0,
        max_right_offset=0,
        max_down_offset=0,
        target=None,
    ):
        """
        Returns a Target object that includes the floating region specified in the arguments.
        See `Defining Ignore and Floating Regions`

                |  *Arguments*            | *Description*                                                                                    |
                |  Left (float)           | The left coordinate of the floating region e.g. 100                                              |
                |  Top (float)            | The top coordinate of the floating region e.g. 150                                               |
                |  Width (float)          | The width of the floating region e.g. 500                                                        |
                |  Height (float)         | The height of the floating region e.g. 120                                                       |
                |  Max Left Offset (int)  | The amount the floating region may move to the left. e.g. 10                                     |
                |  Max Top Offset (int)   | The amount the floating region may moveupwards. e.g. 20                                          |
                |  Max Right Offset (int) | The amount the floating region may move to the right. e.g. 10                                    |
                |  Max Down Offset (int)  | The amount the floating region may move downwards. e.g. 50                                       |
                |  Target (default=None)  | The previously existent Target, to be used if a ignore region or floating region was already set |
                
        *Example:*
            | ${target}=    Floating Region By Coordinates |  10              | 10   | 200  | 150  | 10        | 0 | 50 | 50 | 
            | Check Eyes Window                            |  Google Homepage | True | True | True | ${target} |
        """

        if target is None:
            target = Target()

        region = Region(float(left), float(top), float(width), float(height))
        floating_bounds = FloatingBounds(
            int(max_left_offset),
            int(max_top_offset),
            int(max_right_offset),
            int(max_down_offset),
        )
        floating_region = FloatingRegion(region, floating_bounds)
        target.floating(floating_region)

        return target

    def floating_region_by_element(
        self,
        element,
        max_left_offset=0,
        max_top_offset=0,
        max_right_offset=0,
        max_down_offset=0,
        target=None,
    ):
        """
        Returns a Target object that includes the floating region containing the element specified in the arguments.
        See `Defining Ignore and Floating Regions`.

                |  *Arguments*            | *Description*                                                                                    |
                |  Element (WebElement)   | The WebElement that determines the floating region                                               |
                |  Max Left Offset (int)  | The amount the floating region may move to the left. e.g. 10                                     |
                |  Max Top Offset (int)   | The amount the floating region may moveupwards. e.g. 20                                          |
                |  Max Right Offset (int) | The amount the floating region may move to the right. e.g. 10                                    |
                |  Max Down Offset (int)  | The amount the floating region may move downwards. e.g. 50                                       |
                |  Target (default=None)  | The previously existent Target, to be used if a ignore region or floating region was already set |
                
        *Example:*
            | ${element}=    Get Element               |  //*[@id="hplogo"]  |
            | ${target}=    Floating Region By Element |  ${element}         | 10   | 20   | 0    | 10        |
            | Check Eyes Window                        |  Google Homepage    | True | True | True | ${target} |
        """

        if target is None:
            target = Target()

        floating_bounds = FloatingBounds(
            int(max_left_offset),
            int(max_top_offset),
            int(max_right_offset),
            int(max_down_offset),
        )
        floating_region = FloatingRegionByElement(element, floating_bounds)
        target.floating(floating_region)

        return target

    def floating_region_by_selector(
        self,
        value,
        selector="id",
        max_left_offset=0,
        max_top_offset=0,
        max_right_offset=0,
        max_down_offset=0,
        target=None,
    ):
        """
        Returns a Target object that includes the floating region containing the element specified in the arguments by selector and value.
        See `Defining Ignore and Floating Regions` and `Using Selectors`.

                |  *Arguments*            | *Description*                                                                                                                                                       |
                |  Value (string)         | The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                                              |
                |  Selector (default=id)  | This will decide what element will be located. The supported selectors include: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME.  |
                |  Max Left Offset (int)  | The amount the floating region may move to the left. e.g. 10                                                                                                        |
                |  Max Top Offset (int)   | The amount the floating region may moveupwards. e.g. 20                                                                                                             |
                |  Max Right Offset (int) | The amount the floating region may move to the right. e.g. 10                                                                                                       |
                |  Max Down Offset (int)  | The amount the floating region may move downwards. e.g. 50                                                                                                          |
                |  Target (default=None)  | The previously existent Target, to be used if a ignore region or floating region was already set                                                                    |
                
        *Example:*
            | ${target}=    Floating Region By Selector |  .first.expanded.dropdown |  CSS SELECTOR  | 20     | 10     | 20         | 10 |
            | Check Eyes Window                         |  Google Homepage          |  True          |  True  |   True | ${target}  |
        """

        if target is None:
            target = Target()

        selector_strategy = utils.get_selector_strategy(selector)
        floating_bounds = FloatingBounds(
            int(max_left_offset),
            int(max_top_offset),
            int(max_right_offset),
            int(max_down_offset),
        )
        floating_region = FloatingRegionBySelector(
            selector_strategy, value, floating_bounds
        )
        target.floating(floating_region)

        return target

