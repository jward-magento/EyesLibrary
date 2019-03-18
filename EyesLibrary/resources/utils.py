from applitools.eyes import MatchLevel
from applitools.core import EyesIllegalArgument
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from applitools import logger
from applitools.logger import StdoutLogger
import httplib


def get_match_level(matchlevel):

    selectedMatchLevel = None

    if matchlevel.upper() == "STRICT":
        selectedMatchLevel = MatchLevel.STRICT
    elif matchlevel.upper() == "CONTENT":
        selectedMatchLevel = MatchLevel.CONTENT
    elif matchlevel.upper() == "LAYOUT":
        selectedMatchLevel = MatchLevel.LAYOUT
    elif matchlevel.upper() == "EXACT":
        selectedMatchLevel = MatchLevel.EXACT
    else:
        raise EyesIllegalArgument(
            "Please select a valid match level: Strict, Content, Layout, Exact"
        )

    return selectedMatchLevel


def get_selector_strategy(selector):

    selectedStrategy = None

    if selector.upper() == "CSS SELECTOR":
        selectedStrategy = By.CSS_SELECTOR
    elif selector.upper() == "XPATH":
        selectedStrategy = By.XPATH
    elif selector.upper() == "ID":
        selectedStrategy = By.ID
    elif selector.upper() == "LINK TEXT":
        selectedStrategy = By.LINK_TEXT
    elif selector.upper() == "PARTIAL LINK TEXT":
        selectedStrategy = By.PARTIAL_LINK_TEXT
    elif selector.upper() == "NAME":
        selectedStrategy = By.NAME
    elif selector.upper() == "TAG NAME":
        selectedStrategy = By.TAG_NAME
    elif selector.upper() == "CLASS NAME":
        selectedStrategy = By.CLASS_NAME
    else:
        raise InvalidElementStateException(
            "Please select a valid selector: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME"
        )

    return selectedStrategy


def manage_logging(enableEyesLog, enableenableHttpDebugLog):

    if enableEyesLog is True:
        logger.set_logger(StdoutLogger())
        logger.open_()
    if enableenableHttpDebugLog is True:
        httplib.HTTPConnection.debuglevel = 1
