def success_response(data, message="Data Fetched Successfully.", cached="false"):
    return {
        "success": True,
        "message": message,
        "cached": cached,
        "data": data,
    }
