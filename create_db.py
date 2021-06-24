from database import Base,engine
from models import Item

print("Creating database ....")

Base.metadata.create_all(engine)