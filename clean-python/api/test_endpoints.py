import pytest
import config
import bcrypt

from app import create_app
from sqlalchemy import create_engine, text

database = create_engine(config.test_config['DB_URL'], encoding='utf-8', max_overflow = 0)

@pytest.fixture
def api():
    app = create_app(config.test_config)
    app.config['TEST'] = True
    api = app.test_client()

    return api
def setup_function():
    ## Create a test user
    hashed_password = bcrypt.hashpw(
        b"test password",
        bcrypt.gensalt()
    )
    new_user = {
        'id':1,
        'name':'송은우',
        'email':'songew@gmail.com',
        'profile':'test profile',
        'hashed_password': hashed_password
    }
    database.execute(text("""
        INSERT INTO users (
            id,
            name,
            email,
            profile,
            hashed_password
        ) VALUES (
            :id,
            :name,
            :profile,
            :hashed_password
        )
    """), new_user)

def teardown_function():
    database.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    database.execute(text("TRUNCATE users"))
    database.execute(text("TRUNCATE tweets"))
    database.execute(text("TRUNCATE users_follow_list"))
    database.execute(text("SET FOREIGN_KEY_CHECKS=1"))

def test_tweet(api):
    ## 로그인
    resp = api.post(
        '/login',
        data = json.dumps({
            'email': 'songew@gmail.com',
            'password': 'test password',
        }),
        content_type = 'application/json'
    )
    resp_json = json.loads(resp.data.decode('utf-8'))
    access_token = resp_json['access_token']

    ## tweet
    resp = api.post(
        '/tweet',
        data = json.dumps({'tweet': "Hello World!"}),
        content_type = 'application/json',
        headers = {'Authorization': access_token}
    )
    assert resp.status_code == 200

    ## tweet 확인
    resp = api.get(f'/timeline/1')
    tweets = json.loads(resp.data.decode('utf-8'))

    assert resp.status_code == 200
    assert tweets == {
        'user_id': 1,
        'timeline': [
            {
                'user_id': 1,
                'tweet': "Hello World!"
            }
        ]    
    }

def test_ping(api):
    resp = api.get('/ping')
    assert b'pong' in resp.data
