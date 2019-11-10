# Github Webhook Server

<p align=center>
    <img src="https://files.naresh1318.com/public/github_webhook_server/logo.png" alt="webhook_logo"/>
    <p align="center"> <b>Receives github webhook requests, authenticates them and runs the required deployment script</b> </p>
</p>


## Setup
1. Create a random secret key: `head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''`
2. Save it under project root: `echo "<your key>" >> github_webhook_keys.txt`
3. Create a deployment script under `./deployment_script/<name>.sh`. Look at the example provided
4. Change `webhook_endpoint`, `deployment_script` and `github_webhook_path` to the appropriate values
5. Create a python virtual environment (python 3.6 and up) on your server and install packages: `pip install -r requirements.txt`
6. Change the port you'd want to run the app from on `github_webhook_server.ini` (`http=127.0.0.1:<port>`)
7. Deploy: `uwsgi --ini github_webhook_server.ini`
8. Create a webhook for you repo by going into Settings -> Webhooks -> Add webhook
9. Specify the web server url along with the endpoint you set in step 3
10. Change content type to `application/json`
11. Copy secret key generated in step 1
12. Choose the event you's like
13. Hit Add webhook
