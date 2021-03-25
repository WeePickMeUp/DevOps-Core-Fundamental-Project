from flask import url_for
from flask_testing import TestCase
from application import db
from application.models import Name, Groups
from app import app

#pytest --cov=app --cov-report=term-missing
#pytest --cov . --cov-report html

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        name = Name(title = "Cheese")
        groups = Groups(title = "1.50")
        db.session.add(name)
        db.session.add(groups)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestNew(TestBase):
    def test_new(self):
        response = self.client.post(
            url_for('new'),
            data = dict(name="Cheese"),
            follow_redirects=True
        )
        self.assertIn(b'Cheese',response.data)

class TestNew(TestBase):
    def test_newgroups(self):
        response = self.client.post(
            url_for('newgroups'),
            data = dict(groups="1.50"),
            follow_redirects=True
        )
        self.assertIn(b'1.50',response.data)

class TestRead(TestBase):
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)

class TestIndex(TestBase):
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
