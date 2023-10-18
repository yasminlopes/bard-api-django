from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
from .serializers import BardApiSerializer
import os


class BardApiView(APIView):
    history = {}

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
                'question': question,
                'answer': answer,
                'conversation_id': bard_response['conversation_id'],
            }

            response = {
                'bard': data_object,
            }

            BardApiView.add_to_history(bard_response['conversation_id'], question, answer)

            return Response(response)
        except Exception as error:
            return Response({'error': str(error)})

    def get(self, request, id_conversation):
        if id_conversation not in BardApiView.history:
            return Response({ 'error': 'Conversation ID not found' })
        
        return Response(BardApiView.history[id_conversation])
    
    def put(self, request, id_conversation):
        if id_conversation not in BardApiView.history:
            return Response({ 'error': 'Conversation ID not found' })

        question = request.data.get('question', 'Olá')

        bard_response = BardCookies({
            "__Secure-1PSID": os.getenv('BARD_PSID_KEY'),
            "__Secure-1PSIDTS": os.getenv('BARD_PSIDTS_KEY')
        }).get_answer(question)

        answer = bard_response['content'].split('\r\n')

        BardApiView.add_to_history(id_conversation, question, answer)

        return Response(BardApiView.history[id_conversation])
    
    @staticmethod
    def add_to_history(conversation_id, question, answer):
        if conversation_id not in BardApiView.history:
            BardApiView.history[conversation_id] = []

        BardApiView.history[conversation_id].append({'question': question, 'answer': answer})