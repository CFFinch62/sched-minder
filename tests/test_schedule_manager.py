def test_get_current_event():
    manager = ScheduleManager()
    event = manager.get_current_event(
        "Regular Schedule",
        datetime.strptime("08:30", "%H:%M")
    )
    assert event == "Period 1" 