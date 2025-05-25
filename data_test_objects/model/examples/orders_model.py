from pydantic import BaseModel, Field, UUID4, EmailStr


class ItemsModel(BaseModel, extra="fobid"):
    """Модель данных для проверки элементов заказа - элемент поля items
    ответа ручки POST /orders
    """
    productId: UUID4
    quantity: int


class OrdersModel(BaseModel, extra="fobid"):
    """Модель данных для проверки заказов - ответ ручки POST /orders"""
    orderId: UUID4 = Field(description="Идентификатор заказа")
    items: list[ItemsModel] = Field(description="Исписок продуктов")
    customerEmail: EmailStr = Field(description="Электорнный адрес покупателя")
    deliveryAddress: str
