from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
from .serializers import RespostaSerializer
import os

class RespostaAPIView(APIView):
    conversation_id = None  # inicializa a variável conversation_id como None

    def post(self, request):
        psid_key = os.getenv('BARD_PSID_KEY')
        psidts_key = os.getenv('BARD_PSIDTS_KEY')

        cookie_dict = {
            "__Secure-1PSID": psid_key,
            "__Secure-1PSIDTS": psidts_key,
        }

        pergunta = request.data.get('pergunta', 'Olá')

        if RespostaAPIView.conversation_id:  # verifica se há um conversation_id armazenado
            cookie_dict['conversation_id'] = RespostaAPIView.conversation_id  # adiciona o conversation_id ao cookie_dict

        try:
            resposta_json = BardCookies(cookie_dict=cookie_dict).get_answer(pergunta)
            content = resposta_json['content'].split('\r\n')
            resposta_dict = {
                'content': content,
                'conversation_id': resposta_json['conversation_id'],
            }
            response_dict = {
                'resposta': resposta_dict,
            }

            RespostaAPIView.conversation_id = resposta_json['conversation_id']  # armazena o novo conversation_id

            return Response(response_dict)
        except Exception as error:
            return Response({'error': str(error)})