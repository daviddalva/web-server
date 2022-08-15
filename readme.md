
to install requirements use: pip install -r .\requirements.txt
##############################
to use the app set env variables:
1. createTransactionURL
by doing windows: 
[System.Environment]::SetEnvironmentVariable('createTransactionURL','https://apidemo.gamaf.co.il/gppartner/v1/api/index.php/create-transaction-request')

[System.Environment]::SetEnvironmentVariable('get_transaction_request_statusURL','https://apidemo.gamaf.co.il/gppartner/v1/api/index.php/get-transaction-request-status')

[System.Environment]::SetEnvironmentVariable('keycloak_url','https://login-test.gamaf.co.il/auth/realms/login-test.gamaf.co.il/protocol/openid-connect/token')


[System.Environment]::GetEnvironmentVariable('createTransactionURL')
[System.Environment]::GetEnvironmentVariable('get_transaction_request_statusURL')
[System.Environment]::GetEnvironmentVariable('keycloak_url')
##############################