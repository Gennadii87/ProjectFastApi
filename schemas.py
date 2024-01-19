from pydantic import BaseModel, UUID4

from typing import Union


class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreate(MenuBase):
    pass


class Menu(MenuBase):
    id: UUID4
    title: str
    description: str
    submenus_count: int = 0
    dishes_count: int = 0

    class Config:
        orm_mode = True


class SubMenuBase(BaseModel):
    title: str
    description: str


class SubMenuCreate(SubMenuBase):
    pass


class SubMenu(SubMenuBase):
    id: UUID4
    title: str
    description: str
    dishes_count: int = 0

    class Config:
        orm_mode = True


class DishBase(BaseModel):
    title: str
    description: str
    price: Union[float, str]


class DishCreate(DishBase):
    pass


class Dish(DishBase):
    id: UUID4
    title: str
    description: str
    price: Union[float, str]

    class Config:
        orm_mode = True
