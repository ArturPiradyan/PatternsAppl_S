
class Lights:
    def turn_on(self):
        print("Lights are ON")

    def turn_off(self):
        print("Lights are OFF")

    def dim(self, level):
        print(f"Lights dimmed to {level}%")

class Thermostat:
    def set_temperature(self, temperature):
        print(f"Thermostat set to {temperature}°C")

    def get_temperature(self):
        return 22 
    
    def turn_on_ac(self):
        print("AC is ON")

    def turn_off_ac(self):
        print("AC is OFF")

class MusicPlayer:
    def play_song(self, song_title):
        print(f"Playing '{song_title}'")

    def stop_playing(self):
        print("Music stopped")

    def set_volume(self, volume):
        print(f"Volume set to {volume}")

class HomeAutomationFacade:
    def __init__(self):
        self._lights = Lights() 
        self._thermostat = Thermostat()
        self._music_player = MusicPlayer()

    def evening_mode(self):
        print("\n--- Activating Evening Mode ---")
        self._lights.dim(30)
        self._thermostat.set_temperature(20)
        self._music_player.play_song("Relaxing Jazz")

    def morning_mode(self):
        print("\n--- Activating Morning Mode ---")
        self._lights.turn_on()
        self._thermostat.set_temperature(23)
        self._music_player.stop_playing()

    def party_mode(self):
        print("\n--- Activating Party Mode ---")
        self._lights.dim(80)
        self._lights.turn_on()
        self._thermostat.set_temperature(18)
        self._music_player.play_song("Upbeat Pop")
        self._music_player.set_volume(80)

    def set_room_temperature(self, temperature):
        self._thermostat.set_temperature(temperature)

if __name__ == "__main__":
    home_automation = HomeAutomationFacade()

    home_automation.evening_mode()
    home_automation.party_mode()
    home_automation.morning_mode()

    home_automation.set_room_temperature(25)
