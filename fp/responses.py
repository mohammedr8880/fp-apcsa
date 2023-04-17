import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`You can use this bot to roll a dice by saying \"roll\".\n Tell me \"Hello\".\n If you want to know who I am, then say \"Who are you\".`'

    if p_message == 'who are you':
        return 'I am a bot named CactusJack, created by Mo'

    if p_message == 'tell me all the commands that you know right now':
        return '\"roll\"\n\"hello\"'

    if p_message == 'yo':
        return 'Yo!'

    return 'I didn\'t understand what you wrote. Try typing "!help".'
