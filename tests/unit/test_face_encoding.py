import pytest
from face_recognition_service import encode_face

def test_encode_valid_face():
    """
    Test that encoding a valid face image returns a 128-dim vector.
    """
    image_path = "tests/test_data/sample_faces/player_1.jpg"
    encoding = encode_face(image_path)
    assert encoding is not None
    assert len(encoding) == 128

def test_encode_invalid_face():
    """
    Test that encoding a non-face image raises an exception or returns None.
    """
    image_path = "tests/test_data/sample_faces/unknown.jpg"
    encoding = encode_face(image_path)
    assert encoding is None or isinstance(encoding, Exception)
