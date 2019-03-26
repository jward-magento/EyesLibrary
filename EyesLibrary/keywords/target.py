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
        TODO Documentation
        """

        if target is None:
            target = Target()

        ignore_region = Region(float(left), float(top), float(width), float(height))
        target.ignore(ignore_region)

        return target

    def ignore_region_by_element(self, element, target=None):
        """
        TODO Documentation
        """

        if target is None:
            target = Target()

        ignore_region = IgnoreRegionByElement(element)
        target.ignore(ignore_region)

        return target

    def ignore_region_by_selector(self, value, selector="id", target=None):
        """
        TODO Documentation
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
        TODO Documentation
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
        TODO Documentation
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
        TODO Documentation
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

