class HotTub:
    OFF = 0
    ON = 1

    def __init__(self):
        self.temperature = 50
        self.jets = HotTub.OFF

    def jets_on(self):
        self.jets = HotTub.ON
        print("HotTub Jets are ON.")

    def jets_off(self):
        self.jets = HotTub.OFF
        print("HotTub Jets are OFF.")

    def set_temperature(self, temperature):
        if 50 <= temperature <= 104:
            self.temperature = temperature
            print("HotTub temperature is set to {}F".format(self.temperature))
        else:
            print("Only temperatures between 50-104F are accepted.")

    def circulate(self):
        if self.jets == HotTub.ON:
            print("Hot Tub water is circulating.")
        else:
            print("Hot Tub water is stopped.")
