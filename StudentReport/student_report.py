import typing


class StudentReport:

    def __init__(self, id_in: typing.Tuple[str, ...]):
        self.identity = {'last': id_in[0], 'first': id_in[1], 'id': id_in[2]}
        self.test_cases = {}

    def identifier(self) -> str:
        return self.identity['last'] + '_' + self.identity['first'] + ' ' + self.identity['id']

    def name(self) -> str:
        return self.identity['first'] + ' ' + self.identity['last']

    def id(self) -> str:
        return self.identity['id']

    def passed_part(self, part: str) -> bool:
        for test_case in self.test_cases.keys():
            if part not in self.test_cases[test_case].keys() or not self.test_cases[test_case][part]:
                return False
        return True
