from __future__ import annotations

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        ...

    @abstractmethod
    def remove_book(self, title: str) -> None:
        ...

    @abstractmethod
    def get_books(self) -> list[Book]:
        ...


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info("Додано книгу: %s", book)

    def remove_book(self, title: str) -> None:
        for b in list(self.books):
            if b.title == title:
                self.books.remove(b)
                logger.info("Видалено книгу з назвою: %s", title)
                break
        else:
            logger.info("Книгу з назвою '%s' не знайдено", title)

    def get_books(self) -> list[Book]:
        return list(self.books)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("Бібліотека порожня")
            return
        for b in books:
            logger.info("%s", str(b))


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year_str = input("Enter book year: ").strip()
                try:
                    year = int(year_str)
                except ValueError:
                    logger.info("Рік має бути числом. Спробуйте ще раз.")
                    continue
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
