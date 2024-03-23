import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello, Rotated Text!")
    stdscr.refresh()
    curses.napms(3000)  # Sleep for 3 seconds

curses.wrapper(main)
