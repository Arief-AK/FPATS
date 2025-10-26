# core libraries
import pytest
import numpy as np

# user-defined libraries
from face_recognition_service import load_and_encode_face, compare_face_bool, compare_face_distance, analyze_multiple_faces, batch_match_face

KNOWN_IMAGE_DIR = "tests/test_data/known_faces"                     # TODO HKUR: add `known_faces` directory
UNKNOWN_IMAGE_DIR = "tests/test_data/unknown_faces"                 # TODO HKUR: add `unknown_faces` directory
KNOWN_IMAGE_PATH = f"{KNOWN_IMAGE_DIR}/player_1.jpg"                # TODO HKUR: add player_1 image (known player)
UNKNOWN_IMAGE_PATH = f"{UNKNOWN_IMAGE_DIR}/player_2.jpg"            # TODO HKUR: add player_2 image (unknown player)

IDENTICAL_THRESHOLD = 0.9   # TODO MKUR: check this
MATCH_THRESHOLD = 0.6       # TODO MKUR: check this

def test_compare_matching_face_bool():
    """
    Matching faces using `compare_faces` should return `true`
    """
    image_path = KNOWN_IMAGE_PATH
    known_encoding = load_and_encode_face(image_path)
    identical_encoding = load_and_encode_face(image_path)
    assert compare_face_bool(known_encoding, identical_encoding)[0] == True

def test_compare_different_face_bool():
    """
    Matching different faces using `compare_faces` should return `false`
    """
    known_image_path = KNOWN_IMAGE_PATH
    known_encoding = load_and_encode_face(known_image_path)

    uknown_image_path = UNKNOWN_IMAGE_PATH
    unknown_encoding = load_and_encode_face(uknown_image_path)
    assert compare_face_bool(known_encoding, unknown_encoding)[0] == False

def test_compare_face_matching_distance():
    """
    Matching faces using `face_distance` should produce a return value below `MATCH_THRESHOLD`
    """
    image_path = KNOWN_IMAGE_PATH
    known_encoding = load_and_encode_face(image_path)
    identical_encoding = load_and_encode_face(image_path)
    distances = compare_face_distance(known_encoding, identical_encoding)
    assert distances[0] > IDENTICAL_THRESHOLD

def test_compare_face_different_distance():
    """
    Matching faces using `face_distance` should produce a return value below `MATCH_THRESHOLD`
    """
    known_image_path = KNOWN_IMAGE_PATH
    known_encoding = load_and_encode_face(known_image_path)

    uknown_image_path = UNKNOWN_IMAGE_PATH
    unknown_encoding = load_and_encode_face(uknown_image_path)

    distances = compare_face_distance(known_encoding, unknown_encoding)
    assert distances[0] < MATCH_THRESHOLD

def test_batch_face_matching():
    """
    Matching an unknown face against directory of known faces
    """
    # inside `known_faces` directory, a known image exists: `player_1.jpg`
    known_faces_dir = KNOWN_IMAGE_DIR

    # unknown image is `player_x.jpg` (which is actually `player_1.jpg`)
    unknown_image_path = UNKNOWN_IMAGE_PATH
    matches, distances = batch_match_face(known_faces_dir, unknown_image_path)

    best_match_index = np.argmin(distances)
    assert matches[best_match_index] == True
    assert distances[best_match_index] < MATCH_THRESHOLD
