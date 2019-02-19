*** Settings ***
Library     AppiumLibrary
Library     EyesLibrary
Resource    resources/common.robot
Resource    resources/mobile.robot

*** Test Cases ***
Check Window
    [Setup]                          Setup                                  Mobile Browser - Check Window
    Check Eyes Window                Google Homepage
    [Teardown]                       Teardown
    
Check Region
    [Setup]                          Setup                   Mobile Browser - Check Region 
    Check Eyes Region	//*[@id="hplogo"]    300    50    Google Logo
    [Teardown]        Teardown

Check Region By Element
    [Setup]                          Setup                                  Mobile Browser - Check Region By Element
    ${logo}=    EyesLibrary.Get Element    xpath    //*[@id="hplogo"] 
    Check Eyes Region By Element	${logo}    Google Logo
    [Teardown]                       Teardown

Check Region By Selector
    [Setup]                          Setup                                  Mobile Browser - Check Region By Selector
    Check Eyes Region By Selector    xpath                                  //*[@id="hplogo"]                            Google Logo
    [Teardown]                       Teardown

Is Session Open
    [Setup]                          Setup                                  Mobile Browser - Opened Session
    ${is open}=                      Eyes Session Is Open
    Should Be True                   ${is open}
    [Teardown]                       Teardown

*** Keywords ***
Setup
    [Arguments]                      ${test name}
    Open Application                 remote_url=${REMOTE URL}
    ...                              platformName=${PLATFORM NAME}
    ...                              platformVersion=${PLATFORM VERSION}
    ...                              deviceName=${DEVICE NAME}
    ...                              browserName=Chrome
    ...                              automationName=UiAutomator2
    Go To Url                        http://www.google.pt
    Set Location                     10                                     10                                           
    Open Eyes Session                EyesLibrary                            ${test name}                                 ${API KEY}     AppiumLibrary

Teardown
    Close Application
    Close Eyes Session
