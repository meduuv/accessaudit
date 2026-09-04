from accessaudit import compare

def test_compare():
    result = compare(["admin", "ops"], ["admin", "guest"])
    assert result["unexpected"] == ["guest"]
    assert result["missing"] == ["ops"]
    assert result["ok"] is False
