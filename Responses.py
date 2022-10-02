from datetime import datetime

def get_response(input_text):
    user_message = str(input_text).lower()

    dict={'1':'The front fog lamp is on.',
          '2':'The rear fog lamp is on.',
          '3':'Indicates that the signal is on. When you lower the signal arm,'
              ' the left turn indicates the saga turn when you lift it up.',
          '4':'It means that the long-distance headlights are turned on.',
          '5':'It indicates that the short headlamps and stop lights are on.'}

    if user_message in dict:
        return dict[user_message]

    return "I dont understand you."


