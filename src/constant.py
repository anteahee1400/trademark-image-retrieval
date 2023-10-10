from src.entity import RegisterStatus, TmDivisionCode

RegisterStatusMap: dict[RegisterStatus, str] = {
    "EXPIRED": "소멸",
    "REGISTERED": "등록",
    "ABANDONED": "포기",
    "INVALID": "무효",
    "APPLIED": "출원",
    "REJECTED": "거절",
    "CANCELED": "취하",
    "ANNOUNCED": "공고",
}


TmDivisionCodeMap: dict[TmDivisionCode, str] = {
    "KOREAN_CHARACTER": "한글상표",
    "SHAPE": "도형상표",
    "COMPOSITE": "도형복합",
    "ENGLISH_CHARACTER": "영문상표",
    "CHINESE_CHARACTER": "한자상표",
    "COMPLEX_CHARACTER": "복합문자",
    "JAPANESE_CHARACTER": "일어상표",
}
