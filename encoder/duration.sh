ffmpeg -i "$@" 2>&1 | grep Duration | sed -e 's?.*Duration: \([^,]*\),.*?\1?'
