from daos.user_dao import UserDAO
from models.user import User
import time
from daos.user_dao_mongo import UserDAOMongo 

dao = UserDAO()
daoM = UserDAOMongo()

def test_user_select():
    user_list = daoM.select_all()
    assert len(user_list) >= 3

def test_user_insert():
    user = User(None, 'Joanne Test', 'joannetest@example.com')
    daoM.insert(user)
    user_list = daoM.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails

def test_user_update():
    user = User(None, 'Joe Test', 'testttt@example.com')
    assigned_id = daoM.insert(user)

    corrected_email = 'joetest@example.com'
    user.id = assigned_id
    user.email = corrected_email
    daoM.update(user)

    user_list = daoM.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails

    # cleanup
    daoM.delete(assigned_id)

def test_user_delete():
    user = User(None, 'Joe Test', 'joetest@example.com')
    assigned_id = daoM.insert(user)
    daoM.delete(assigned_id)

    new_dao = UserDAOMongo()
    user_list = new_dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails