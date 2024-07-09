import uuid

import pytest  # type: ignore

from src.models.settings.db_connection_handler import db_connection_handler

from .links_repositoriy import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


@pytest.mark.skip(reason="This test is not implemented yet.")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "https://www.google.com",
        "title": "Google",
    }

    link_repository.registry_link(link_infos)


@pytest.mark.skip(reason="This test is not implemented yet.")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    response = link_repository.find_links_from_trip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
