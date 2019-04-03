*** Settings ***
Library     AppiumLibrary
Library     EyesLibrary
Library     SeleniumLibrary
Resource    resources/common.robot
Resource    resources/mobile.robot
Resource    resources/android.robot

*** Variable ***
&{LOGO}     id=hplogo                  xpath=//*[@id="hplogo"]

*** Test Cases ***
Check Window
    [Setup]                                         Setup                                                               Android Browser - Check Window
    Check Eyes Window                               Google Homepage
    [Teardown]                                      Teardown

Check Region
    [Setup]                                         Setup                                                               Android Browser - Check Region
    ${location}=                                    Get Element Location                                                ${LOGO.id}
    Check Eyes Region                               ${location['x']}                                                    ${location['y']}                                       300                                            200              Google Logo
    [Teardown]                                      Teardown

Check Region By Element
    [Setup]                                         Setup                                                               Android Browser - Check Region By Element
    ${logo}=                                        Get Webelement                                                      ${LOGO.id}
    Check Eyes Region By Element                    ${logo}                                                             Google Logo
    [Teardown]                                      Teardown

Check Region By Selector
    [Setup]                                         Setup                                                               Android Browser - Check Region By Selector
    Check Eyes Region By Selector                   ${LOGO.id}                                                          Google Logo
    [Teardown]                                      Teardown

Check Region In Frame By Selector
    [Setup]                                         Setup for Check Region in Frame                                     Android Browser - Check Region In Frame By Selector
    Check Eyes Region In Frame By Selector          iframeResult                                                        body                                                   Frame Elements                                 tag name
    [Teardown]                                      Teardown

Is Session Open
    [Setup]                                         Setup                                                               Android Browser - Opened Session
    ${is open}=                                     Eyes Session Is Open
    Should Be True                                  ${is open}
    [Teardown]                                      Teardown

Floating Region By Coordinates
    [Setup]                                         Setup                                                               Android Browser - Floating Region By Coordinates
    ${width}=                                       Get Window Width
    ${target}=                                      Floating Region By Coordinates                                      0                                                      0                                              100              70                         0     0    10    10
    Check Eyes Window                               Google Calendar                                                     target=${target}
    [Teardown]                                      Teardown

Floating Region By Element
    [Setup]                                         Setup                                                               Android Browser - Floating Region By Element
    ${element}=                                     Get Webelement                                                      ${LOGO.id}
    ${target}=                                      Floating Region By Element                                          ${element}                                             20                                             20               10                         10
    Check Eyes Window                               Google Calendar                                                     target=${target}
    [Teardown]                                      Teardown

Floating Region By Selector
    [Setup]                                         Setup                                                               Android Browser - Floating Region By Selector
    ${target}=                                      Floating Region By Selector                                         ${LOGO.id}                                             max_left_offset=20
    Check Eyes Window                               Google Calendar                                                     target=${target}
    [Teardown]                                      Teardown

*** Keywords ***
Setup
    [Arguments]                                     ${test name}
    Open Application                                remote_url=${REMOTE URL}
    ...                                             platformName=${PLATFORM NAME}
    ...                                             platformVersion=${PLATFORM VERSION}
    ...                                             deviceName=${DEVICE NAME}
    ...                                             browserName=Chrome
    ...                                             automationName=UiAutomator2
    Go To Url                                       http://www.google.pt
    Set Location                                    10                                                                  10
    Open Eyes Session                               ${API KEY}                                                          EyesLibrary                                            ${test name}                                   AppiumLibrary    enable_eyes_log=${true}

Setup for Check Region in Frame
    [Arguments]                                     ${test name}
    Open Application                                remote_url=${REMOTE URL}
    ...                                             platformName=${PLATFORM NAME}
    ...                                             platformVersion=${PLATFORM VERSION}
    ...                                             deviceName=${DEVICE NAME}
    ...                                             browserName=Chrome
    ...                                             automationName=UiAutomator2
    Go To Url                                       https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe
    Set Location                                    10                                                                  10
    Integrate SeleniumLibrary with AppiumLibrary
    Accept Cookies
    Open Eyes Session                               ${API KEY}                                                          EyesLibraryBaseline                                    ${test name}                                   AppiumLibrary    enable_eyes_log=${true}

Integrate SeleniumLibrary with AppiumLibrary
    Import Library                                  SeleniumLibrary
    Set Library Search Order                        SeleniumLibrary
    ${AppiumLibInstance}=                           Get Library Instance                                                AppiumLibrary
    ${SeleniumLibInstance}=                         Get Library Instance                                                SeleniumLibrary
    Call Method                                     ${SeleniumLibInstance._cache}                                       register                                               ${AppiumLibInstance._current_application()}    Appium

Accept Cookies
    Click Element                                   xpath=//*[@id="sncmp-banner-btn-agree"]
    Select Frame                                    xpath=//iframe[@id="iframeResult"]
    Select Frame                                    xpath=//iframe[@src="https://www.w3schools.com"]                                                
    Scroll Element Into View                        xpath=//*[text()="LEARN HTML"]
    Click Element                                   xpath=//*[@id="sncmp-banner-btn-agree"]
    Unselect Frame
    Unselect Frame

Teardown
    Close Application
    Close Eyes Session
