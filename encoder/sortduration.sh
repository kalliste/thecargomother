mkdir -p long
for I in *.wav; do 
  if ((`./duration.sh $I | tr -cd '0-9' | sed -e 's?^0*??'` > 600)); then 
    mv "$I" long
    echo "$I" long
  fi
done
