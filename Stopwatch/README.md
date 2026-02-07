# Stopwatch

A command-line stopwatch for tracking time spent on focused work sessions. Built while working through *Automate the Boring Stuff with Python*.

## The Problem

I needed to track how long specific tasks take for personal productivity tracking. Using my phone's timer meant switching devices and breaking my workflow; I wanted a solution that stays within my computer environment, where I'm already working.

## What It Does

- Start/stop timer with Enter key
- Calculates elapsed time in HH:MM:SS format
- Logs all timer events to a local file (in case you accidentally press start too soon)
- Runs continuously - just press start again for the next session
- No device switching required

## Features Checklist

- [x] Start & stop controls
- [x] Track elapsed time in seconds
- [x] Display time in HH:MM:SS format
- [x] No reset button needed (just start again)
- [x] Write start-stop history to log file
- [ ] Accept keyboard shortcuts (currently uses Enter)
- [ ] Simple GUI interface

## Usage

```bash
python3 stopwatch.py
```

Press Enter to start, Enter again to stop. The elapsed time displays in the terminal. `Ctrl+C` to exit the program.

All timer events are logged to `time_history_log.txt` in the same directory.

## What I Learned

- Working with `datetime` module for precise time tracking
- File I/O with append mode for persistent logging
- Global state management between function calls
- Exception handling for graceful program exits
- String manipulation (removing microseconds from display output)

## Future Improvements

- Keyboard shortcuts for start/stop (instead of Enter key)
- Simple GUI using tkinter
- Display historical session times in the interface
- Implement proper logging with `logging.basicConfig()`
- Automation: copy final time to clipboard for easy pasting

---

*Written February 2026 | Part of hands-on practice with Python fundamentals*
