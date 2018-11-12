# $ crontab -l
# @reboot /home/ec2-user/startup.sh
#
# $ cat /home/ec2-user/startup.sh
# sudo service docker start
# docker pull avishayp/tcpserver
# docker run --rm -d -p 443:8888 --name tcpserv avishayp/tcpserver