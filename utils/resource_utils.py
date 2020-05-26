def make_response(data):
    response = {
        "data": data,
        "status": "success",
        "message": ""
    }

    if isinstance(data, dict) and data.get("message"):
        response["message"] = data["message"]
        response["status"] = "failure"
        response["data"] = []

    return response
