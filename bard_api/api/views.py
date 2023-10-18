from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
from .serializers import BardApiSerializer
import os


class BardApiView(APIView):
    conversation_id = None

    def post(self, request):
        cookie_dict = {
            "__Secure-1PSID": os.getenv('BARD_PSID_KEY'),
            "__Secure-1PSIDTS": os.getenv('BARD_PSIDTS_KEY')
        }

        question = request.data.get('question', 'Olá')

        try:
            bard_response = BardCookies(
                cookie_dict=cookie_dict).get_answer(question)

            answer = bard_response['content'].split('\r\n')

            data_object = {
                'answer': answer,
                'conversation_id': bard_response['conversation_id'],
            }

            response = {
                'bard': data_object,
            }

            BardApiView.conversation_id = bard_response['conversation_id']

            return Response(response)
        except Exception as error:
            return Response({'error': str(error)})
