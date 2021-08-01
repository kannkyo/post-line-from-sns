import logging
import os
import traceback

from line import notify
from secret import get_secret

level = os.environ.get('LOG_LEVEL', 'DEBUG')


def logger_level():
    print(f"set log level = {level}")
    if level == 'CRITICAL':
        return 50
    elif level == 'ERROR':
        return 40
    elif level == 'WARNING':
        return 30
    elif level == 'INFO':
        return 20
    elif level == 'DEBUG':
        return 10
    else:
        return 0


logger = logging.getLogger()
logger.setLevel(logger_level())


def lambda_handler(event, context):
    logger.debug(event)

    try:
        secret = get_secret(
            region_name="ap-northeast-1",
            secret_name=os.environ.get('LINE_SECRET_NAME'))

        message = event['Records'][0]['Sns']['Message']
        print("From SNS: " + message)

        response = notify(token=secret['api_key'], message=message)

        if response == None:
            return {'status_code': '200'}
        else:
            return {'status_code': response.status_code, 'reason': response.reason}

    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


if __name__ == "__main__":
    lambda_handler(None, None)
