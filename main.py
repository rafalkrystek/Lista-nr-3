
### Skrypt: `api_test.py`

import os
import json
import subprocess

def run_curl_command(url):
    result = subprocess.run(['curl', '-s', '-w', '%{http_code}', url], capture_output=True, text=True)
    http_body = result.stdout[:-3]
    http_code = result.stdout[-3:]
    return http_body, int(http_code)

def check_response(endpoint, required_keys):
    url = f'https://jsonplaceholder.typicode.com/{endpoint}'
    body, status_code = run_curl_command(url)

    if status_code != 200:
        return False, f"HTTP status {status_code}"

    try:
        json_body = json.loads(body)
    except json.JSONDecodeError:
        return False, "Invalid JSON"

    if isinstance(json_body, list):
        json_body = json_body[0] if json_body else {}

    for key in required_keys:
        if key not in json_body:
            return False, f"Missing key: {key}"

    return True, "PASSED"

def main():
    tests = [
        ('posts/1', ['userId', 'id', 'title', 'body']),
        ('comments/1', ['postId', 'id', 'name', 'email', 'body']),
        ('users/1', ['id', 'name', 'username', 'email'])
    ]

    for i, (endpoint, keys) in enumerate(tests, 1):
        passed, message = check_response(endpoint, keys)
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: {status} - {message}")

if __name__ == "__main__":
    main()
