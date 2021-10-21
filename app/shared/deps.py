from app.db.database import SessionLocal

# Dependency
def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        print("}++++++++++++++++++++++++++++++")
        print('returning', db)
        yield db
    finally:
        db.close()