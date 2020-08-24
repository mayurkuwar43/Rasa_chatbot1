from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction
from database_connectivity import DataUpdate




class TripplanForm(FormAction):
 def name(self):
  return "trip_plan_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["travel_date","travel_period","trip_type","adults","child","budget","Name","email","phno"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "travel_date": [
                self.from_text(),
            ],
            "travel_period": [
                self.from_text(),
            ],
            
            "trip_type": [
                self.from_text(),
            ],
            "adults": [
                self.from_text(),
            ],
            "child": [
                self.from_text(),
            ],
            "budget": [
                self.from_text(),
            ],
            "Name": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
            "phno": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    DataUpdate(tracker.get_slot("travel_date"),tracker.get_slot("travel_period"),tracker.get_slot("trip_type"),tracker.get_slot("adults"),tracker.get_slot("child"),tracker.get_slot("budget"),tracker.get_slot("name"),tracker.get_slot("email"),tracker.get_slot("phno"))
    dispatcher.utter_message("❤️❤️❤️Thank you so much for showing your intrest in traveling with us our team will contact you soon . bye! Take care!.")    
    return []

