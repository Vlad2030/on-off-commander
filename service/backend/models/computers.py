from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class ComputersDatabase(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    device_name = Column(String, nullable=False)
    device_platform = Column(String, nullable=False)
    device_ip = Column(String, nullable=False)
    device_online = Column(Boolean, nullable=False)
