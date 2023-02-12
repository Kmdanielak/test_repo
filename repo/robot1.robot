*** Settings ***
Library  SeleniumLibrary



*** Variables ***
#${}
#@
#&

*** Keywords ***



*** Test Cases ***
Test 1
    Open Browser                        https://pl.wikipedia.org    chrome
    Click Element                       pt-login
    ${my_value}                         Get Text                    wpName1
    Should Be Empty                     ${my_value}
    Input Text                          wpName1                     RobotTests
    ${my_value}                         Get Text                    //*[@id="wpPassword1"]
    Should Be Empty                     ${my_value}
    Input Password                      //*[@id="wpPassword1"]      RobotFramework
    Checkbox Should Not Be Selected     wpRemember
    Select Checkbox                     wpRemember
    Click Button                        //*[@id="wpLoginAttempt"]
    Close Browser






