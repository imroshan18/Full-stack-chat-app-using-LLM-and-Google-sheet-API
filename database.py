"""
Database configuration and session management for HRMS Backend.
All sensitive values are loaded from environment variables via .env file.
"""
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

# ── Connection URL ──────────────────────────────────────────────────────────
# Set DATABASE_URL in your .env file, e.g.:
#   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/hrms_db
DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/hrms_db",  # dev fallback only
)

# ── Engine ──────────────────────────────────────────────────────────────────
engine = create_async_engine(
    DATABASE_URL,
    echo=os.getenv("DB_ECHO", "false").lower() == "true",
    pool_pre_ping=True,
)

# ── Session factory ─────────────────────────────────────────────────────────
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ── Base model ───────────────────────────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ── Dependency (FastAPI) ─────────────────────────────────────────────────────
async def get_db() -> AsyncSession:
    """Yield a database session; close it when the request is done."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# ── Table initialisation ─────────────────────────────────────────────────────
async def init_db() -> None:
    """Create all tables (use Alembic for production migrations)."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
