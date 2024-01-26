from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.models import Menu as DBMenu, SubMenu as DBSubMenu, Dish as DBDish
from database.schemas import Menu, MenuCreate
from database.database import get_db
from typing import List
from fastapi import status
from sqlalchemy import func


router = APIRouter()


@router.get("/api/v1/menus/", response_model=List[Menu])
def read_all_menus(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    menus_with_counts = db.query(
        DBMenu,
        func.count(DBSubMenu.id.distinct()).label('submenus_count'),
        func.count(DBDish.id.distinct()).label('dishes_count')
    ).select_from(DBMenu).outerjoin(DBSubMenu).outerjoin(DBDish).group_by(DBMenu.id).offset(skip).limit(limit).all()
    result_menus = []
    for menu, submenus_count, dishes_count in menus_with_counts:
        menu_with_counts = Menu(
            id=menu.id,
            title=menu.title,
            description=menu.description,
            submenus_count=submenus_count,
            dishes_count=dishes_count
        )
        result_menus.append(menu_with_counts)

    return result_menus


@router.get("/api/v1/menus/{menu_id}", response_model=Menu)
def read_menu(menu_id: str, db: Session = Depends(get_db)):
    menu_data = db.query(
        DBMenu,
        func.count(DBSubMenu.id.distinct()).label('submenus_count'),
        func.count(DBDish.id.distinct()).label('dishes_count')
    ).outerjoin(DBSubMenu, DBMenu.id == DBSubMenu.menu_id)\
     .outerjoin(DBDish, DBSubMenu.id == DBDish.submenu_id)\
     .filter(DBMenu.id == menu_id)\
     .group_by(DBMenu.id).first()

    if not menu_data:
        raise HTTPException(status_code=404, detail="menu not found")

    menu, submenus_count, dishes_count = menu_data
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
