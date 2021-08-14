from main import hello  # , echo


def test_hello():
    assert hello() == "Hello World"


# # This needs flask specific mocking, outside scope of this tutorial
# def test_echo():
#     result = echo("Trevor")
#     print("*" * 50 + result + "*" * 50)
#     assert echo("Trevor") == "new-name: Trevor"
