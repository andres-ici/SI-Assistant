from datetime import datetime

def sample_responses(input_test):
    user_message = str(input_test).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am SI-Assistant!"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("horario"):
        return "https://ibb.co/vqW91sZ"

    if user_message in ("malla"):
        return "https://admision.ufro.cl/wp-content/uploads/mallas-ufro/26-ingenieria-civil-electronica.jpg"

    return "I don't understand you :("

    