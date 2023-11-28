from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 이 코드는 SQLAlchemy를 사용하여 데이터베이스와의 상호 작용을 
# 용이하게 하기 위한 기본적인 설정을 수행합니다.


# sql_app.db 파일에 데이터베이스 저장됨
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# SQLAlchemy의 create_engine 함수를 사용하여 데이터베이스 엔진을 생성합니다.
# SQLALCHEMY_DATABASE_URL에 지정된 데이터베이스에 연결합니다.
# connect_args={"check_same_thread": False}는 SQLite 데이터베이스를 사용할 때, 
# 동일한 스레드에서 여러 연결을 허용하도록 하는 옵션입니다. SQLite는 기본적으로 동일한 스레드에서만 연결이 가능합니다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}   
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()