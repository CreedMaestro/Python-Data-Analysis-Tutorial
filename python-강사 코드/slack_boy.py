import requests
import json

def send_slack_message():
    slack_url = " https://hooks.slack.com/services/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"
    message = """
    뉴스봇 테스트
    """ 

    payloads = {
        "text": message,
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )
    
    print(response)
        
send_slack_message()