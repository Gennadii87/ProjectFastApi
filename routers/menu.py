from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Menu as DBMenu, SubMenu as DBSubMenu, Dish as DBDish
from schemas import Menu, MenuCreate
from database import get_db
from typing import List
from fastapi import status


router = APIRouter()


@router.get("/api/v1/menus/", response_model=List[Menu])
def read_all_menus(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    menus = db.query(DBMenu).offset(skip).limit(limit).all()

    menus_with_counts = []
    for menu in menus:
        submenus_count = db.query(DBSubMenu).filter(DBSubMenu.menu_id == menu.id).count()
        dishes_count = db.query(DBDish).join(DBSubMenu).filter(DBSubMenu.menu_id == menu.id).count()

        menu_with_counts = Menu(
            id=menu.id,
            title=menu.title,
            description=menu.description,
            submenus_count=submenus_count,
            dishes_count=dishes_count
        )

        menus_with_counts.append(menu_with_counts)

    return menus_with_counts


@router.get("/api/v1/menus/{menu_id}", response_model=Menu)
def read_menu(menu_id: str, db: Session = Depends(get_db)):
    menu = db.query(DBMenu).filter(DBMenu.id == menu_id).first()
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")

    submenus_count = db.query(DBSubMenu).filter(DBSubMenu.menu_id == menu.id).count()
    dishes_count = db.query(DBDish).join(DBSubMenu).filter(DBSubMenu.menu_id == menu.id).count()

    menu_with_counts = Menu(
        id=menu.id,
        title=menu.title,
        description=menu.description,
        submenus_count=submenus_count,
        dishes_count=dishes_count
    )

    return menu_with_counts


@router.post("/api/v1/menus/", response_model=Menu, status_code=status.HTTP_201_CREATED)
def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    db_menu = DBMenu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


@router.patch("/api/v1/menus/{menu_id}", response_model=Menu)
def update_menu(menu_id: str, menu: MenuCreate, db: Session = Depends(get_db)):
    db_menu = db.query(DBMenu).filter(DBMenu.id == menu_id).first()
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    for key, value in menu.dict(exclude_unset=True).items():
        setattr(db_menu, key, value)
    db.commit()
    db.refresh(db_menu)
    return db_menu


@router.delete("/api/v1/menus/{menu_id}")
def delete_menu(menu_id: str, db: Session = Depends(get_db)):
    menu = db.query(DBMenu).filter(DBMenu.id == menu_id).first()
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    db.delete(menu)
    db.commit()
    return {"message": "Menu deleted successfully"}
