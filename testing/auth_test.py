from ..middlewares.hashing import hash_password
from ..src.db_auth import get_pw_and_salt, verify_password, new_user, user_is_active, alter_user_state, delete_user, \
    get_role
from sqlalchemy.exc import IntegrityError


def test_hash_password():
    hashed_password, salt = hash_password("test")
    hashed_password2, _ = hash_password("test", salt)

    assert hashed_password == hashed_password2


def test_verify_password():
    # pw = '243262243132244e42696e363155475953464d436541364f3151534e2e35697777334532463548674a746d494556566d594369536b525047446b6965'
    # salt = '243262243132244e42696e363155475953464d436541364f3151534e2e'

    # assert verify_password("test", pw, salt)

    creds = get_pw_and_salt("andres.gonzalezpineda@gmail.com")
    assert verify_password("Hola1234", creds["password"], creds["salt"])


def test_new_user():
    email = "gusanitor8@gmail.com"
    name = "Gustavo Gonzalez"
    password = "Hola1234"
    role = "viewer"

    passed = False

    try:
        new_user(email=email,
                 password=password,
                 rol=role,
                 name=name)
        passed = True
    except IntegrityError:
        passed = False

    assert passed


def test_get_pw_and_salt():
    email = "andres.gonzalezpineda@gmail.com"
    pw_hahsed = "24326224313224584b702f705374384b4c717469756255527045344a4f784868596a6a78716178417831686468312e6c7837527255556e324148364b"
    salt = "24326224313224584b702f705374384b4c717469756255527045344a4f"
    credentials = get_pw_and_salt(email)

    assert credentials['password'] == pw_hahsed
    assert credentials['salt'] == salt


def test_is_user_active():
    email = "gusanitor8@gmail.com"
    assert user_is_active(email) == True

    email = "pepe"
    assert user_is_active(email) == False


def test_alter_user_state():
    email = "gusanitor8@gmail.com"
    alter_user_state(email, False)

    assert user_is_active(email) == False

    alter_user_state(email, True)

    assert user_is_active(email) == True


def test_delete_user():
    email = "pepe"
    res = delete_user(email)

    assert res == False

    email = "gusanitor8@gmail.com"
    res = delete_user(email)

    assert res == True

    test_new_user()


def test_get_user_role():
    user_id = 8
    role = get_role(user_id)

    assert role == "admin"
