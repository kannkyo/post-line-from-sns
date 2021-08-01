import logging
import requests

logger = logging.getLogger()


def notify(token: str, message: str):
    end_point = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {message}'}
    response = requests.post(end_point, headers=headers, data=data)

    logger.info(response.status_code)
    logger.info(response.text)

    return response
