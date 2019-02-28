*** Settings ***
Library           AppiumLibrary
#Library          SeleniumLibrary
Library           EyesLibrary
Resource          resources/common.robot
Resource          resources/mobile.robot

*** Variables ***
&{MAIN IMAGE}     id=fillingImg                                                   xpath=//img[@id="tortillaImg"]
&{FLOUR RADIO}    xpath=//label//img[@src="assets/taco-shell-flour-small.png"]


*** Test Cases ***
Check Window
    [Setup]                          Setup                              Mobile Hybrid - Check Window
    Check Eyes Window                Main Screen
    [Teardown]                       Teardown

Get Element Location
    [Setup]                          Setup                              Mobile Hybrid - Element Location
    ${height}=                       Get Window Height
    ${width}=                        Get Window Width
    Get Element Location             ${MAIN IMAGE.id}
    [Teardown]                       Teardown

Check Region
    [Setup]                          Setup                              Mobile Hybrid - Check Region
    ${location}=                     Get Element Location               ${MAIN IMAGE.id}
    Check Eyes Region                ${location['x']}                   ${location['y']}                            500    500    Image Region
    [Teardown]                       Teardown

Check Region By Element
    [Setup]                          Setup                              Mobile Hybrid - Check Region By Element
    ${element}=                      Get Webelement                     ${MAIN IMAGE.id}
    Check Eyes Region By Element     ${element}                         Image
    [Teardown]                       Teardown

Check Region By Selector
    [Setup]                          Setup                              Mobile Hybrid - Check Region By Selector
    Check Eyes Region By Selector    ${MAIN IMAGE.id}                   Image    
    [Teardown]                       Teardown

Is Session Open
    [Setup]                          Setup                              Mobile Hybrid - Opened Session
    ${is open}=                      Eyes Session Is Open
    Should Be True                   ${is open}
    [Teardown]                       Teardown

*** Keywords ***
Setup
    [Arguments]                      ${test name}
    Set Test Variable                ${APP PACKAGE}                     io.cordova.hellocordova
    Set Test Variable                ${APP ACTIVITY}                    io.cordova.hellocordova.MainActivity
    Open Application                 remote_url=${REMOTE URL}
    ...                              appPackage=${APP PACKAGE}
    ...                              appActivity=${APP ACTIVITY}
    ...                              nativeWebScreenshot=true
    ...                              deviceName=${DEVICE NAME}
    ...                              platformName=${PLATFORM NAME}
    ...                              automationName=UiAutomator2
    #...    autoGrantPermissions=true
   
    #...                                            chromedriverExecutableDir=C:/Users/sfnunes/Downloads/chromedrivers/2.34
    ${context}=    Get Current Context
    Switch To Context                WEBVIEW_io.cordova.hellocordova
    ${height}=    Get Window Height
    #Switch To Context                NATIVE_APP
    Set Location                     10                                     10
    Open Eyes Session                EyesLibrary
    ...                              ${test name}
    ...                              ${API KEY}
   ...                              AppiumLibrary
    ...                              includeEyesLog=true
    

Teardown
    Close Application
    Close Eyes Session

Wait And Click Element
    [Arguments]                      ${locator}
    Wait Until Element Is Visible    ${locator}
    Click Element                    ${locator}

#Integrate SeleniumLibrary With Appium
#                 Set Library Search Order                                        SeleniumLibrary
#                 ${AppiumLibInstance} =                                          Get Library Instance              AppiumLibrary
#                 ${SeleniumLibInstance} =                                        Get Library Instance              SeleniumLibrary
#                 Call Method                                                     ${SeleniumLibInstance._cache}     register           ${AppiumLibInstance._current_application()}    AppiumLibrary
