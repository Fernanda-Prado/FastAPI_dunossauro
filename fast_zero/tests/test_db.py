from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='nome', email='mail@email.com', password='secret')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'mail@email.com'))
    assert result.username == 'nome'
