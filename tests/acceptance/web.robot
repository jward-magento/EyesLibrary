*** Settings ***
Library          SeleniumLibrary
Library          EyesLibrary
Resource         resources/common.robot

*** Variables ***
${LOGO XPATH}    //*[@id="hplogo"]

*** Test Cases ***
Check Window
    [Setup]                            Setup                      Web - Check Window
    Check Eyes Window                  Google Homepage
    [Teardown]                         Teardown

Check Region
    [Setup]                            Setup                      Web - Check Region
    Check Eyes Region	               ${LOGO XPATH}              400                               200            Google Logo
    [Teardown]                         Teardown

Check Region By Element
    [Setup]                            Setup                      Web - Check Region By Element
    ${logo}=                           EyesLibrary.Get Element    xpath                             ${LOGO XPATH}
    Check Eyes Region By Element       ${logo}                    Google Logo
    [Teardown]                         Teardown

Check Region By Selector
    [Setup]                            Setup                      Web - Check Region By Selector
    Check Eyes Region By Selector      xpath                      ${LOGO XPATH}                     Google Logo
    [Teardown]                         Teardown

Is Session Open
    [Setup]                            Setup                      Web - Opened Session
    ${is open}=                        Eyes Session Is Open
    Should Be True                     ${is open}
    [Teardown]                         Teardown

*** Keywords ***
Setup
    [Arguments]                        ${test name}
    Open Browser                       http://www.google.com      gc
    Open Eyes Session                  EyesLibrary                ${test name}                      ${API KEY}

Teardown
    Close All Browsers
    Close Eyes Session
