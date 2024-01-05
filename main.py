# Task Nr.1:

# Nasa needs to calculate expenses for the new mission: using OOP principles implement Base and Space Shuttle classes. Create a simple calculator with:

# Base class should give a functionality to know info about spacecraft (age, cost, year built, weight etc.. ).
# Through the main class you should be able to calculate the mission cost which includes:
# fuel cost (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))) , average personals expenditures ( ppl x base_salary ).
# Prepare the final report in the file document and on screen with a method get_full_report with all gathered and calculated data.
import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.DEBUG,
    filename="space.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Spacecraft(ABC):
    def __init__(self, age: int, cost: int, built_year: int, weight: int) -> None:
        self.__age = age
        self.__cost = cost
        self.__built_year = built_year
        self.__weight = weight

    def get_info(self) -> str:
        return f"Age: {self.__age} Years\nCost: {self.__cost}$\nBuilt year: {self.__built_year}\nWeight: {self.__weight}T"

    @abstractmethod
    def _get_fuel_cost(self) -> float:
        pass

    @abstractmethod
    def _personals_expenditures(self) -> float:
        pass


class SpaceShuttle(Spacecraft):
    def __init__(
        self,
        age: int,
        cost: int,
        built_year: int,
        weight: int,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        people_count: int,
        base_salary: int,
    ) -> None:
        super().__init__(age, cost, built_year, weight)
        self.__fuel_cost = fuel_cost
        self.__burn_rate = burn_rate
        self.__orbit_height = orbit_height
        self.__people_count = people_count
        self.__base_salary = base_salary

    def __get_burn_rate_variable(self) -> float:
        return 2500 / self.__orbit_height

    def _get_fuel_cost(self) -> float:
        return round(
            self.__fuel_cost * self.__burn_rate * self.__get_burn_rate_variable(),
            2,
        )

    def _personals_expenditures(self) -> float:
        return self.__people_count * self.__base_salary

    def get_full_report(self) -> str:
        return f"-Spacecraft info-\n{self.get_info()}\n\n-Expedition costs-\nFuel cost: {self._get_fuel_cost()}\nPersonals expenditures: {self._personals_expenditures()}"


spaceshuttle = SpaceShuttle(
    age=26,
    cost=1300000,
    built_year=1997,
    weight=100,
    fuel_cost=1.2,
    burn_rate=150.5,
    orbit_height=22.236,
    people_count=30,
    base_salary=5000,
)

print(spaceshuttle.get_full_report())
logging.info(spaceshuttle.get_full_report())
