# Учебный проект

## Описание:

Учебный проект - это виджет, который показывает несколько последних успешных банковских операций клиента

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/Sositrina/Project3
```

## Функционал

- `get_mask_card_number(card_number: int) -> str` — маскирует номер банковской карты (16 цифр).
- `get_mask_account(account_number: int) -> str` — маскирует номер банковского счёта (20 цифр).
- `mask_account_card(props: str) -> str` — определяет, карта или счёт, и маскирует номер.
- `get_date(str_date: str) -> str` — преобразует дату в формат `ДД.ММ.ГГГГ`.
- `filter_by_state(dictionaries, state="EXECUTED")` — фильтрует список операций по статусу.
- `sort_by_date(dictionaries, reverse=True)` — сортирует список операций по дате. 