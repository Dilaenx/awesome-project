from sqlalchemy import create_engine, text
from config import settings

engine = create_engine(settings.database_url())
with engine.connect() as conn:
    conn.execute(text("SELECT 1"))  # Added a SQL string inside text()
print("Engin Start")