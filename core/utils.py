import africastalking
import environ

def send_sms(phone_number, message):
    env = environ.Env()
    environ.Env.read_env()

    username = env("AFRICASTALKING_USERNAME")
    api_key = env("AFRICASTALKING_API_KEY")
    
    africastalking.initialize(username, api_key)

    # Initialize SMS service
    sms = africastalking.SMS

    try:
        # Send the message
        response = sms.send(message, [phone_number])
        print(response)
        return response
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None