*** Settings ***
Resource              resources/common.robot
Library               SeleniumLibrary
Library               EyesLibrary                                  ${API KEY}    Triangles                           matchlevel=layout    enable_eyes_log=${true}

*** Variables ***
${URL}                http://joel-oliveira.github.io/triangles/
${TRIANGLE DIV ID}    triangle_frame
${SIDE 1 ID}          side1
${SIDE 2 ID}          side2
${SIDE 3 ID}          side3

*** Test Cases ***
Equilateral Triangle - Chrome
    [Setup]                        Setup                                    Equilateral Triangle                    gc                               Chrome Baseline
    Check Equilateral Triangle
    [Teardown]                     Teardown

Equilateral Triangle - Firefox
    [Setup]                        Setup                                    Equilateral Triangle                    ff                               Chrome Baseline
    Check Equilateral Triangle
    [Teardown]                     Teardown

Equilateral Triangle - Edge
    [Setup]                        Setup                                    Equilateral Triangle                    edge                             Chrome Baseline
    Check Equilateral Triangle
    [Teardown]                     Teardown

Isosceles Triangle - Chrome
    [Setup]                        Setup                                    Isosceles Triangle                      gc
    Check Isosceles Triangle
    [Teardown]                     Teardown

Isosceles Triangle - Firefox
    [Setup]                        Setup                                    Isosceles Triangle                      ff                               Chrome Baseline
    Check Isosceles Triangle
    [Teardown]                     Teardown

Isosceles Triangle - Edge
    [Setup]                        Setup                                    Isosceles Triangle                      edge                             Chrome Baseline
    Check Isosceles Triangle
    [Teardown]                     Teardown

Scalene Triangle - Chrome
    [Setup]                        Setup                                    Scalene Triangle                        gc
    Check Scalene Triangle
    [Teardown]                     Teardown

Scalene Triangle - Firefox
    [Setup]                        Setup                                    Scalene Triangle                        ff                               Chrome Baseline
    Check Scalene Triangle
    [Teardown]                     Teardown

Scalene Triangle - Edge
    [Setup]                        Setup                                    Scalene Triangle                        edge                             Chrome Baseline
    Check Scalene Triangle
    [Teardown]                     Teardown

Invalid Triangle - Chrome
    [Setup]                        Setup                                    Invalid Triangle                        gc
    Check Invalid Triangle
    [Teardown]                     Teardown

Invalid Triangle - Firefox
    [Setup]                        Setup                                    Invalid Triangle                        ff                               Chrome Baseline
    Check Invalid Triangle
    [Teardown]                     Teardown

Invalid Triangle - Edge
    [Setup]                        Setup                                    Invalid Triangle                        edge                             Chrome Baseline
    Check Invalid Triangle
    [Teardown]                     Teardown


#Equilateral Triangle Baseline - Chrome
#                     [Setup]                                      Setup         Equilateral Triangle                  gc                   Chrome Baseline
#                     Check Equilateral Triangle
#                     [Teardown]                                   Teardown

Isosceles Triangle Against Equilateral Triangle - Chrome
    [Setup]                        Setup                                    Equilateral Triangle                    gc
    Check Isosceles Triangle
    [Teardown]                     Teardown

Full Page - Chrome
    [Setup]                        Setup                                    Full Page                               gc    stitchmode=css
    Click Element                  reset
    Check Eyes Window              Full Page                                force_full_page_screenshot=${true}
    [Teardown]                     Teardown

Full Page - Firefox
    [Setup]                        Setup                                    Full Page                               ff                               Chrome Baseline    css
    Click Element                  reset
    Check Eyes Window              Full Page                                force_full_page_screenshot=${true}
    [Teardown]                     Teardown

Full Page - Edge
    [Setup]                        Setup                                    Full Page                               edge                             Chrome Baseline    css
    Click Element                  reset
    Wait Until Keyword Succeeds    30s                                      5s    Check Eyes Window              Full Page                                force_full_page_screenshot=${true}
    [Teardown]                     Teardown

Full Page After Drawing One Triangle - Chrome
    [Setup]                        Setup                                    Full Page After Drawing One Triangle    gc    stitchmode=css
    Click Element                  reset
    Draw Triangle                  5                                        5                                       9
    Check Eyes Window              Full Page                                force_full_page_screenshot=${true}
    [Teardown]                     Teardown

Full Page After Drawing One Triangle - Firefox
    [Setup]                        Setup                                    Full Page After Drawing One Triangle    ff                               Chrome Baseline    css
    Click Element                  reset
    Draw Triangle                  5                                        5                                       9
    Check Eyes Window              Full Page                                force_full_page_screenshot=${true}
    [Teardown]                     Teardown

Full Page After Drawing One Triangle - Edge
    [Setup]                        Setup                                    Full Page After Drawing One Triangle    edge                             Chrome Baseline    css
    Click Element                  reset
    Draw Triangle                  5                                        5                                       9
    Wait Until Keyword Succeeds    30s                                      5s    Check Eyes Window              Full Page                                force_full_page_screenshot=${true}
    [Teardown]                     Teardown

#Full Page Baseline - Chrome
#                     [Setup]                                      Setup         Full Page                             gc
#                     Check Eyes Window                            Full Page     force_full_page_screenshot=${true}
#                     [Teardown]                                   Teardown

Full Page After Drawing Two Triangles - Chrome
    [Setup]                        Setup                                    Full Page                               gc    stitchmode=css
    Click Element                  reset
    Draw Triangle                  4                                        4                                       0
    Draw Triangle                  9                                        10                                      11
    Check Eyes Window              Full Page After Drawing Two Triangles    force_full_page_screenshot=${true}
    [Teardown]                     Teardown

*** Keywords ***
Setup
    [Arguments]                    ${test name}                             ${browser}                              ${baseline name}=${NONE}         ${stitchmode}=${NONE}
    Open Browser                   ${URL}                                   ${browser}
    Maximize Browser Window
    Open Eyes Session              testname=${test name}                    baselinename=${baseline name}           stitchmode=${stitchmode}

Teardown
    Close All Browsers
    Close Eyes Session

Draw Triangle
    [Arguments]                    ${side 1}                                ${side 2}                               ${side 3}
    Input Text                     ${SIDE 1 ID}                             ${side 1}
    Input Text                     ${SIDE 2 ID}                             ${side 2}
    Input Text                     ${SIDE 3 ID}                             ${side 3}
    Click Button                   Draw Triangle

Check Equilateral Triangle
    Draw Triangle                  3                                        3                                       3
    Wait Until Keyword Succeeds    30s                                      5s                                      Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Equilateral Triangle

Check Isosceles Triangle
    Draw Triangle                  4                                        4                                       5
    Wait Until Keyword Succeeds    30s                                      5s                                      Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Isosceles Triangle

Check Scalene Triangle
    Draw Triangle                  3                                        6                                       4
    Wait Until Keyword Succeeds    30s                                      5s                                      Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Scalene Triangle

Check Invalid Triangle
    Draw Triangle                  3                                        3                                       10
    Wait Until Keyword Succeeds    30s                                      5s                                      Check Eyes Region By Selector    ${TRIANGLE DIV ID}       Invalid Triangle