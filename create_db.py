from database import engine, Base
import users

Base.metadata.create_all(engine)
