# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class ActionScrapeNiftyData(Action):
#     def name(self) -> Text:
#         return "action_scrape_nifty_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Initialize the Chrome WebDriver
#         driver = webdriver.Chrome()

#         try:
#             # Open the webpage
#             driver.get('http://127.0.0.1:5501/Rasa/web.html')

#             # Find the table element
#             table = driver.find_element(By.TAG_NAME, 'table')

#             # Get all rows in the table
#             rows = table.find_elements(By.TAG_NAME, 'tr')

#             # Prepare header and data
#             header = ['Date', 'Nifty 50 Index', 'Open', 'High', 'Low', 'Close']
#             data = []

#             # Iterate through the rows and collect data
#             for row in rows[2:]:  # Skip the first two header rows
#                 cols = row.find_elements(By.TAG_NAME, 'td')
#                 cols = [col.text for col in cols]
#                 data.append(cols)

#             # Prepare message
#             message = ""
#             for row in data:
#                 message += (
#                     f"Date: {row[0]}\n"
#                     f"Nifty 50 Index: {row[1]}\n"
#                     f"Open: {row[2]}\n"
#                     f"High: {row[3]}\n"
#                     f"Low: {row[4]}\n"
#                     f"Close: {row[5]}\n"
#                     f"{'-'*20}\n"
#                 )

#             # Send the message
#             dispatcher.utter_message(message)

#         except Exception as e:
#             dispatcher.utter_message(f"An error occurred: {str(e)}")
        
#         finally:
#             # Close the WebDriver
#             driver.quit()

#         return []

# class ActionAskAnythingElse(Action):
#     def name(self) -> Text:
#         return "utter_ask_anything_else"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message("Do you need anything else?")
#         return []



# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message = (
#             "Sorry, I didn't get it. Would you please choose from below:\n"
#             "A. Access issues\n"
#             "B. Status\n"
#             "C. Database\n"
#             "D. Nifty data\n"
#             "E. Git."
#         )
#         dispatcher.utter_message(text=message)
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet
from selenium import webdriver
from selenium.webdriver.common.by import By

# Action to scrape Nifty data
class ActionScrapeNiftyData(Action):
    def name(self) -> Text:
        return "action_scrape_nifty_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()

        try:
            # Open the webpage
            driver.get('http://127.0.0.1:5501/Rasa/web.html')

            # Find the table element
            table = driver.find_element(By.TAG_NAME, 'table')

            # Get all rows in the table
            rows = table.find_elements(By.TAG_NAME, 'tr')

            # Prepare header and data
            header = ['Date', 'Nifty 50 Index', 'Open', 'High', 'Low', 'Close']
            data = []

            # Iterate through the rows and collect data
            for row in rows[2:]:  # Skip the first two header rows
                cols = row.find_elements(By.TAG_NAME, 'td')
                cols = [col.text for col in cols]
                data.append(cols)

            # Prepare message
            message = ""
            for row in data:
                message += (
                    f"Date: {row[0]}\n"
                    f"Nifty 50 Index: {row[1]}\n"
                    f"Open: {row[2]}\n"
                    f"High: {row[3]}\n"
                    f"Low: {row[4]}\n"
                    f"Close: {row[5]}\n"
                    f"{'-'*20}\n"
                )

            # Send the message
            dispatcher.utter_message(message)

        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")
        
        finally:
            # Close the WebDriver
            driver.quit()

        return []

# Action to ask if the user needs anything else
class ActionAskAnythingElse(Action):
    def name(self) -> Text:
        return "utter_ask_anything_else"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Do you need anything else?")
        return []

# Default fallback action
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = (
            "Sorry, I didn't get it. Would you please choose from below:\n"
            "A. Access issues\n"
            "B. Status\n"
            "C. Database\n"
            "D. Nifty data\n"
            "E. Git."
        )
        dispatcher.utter_message(text=message)
        return []

# Form validation for access issues
class ValidateAccessIssuesForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_access_issues_form"

    def validate_access_issue_type(self, 
                                   slot_value: Any, 
                                   dispatcher: CollectingDispatcher, 
                                   tracker: Tracker, 
                                   domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value.lower() in ["hive query", "firewall request", "artifact", "employee education program"]:
            return {"access_issue_type": slot_value}
        else:
            dispatcher.utter_message(text="Please select a valid option: a. Hive query, b. Firewall request, c. Artifact, d. Employee Education Program")
            return {"access_issue_type": None}

    def validate_device_type(self, 
                             slot_value: Any, 
                             dispatcher: CollectingDispatcher, 
                             tracker: Tracker, 
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value.lower() in ["desktop", "laptop"]:
            return {"device_type": slot_value}
        else:
            dispatcher.utter_message(text="Please select a valid option: 1. Desktop, 2. Laptop")
            return {"device_type": None}

# Action to handle the submission of access issues form
class ActionSubmitAccessIssuesForm(Action):
    def name(self) -> Text:
        return "action_submit_access_issues_form"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        access_issue_type = tracker.get_slot('access_issue_type')
        device_type = tracker.get_slot('device_type')

        if access_issue_type.lower() == "hive query":
            if device_type.lower() == "desktop":
                dispatcher.utter_message(template="utter_desktop")
            elif device_type.lower() == "laptop":
                dispatcher.utter_message(template="utter_laptop")
        elif access_issue_type.lower() == "firewall request":
            dispatcher.utter_message(template="utter_firewall_request")
        elif access_issue_type.lower() == "artifact":
            dispatcher.utter_message(template="utter_artifact")
        elif access_issue_type.lower() == "employee education program":
            dispatcher.utter_message(template="utter_eep")

        dispatcher.utter_message(template="utter_ask_satisfaction")

        return []
class ActionHandleNumericValue(Action):
    def name(self):
        return "utter_handle_numeric_value"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Logic to handle numeric values
        dispatcher.utter_message(text="You've provided a numeric value. How can I assist you further?")
        return []
