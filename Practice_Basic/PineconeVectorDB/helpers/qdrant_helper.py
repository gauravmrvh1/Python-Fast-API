def normalize_qdrant_response(response):
    if hasattr(response, "points"):
        return response.points
    elif isinstance(response, tuple):
        return response[0]
    elif isinstance(response, list):
        return response
    return response