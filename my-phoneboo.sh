sudo su
yum update -y
yum install python3 -y
yum install python-pip -y
pip3 install Flask==2.3.3
pip3 install Flask-MySql
yum install git -y
echo "phonebook-instance.cviceauwugl8.us-east-1.rds.amazonaws.com" > /home/ec2-user/dbserver.endpoint
git clone https://github.com/gnukum511/my-repository.git
python3 /home/ec2-user/my-repository/Project-004-Phonebook-Application/phonebook-app.py
