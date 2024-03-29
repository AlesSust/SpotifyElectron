from enum import Enum


class Genre(Enum):
    POP = "Pop"
    ROCK = "Rock"
    HIP_HOP = "Hip-hop"
    RNB = "R&B (Ritmo y Blues)"
    JAZZ = "Jazz"
    BLUES = "Blues"
    REGGAE = "Reggae"
    COUNTRY = "Country"
    FOLK = "Folk"
    CLASICA = "Clásica"
    ELECTRONICA = "Electrónica"
    DANCE = "Dance"
    METAL = "Metal"
    PUNK = "Punk"
    FUNK = "Funk"
    SOUL = "Soul"
    GOSPEL = "Gospel"
    LATIN = "Latina"
    WORLD_MUSIC = "Música del mundo"
    EXPERIMENTAL = "Experimental"
    AMBIENT = "Ambiental"
    FUSION = "Fusión"
    INSTRUMENTAL = "Instrumental"
    ALTERNATIVE = "Alternativa"
    INDIE = "Indie"
    RAP = "Rap"
    SKA = "Ska"
    GRUNGE = "Grunge"
    TRAP = "Trap"
    REGGAETON = "Reggaeton"

    @staticmethod
    def checkValidGenre(genre: str) -> bool:
        """Checks if the genre is valid"""
        try:
            Genre(genre)
            return True
        except ValueError:
            return False

    @staticmethod
    def getGenre(genre: Enum) -> str:
        # TODO raise exception if not
        return str(genre.value)
