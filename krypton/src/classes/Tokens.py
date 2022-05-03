from dataclasses import dataclass


@dataclass
class Token:
    line: int


@dataclass
class VAR_DECLERATION(Token):
    name: str
    value: object


@dataclass
class DEFINE_FUNCTION(Token):
    function_name: str
    function_params: list[object]


@dataclass
class INVOKE_FUNCTION(Token):
    function_name: str
    function_params: list[object]
