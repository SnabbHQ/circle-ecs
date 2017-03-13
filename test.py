import hello
import logging

def test_hello():
    resp = hello.app.test_client().get('/')
    logging.info(resp.data)
    assert b'Hello' in resp.data
