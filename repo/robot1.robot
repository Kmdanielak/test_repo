*** Settings ***
Library  SeleniumLibrary



*** Variables ***
#$
#@
#&
${error_message}                       Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
Poprawne logowanie
    Open Browser                        https://pl.wikipedia.org    chrome
    Wait Until Element Is Visible       pt-login                    3                           No mamy blad
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
    Capture Page Screenshot             screen.png
    Close Browser


*** Test Cases ***
Niepoprawne logowanie
    Open Browser                        https://pl.wikipedia.org    chrome
    Wait Until Element Is Visible       pt-login                    3                           No mamy blad
    Click Element                       pt-login
    ${my_value}                         Get Text                    wpName1
    Should Be Empty                     ${my_value}
    Input Text                          wpName1                     RobotTests
    ${my_value}                         Get Text                    //*[@id="wpPassword1"]
    Should Be Empty                     ${my_value}
    Input Password                      //*[@id="wpPassword1"]      123123
    Checkbox Should Not Be Selected     wpRemember
    Select Checkbox                     wpRemember
    Click Button                        //*[@id="wpLoginAttempt"]
    Wait Until Element Is Visible       //*[@id="userloginForm"]/form/div[1]                    3
    ${my_error_message}                 Get Text                    //*[@id="userloginForm"]/form/div[1]
    Log To Console                      ${my_error_message}
    Log                                 ${my_error_message}
    Should Be Equal As Strings          ${my_error_message}         ${error_message}
    Capture Page Screenshot             screen.png
    Close Browser






