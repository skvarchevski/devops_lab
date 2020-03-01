 #!/bin/bash
sudo yum -y install epel-release
yum install -y python-pip git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
. ~/.bashrc
sudo pip install --upgrade pip
sudo pip install virtualenv
pyenv install 2.7.5
pyenv virtualenv 2.7.5 env_2.7.5
pyenv install 3.8.0
pyenv virtualenv 3.8.0 env_3.8.0
pyenv global 3.8.0