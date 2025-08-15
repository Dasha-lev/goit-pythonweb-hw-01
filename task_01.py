import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str | None = None) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        ...


class Car(Vehicle):
    def start_engine(self) -> None:
        if self.spec:
            logger.info("%s %s (%s): Двигун запущено", self.make, self.model, self.spec)
        else:
            logger.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        if self.spec:
            logger.info("%s %s (%s): Мотор заведено", self.make, self.model, self.spec)
        else:
            logger.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        ...

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        ...


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    vehicle3 = eu_factory.create_car("Ford", "Focus")
    vehicle3.start_engine()

    vehicle4 = eu_factory.create_motorcycle("BMW", "R1250")
    vehicle4.start_engine()
