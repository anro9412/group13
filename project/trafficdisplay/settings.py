import json


class Settings:

    saved_default_settings: dict = {}
    filepath_saved_default_settings = "saved_default_settings.json"

    traffic_stops_dict: dict = {}
    filepath_traffic_stops = "traffic_stops.json"

    @staticmethod
    def init() -> tuple[Exception | None, ...]:
        Settings.saved_default_settings = {
            "transport_type_selected_text": "\uE900   Ferry",
            "transport_type_selected_text_bare": "Ferry",
            "transport_type_selected_index": 2,
            "stop_selected_text": "\uE902   Karlskrona Centralstation",
            "stop_selected_text_bare": "Karlskrona Centralstation",
            "stop_selected_index": 6,
            "transport_type_and_stop_selected_text":
                "Ferry · Karlskrona Centralstation"
        }

        Settings.traffic_stops_dict = {
            "740011100:24310": {
                "stop": "M\u00f6lletorp",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740011253:24447": {
                "stop": "Allatorp",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740040917:24483": {
                "stop": "Amiralitetstorget",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740001537:1537": {
                "stop": "Berg\u00e5sa station",
                "transport_modes": [
                    "BUS",
                    "TRAIN"
                ]
            },
            "740074440:24515": {
                "stop": "W\u00e4m\u00f6parken brygga",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740074437:24516": {
                "stop": "Pottholmen brygga",
                "transport_modes": []
            },
            "740074438:24517": {
                "stop": "Salt\u00f6 Fiskhamn brygga",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740074431:74230": {
                "stop": "Skeppsbron brygga",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740074432:24518": {
                "stop": "Bj\u00f6rkholmen brygga",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740031827:24154": {
                "stop": "Kungsmarken centrum",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031828:24155": {
                "stop": "Gullaberg",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031825:24152": {
                "stop": "Kungsmarken B-huset",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031826:24153": {
                "stop": "Kungsmarken A-huset",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031829:24156": {
                "stop": "Marieberg",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031831:24158": {
                "stop": "Kyrkog\u00e5rden",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031834:24161": {
                "stop": "Ekedalsv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031835:24162": {
                "stop": "Ga Riksv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031832:24159": {
                "stop": "H\u00e4lsov\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031833:24160": {
                "stop": "Kn\u00f6s\u00f6v\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031816:24147": {
                "stop": "Sparre",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031817:24148": {
                "stop": "Alamedan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031814:24145": {
                "stop": "Af Chapmangymnasiet",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031815:24146": {
                "stop": "Drottninggatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031823:24150": {
                "stop": "Ankaret",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031824:24151": {
                "stop": "Kungsmarken C-huset",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031821:24149": {
                "stop": "Varvet",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031805:24136": {
                "stop": "S\u00f6dra H\u00e4ssleg\u00e5rden",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031806:24137": {
                "stop": "Silverv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031803:24135": {
                "stop": "H\u00e4ssleg\u00e5rdens f\u00f6rskola",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031809:24140": {
                "stop": "H Martinsons v\u00e4g",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031807:24138": {
                "stop": "Spandelstorpskolan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031808:24139": {
                "stop": "Spandelstorp",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031812:24143": {
                "stop": "Carlandrav\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031813:24144": {
                "stop": "AWA v\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031810:24141": {
                "stop": "G Torhamns v\u00e4g",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031811:24142": {
                "stop": "Afvelsg\u00e4rdev\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031801:24133": {
                "stop": "Bastasj\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031802:24134": {
                "stop": "Norra H\u00e4ssleg\u00e5rden",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031800:24132": {
                "stop": "Amiralen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031869:24180": {
                "stop": "Kn\u00f6s\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031874:24183": {
                "stop": "Ekholmen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031878:24185": {
                "stop": "Strandgatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031879:24186": {
                "stop": "L\u00e5ng\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031877:24184": {
                "stop": "Tullparken",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031870:24181": {
                "stop": "Salt\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031871:24182": {
                "stop": "Salt\u00f6 torg",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031859:24174": {
                "stop": "Uranv\u00e4gen Torskors",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031863:24175": {
                "stop": "Gullberna station",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031864:24176": {
                "stop": "Ring\u00f6bron",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031868:24179": {
                "stop": "Hultv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031865:24177": {
                "stop": "Lallerstedts gata",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031866:24178": {
                "stop": "Gullberna Park",
                "transport_modes": []
            },
            "740031849:24172": {
                "stop": "H\u00e4st\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031847:24170": {
                "stop": "H\u00e4st\u00f6 idrottsplats",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031848:24171": {
                "stop": "Herrg\u00e5rdsv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031853:24173": {
                "stop": "Chapmansplan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031838:24164": {
                "stop": "S\u00f6dra Ring\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031839:24165": {
                "stop": "\u00c4ngholmen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031837:24163": {
                "stop": "Ring\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031841:24167": {
                "stop": "Toras v\u00e4g",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031842:24168": {
                "stop": "Roxtec Verk\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031840:24166": {
                "stop": "Verk\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031844:73222": {
                "stop": "NKT Verk\u00f6",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031886:24190": {
                "stop": "Ang\u00f6ringen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031889:24193": {
                "stop": "L\u00f6sen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031887:24191": {
                "stop": "Kvarngatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031888:24192": {
                "stop": "Galgamarkstrappan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031881:24188": {
                "stop": "Egilslunden",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031882:24189": {
                "stop": "Ordensgatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031880:24187": {
                "stop": "Lagmansgatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031795:24130": {
                "stop": "\u00d6stra Torp",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031796:24131": {
                "stop": "Annebo",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031799:73221": {
                "stop": "Stationsv\u00e4gen Slottsbacken",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031790:24125": {
                "stop": "Intagsv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031793:24128": {
                "stop": "Carlemansv\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031794:24129": {
                "stop": "Kronotorp",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031791:24126": {
                "stop": "Backabo",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031792:24127": {
                "stop": "Stadstr\u00e4dg\u00e5rden",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031784:24122": {
                "stop": "Sunnadal",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031789:24124": {
                "stop": "Ekeberg",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031783:24121": {
                "stop": "Lindesn\u00e4s",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031781:24120": {
                "stop": "Berg\u00e5sa centrum",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031779:24119": {
                "stop": "Polhemsgatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031777:24117": {
                "stop": "Landsv\u00e4gsgatan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031778:24118": {
                "stop": "Tullskolan",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740011646:24327": {
                "stop": "Torskors",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031996:24311": {
                "stop": "Augerums kyrka",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031994:24309": {
                "stop": "R\u00e5backen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031997:24312": {
                "stop": "Mariefors",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740031998:24313": {
                "stop": "M\u00f6lle\u00e5ker",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032976:24510": {
                "stop": "W\u00e4m\u00f6parken",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032010:24329": {
                "stop": "Bubbetorp",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032087:24422": {
                "stop": "Silleboda",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032074:24405": {
                "stop": "Sk\u00e4rfva by",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032091:24427": {
                "stop": "Sk\u00f6nstavik",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032092:24428": {
                "stop": "Karlsg\u00e4rde",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032125:24460": {
                "stop": "Asp\u00f6f\u00e4rjan",
                "transport_modes": []
            },
            "740032110:24448": {
                "stop": "Bor\u00e5kra",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032109:24446": {
                "stop": "All\u00e9v\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032108:24444": {
                "stop": "Rosenholm",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032009:24326": {
                "stop": "Berget",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740022976:24474": {
                "stop": "Verk\u00f6 f\u00e4rjeterminalen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032169:24482": {
                "stop": "J\u00e4rav\u00e4gen",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032149:24476": {
                "stop": "Sk\u00e4rva",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032145:24472": {
                "stop": "Allatorp norra",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032144:72717": {
                "stop": "W\u00e4m\u00f6skolan Ekorrv\u00e4gen",
                "transport_modes": []
            },
            "740032192:24507": {
                "stop": "NKT Arena Karlskrona",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032193:24508": {
                "stop": "Lyckeby Slottsbacken",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740032188:24505": {
                "stop": "Campus Gr\u00e4svik",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740023372:24481": {
                "stop": "Karlskrona centrum",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740037242:24511": {
                "stop": "Lokstallarna",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740017989:68911": {
                "stop": "Drags\u00f6 brygga",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740017988:74167": {
                "stop": "Sjuhalla",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740017997:74229": {
                "stop": "Marinmuseum",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740017990:68906": {
                "stop": "Br\u00e4ndaholm",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740072447:24484": {
                "stop": "Gullberna",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740024365:24157": {
                "stop": "Sjukhuset huvudentr\u00e9n",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740010009:24445": {
                "stop": "Allatorps g\u00e5rd",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740000663:663": {
                "stop": "Lyckeby centrum",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740000230:230": {
                "stop": "Karlskrona Centralstation",
                "transport_modes": [
                    "BOAT",
                    "BUS",
                    "TRAIN"
                ]
            },
            "740000230:73624": {
                "stop": "Karlskrona central",
                "transport_modes": [
                    "BOAT",
                    "BUS",
                    "TRAIN"
                ]
            },
            "740020510:73602": {
                "stop": "Kungsplan Hoglands Park",
                "transport_modes": [
                    "BUS",
                    "TRAIN"
                ]
            },
            "740020510:24116": {
                "stop": "Kungsplan",
                "transport_modes": [
                    "BUS",
                    "TRAIN"
                ]
            },
            "740020700:24486": {
                "stop": "Fisktorget",
                "transport_modes": [
                    "BOAT"
                ]
            },
            "740020699:24503": {
                "stop": "Handelshamnen",
                "transport_modes": [
                    "BOAT",
                    "BUS"
                ]
            },
            "740010999:24314": {
                "stop": "Lycke\u00e5borg",
                "transport_modes": [
                    "BUS"
                ]
            },
            "740024915:24123": {
                "stop": "Motellet",
                "transport_modes": [
                    "BUS"
                ]
            }
        }
        exception_saved_default_settings = Settings.load_saved_file(
            Settings.filepath_saved_default_settings,
            Settings.saved_default_settings
        )
        exception_saved_traffic_stops = Settings.load_saved_file(
            Settings.filepath_traffic_stops,
            Settings.traffic_stops_dict
        )

        return (
            exception_saved_default_settings,
            exception_saved_traffic_stops
        )

    @staticmethod
    def load_saved_file(
        filepaths: str,
        data_dict: dict
    ) -> None | Exception:

        filepaths_is_str = isinstance(filepaths, str)
        exception = None

        if not filepaths_is_str:
            return TypeError()

        try:
            with open(filepaths, 'r') as source:
                saved_json: dict = json.load(source)

            if isinstance(saved_json, dict):
                data_dict.clear()
                data_dict.update(saved_json)

            else:
                exception = TypeError()

        except Exception as e:
            exception = e

        return exception

    @staticmethod
    def get_saved_default_settings():
        return Settings.saved_default_settings

    @staticmethod
    def save_to_files(
        filepath: str,
        save_dict: dict
    ) -> None | Exception:

        filepath_is_string = isinstance(filepath, str)
        exception = None

        if not filepath_is_string:
            return TypeError()

        try:
            serialized = json.dumps(save_dict)
            with open(filepath, 'w') as destination:
                destination.write(serialized)

        except Exception as e:
            exception = e

        return exception

    @staticmethod
    def save_to_default_settings(
        new_default_settings: dict
    ) -> None | Exception:

        Settings.saved_default_settings = new_default_settings
        exception = None
        exception = Settings.save_to_files(
            Settings.filepath_saved_default_settings,
            Settings.saved_default_settings
        )

        return exception
