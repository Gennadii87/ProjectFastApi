from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Dish as DBDish
from schemas import Dish, DishCreate
from database import get_db
from typing import List
from fastapi import status

router = APIRouter()


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=List[Dish])
def read_all_dishes(submenu_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    dishes = (db.query(DBDish).filter(DBDish.submenu_id == submenu_id).offset(skip)
              .limit(limit).all())
    for dish in dishes:
        dish.price = f"{dish.price:.2f}"

    return dishes


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=Dish)
def read_dish(submenu_id: str, dish_id: str, db: Session = Depends(get_db)):
    dish = (db.query(DBDish).filter(DBDish.id == dish_id, DBDish.submenu_id == submenu_id)
            .first())
    if dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    dish.price = f"{dish.price:.2f}"
    return dish


@router.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=Dish, status_code=status
             .HTTP_201_CREATED)
def create_dish(submenu_id: str, dish: DishCreate, db: Session = Depends(get_db)):
    db_dish = DBDish(**dish.dict(), submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    db_dish.price = "{:.2f}".format(db_dish.price)
    return db_dish


@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=Dish)
def update_dish(submenu_id: str, dish_id: str, dish: DishCreate, db: Session = Depends(get_db)):
    db_dish = (db.query(DBDish).filter(DBDish.id == dish_id, DBDish.submenu_id == submenu_id)
               .first())
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    for key, value in dish.dict().items():
        setattr(db_dish, key, value)

    db.commit()
    db.refresh(db_dish)
    db_dish.price = "{:.2f}".format(db_dish.price)
    return db_dish


@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(submenu_id: str, dish_id: str, db: Session = Depends(get_db)):
    dish = (db.query(DBDish).filter(DBDish.id == dish_id, DBDish.submenu_id == submenu_id)
            .first())
    if dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    db.delete(dish)
    db.commit()
    return {"message": "Dish deleted successfully"}
