echo Alpaca{REDACTED} > flag.txt
chmod 400 flag.txt
runuser -u nobody -- sh
rm flag.txt
