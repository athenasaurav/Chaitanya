# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Form, AllSlotsReset, Restarted
import config
import mysql.connector as sql

class ActionPasswordReset(Action):

    def name(self) -> Text:
        return "action_password_reset"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        connection = sql.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
        )
        cursor = connection.cursor()
        email = str(tracker.get_slot("email")).lower()
        cursor.execute("Select * from {} where Email='{}' ".format(config.LOGIN_TABLE_NAME, email))
        result = cursor.fetchall()
        if len(result) == 0:
            dispatcher.utter_message("Sorry we couldn't find Email in our database")
        else:
            dispatcher.utter_message("Here is your details: email : {} password: {}".format(result[0][0], result[0][1]))
        # dispatcher.utter_message(text="Hello World!")

        return []



class ActionIncidentStatusId(Action):

    def name(self) -> Text:
        return "action_incident_status_Id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        connection = sql.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
        )
        cursor = connection.cursor()
        incident_status_Id = str(tracker.get_slot("incident_status_Id")).lower()
        cursor.execute("Select * from {} where Id='{}' ".format(config.INCIDENT_TABLE_NAME, incident_status_Id))
        result = cursor.fetchall()
        if len(result) == 0:
            dispatcher.utter_message("Sorry we couldn't find Email in our database")
        else:
            dispatcher.utter_message("Here is your details: email : {}, id: {}, status : {}".format(result[0][0], result[0][1], result[0][2]))
            # dispatcher.utter_message(text="Hello World!")

        return []



class ActionOpenIncident(Action):

    def name(self) -> Text:
        return "action_open_incident"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        connection = sql.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
        )
        cursor = connection.cursor()
        email = str(tracker.get_slot("email")).lower()
        cursor.execute("Select * from {}".format(config.INCIDENT_TABLE_NAME))
        result = cursor.fetchall()
        new_id = len(result) + 1
        status = 'unresolved'
        open_incident = (email, new_id, status)
        query = "INSERT INTO {}.{} VALUES (%s,%s,%s)".format(config.database, config.INCIDENT_TABLE_NAME)
        cursor.execute(query, tuple(open_incident))
        connection.commit()
        dispatcher.utter_message("Incident opened successfully. Email : {} , id: {}, status : {}".format(email, new_id, status))

        return []


class ActionRestarted(Action):
    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):

        # dispatcher.utter_message(template="utter_greet")
        return [Form(None), AllSlotsReset(None), Restarted(None)]