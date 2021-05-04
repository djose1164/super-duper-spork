import kivy
import json
import time
from os import system
from kivy.app import App

from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

kivy.require("1.11.1")

'''
class RV(RecycleView):
    """
    Update the current items to show.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_content_to_show()
        # self.data = [{"text": item} for item in ["content", "Adios"]]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # time.sleep(10)


    def update_content_to_show(self, content):
        assert content

        #self.data = [{"text": item} for item in ["first", "second"]]
        self.id_rb.data = [{"text": item} for item in ["first", "second"]]
        self.refresh_from_data()
        i = 0
        for key, value in self.data[i].items():
            print(f"{key + '->' + value}")
            i += 1
        print("## Updated list view!")
'''

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    id_rv = ObjectProperty()

    def search_location(self):
        """
        Search for the given location throut all available locations in OpenWeater.

        """
        # The URL's base.
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        # The place to search.
        place_to_search = f"?q={self.search_input.text}&type=like"
        # My API key.
        api_key = "&APPID=7b6e61038914b2c13915adcb9087ce7d"
        # The above variables together to make the complete search request.
        search_url = base_url + place_to_search + api_key
        # Make the request to OpenWeatherMap
        self.request = UrlRequest(search_url, self.found_location)
        print(f"## search_location (type: {type(self.request)}\t data: {self.request.result}")

    def found_location(self, request, data, *args):
        """
        Add the given location by the user to list view.


        Args:
            request (UrlRequest): Object request.
            data (list): List with requested data.
        """
        # If the data is type dict there's no to do decode, else will decode
        # the data.
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        print(f"## found_location: {type(data)}")
       # system("cls||clear")
        for key in data:
            print(f"## key: {key}")
        cities = [data['name']]
        self.id_rv.data = [{"text": item} for item in ["Aloha", "sayonara"]]
        print("## In found_location ##")
        print("\n".join(cities))
        for i in range(len(self.id_rv.data)):
            print(f"## ids: {self.id_rv.data[i]}")
        # Update the list with de given data.
        #RV().update_content_to_show(cities)


class WeatherApp(App):
    def build(self):
        return AddLocationForm()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
