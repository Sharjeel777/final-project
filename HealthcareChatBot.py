import re

class HealthcareChatbot:
    def __init__(self):
        self.responses = {
            'greeting': ['Hello! How can I assist you today?', 'Hi there! How can I help?'],
            'goodbye': ['Goodbye! Take care.', 'See you later!', 'Bye!'],
            'ask_symptoms': ['What symptoms are you experiencing?', 'Can you describe your symptoms?'],
            'ask_condition': ['Do you have any medical condition?', 'Do you have any pre-existing conditions?'],
            'ask_allergies': ['Are you allergic to any medication or substances?', 'Do you have any allergies?'],
            'ask_age': ['May I know your age?', 'How old are you?'],
            'ask_gender': ['What is your gender?', 'Are you male or female?'],
            'ask_location': ['Where are you currently located?'],
            'ask_contact': ['What is your contact number?', 'Can you provide a contact number?'],
            'unknown': ["I'm sorry, I don't understand that. Can you please rephrase?"],
        }
        self.context = {}

    def respond(self, user_input):
        # Determine intent
        intent = self.get_intent(user_input)

        # Respond based on intent
        if intent in self.responses:
            return self.responses[intent][0]
        else:
            return self.responses['unknown'][0]

    def get_intent(self, user_input):
        user_input = user_input.lower()

        # Greeting detection
        if any(word in user_input for word in ['hello', 'hi', 'hey']):
            return 'greeting'

        # Goodbye detection
        if any(word in user_input for word in ['bye', 'goodbye', 'see you']):
            return 'goodbye'

        # Intent detection based on keywords
        if any(word in user_input for word in ['symptoms', 'feel']):
            return 'ask_symptoms'
        if any(word in user_input for word in ['condition', 'medical']):
            return 'ask_condition'
        if any(word in user_input for word in ['allergy', 'allergic']):
            return 'ask_allergies'
        if any(word in user_input for word in ['age', 'old']):
            return 'ask_age'
        if any(word in user_input for word in ['gender', 'male', 'female']):
            return 'ask_gender'
        if any(word in user_input for word in ['location', 'where']):
            return 'ask_location'
        if any(word in user_input for word in ['contact', 'phone']):
            return 'ask_contact'

        # Default intent if none of the above matched
        return 'unknown'

# Example usage
chatbot = HealthcareChatbot()

while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
