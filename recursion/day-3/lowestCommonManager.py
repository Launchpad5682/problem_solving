from os import name


class OrgInfo:

    def __init__(self) -> None:
        pass


class OrgChart:

    def __init__(self, name) -> None:
        self.name = name
        self.directReports = []


a = OrgChart("A")
a.directReports.append(b)
a.directReports.append(c)
b = OrgChart("B")
c = OrgChart("C")
