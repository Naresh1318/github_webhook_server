import os
import json

from flask import request, Flask

app = Flask(__name__)


@app.route("/github/topaz", methods=["POST"])
def topaz():
    """
    POST request from github received on push to master

    Returns:

    """
    import hmac
    import hashlib

    deployment_script = "./deployment_script/topaz.sh"
    github_webhook_path = "./github_webhook_keys.txt"
    with open(github_webhook_path) as f:
        # I don't really know why, but, \n is not removed when using readline when deployed on server
        local_key = f.read()
        if "\n" in local_key:
            local_key = local_key[:-1]
    digester = hmac.new(key=bytes(local_key, "utf-8"), msg=request.data, digestmod=hashlib.sha1)
    signature = digester.hexdigest()

    github_webhook_key = request.headers["X-Hub-Signature"]

    if not hmac.compare_digest("sha1=" + signature, github_webhook_key):
        return json.dumps({"success": False, "signature": signature, "key": github_webhook_key, "local_key": local_key}), 401, \
               {"ContentType": "application/json"}
    else:
        # Run deployment script
        os.system(f"sh {deployment_script}")
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
