def reusable_response(data=None, message="Request successful", status="success"):
    return {
        "status": status,
        "message": message,
        "data": data
    }
