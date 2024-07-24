from pydantic import AliasChoices, BaseModel, Field

# ======================  req type ===============================


class ReqData(BaseModel):
    name: str
    year: int
    month: int
    day: int
    hours: int
    minutes: int
    type_of_time: int = Field(
        validation_alias=AliasChoices("type_of_time", "typeOfTime"),
        serialization_alias="typeOfTime",
    )
    offset: int
    place: str
    latitude: float
    longitude: float
    time_zone_id: str = Field(
        validation_alias=AliasChoices("time_zone_id", "timeZoneId"),
        serialization_alias="timeZoneId",
    )


# ==================  ephem files types  =======================


#  [-4733494022,"north"],[-4732252235,"south"]
class NodesJsonStruct(BaseModel):
    time: float
    which: str


class BspFile(BaseModel):
    bsp_ptr: bytes
    nodes_ptr: tuple[NodesJsonStruct]


# ==================  coord types  =======================
class Position(BaseModel):
    x: float
    y: float
    z: float


# ==================  time types  ===============================


class GregDate(BaseModel):
    year: int
    month: int
    day: int
    hours: int
    minutes: int


class LocalTime(GregDate):
    offset: int
    place: str
    longitude: float
    latitude: float
    time_zone_id: str = Field(
        validation_alias=AliasChoices("time_zone_id", "timeZoneId"),
        serialization_alias="timeZoneId",
    )


class CDTime(BaseModel):
    pers_time_sec: int = Field(
        validation_alias=AliasChoices("pers_time_sec", "persTimeSec"),
        serialization_alias="persTimeSec",
    )
    pers_time_local: LocalTime = Field(
        validation_alias=AliasChoices("pers_time_local", "persTimeLocal"),
        serialization_alias="persTimeLocal",
    )
    pers_time_utc: GregDate = Field(
        validation_alias=AliasChoices("pers_time_utc", "persTimeUtc"),
        serialization_alias="persTimeUtc",
    )
    des_time_sec: int = Field(
        validation_alias=AliasChoices("des_time_sec", "desTimeSec"),
        serialization_alias="desTimeSec",
    )
    des_time: GregDate = Field(
        validation_alias=AliasChoices("des_time", "desTime"),
        serialization_alias="desTime",
    )
    type_of_time: int = Field(
        validation_alias=AliasChoices("type_of_time", "typeOfTime"),
        serialization_alias="typeOfTime",
    )


# ======================  astro ===============================
class UranusOpp(BaseModel):
    ur_op_start_sec: int = Field(
        validation_alias=AliasChoices("ur_op_start_sec", "uranusOppStartSec"),
        serialization_alias="uranusOppStartSec",
    )
    ur_op_end_sec: int = Field(
        validation_alias=AliasChoices("ur_op_end_sec", "uranusOppEndSec"),
        serialization_alias="uranusOppEndSec",
    )
    ur_op_start_utc: GregDate = Field(
        validation_alias=AliasChoices("ur_op_start_utc", "uranusOppStartUTC"),
        serialization_alias="uranusOppStartUTC",
    )
    ur_op_end_utc: GregDate = Field(
        validation_alias=AliasChoices("ur_op_end_utc", "uranusOppEndUTC"),
        serialization_alias="uranusOppEndUTC",
    )


class Astro(BaseModel):
    uranus_opp: UranusOpp = Field(
        validation_alias=AliasChoices("uranus_opp", "uranusOpp"),
        serialization_alias="uranusOpp",
    )


# ===================  numerology ============================


