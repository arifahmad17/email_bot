# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/dsocs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import email
from email import message
from typing import Any, Text, Dict, List
from mail import send_email 
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
#from email import send_email
#
#





class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"
    
    @staticmethod
    def required_slot(tracker:Tracker) -> List[Text]:
        return ["email","subject","message"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
        "name": [self.from_entity(entity = "name", intent="email_name"),],
        "subject": [self.from_entity(entity = "subject", intent="email_name"),],
        "message": [self.from_entity(entity = "message", intent="message_name"),]
        }

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        


        
        send_email(
            tracker.get_slot("email"),
            tracker.get_slot("subject"),
            tracker.get_slot("message")
            )

        dispatcher.utter_message(text="We have sent you an email at{}".format(tracker.get_slot("email")))

        return []

