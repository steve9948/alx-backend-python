import logging
from datetime import datetime
import os

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        log_dir = os.path.join(os.path.dirname(__file__), 'logs')
        os.makedirs(log_dir, exist_ok=True)  # Ensure the directory exists
        log_file = os.path.join(log_dir, 'requests.log')
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)
        response = self.get_response(request)
        return response
