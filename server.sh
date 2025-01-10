./shell2http -export-vars=DISPLAY \
    -form /fullscreen "xdotool key f" /move-up "xdotool key k" \
    /move-down "xdotool key j" /move-right "xdotool key l" \
    /move-left "xdotool key h" /zoom "xdotool key plus" \
    /zoom-out "xdotool key minus" /page-up "xdotool key Prior" \
    /page-down "xdotool key Next" /open-pdf 'mupdf $v_file' \
    /quit "xdotool key q"
