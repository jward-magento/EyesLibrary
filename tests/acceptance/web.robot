*** Settings ***
Resource    resources/common.robot
Library     SeleniumLibrary
Library     EyesLibrary    ${API KEY}                 EyesLibrary

*** Variables ***
&{LOGO}     id=hplogo                 xpath=//*[@id="hplogo"]

*** Test Cases ***
Check Window
    [Setup]                          Setup                      Web - Check Window
    Check Eyes Window                Google Homepage
    [Teardown]                       Teardown

Check Region
    [Setup]                          Setup                      Web - Check Region
    ${x}=                            Get Horizontal Position    ${LOGO.id}
    ${y}=                            Get Vertical Position      ${LOGO.id}
    Check Eyes Region                ${x}                       ${y}                              400             200                  Google Logo
    [Teardown]                       Teardown

Check Region By Element
    [Setup]                          Setup                      Web - Check Region By Element
    ${logo}=                         Get WebElement             ${LOGO.id}
    Check Eyes Region By Element     ${logo}                    Google Logo
    [Teardown]                       Teardown

Check Region By Selector
    [Setup]                          Setup                      Web - Check Region By Selector
    Check Eyes Region By Selector    ${LOGO.id}                 Google Logo
    [Teardown]                       Teardown

Is Session Open
    [Setup]                          Setup                      Web - Opened Session
    ${is open}=                      Eyes Session Is Open
    Should Be True                   ${is open}
    [Teardown]                       Teardown
    
Batch Test 1
    [Setup]                          Setup with BatchName                      Web - Batch Test 1    Batch Test
    Check Eyes Window                Homepage
    [Teardown]                       Teardown
    
Batch Test 2
    [Setup]                          Setup with BatchName                      Web - Batch Test 2    Batch Test
    Check Eyes Region By Selector    ${LOGO.id}                 Logo
    [Teardown]                       Teardown

*** Keywords ***
Setup
    [Arguments]                      ${test name}
    Open Browser                     http://www.google.com      gc
    #Open Browser                     http://www.google.com      ff
    Maximize Browser Window
    Open Eyes Session                ${API KEY}                 EyesLibrary                       ${test name}    matchlevel=layout    enable_eyes_log=true
    #baselinename=googlePageMax
    
Setup with BatchName
    [Arguments]                      ${test name}    ${batchname}
    Open Browser                     http://www.google.com      gc
    Maximize Browser Window
    Open Eyes Session                testname=${test name}    matchlevel=layout    enable_eyes_log=true    batchname=${batchname}

Teardown
    Close All Browsers
    Close Eyes Session