class Numerology(BaseModel):
    pifagor1: int
    pifagor2: int
    pifagor3: int
    pifagor4: int
    pifagor5: int
    pifagor6: int
    mc1: list[int]
    mc2: list[int]
    mc3: list[int]
    karmic_task: str = Field(
        validation_alias=AliasChoices("karmic_task", "karmicTask"),
        serialization_alias="karmicTask",
    )

    soul_level: int = Field(
        validation_alias=AliasChoices("soul_level", "soulLevel"),
        serialization_alias="soulLevel",
    )
    opv: int
    opv2: int
    tp: int
    planetary_task: int = Field(
        validation_alias=AliasChoices("planetary_task", "planetaryTask"),
        serialization_alias="planetaryTask",
    )
    soul_lvl_past_life: int = Field(
        validation_alias=AliasChoices("soul_lvl_past_life", "soulLevelPastLife"),
        serialization_alias="soulLevelPastLife",
    )
    keeper: bool
    mage: bool = Field(
        validation_alias=AliasChoices("mage", "whiteMage"),
        serialization_alias="whiteMage",
    )
    social_task: int = Field(
        validation_alias=AliasChoices("social_task", "socialTask"),
        serialization_alias="socialTask",
    )
    mc_whole_life_task: int = Field(
        validation_alias=AliasChoices("mc_whole_life_task", "mcWholeLifeTask"),
        serialization_alias="mcWholeLifeTask",
    )
    mc1_task: int = Field(
        validation_alias=AliasChoices("mc1_task", "mc1Task"),
        serialization_alias="mc1Task",
    )
    mc2_task: int = Field(
        validation_alias=AliasChoices("mc2_task", "mc2Task"),
        serialization_alias="mc2Task",
    )
    mc3_task: int = Field(
        validation_alias=AliasChoices("mc3_task", "mc3Task"),
        serialization_alias="mc3Task",
    )
    mc2_opt_task: str = Field(
        validation_alias=AliasChoices("mc2_opt_task", "mc2OptionalTask"),
        serialization_alias="mc2OptionalTask",
    )
    matrix_code: int = Field(
        validation_alias=AliasChoices("matrix_code", "matrixCode"),
        serialization_alias="matrixCode",
    )


class NM(BaseModel):
    pers: Numerology
    des: Numerology


# ======================  hd ===============================


class Zodiac(BaseModel):
    name: str
    degrees: int
    minutes: int
    seconds: int
    text: str


class PlanetsData(BaseModel):
    name: str
    number: int
    longitude: float
    hex: int
    line: int
    color: int
    tone: int
    base: int
    power: int
    direction: str
    zodiac: Zodiac


class Cross(BaseModel):
    first: int
    second: int
    third: int
    fourth: int


class GeneralInfo(BaseModel):
    authority: str
    hd_type: str = Field(
        validation_alias=AliasChoices("hd_type", "hdType"), serialization_alias="hdType"
    )
    definition: str


class SpecialInfo(BaseModel):
    cogn: str

    cogn_transf: str = Field(
        validation_alias=AliasChoices("cogn_transf", "cognTtransf"),
        serialization_alias="cognTtransf",
    )
    theme: str
    theme_transf: str = Field(
        validation_alias=AliasChoices("theme_transf", "themeTransf"),
        serialization_alias="themeTransf",
    )
    nutr_type: str = Field(
        validation_alias=AliasChoices("nutr_type", "nutrType"),
        serialization_alias="nutrType",
    )
    nutr_type_transf: str = Field(
        validation_alias=AliasChoices("nutr_type_transf", "nutrTypeTransf"),
        serialization_alias="nutrTypeTransf",
    )

    env: str

    env_transf: str = Field(
        validation_alias=AliasChoices("env_transf", "envTransf"),
        serialization_alias="envTransf",
    )
    mind: str
    motiv: str
    motiv_transf: str = Field(
        validation_alias=AliasChoices("motiv_transf", "motivTransf"),
        serialization_alias="motivTransf",
    )
    mind_transf: str = Field(
        validation_alias=AliasChoices("mind_transf", "mindTransf"),
        serialization_alias="mindTransf",
    )
    view: str
    view_transf: str = Field(
        validation_alias=AliasChoices("view_transf", "viewTransf"),
        serialization_alias="viewTransf",
    )
    persp: str
    persp_transf: str = Field(
        validation_alias=AliasChoices("persp_transf", "perspTransf"),
        serialization_alias="perspTransf",
    )
    variable: str
    cross: Cross
    profile: str


