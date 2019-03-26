#!/usr/bin/env python

from .keywords import SessionKeywords, CheckKeywords, TargetKeywords
from .resources import variables
from .version import VERSION

_version_ = VERSION


class EyesLibrary(SessionKeywords, CheckKeywords, TargetKeywords):
    """
    EyesLibrary is a visual verification library for Robot Framework that leverages
    the Eyes-Selenium and Selenium/Appium libraries.

    = Table of contents =
    - `Before running tests`
    - `Writing tests`
    - `Using selectors`
    - `Defining Ignore and Floating regions`
    - `Importing`
    - `Shortcuts`
    - `Keywords`

    = Before running tests =

    In order to run EyesLibrary and return results, you have to create a free account https://applitools.com/sign-up/ with Applitools.
    You can retrieve your API key from the applitools website and that will need to be passed in your Open Eyes Session keyword.

    Prior to running tests, EyesLibrary must first be imported into your Robot test suite.

    Example:
        | Library | EyesLibrary | 

    You may define the following arguments when importing the library (You may also define them on `Open Eyes Session`):
    - API Key (apikey)
    - Application Name (appname)
    - Test Name (testname)
    - Library - SeleniumLibrary or AppiumLibrary (library)
    - Match Level - Strict, Exact, Content or Layout (matchlevel)
    - Enable Eyes Logs (enable_eyes_log)
    - OS Name (osname)
    - Browser Name (browsername)
    - Server URL (serverurl)       

    Example:
        | Library | EyesLibrary | ApiKey | AppName | TestName | SeleniumLibrary | Layout | True | Windows | Firefox | https://myserver.com |
        
    = Writing tests =

    When writing the tests, the following structure must be adopted:

    | *Open Eyes Session* |
    | A browser or application must be running when opening the session. To open a browser/application, consult the documentation for SeleniumLibrary and/or AppiumLibrary. |
    | Afterwards, the session may be opened. See `Open Eyes Session`. |
    | *Visual Checks* |
    | Between opening and closing the session, you can run your visual checks. |
    | See `Check Eyes Region`, `Check Eyes Region By Element`, `Check Eyes Region By Selector` and `Check Eyes Window` |
    | You can also verify if there's an open session with `Eyes Session Is Open` |
    | *Close Eyes Session* |
    | See `Close Eyes Session`. |

    - Example:

        | =Keywords=         | =Parameters=       |
        | Open Browser       | http://google.com/ | gc                  |                       
        | Open Eyes Session  | YourApplitoolsKey  | EyesLibrary_AppName | EyesLibrary_TestName |
        | Check Eyes Window  | Google Homepage    |                              
        | Close Eyes Session | 

    == Using selectors ==

    Using the keywords `Check Eyes Region By Selector`, `Ignore Region By Selector` or `Floating Region By Selector`.
    The following strategies are supported:

    | =Strategy=        | =Example=                                                                                                   | =Description=                                |
    | CSS SELECTOR      | Check Eyes Region By Selector `|` .first.expanded.dropdown `|` CssElement             `|` CSS SELECTOR      | Matches by CSS Selector                      |
    | XPATH             | Check Eyes Region By Selector `|` //div[@id='my_element']  `|` XpathElement           `|` XPATH             | Matches with arbitrary XPath expression      |
    | ID                | Check Eyes Region By Selector `|` my_element               `|` IdElement              `|` ID                | Matches by @id attribute                     |
    | CLASS NAME        | Check Eyes Region By Selector `|` element-search           `|` ClassElement           `|` CLASS NAME        | Matches by @class attribute                  |
    | LINK TEXT         | Check Eyes Region By Selector `|` My Link                  `|` LinkTextElement        `|` LINK TEXT         | Matches anchor elements by their link text   |
    | PARTIAL LINK TEXT | Check Eyes Region By Selector `|` My Li                    `|` PartialLinkTextElement `|` PARTIAL LINK TEXT | Matches anchor elements by partial link text |
    | NAME              | Check Eyes Region By Selector `|` my_element               `|` NameElement            `|` NAME              | Matches by @name attribute                   |
    | TAG NAME          | Check Eyes Region By Selector `|` div                      `|` TagNameElement         `|` TAG NAME          | Matches by HTML tag name                     |
    
    == Defining Ignore and Floating regions  ==

    A *Ignore Region* defines a region to be ignored on the checks, ie, to always be considered matching.

    A *Floating Region* defines an inner region to be matched and outer bounds in which the inner region can move and still be considered matching.

    To get more details, consult [https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python.html| Applitools Eyes Documentation]

    These regions may be defined using the following keywords:
    - `Ignore Region By Coordinates`
    - `Ignore Region By Element`
    - `Ignore Region By Selector`
    - `Floating Region By Coordinates`
    - `Floating Region By Element`
    - `Floating Region By Selector`

    All of these keywords return a Target object, that must be passed as an argument of the chosen Check Keyword.
    
    For example, when using `Check Eyes Window` and defining `Ignore Region By Coordinates` and `Floating Region By Selector`.
 
        | {target}=         | Ignore Region By Coordinates | 20                      | 100   | 200 | 100 |
        | {target}=         | Floating Region By Selector  | //div[@id='my_element'] | xpath | 20  | 10  | 10 | 20 | {target} |
        | Check Eyes Window | Google Homepage              | target={target}         |          
    
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(
        self,
        apikey=None,
        appname=None,
        testname=None,
        library="SeleniumLibrary",
        matchlevel=None,
        enable_eyes_log=False,
        osname=None,
        browsername=None,
        serverurl=None,
    ):

        self.library_arguments = {
            "apikey": apikey,
            "appname": appname,
            "testname": testname,
            "library": library,
            "matchlevel": matchlevel,
            "enable_eyes_log": enable_eyes_log,
            "osname": osname,
            "browsername": browsername,
            "serverurl": serverurl,
        }

        variables.init()

