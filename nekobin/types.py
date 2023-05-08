from datetime import datetime


class NekoFy:
    def __str__(self) -> str:
        return f"<{self.__class__.__name__}: {self.__dict__}>"

    def __repr__(self) -> str:
        return self.__str__()


class Neko(NekoFy):
    def __init__(
        self,
        ok: bool,
        result: dict,
        **kwargs
    ):
        self.success = ok
        self.key = result["key"]
        self.url = "https://nekobin.com/" + result["key"]
        self.raw = "https://nekobin.com/raw/" + result["key"]
        self.title = result["title"]
        self.author = result["author"]
        self.date = self.format_date(result["date"])
        self.length = result["length"]
        self.content = result["content"]

    def format_date(self, date: str):
        dt_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        py_timestamp = dt_obj.timestamp()
        return datetime.fromtimestamp(py_timestamp)
