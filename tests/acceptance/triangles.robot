*** Settings ***
Resource              resources/common.robot
Library               SeleniumLibrary
Library               EyesLibrary                                  ${API KEY}    EyesLibrary    matchlevel=layout    enable_eyes_log=${true}

*** Variables ***
${URL}                http://joel-oliveira.github.io/triangles/
${TRIANGLE DIV ID}    triangle_frame
${SIDE 1 ID}          side1
${SIDE 2 ID}          side2
${SIDE 3 ID}          side3

*** Test Cases ***
Equilateral Triangle - Chrome
    [Setup]                          Setup                    Equilateral Triangle             Equilateral Test Draft 1    gc
    Check Equilateral Triangle
    [Teardown]                       Teardown

Equilateral Triangle - Firefox
    [Setup]                          Setup                    Equilateral Triangle             Equilateral Test Draft 1    ff
    Check Equilateral Triangle
    [Teardown]                       Teardown
    
Equilateral Triangle - Edge
    [Setup]                          Setup                    Equilateral Triangle             Equilateral Test Draft 1    edge
    Check Equilateral Triangle
    [Teardown]                       Teardown

Isosceles Triangle - Chrome
    [Setup]                          Setup                    Isosceles Triangle               Isosceles Test Draft 1      gc
    Check Isosceles Triangle
    [Teardown]                       Teardown

Isosceles Triangle - Firefox
    [Setup]                          Setup                    Isosceles Triangle               Isosceles Test Draft 1      ff
    Check Isosceles Triangle
    [Teardown]                       Teardown

Isosceles Triangle - Edge
    [Setup]                          Setup                    Isosceles Triangle               Isosceles Test Draft 1      edge
    Check Isosceles Triangle
    [Teardown]                       Teardown

Scalene Triangle - Chrome
    [Setup]                          Setup                    Scalene Triangle               Scalene Test Draft 1      gc
    Check Scalene Triangle
    [Teardown]                       Teardown

Scalene Triangle - Firefox
    [Setup]                          Setup                    Scalene Triangle               Scalene Test Draft 1      ff
    Check Scalene Triangle
    [Teardown]                       Teardown

Scalene Triangle - Edge
    [Setup]                          Setup                    Scalene Triangle               Scalene Test Draft 1      edge
    Check Scalene Triangle
    [Teardown]                       Teardown
    
Invalid Triangle - Chrome
    [Setup]                          Setup                    Invalid Triangle               Invalid Test Draft 1      gc
    Check Invalid Triangle
    [Teardown]                       Teardown

Invalid Triangle - Firefox
    [Setup]                          Setup                    Invalid Triangle               Invalid Test Draft 1      ff
    Check Invalid Triangle
    [Teardown]                       Teardown

Invalid Triangle - Edge
    [Setup]                          Setup                    Invalid Triangle               Invalid Test Draft 1      edge
    Check Invalid Triangle
    [Teardown]                       Teardown
    
    
Equilateral Triangle Baseline - Chrome
    [Setup]                          Setup                    Equilateral Triangle               Equilateral Test Draft 2      gc
    Check Equilateral Triangle
    [Teardown]                       Teardown
    
Isosceles Triangle Against Equilateral Triangle - Chrome
    [Setup]                          Setup                    Equilateral Triangle               Equilateral Test Draft 2      gc
    Check Isosceles Triangle
    [Teardown]                       Teardown

*** Keywords ***
Setup
    [Arguments]                      ${test name}             ${baseline name}                 ${browser}
    Open Browser                     ${URL}                   ${browser}
    Maximize Browser Window
    Open Eyes Session                testname=${test name}    baselinename=${baseline name}

Teardown
    Close All Browsers
    Close Eyes Session

Draw Triangle
    [Arguments]                      ${side 1}                ${side 2}                        ${side 3}
    Input Text                       ${SIDE 1 ID}             ${side 1}
    Input Text                       ${SIDE 2 ID}             ${side 2}
    Input Text                       ${SIDE 3 ID}             ${side 3}
    Click Button                     Draw Triangle

Check Equilateral Triangle
    Draw Triangle                    3                        3                                3
    Wait Until Keyword Succeeds    30s    5s    Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Equilateral Triangle

Check Isosceles Triangle
    Draw Triangle                    4                        4                                5
    Wait Until Keyword Succeeds    30s    5s    Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Isosceles Triangle

Check Scalene Triangle
    Draw Triangle                    3                        6                                4
    Wait Until Keyword Succeeds    30s    5s    Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Scalene Triangle
    
Check Invalid Triangle
    Draw Triangle                    3                        3                                10
    Wait Until Keyword Succeeds    30s    5s    Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Invalid Triangle