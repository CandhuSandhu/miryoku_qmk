import qmk.keyboard


def test_keyboard_alias_boardsource_unicorne():
    assert qmk.keyboard.keyboard_folder('boardsource/unicorne') == 'boardsource/unicorne'
