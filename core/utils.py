import africastalking

def send_sms(phone_number, message):
    # Initialize SDK
    username = "YOUR_USERNAME"  # 'sandbox' for development
    api_key = "YOUR_API_KEY"    # sandbox API key for development
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