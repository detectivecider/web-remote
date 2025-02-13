shell2http -export-all-vars -form \
	/fullscreen "echo 'key f' | dotool" \
    /move-up "echo 'key k' | dotool" \
    /move-down "echo 'key j' | dotool" \
    /move-right "echo key l | dotool" \
    /move-left "echo 'key h' | dotool" \
    /zoom "echo 'key k:78' | dotool" \
    /zoom-out "echo 'key k:12' | dotool" \
    /page-up "echo 'key k:104' | dotool" \
    /page-down "echo 'key k:109' | dotool" \
    /open-pdf 'zathura $v_file' \
    /quit "echo 'key q' | dotool" &

python server.py &
