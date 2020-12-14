from trailblazer_scraper import Profile


def test_tbid_provided():
    test_tbid = "testtbid"
    u = Profile("ecastelli", test_tbid)
    assert u.tbid == test_tbid


def test_scrape_basics():
    u = Profile("ecastelli")
    assert u.first_name == "Emily"
    assert u.last_name == "Castelli"
    assert len(u.tbid) == 18


def test_fetch_rank_data():
    u = Profile("ecastelli")
    assert u.rank_data is None
    u.fetch_rank_data()
    assert u.rank_data is not None
    assert "Id" in u.rank_data


def test_fetch_awards():
    u = Profile("ecastelli")
    assert len(u.awards) <= 0
    u.fetch_awards()
    assert len(u.awards) > 0
