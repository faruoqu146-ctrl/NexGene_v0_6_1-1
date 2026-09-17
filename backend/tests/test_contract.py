def test_contract():
    backend = open("backend/app/main.py").read()
    ui = open("mobile/app.js").read()
    assert "/api/v1/checkins/morning" in backend
    assert "/api/v1/checkins/evening" in backend
    assert "sleep_duration" in ui
    assert "diet_quality" in ui
    assert "nicotine" in ui
