from database import engine, Base
import users
import registration

Base.metadata.create_all(engine)
