from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

import requests, json

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                answer = get_answer(event.message.text)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=answer)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def get_answer(message_text):
    """
    {
        "answers": [
            {
                "answer": "No good match found in the KB",
                "questions": [],
                "score": 0
            }
        ]
    }
    :param message_text: line bot message
    :return: answer
    """
    url = "https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/{YOUR QNA MAKER UUID}/generateAnswer"

    # call post service with headers and params
    response = requests.post(
                   url,
                   json.dumps({'question': message_text}),
                   headers={
                       'Content-Type': 'application/json',
                       'Ocp-Apim-Subscription-Key': '{YOUR KEY}'
                   }
               )

    data = response.json()

    try:
        if "error" in data:
            # {
            #   'error':{
            #       'message': 'Rate limit is exceeded. Try again later.',
            #       'code': 'RateLimitExceeded'
            #    }
            # }
            return data["error"]["message"]

        answer = data['answers'][0]['answer']

        return answer

    except Exception:

        return "Error occurs when finding answer"



