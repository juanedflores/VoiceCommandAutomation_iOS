# /usr/bin/osascript /Users/juaneduardoflores/apple_scripts/closeApps.scpt 
# wait
source /Users/juaneduardoflores/.zshrc
# wait
/Applications/kitty.app/Contents/MacOS/kitty --single-instance /usr/local/bin/nvim /Users/juaneduardoflores/Documents/Websites/ArtistWebsite/Blog/
cd '/Users/juaneduardoflores/Documents/Websites/ArtistWebsite/'
/usr/local/bin/browser-sync start --no-notify --server --files .
# /usr/local/bin/yabai -m window --toggle zoom-fullscreen
