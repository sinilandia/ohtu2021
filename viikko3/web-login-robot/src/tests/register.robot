*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Tests and Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  siniliu
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  s 
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Credentials
    Register Should Fail With Message  Too short

Register With Valid Username And Too Short Password
    Set Username  sininene 
    Set Password  s
    Set Password Confirmation  s
    Submit Credentials
    Register Should Fail With Message  Too short

Register With Nonmatching Password And Password Confirmation
    Set Username  sini 
    Set Password  salasana123
    Set Password Confirmation  sala
    Submit Credentials
    Register Should Fail With Message   Passwords do not match

*** Keywords ***
Reset Tests and Go To Register Page
    Go To Reset Page
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message 
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}