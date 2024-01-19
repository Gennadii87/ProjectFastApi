from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SubMenu as DBSubMenu, Dish as DBDish
from schemas import SubMenu, SubMenuCreate
from database import get_db
from typing import List
from fastapi import status

router = APIRouter()


@router.get("/api/v1/menus/{menu_id}/submenus/", response_model=List[SubMenu])
def read_all_submenus(menu_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    submenus = db.query(DBSubMenu).filter(DBSubMenu.menu_id == menu_id).offset(skip).limit(limit).all()

    submenus_with_counts = []
    for submenu in submenus:
        dishes_count = db.query(DBDish).filter(DBDish.submenu_id == submenu.id).count()

        submenu_with_counts = SubMenu(
            id=submenu.id,
            title=submenu.title,
            description=submenu.description,
            dishes_count=dishes_count
        )

        submenus_with_counts.append(submenu_with_counts)

    return submenus_with_counts


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=SubMenu)
def read_submenu(menu_id: str, submenu_id: str, db: Session = Depends(get_db)):
    submenu = db.query(DBSubMenu).filter(DBSubMenu.id == submenu_id, DBSubMenu.menu_id == menu_id).first()
    if submenu is None:
        raise HTTPException(status_code=404, detail='submenu not found')

    # Подсчитываем количество блюд в подменю
    dishes_count = db.query(DBDish).filter(DBDish.submenu_id == submenu_id).count()

    # Создаем объект SubMenu с учетом количества блюд
    submenu_with_counts = SubMenu(
        id=submenu.id,
        title=submenu.title,
        description=submenu.description,
        dishes_count=dishes_count
    )

    return submenu_with_counts


@router.post("/api/v1/menus/{menu_id}/submenus/", response_model=SubMenu, status_code=status.HTTP_201_CREATED)
def create_submenu(menu_id: str, submenu: SubMenuCreate, db: Session = Depends(get_db)):
    submenu_data = submenu.dict()
    submenu_data["menu_id"] = menu_id

    db_submenu = DBSubMenu(**submenu_data)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=SubMenu)
def update_submenu(menu_id: str, submenu_id: str, submenu: SubMenuCreate, db: Session = Depends(get_db)):
    db_submenu = db.query(DBSubMenu).filter(DBSubMenu.id == submenu_id, DBSubMenu.menu_id == menu_id).first()
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="SubMenu not found")
    for key, value in submenu.dict().items():
        setattr(db_submenu, key, value)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
def delete_submenu(menu_id: str, submenu_id: str, db: Session = Depends(get_db)):
    submenu = db.query(DBSubMenu).filter(DBSubMenu.id == submenu_id, DBSubMenu.menu_id == menu_id).first()
    if submenu is None:
        raise HTTPException(status_code=404, detail="SubMenu not found")
    db.delete(submenu)
    db.commit()
    return {"message": "SubMenu deleted successfully"}
