# 0) Prereq: doctl logged in (doctl auth init) & SSH key added
#    Find your key id: doctl compute ssh-key list

export KEY_ID=50466671
set -e
IP=$1

echo "IP: $IP"
# Configure and serve a page
ssh -i /Users/ray/.ssh/uug_do_id_ed25519 -o StrictHostKeyChecking=no root@$IP \
  'apt-get update && apt-get -y install nginx && \
   echo "Hello from Linux on DigitalOcean $(hostname)" > /var/www/html/index.html && \
   systemctl enable --now nginx'

# Clean up
# doctl compute droplet delete $NAME -f
# echo "Deleted droplet $NAME"