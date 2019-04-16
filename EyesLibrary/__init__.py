#!/usr/bin/env python

from .keywords import SessionKeywords, CheckKeywords, TargetKeywords
from .resources import variables
from .version import VERSION

_version_ = VERSION


class EyesLibrary(SessionKeywords, CheckKeywords, TargetKeywords):
    """
    EyesLibrary is a visual verification library for [http://robotframework.org/|Robot Framework] that leverages
    [https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python.html|Eyes-Selenium] and
    [http://robotframework.org/SeleniumLibrary/SeleniumLibrary.html|SeleniumLibrary] / 
    [http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html|AppiumLibrary].

    = Table of contents =
    - `Before running tests`
    - `Writing tests`
    - `Analysing the test results`
    - `Importing`
    - `Shortcuts`
    - `Keywords`

    = Before running tests =

    In order to run EyesLibrary, you have to create a [https://applitools.com/sign-up/|free account] with Applitools, to retrieve your API key.
    After signing up, you can get it from the [https://eyes.applitools.com/app/test-results/|Applitools Eyes Test Manager].
        
    You may want to read [https://applitools.com/docs|Applitools documentation] in order to better understand how Eyes works.
    
    Prior to running tests, EyesLibrary must be imported into your Robot test suite.

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
    - Match Timeout (matchtimeout)     
    - Save New Tests (save_new_tests)        

    Example:
        | Library | EyesLibrary | ApiKey | AppName | TestName | SeleniumLibrary | layout | ${true} | Windows | Firefox | https://myserver.com | 5000 | ${false} |
        
    = Writing tests =

    When writing the tests, the following structure must be adopted:
    
    1. *Open Eyes Session* 

    A browser or application must be running when opening the session. To open a browser/application, consult the documentation for SeleniumLibrary and/or AppiumLibrary.
    
    Afterwards, the session may be opened. See `Open Eyes Session`.                                                                                                      

    2. *Visual Checks* 

    Between opening and closing the session, you can run your visual checks.
    
    See `Check Eyes Region`, `Check Eyes Region By Element`, `Check Eyes Region By Selector`, `Check Eyes Region In Frame By Selector` and `Check Eyes Window`.
    
    You can also verify if there's an open session with `Eyes Session Is Open`.
    
    3. *Close Eyes Session*

    See `Close Eyes Session`.
    	
    == Test Case Example ==

    Above, we consider the *structure of a test*. For each test (=session), there may be as many checkpoints as you want. Here's a test case example:

        | =Keywords=         | =Parameters=       |
        | Open Browser       | http://google.com/ | gc      |                       
        | Open Eyes Session  | YourApplitoolsKey  | AppName | TestName |
        | Check Eyes Window  | Google Homepage    |                              
        | Close Eyes Session | 

    == Open vs Check keyword arguments ==

    Some arguments may be defined either on `Open Eyes Session` or on `Check keywords`.

    When defining an argument on Open Eyes Session, it will be aplied to _all the checks of that session_.

    On the other hand, when an argument is defined on a Check keyword, it will determine the behaviour _specific to that checkpoint_, not to the other checks of the session.

    When an argument is defined both on Open and Check keywords during the same test, the latter will be used for that specific checkpoint.

    == Check keywords ==

    These are the available Check keywords:
    - `Check Eyes Window`
    - `Check Eyes Region`
    - `Check Eyes Region By Element`
    - `Check Eyes Region By Selector`
    - `Check Eyes Region In Frame By Selector`

    == Using selectors ==

    Using the keywords `Check Eyes Region By Selector`, `Check Eyes Region In Frame By Selector`, `Ignore Region By Selector`, or `Floating Region By Selector`.
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
    
    == Defining Ignore and Floating regions ==

    A *Ignore Region* defines a region to be ignored on the checks, ie, to always be considered matching.

    A *Floating Region* defines an inner region to be matched and outer bounds in which the inner region can move and still be considered matching.

    To get more details, consult [https://applitools.com/docs/api/eyes-sdk/index-gen/classindex-selenium-python.html|Eyes Selenium SDK Documentation]

    These regions may be defined using the following keywords:
    - `Ignore Region By Coordinates`
    - `Ignore Region By Element`
    - `Ignore Region By Selector`
    - `Floating Region By Coordinates`
    - `Floating Region By Element`
    - `Floating Region By Selector`
    - `Ignore Caret`

    All of these keywords return a Target object, that must be passed as an argument of the chosen Check keyword.
    
    For example, when using `Check Eyes Window` and defining `Ignore Region By Coordinates` and `Floating Region By Selector`:
 
        | {target}=         | Ignore Region By Coordinates | 20                      | 100   | 200 | 100 |
        | {target}=         | Floating Region By Selector  | //div[@id='my_element'] | xpath | 20  | 10  | 10 | 20 | {target} |
        | Check Eyes Window | Google Homepage              | target={target}         |          
    
    = Analysing the test results =

    In order to review and analyse the test results, you have to access the  [https://eyes.applitools.com/app/test-results/|Test Manager].

    For more information on it, read the [https://applitools.com/docs/topics/test-manager/tm-overview.html|Test Manager Documentation].
    
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
        matchtimeout=None,
        save_new_tests=True,
    ):
        """
        EyesLibrary can be imported with optional arguments.
        
        - ``apikey``: Applitools API key
        - ``appname``: Application name
        - ``testname``: Test name
        - ``library``: Library used to open browser/application (SeleniumLibrary or AppiumLibrary)
        - ``matchlevel``: Match level used for the comparation of screenshots
        - ``enable_eyes_log``: Activation of Applitools Eyes SDK trace logs         
        - ``osname``: Overridden OS name
        - ``browsername``: Overridden Browser name
        - ``serverurl``: The URL of the Eyes server
        - ``matchtimeout``: Time until Eyes stops retrying the matching (milliseconds)
        - ``save_new_tests``: Automatically accepting new tests
        """

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
            "matchtimeout": matchtimeout,
            "save_new_tests": save_new_tests,
        }

        variables.init()

