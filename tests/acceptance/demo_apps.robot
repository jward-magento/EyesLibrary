*** Settings ***
Library           AppiumLibrary
Library           EyesLibrary
Resource          resources/common.robot
Resource          resources/mobile.robot

*** Test Cases ***
Contact Manager
    [Setup]    Open Application      remote_url=${REMOTE URL}
    ...                              appPackage=com.example.android.contactmanager
    ...                              appActivity=com.example.android.contactmanager.ContactManager
    ...                              nativeWebScreenshot=true
    ...                              deviceName=${DEVICE NAME}
    ...                              platformName=${PLATFORM NAME}
    ...                              automationName=UiAutomator2
    @{CONTEXTS}=    Get Contexts
    [Teardown]    Close Application

Orange Demo App
    [Setup]    Open Application      remote_url=${REMOTE URL}
    ...                              appPackage=com.netease.qa.orangedemo
    ...                              appActivity=com.netease.qa.orangedemo.MainActivity
    ...                              nativeWebScreenshot=true
    ...                              deviceName=${DEVICE NAME}
    ...                              platformName=${PLATFORM NAME}
    ...                              automationName=UiAutomator2
    @{CONTEXTS}=    Get Contexts
    [Teardown]    Close Application
   