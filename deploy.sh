docker build --tag avishayp/tcpserver tcpserver && docker push avishayp/tcpserver && ssh -i ~/.ssh/noyad.pem ec2-user@tcpapi.noyad.in 'sh ~/startup.sh'
