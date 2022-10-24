mappings = {
    "Mercury": 0.2408467 * 31557600,
    "Venus": 0.61519726 * 31557600,
    "Earth": 1.0 * 31557600,
    "Mars": 1.8808158 * 31557600,
    "Jupiter": 11.862615 * 31557600,
    "Saturn": 29.447498 * 31557600,
    "Uranus": 84.016846 * 31557600,
    "Neptune": 164.79132 * 31557600,
}


class SpaceAge:
    def __init__(self, seconds):
        self.ages = {
            "Mercury": seconds / mappings["Mercury"],
            "Venus": seconds / mappings["Venus"],
            "Earth": seconds / mappings["Earth"],
            "Mars": seconds / mappings["Mars"],
            "Jupiter": seconds / mappings["Jupiter"],
            "Saturn": seconds / mappings["Saturn"],
            "Uranus": seconds / mappings["Uranus"],
            "Neptune": seconds / mappings["Neptune"],
        }

    def on_mercury(self):
        return round(self.ages["Mercury"], 2)

    def on_venus(self):
        return round(self.ages["Venus"], 2)

    def on_earth(self):
        return round(self.ages["Earth"], 2)

    def on_mars(self):
        return round(self.ages["Mars"], 2)

    def on_jupiter(self):
        return round(self.ages["Jupiter"], 2)

    def on_saturn(self):
        return round(self.ages["Saturn"], 2)

    def on_uranus(self):
        return round(self.ages["Uranus"], 2)

    def on_neptune(self):
        return round(self.ages["Neptune"], 2)
