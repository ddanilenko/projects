def make_response(data):
    response = {
        "data": [],
        "status": "failure",
        "message": ""
    }

    if isinstance(data, list):
        response["data"] = data
        response["status"] = "success"
    elif isinstance(data, dict) and data.get("message"):
        response["message"] = data["message"]
    else:
        response["data"] = [data]
        response["status"] = "success"

    return response
