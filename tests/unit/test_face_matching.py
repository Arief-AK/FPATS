import pytest
from face_recognition_service import encode_face, match_face

def test_match_same_face():
    """
    Encoding the same face twice should match above a high threshold.
    """
    image_path = "tests/test_data/sample_faces/player_1.jpg"
    encoding1 = encode_face(image_path)
    encoding2 = encode_face(image_path)
    similarity = match_face(encoding1, encoding2)
    assert similarity > 0.9

def test_match_different_faces():
    """
    Encoding different faces should return low similarity.
    """
    image1 = "tests/test_data/sample_faces/player_1.jpg"
    image2 = "tests/test_data/sample_faces/unknown.jpg"
    encoding1 = encode_face(image1)
    encoding2 = encode_face(image2)
    similarity = match_face(encoding1, encoding2)
    assert similarity < 0.6
