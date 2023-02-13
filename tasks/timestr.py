__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    output = ""
    days = seconds // (3600 * 24)
    first_flag = False
    if days != 0:
        output += (f"{days:02}d")
        seconds -= days*3600*24
        first_flag = True
    hours = seconds//3600
    if hours != 0 or first_flag:
        output += (f"{hours:02}h")
        seconds -= hours * 3600
        first_flag = True
    min = seconds//60
    if min != 0 or first_flag:
        output += (f"{min:02}m")
        seconds -= min*60
    output += (f"{seconds:02}s")

    return output
