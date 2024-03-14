# import time
#
# current_time = time.time()
#
#
# # Write your code below 👇
#
# def speed_calc_decorator(function):
#     def wrapper():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run time is: {end_time - start_time}")
#
#     return wrapper
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# fast_function()


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)
