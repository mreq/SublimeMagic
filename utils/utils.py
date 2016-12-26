import sublime


def find_previous_delimiter(view, line, re_delimiter, start):
    found = None

    while start > line.a and start > 0:
        region = sublime.Region(start - 1, start)
        if re_delimiter.match(view.substr(region)):
            found = start
            break
        start -= 1

    return found


def find_next_delimiter(view, line, re_delimiter, delimiter_length, start):
    found = None

    while start < line.b and start < 999999:
        region = sublime.Region(start, start + delimiter_length)
        if re_delimiter.match(view.substr(region)):
            found = start
            break
        start += 1

    return found
