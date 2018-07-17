from guizero import App, Text
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    enable_test,
    display_test,
    text_test,
    color_test, 
    size_text_test,
    events_test,
    cascaded_properties_test,
    inherited_properties_test
    )

def test_default_values():
    a = App()
    t = Text(a, multiline=True)
    assert t.master == a
    assert t.grid == None
    assert t.align == None
    assert t.size == 12
    assert t.text_color == "black"
    assert t.font == "Arial"
    assert t.value == ""
    a.destroy() 

def test_alt_values():
    a = App(layout = "grid")
    t = Text(
        a,
        multiline=True,
        text="foo", 
        size = 14, 
        color="green", 
        bg="red", 
        font="Times New Roman", 
        grid = [0,1], 
        align="top")

    assert t.master == a
    assert t.grid[0] == 0
    assert t.grid[1] == 1
    assert t.align == "top"
    assert t.size == 14
    assert t.text_color == "green"
    assert t.bg == "red"
    assert t.font == "Times New Roman"
    assert t.value == "foo"
    a.destroy()

def test_getters_setters():
    a = App()
    t = Text(a, multiline=True)
    t.value = "foo"
    assert t.value == "foo"
    t.size = 18
    assert t.size == 18
    a.destroy()

def test_clear():
    a = App()
    t = Text(a, text = "foo", multiline=True)
    t.clear()
    assert t.value == ""
    a.destroy()

def test_append():
    a = App()
    t = Text(a, text = "foo", multiline=True)
    t.append("bar")
    assert t.value == "foobar"
    a.destroy()

def test_after_schedule():
    a = App()
    t = Text(a, multiline=True)
    schedule_after_test(a, t)
    a.destroy()

def test_repeat_schedule():
    a = App()
    t = Text(a, multiline=True)
    schedule_repeat_test(a, t)
    a.destroy()

def test_destroy():
    a = App()
    t = Text(a, multiline=True)
    destroy_test(t)
    a.destroy()

def test_display():
    a = App()
    t = Text(a, multiline=True)
    display_test(t)
    a.destroy()

def test_text():
    a = App()
    t = Text(a, multiline=True)
    text_test(t)
    a.destroy()

def test_color():
    a = App()
    t = Text(a, multiline=True)
    color_test(t)
    a.destroy()

def test_width():
    a = App()
    t = Text(a, multiline=True)
    default = t.width
    t.width = 30
    assert t.width == 30
    t.width = None
    assert t.width == default
    a.destroy()

def test_events():
    a = App()
    t = Text(a, multiline=True)
    events_test(t)
    a.destroy()

def test_cascaded_properties():
    a = App()
    t = Text(a, multiline=True)
    cascaded_properties_test(a, t, True)
    a.destroy()

def test_inherited_properties():
    a = App()
    inherited_properties_test(a, lambda: Text(a, multiline=True), True)
    a.destroy()