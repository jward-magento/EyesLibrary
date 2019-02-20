*** Settings ***
Library          AppiumLibrary
Library          SeleniumLibrary
Library          EyesLibrary
Resource         resources/common.robot
Resource         resources/mobile.robot

*** Variables ***
&{MAIN IMAGE}    id=fillingImg             xpath=//img[@id="fillingImg"]

*** Test Cases ***
Check Window
    [Setup]                                        Setup                              Mobile Hybrid - Check Window
    Check Eyes Window                              Main Screen
    [Teardown]                                     Teardown

Get Element Location
    [Setup]                                        Setup                              Mobile Hybrid - Element Location
    ${height}=                                     Get Window Height
    ${width}=                                      Get Window Width
    Get Element Location                           xpath=${MAIN IMAGE.xpath}
    [Teardown]                                     Teardown

Check Region
    [Setup]                                        Setup                              Mobile Hybrid - Check Region
    Check Eyes Region                              ${MAIN IMAGE.xpath}                500                                         500                                            Image Region
    [Teardown]                                     Teardown

Check Region By Element
    [Setup]                                        Setup                              Mobile Hybrid - Check Region By Element
    ${height} =                                    Get Window Height
    ${width} =                                     Get Window Width
    ${button}=                                     EyesLibrary.Get Element            id                                          ${MAIN IMAGE.id}
    Check Eyes Region By Element                   ${button}                          Image
    [Teardown]                                     Teardown

Check Region By Selector
    [Setup]                                        Setup                              Mobile Hybrid - Check Region By Selector
    Check Eyes Region By Selector                  id                                 ${MAIN IMAGE.id}                            Image
    [Teardown]                                     Teardown

Is Session Open
    [Setup]                                        Setup                              Mobile Hybrid - Opened Session
    ${is open}=                                    Eyes Session Is Open
    Should Be True                                 ${is open}
    [Teardown]                                     Teardown

*** Keywords ***
Setup
    [Arguments]                                    ${test name}
    Set Test Variable                              ${APP PACKAGE}                     io.cordova.hellocordova
    Set Test Variable                              ${APP ACTIVITY}                    io.cordova.hellocordova.MainActivity
    Open Application                               remote_url=${REMOTE URL}
    ...                                            appPackage=${APP PACKAGE}
    ...                                            appActivity=${APP ACTIVITY}
    ...                                            nativeWebScreenshot=true
    ...                                            deviceName=${DEVICE NAME}
    ...                                            platformName=${PLATFORM NAME}
    ...                                            automationName=UiAutomator2
    Open Eyes Session                              EyesLibrary                        ${test name}                                ${API KEY}                                     AppiumLibrary    includeEyesLog=true
    Switch To Context                              WEBVIEW_io.cordova.hellocordova


Teardown
    Close Application
    Close Eyes Session

Wait And Click Element
    [Arguments]                                    ${locator}
    AppiumLibrary.Wait Until Element Is Visible    ${locator}
    AppiumLibrary.Click Element                    ${locator}

Integrate SeleniumLibrary With Appium
    Set Library Search Order                       SeleniumLibrary
    ${AppiumLibInstance} =                         Get Library Instance               AppiumLibrary
    ${SeleniumLibInstance} =                       Get Library Instance               SeleniumLibrary
    Call Method                                    ${SeleniumLibInstance._cache}      register                                    ${AppiumLibInstance._current_application()}    AppiumLibrary