class Gate(BaseModel):
    defined: bool
    number: int
    pers: bool
    des: bool


class Channel(BaseModel):
    defined: bool
    number: int
    first_gate: Gate = Field(
        validation_alias=AliasChoices("first_gate", "firstGate"),
        serialization_alias="firstGate",
    )
    second_gate: Gate = Field(
        validation_alias=AliasChoices("second_gate", "secondGate"),
        serialization_alias="secondGate",
    )


class Centers(BaseModel):
    head: bool
    ajna: bool
    throat: bool
    g: bool
    ego: bool
    emo: bool
    spleen: bool
    sacral: bool
    root: bool


# start_degree incl. , end_degree excl.
class HexRangeRAD(BaseModel):
    start_degree: float = Field(
        validation_alias=AliasChoices("start_degree", "startDegree"),
        serialization_alias="startDegree",
    )

    end_degree: float = Field(
        validation_alias=AliasChoices("end_degree", "endDegree"),
        serialization_alias="endDegree",
    )


class ChannelsNumbers(BaseModel):
    number: int
    first_gate: int = Field(
        validation_alias=AliasChoices("first_gate", "firstGate"),
        serialization_alias="firstGate",
    )
    second_gate: int = Field(
        validation_alias=AliasChoices("second_gate", "secondGate"),
        serialization_alias="secondGate",
    )


class BaseHD(BaseModel):
    general_inf: GeneralInfo = Field(
        validation_alias=AliasChoices("general_inf", "generalInfo"),
        serialization_alias="generalInfo",
    )
    gates: list[Gate]  # 64 gates   and number 0 is empty
    channels: list[Channel]  # 36 channels and number 0 is empty
    centers: Centers  # 9 centers


class OneSide(BaseHD):
    planets_data: list[PlanetsData] = Field(
        validation_alias=AliasChoices("planets_data", "planetsData"),
        serialization_alias="planetsData",
    )  # 13 planets + 0 SSB


class HD(BaseHD):
    pers: OneSide
    des: OneSide
    special_inf: SpecialInfo = Field(
        validation_alias=AliasChoices("special_inf", "specialInfo"),
        serialization_alias="specialInfo",
    )


# ============= fd (formula of the soul)  =====================


class PlFdData(BaseModel):
    orbit: int
    point_to_planet: str = Field(
        validation_alias=AliasChoices("point_to_planet", "pointToPlanet"),
        serialization_alias="pointToPlanet",
    )
    centers_number: int = Field(
        validation_alias=AliasChoices("centers_number", "centersNumber"),
        serialization_alias="centersNumber",
    )


class FdSubStruct(BaseModel):
    pl_fdata: list[PlFdData] = Field(
        validation_alias=AliasChoices("pl_fdata", "plFdata"),
        serialization_alias="plFdata",
    )
    centers_arr: list[list[str]] = Field(
        validation_alias=AliasChoices("centers_arr", "centersArr"),
        serialization_alias="centersArr",
    )


class FD(BaseModel):
    pers: FdSubStruct
    des: FdSubStruct


# ========= the main CD type and the one to respond  ============


class CDinfo(BaseModel):
    name: str
    time: CDTime
    hd: HD = Field(
        validation_alias=AliasChoices("hd", "hdInfo"),
        serialization_alias="hdInfo",
    )
    fd: FD = Field(
        validation_alias=AliasChoices("fd", "fdInfo"),
        serialization_alias="fdInfo",
    )
    astro: Astro = Field(
        validation_alias=AliasChoices("astro", "astroInfo"),
        serialization_alias="astroInfo",
    )
    nm: NM = Field(
        validation_alias=AliasChoices("nm", "numerologyInfo"),
        serialization_alias="numerologyInfo",
    )
