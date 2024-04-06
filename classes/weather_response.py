from pydantic import BaseModel


class Condition(BaseModel):
    """Состояние погоды (облачно, ясно) и ссылка на иконку"""

    text: str
    icon: str
    code: int


class Location(BaseModel):
    """Информация о запрашиваемой локации"""

    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str


class Current(BaseModel):
    """Основная информация о погоде"""

    last_updated_epoch: int
    last_updated: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    vis_km: float
    vis_miles: float
    uv: float
    gust_mph: float
    gust_kph: float


class WeatherResponse(BaseModel):
    """Корневой объект ответа АПИ погоды"""

    location: Location
    current: Current
