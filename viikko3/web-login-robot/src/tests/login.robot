*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle   
    Set Password  kalle12345
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  kal
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login After Successful Registration
    Create User  kallekalle  kalle12345
    Go To Login Page
    Login Page Should Be Open
    Set Username  kallekalle
    Set Password  kalle12345
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Create User  kal  kalle12345
    Go To Login Page
    Login Page Should Be Open
    Set Username  kal
    Set Password  kalle12345
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle12345
    Go To Login Page
    Login Page Should Be Open