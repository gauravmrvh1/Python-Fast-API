def success_response(data, message="Success"):
    return {
        "success": True,
        "message": message,
        "data": data
    }
