*** Settings ***
Library     AppiumLibrary
Library     EyesLibrary
Resource    resources/common.robot
Resource    resources/mobile.robot

*** Test Cases ***
Check Window
    [Setup]                          Setup                            Mobile App - Check Window
    Check Eyes Window                Google Calendar
    [Teardown]                       Teardown
    
Check Region
    [Setup]                          Setup                   Mobile App - Check Region 
    Check Eyes Region	//android.widget.ImageView[@content-desc="next page"]    150  	150    Next Page Button
    [Teardown]        Teardown

Is Session Open
    [Setup]                          Setup                            Mobile App - Opened Session
    ${is open}=                      Eyes Session Is Open
    Should Be True                   ${is open}
    [Teardown]                       Teardown

*** Keywords ***
Setup
    [Arguments]                      ${test name}
    Set Test Variable                ${APP PACKAGE}                   com.google.android.calendar
    Set Test Variable                ${APP ACTIVITY}                  com.android.calendar.AllInOneActivity
    Open Application                 remote_url=${REMOTE URL}
    ...                              appPackage=${APP PACKAGE}
    ...                              appActivity=${APP ACTIVITY}
    ...                              nativeWebScreenshot=true
    ...                              deviceName=${DEVICE NAME}
    ...                              platformName=${PLATFORM NAME}
    ...                              automationName=UiAutomator2
    Open Eyes Session                EyesLibrary                      ${test name}                             ${API KEY}     AppiumLibrary    includeEyesLog=true

Teardown
    Close Application
    Close Eyes Session
