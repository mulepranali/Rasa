from typing import Any, Dict, List, Text
from bs4 import BeautifulSoup
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionScrapeNiftyData(Action):
    def name(self) -> Text:
        return "action_scrape_nifty_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Send a request to the webpage
            response = requests.get('http://127.0.0.1:5501/Rasa/web.html')
            response.raise_for_status()  # Check if the request was successful

            # Print the response content for debugging
            print(response.text)  # Check the HTML content

            # Parse the webpage content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the table element
            table = soup.find('table')

            # Print the table HTML for debugging
            print(table)  # Check if the table is found

            if table is None:
                dispatcher.utter_message("Table not found in the HTML.")
                return []

            # Get all rows in the table
            rows = table.find_all('tr')

            # Prepare header and data
            header = ['Date', 'Nifty 50 Index', 'Open', 'High', 'Low', 'Close']
            data = []

            # Iterate through the rows and collect data
            for row in rows[2:]:  # Skip the first two header rows
                cols = row.find_all('td')
                cols = [col.get_text() for col in cols]
                data.append(cols)

            # Print collected data for debugging
            print(data)  # Check the collected data

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

        return []


