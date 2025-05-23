import json

def handler(request):
    from urllib.parse import parse_qs

    # Enable CORS
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json"
    }

    try:
        query = parse_qs(request["queryStringParameters"])
        names = query.get("name", [])
    except Exception:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"error": "Invalid query parameters"})
        }

    # Load marks
    with open("students.json") as f:
        data = json.load(f)

    marks = [data.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"marks": marks})
    }

# Required for Vercel's Python runtime
handler = handler
