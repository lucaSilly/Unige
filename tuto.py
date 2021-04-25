from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'HO3qMewi7bwKF16FjcAV76EZMOCTe3vsGGACVZiE2myy'
url = 'https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/07c01bed-2d84-4677-9d88-2c72c9c1f470'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

with open('./audio/poutine.mp3','rb') as file :
    res = stt.recognize (
        audio=file, 
        content_type= 'audio/mp3',
        #model='en-US_BroadbandModel',
        model = 'fr-FR_NarrowbandModel',
        continuous = True
        ).get_result()

text = res['results'][0]['alternatives'][0]['transcript']
print(text)

with open ('output.txt', 'w') as out : 
    out.writelines(text)