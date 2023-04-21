
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
import requests
import json
from django.templatetags.static import static
import base64
from heyoo import WhatsApp
# Create your views here.

messenger = WhatsApp('EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD',  phone_number_id='108697735516128')

VERIFY_TOKEN = "23189345712"

head = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'}



class HelloView(APIView):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        print(incoming_message)


        sms(request)



        return HttpResponse()


@csrf_exempt
def sms(request):
    if request.method == 'POST':

        incoming_message = json.loads(request.body.decode('utf-8'))

        profile = ""
        print(incoming_message)
        print("the_incoming_message")
        income = incoming_message['entry']
        entry = income[-1]
        for message in entry['changes']:
            valu = message['value']

            if 'messages' in valu:

                for contactlist in valu['contacts']:

                    number = contactlist['wa_id']

                    profile = contactlist['profile']['name']

                for messag in valu['messages']:

                    if messag['type'] == 'text':

                        msg = messag['text']['body']





                        msgid = messag['id']

                        datobj = {
                                  "messaging_product": "whatsapp",
                                  "status": "read",
                                  "message_id": msgid
                                }

                        respo = requests.post('https://graph.facebook.com/v13.0/108697735516128/messages', json = datobj, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

                        print(respo.text)



                        tabol(number, msg, profile)

                    if messag['type'] == 'image':

                        msg = messag['image']['caption']

                        msgid = messag['id']

                        media_id = messag['image']['id']

                        datobj = {
                                  "messaging_product": "whatsapp",
                                  "status": "read",
                                  "message_id": msgid
                                }

                        respo = requests.post('https://graph.facebook.com/v13.0/108697735516128/messages', json = datobj, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

                        print(respo.text)

                        r = requests.get(f"https://graph.facebook.com/v14.0/{media_id}", headers=head)

                        print(r.json()["url"])


                        media_url = r.json()["url"]

                        r = requests.get(media_url, headers=head)

                        print(r)

                        img = r.content

                        #tabol(number, msg, profile, media_url)

                    if messag['type'] == 'interactive':

                        msgid = messag['id']

                        if messag['interactive']['type'] == 'list_reply':

                            msg = messag['interactive']['list_reply']['id']



                            datobj = {
                                  "messaging_product": "whatsapp",
                                  "status": "read",
                                  "message_id": msgid
                                }

                            respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

                            print(respo.text)

                            tabol(number, msg, profile)
                        if messag['interactive']['type'] == 'button_reply':

                            msg = messag['interactive']['button_reply']['id']



                            datobj = {
                                  "messaging_product": "whatsapp",
                                  "status": "read",
                                  "message_id": msgid
                                }

                            respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

                            print(respo.text)

                            tabol(number, msg, profile)


def tabol(number, mesg, profile, media=None):

    print("now here now")

    start = ("HI *"+ str(profile)+"* \n\nPlease Enter your fullname in the format \n\n name=Tatenda Kachere")



    main = ("HI *"+ str(profile)+"* \n\nWelcome to Mr Fixit Delivery Services CHATBOT \n\n"
        "Below is our main menu NB: Click the links below each category or section to get access to that section's menu \n\n ")

    mainly = ("Welcome Back, *"+ str(profile)+"* \n\nWelcome to Mr Fixit Delivery Services CHATBOT \n\n"
        "Below is our main menu NB: Click the links below each category or section to get access to that section's menu \n\n ")

    regsuccess = ("Registered Successfully Please check menu below:")

    watnum = number
    print(watnum)
    msg = mesg

    msg = msg.lower()

    member = Client.objects.filter(phone=watnum).first()


    print(msg)

    


    if member is not None :

        if member.admin_status == False:

            print("Check Now")

            datobj1 = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": "Message sent, will be responded shortly"
            }
            }

            datobj = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": "263784873574",
            "type": "text",
            "text": {
                "body": suggestion
            }
            }

            message = Message.objects.create(client=member, messagely=msg)

            message.save()

            suggestion = ("A message has been sent by " + member.firstname + " " + member.lastname + "\n Message: " +  "msg")

            respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

            respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj1, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

            print(respo.text)

        else:

            if "number=" in str(msg):

                numfindstart = str(msg).index("number=", 0)

                numfindend = str(msg).index(",", numfindstart)

                numfind = msg[numfindstart + 5:numfindend]

                datobj = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": numfind,
                "type": "text",
                "text": {
                    "body": msg[numfindend:]
                }
                }

                respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj1, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )
            
            else:

                datobj = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": "Please use the format:\n number=[recipent_number], \n [message]"
                }
                }

                respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj1, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )
            
    else:

        client = Client.objects.create(firstname=str(profile), phone=watnum)

        client.save()

        datobj1 = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": "Message sent, will be responded shortly"
            }
            }

        datobj = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "263784873574",
        "type": "text",
        "text": {
            "body": suggestion
        }
        }

        message = Message.objects.create(client=member, messagely=msg)

        message.save()

        suggestion = ("A message has been sent by " + member.firstname + " " + member.lastname + "\n Message: " +  "msg")

        respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

        respo = requests.post('https://graph.facebook.com/v15.0/108697735516128/messages', json = datobj1, headers = {'Authorization' : 'Bearer EAAKt8kjeARQBAOsh2h0goywP2jB1FYxeS23g9vpE286IgkXRTwUepD5sMqpWrLs3ewkZBxmzgnORzmgbPZB0vUDJZAtxrLKDjKUpgZC1XZAtePld0CFxelTqhzNafpkcp4YegrR20VOktkfufVpE1BIBXRyoRqEgz8MMPZButaiLJU97tAkWsBBsaVZCaZBSBnaK7FdHcZBZAt5orZAcvHswCz87EBO1rpjdq4ZD'} )

        print(respo.text)






