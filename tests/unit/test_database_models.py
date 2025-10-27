import pytest
from database import get_session, Player, Attendance

@pytest.fixture
def db_session():
    """
    Provides a database session for testing.
    """
    session = get_session(test=True)    # test=True -> in-memory SQLite DB
    yield session
    session.close()

def test_insert_and_fetch_player(db_session):
    """
    Inserting and fetching a Player record.
    """
    player = Player(name="Test Player", face_encoding=b"123456")
    db_session.add(player)
    db_session.commit()

    fetched_player = db_session.query(Player).filter_by(name="Test Player").first()
    assert fetched_player is not None
    assert fetched_player.face_encoding == b"123456"

def test_attendance_foreign_key(db_session):
    """
    Testing foreign key relationship between Attendance and Player.
    """
    player = Player(name="Attendance Player", face_encoding=b"654321")
    db_session.add(player)
    db_session.commit()

    attendance = Attendance(player_id=player.id)
    db_session.add(attendance)
    db_session.commit()

    fetched_attendance = db_session.query(Attendance).filter_by(player_id=player.id).first()
    assert fetched_attendance is not None
    assert fetched_attendance.player_id == player.id