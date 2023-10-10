from dataclasses import dataclass
from typing import Literal


RegisterStatus = Literal[
    "EXPIRED",  # 소멸
    "REGISTERED",  # 등록
    "ABANDONED",  # 포기
    "INVALID",  # 무효
    "APPLIED",  # 출원
    "REJECTED",  # 거절
    "CANCELED",  # 취하
    "ANNOUNCED",  # 공고
    "UNKNOWN",  # 알 수 없음
]

TmDivisionCode = Literal[
    "KOREAN_CHARACTER",  # 한글상표
    "SHAPE",  # 도형상표
    "COMPOSITE",  # 도형복합
    "ENGLISH_CHARACTER",  # 영문상표
    "CHINESE_CHARACTER",  # 한자상표
    "COMPLEX_CHARACTER",  # 복합문자
    "JAPANESE_CHARACTER",  # 일어상표
    "UNKNOWN",  # 알 수 없음
]


@dataclass
class Trademark:
    application_number: str
    register_status: RegisterStatus
    tm_division_code: TmDivisionCode
    product_name: str | None
    product_name_eng: str | None
    image_url: str | None
    product_types: list[str] | None
    similar_group_codes: list[str] | None


@dataclass
class Filter:
    registerStatus: list[RegisterStatus] | None
    tmDivisionCode: list[TmDivisionCode] | None
    productTypes: list[str] | None
    similarGroupCodes: list[str] | None

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v:
                d[k] = v

        return d
