*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Output Should Contain  []

Register With Already Taken Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  UserInputError: Username and password are invalid

Register With Too Short Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters

*** Keywords ***