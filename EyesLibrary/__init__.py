#!/usr/bin/env python

from EyesLibrary.eyeslibrary import EyesLibrary
from EyesLibrary.version import VERSION

_version_ = VERSION


class EyesLibrary(EyesLibrary):
    """
    EyesLibrary is a visual verification library for Robot Framework that leverages
    the Eyes-Selenium and Selenium/Appium libraries.

    *Before running tests*

    Prior to running tests, EyesLibrary must first be imported into your Robot test suite.

    Example:
        | Library | EyesLibrary | 

    In order to run EyesLibrary and return results, you have to create a free account https://applitools.com/sign-up/ with Applitools.
    You can retrieve your API key from the applitools website and that will need to be passed in your Open Eyes Session keyword.

    *Writing tests*

    When writing the tests, the following structure must be adopted:

    | *Open Eyes Session* |
    | A browser or application must be running when opening the session. To open a browser/application, consult the documentation for SeleniumLibrary and/or AppiumLibrary. |
    | Afterwards, the session may be opened. See `Open Eyes Session`.  |
    | *Visual Checks* |
    | Between opening and closing the session, you can run your visual checks. |
    | See `Check Eyes Region`, `Check Eyes Region By Element`, `Check Eyes Region By Selector` and `Check Eyes Window` |
    | You can also verify if there's an open session with `Eyes Session Is Open` |
    | *Close Eyes Session* |
    | See `Close Eyes Session`. |

    - Example:

        | *Keywords*         |  *Parameters*                                                                                                                                                                                                                    |
        | Open Browser       |  http://google.com/ | gc                |                       
        | Open Eyes Session  |  EyesLibrary_AppName |  EyesLibrary_TestName |  YourApplitoolsKey  |
        | Check Eyes Window  |  Google Homepage            |                              
        | Close Eyes Session |  

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

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = VERSION
