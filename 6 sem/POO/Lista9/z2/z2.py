from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from contextlib import contextmanager
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, relationship

engine = create_engine("sqlite:///database.db", echo=False, future=True)
SessionFactory = sessionmaker(bind=engine, autoflush=False, future=True)
ScopedSession = scoped_session(SessionFactory)

Base = declarative_base()

@contextmanager
def session_scope(desktop: bool = False):
    sess = SessionFactory() if desktop else ScopedSession()
    try:
        yield sess
        sess.commit()
    except Exception:
        sess.rollback()
        raise
    finally:
        sess.close()

class Parent(Base):
    __tablename__ = "parents"
    id   = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    children = relationship("Child", back_populates="parent", cascade="all, delete")

    def __repr__(self):
        return f"<Parent id={self.id} name={self.name!r}>"


class Child(Base):
    __tablename__ = "children"
    id        = Column(Integer, primary_key=True)
    name      = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)

    parent = relationship("Parent", back_populates="children")

    def __repr__(self):
        return f"<Child id={self.id} name={self.name!r} parent_id={self.parent_id}>"

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    with session_scope(desktop=True) as s:
        p = Parent(name="Karol")
        p.children.append(Child(name="Gosia"))
        p.children.append(Child(name="Jan"))
        s.add(p)

    with session_scope(desktop=False) as s:
        result = s.query(Parent).first()
        print(result, result.children)