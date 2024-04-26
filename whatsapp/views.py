from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import MessageImages

from .utils import WhatsAppClient

API_KEY = "EAAGuKjgErkMBO7OKMi70irCjLCSHtsYpjCZB2iAOPbULC1eYuupx6huFZAW5mEKdjqZC4vpr4ORh7AZCZCg7PZAgUgNdcbpwacIRGq66hZAMSVXrd2ZCVJsBjDUl0KZA5fdlkwGtn6LtGihI479C06SOwSoc3zpZBvKM5X18H4JjFFb6Wy23nY7ouef07FAm4vFTTgnebAG7TmHiPjlwug3qwZD"
WA_ID = "285776191286365"
MSG_SECRET = "secret9045"
BASE_URL = "https://leading-blindly-seahorse.ngrok-free.app"

whatsapp_config = WhatsAppClient(api_key=API_KEY,wa_id=WA_ID)
client = whatsapp_config.get_client()

class WhatsAppAPIView(APIView):
    def get(self, request: Request) -> Response:
        try:
            secret = request.GET.get("secret")
            if secret != MSG_SECRET:
                return Response({"message": "Invalid Secret"}, status=status.HTTP_200_OK)
            recipient_number = request.GET.get("number")
            
            for image in MessageImages.objects.all():
                payload = {
                    "link": f"{BASE_URL}{image.image.url}",
                }
                if image.caption:
                    payload["caption"] = image.caption
                whatsapp_config.send_message(recipient_number, "image", payload)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"message": str(e)}, status=status.HTTP_200_OK)