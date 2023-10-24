from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from core.database import Base


class ComputersDatabase(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    device_hostname = Column(String, nullable=False)
    device_platform = Column(String, nullable=False)
    device_ipv4 = Column(ARRAY(String), nullable=False)
    device_ipv6 = Column(ARRAY(String), nullable=False)
    device_online = Column(Boolean, nullable=False)
